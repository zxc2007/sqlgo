#!/usr/bin/env python
"""
# SQLGO License - Version 1.4

Copyright (C) 2023-2024 Heisenberg

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.


"""
from __future__ import division

import os
import re
import tempfile
import time

from sqlmap.lib.core.common import checkSameHost
from sqlmap.lib.core.common import clearConsoleLine
from sqlmap.lib.core.common import dataToStdout
from sqlmap.lib.core.common import extractRegexResult
from sqlmap.lib.core.common import findPageForms
from sqlmap.lib.core.common import getSafeExString
from sqlmap.lib.core.common import openFile
from sqlmap.lib.core.common import readInput
from sqlmap.lib.core.common import safeCSValue
from sqlmap.lib.core.common import urldecode
from sqlmap.lib.core.compat import xrange
from sqlmap.lib.core.convert import htmlUnescape
from sqlmap.lib.core.data import conf
from sqlmap.lib.core.data import kb
from sqlmap.lib.core.data import logger
from sqlmap.lib.core.datatype import OrderedSet
from sqlmap.lib.core.enums import MKSTEMP_PREFIX
from sqlmap.lib.core.exception import SqlmapConnectionException
from sqlmap.lib.core.exception import SqlmapSyntaxException
from sqlmap.lib.core.settings import CRAWL_EXCLUDE_EXTENSIONS
from sqlmap.lib.core.threads import getCurrentThreadData
from sqlmap.lib.core.threads import runThreads
from sqlmap.lib.parse.sitemap import parseSitemap
from sqlmap.lib.request.connect import Connect as Request
from sqlmap.thirdparty import six
from sqlmap.thirdparty.beautifulsoup.beautifulsoup import BeautifulSoup
from sqlmap.thirdparty.six.moves import http_client as _http_client
from sqlmap.thirdparty.six.moves import urllib as _urllib
conf.crawlDepth = 3

def crawl(target, post=None, cookie=None):
    if not target:
        return

    try:
        visited = set()
        threadData = getCurrentThreadData()
        threadData.shared.value = OrderedSet()
        threadData.shared.formsFound = False

        def crawlThread():
            threadData = getCurrentThreadData()

            while kb.threadContinue:
                with kb.locks.limit:
                    if threadData.shared.unprocessed:
                        current = threadData.shared.unprocessed.pop()
                        if current in visited:
                            continue
                        elif conf.crawlExclude and re.search(conf.crawlExclude, current):
                            dbgMsg = "skipping '%s'" % current
                            logger.debug(dbgMsg)
                            continue
                        else:
                            visited.add(current)
                    else:
                        break

                content = None
                try:
                    if current:
                        content = Request.getPage(url=current, post=post, cookie=None, crawling=True, raise404=False)[0]
                except SqlmapConnectionException as ex:
                    errMsg = "connection exception detected ('%s'). skipping " % getSafeExString(ex)
                    errMsg += "URL '%s'" % current
                    logger.critical(errMsg)
                except SqlmapSyntaxException:
                    errMsg = "invalid URL detected. skipping '%s'" % current
                    logger.critical(errMsg)
                except _http_client.InvalidURL as ex:
                    errMsg = "invalid URL detected ('%s'). skipping " % getSafeExString(ex)
                    errMsg += "URL '%s'" % current
                    logger.critical(errMsg)

                if not kb.threadContinue:
                    break

                if isinstance(content, six.text_type):
                    try:
                        match = re.search(r"(?si)<html[^>]*>(.+)</html>", content)
                        if match:
                            content = "<html>%s</html>" % match.group(1)

                        soup = BeautifulSoup(content)
                        tags = soup('a')

                        tags += re.finditer(r'(?i)\s(href|src)=["\'](?P<href>[^>"\']+)', content)
                        tags += re.finditer(r'(?i)window\.open\(["\'](?P<href>[^)"\']+)["\']', content)

                        for tag in tags:
                            href = tag.get("href") if hasattr(tag, "get") else tag.group("href")

                            if href:
                                if threadData.lastRedirectURL and threadData.lastRedirectURL[0] == threadData.lastRequestUID:
                                    current = threadData.lastRedirectURL[1]
                                url = _urllib.parse.urljoin(current, htmlUnescape(href))

                                # flag to know if we are dealing with the same target host
                                _ = checkSameHost(url, target)

                                if conf.scope:
                                    if not re.search(conf.scope, url, re.I):
                                        continue
                                elif not _:
                                    continue

                                if (extractRegexResult(r"\A[^?]+\.(?P<result>\w+)(\?|\Z)", url) or "").lower() not in CRAWL_EXCLUDE_EXTENSIONS:
                                    with kb.locks.value:
                                        threadData.shared.deeper.add(url)
                                        if re.search(r"(.*?)\?(.+)", url) and not re.search(r"\?(v=)?\d+\Z", url) and not re.search(r"(?i)\.(js|css)(\?|\Z)", url):
                                            threadData.shared.value.add(url)
                    except UnicodeEncodeError:  # for non-HTML files
                        pass
                    except ValueError:          # for non-valid links
                        pass
                    except AssertionError:      # for invalid HTML
                        pass
                    finally:
                        if conf.forms:
                            threadData.shared.formsFound |= len(findPageForms(content, current, False, True)) > 0

                if conf.verbose in (1, 2):
                    threadData.shared.count += 1
                    status = '%d/%d links visited (%d%%)' % (threadData.shared.count, threadData.shared.length, round(100.0 * threadData.shared.count / threadData.shared.length))
                    dataToStdout("\r[%s] [INFO] %s" % (time.strftime("%X"), status), True)

        threadData.shared.deeper = set()
        threadData.shared.unprocessed = set([target])

        _ = re.sub(r"(?<!/)/(?!/).*", "", target)
        if _:
            if target.strip('/') != _.strip('/'):
                threadData.shared.unprocessed.add(_)

        if re.search(r"\?.*\b\w+=", target):
            threadData.shared.value.add(target)

        if kb.checkSitemap is None:
            message = "do you want to check for the existence of "
            message += "site's sitemap(.xml) [y/N] "
            kb.checkSitemap = readInput(message, default='N', boolean=True)

        if kb.checkSitemap:
            found = True
            items = None
            url = _urllib.parse.urljoin(target, "/sitemap.xml")
            try:
                items = parseSitemap(url)
            except SqlmapConnectionException as ex:
                if "page not found" in getSafeExString(ex):
                    found = False
                    logger.warning("'sitemap.xml' not found")
            except:
                pass
            finally:
                if found:
                    if items:
                        for item in items:
                            if re.search(r"(.*?)\?(.+)", item):
                                threadData.shared.value.add(item)
                        if conf.crawlDepth > 1:
                            threadData.shared.unprocessed.update(items)
                    logger.info("%s links found" % ("no" if not items else len(items)))

        if not conf.bulkFile:
            infoMsg = "starting crawler for target URL '%s'" % target
            logger.info(infoMsg)

        for i in xrange(conf.crawlDepth):
            threadData.shared.count = 0
            threadData.shared.length = len(threadData.shared.unprocessed)
            numThreads = min(conf.threads, len(threadData.shared.unprocessed))

            if not conf.bulkFile:
                logger.info("searching for links with depth %d" % (i + 1))

            clearConsoleLine(True)

            if threadData.shared.deeper:
                threadData.shared.unprocessed = set(threadData.shared.deeper)
            else:
                break

    except KeyboardInterrupt:
        warnMsg = "user aborted during crawling. sqlmap "
        warnMsg += "will use partial list"
        logger.warning(warnMsg)

    finally:
        clearConsoleLine(True)

        if not threadData.shared.value:
            if not (conf.forms and threadData.shared.formsFound):
                warnMsg = "no usable links found (with GET parameters)"
                if conf.forms:
                    warnMsg += " or forms"
                logger.warning(warnMsg)
        else:
            for url in threadData.shared.value:
                kb.targets.add((urldecode(url, kb.pageEncoding), None, None, None, None))

        if kb.targets:
            if kb.normalizeCrawlingChoice is None:
                message = "do you want to normalize "
                message += "crawling results [Y/n] "

                kb.normalizeCrawlingChoice = readInput(message, default='Y', boolean=True)

            if kb.normalizeCrawlingChoice:
                seen = set()
                results = OrderedSet()

                for target in kb.targets:
                    value = "%s%s%s" % (target[0], '&' if '?' in target[0] else '?', target[2] or "")
                    match = re.search(r"/[^/?]*\?.+\Z", value)
                    if match:
                        key = re.sub(r"=[^=&]*", "=", match.group(0)).strip("&?")
                        if '=' in key and key not in seen:
                            results.add(target)
                            seen.add(key)

                kb.targets = results

            storeResultsToFile(kb.targets)

def storeResultsToFile(results):
    if not results:
        return

    # Check user's choice to store crawling results
    if kb.storeCrawlingChoice is None:
        message = "do you want to store crawling results to a temporary file "
        message += "for eventual further processing with other tools [y/N] "
        kb.storeCrawlingChoice = readInput(message, default='N', boolean=True)

    # Store results to a temporary file if the user chooses to do so
    if kb.storeCrawlingChoice:
        handle, filename = tempfile.mkstemp(prefix=MKSTEMP_PREFIX.CRAWLER, suffix=".csv" if conf.forms else ".txt")
        os.close(handle)

        infoMsg = "writing crawling results to a temporary file '%s' " % filename
        logger.info(infoMsg)

        with openFile(filename, "w+b") as f:
            if conf.forms:
                f.write("URL,POST\n")

                for result in results:
                    if len(result) >= 2:
                        f.write("%s,%s\n" % (safeCSValue(result[0]), safeCSValue(result[2] or "")))
                    else:
                        f.write("%s\n" % result[0])


kb.targets = set()
kb.pageEncoding = True
kb.normalizeCrawlingChoice = ""
conf.normalizeCrawlingChoice = ""
kb.storeCrawlingChoice = 1
kb.forms = ''
conf.forms = ""
conf.checkSitemap = ''
kb.checkSitemap = 2
kb.bulkFile = 3
conf.bulkFile = ""
kb.crawlDepth = 3
conf.crawlDepth = 5
conf.threads = 4
kb.locks = 3
conf.locks = ""

