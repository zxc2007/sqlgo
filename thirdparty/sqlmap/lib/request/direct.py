#!/usr/bin/env python

"""
Copyright (c) 2006-2024 sqlmap developers (https://sqlmap.org/)
See the file 'LICENSE' for copying permission
"""

import re
import time

from lib.core.agent import agent
from src.core.common import Backend
from src.core.common import calculateDeltaSeconds
from src.core.common import extractExpectedValue
from src.core.common import getCurrentThreadData
from src.core.common import hashDBRetrieve
from src.core.common import hashDBWrite
from src.core.common import isListLike
from lib.core.convert import getUnicode
from lib.core.data import conf
from lib.core.data import kb
from lib.core.data import logger
from src.core.dicts import SQL_STATEMENTS
from src.core.enums import CUSTOM_LOGGING
from src.core.enums import DBMS
from src.core.enums import EXPECTED
from src.core.enums import TIMEOUT_STATE
from lib.core.settings import UNICODE_ENCODING
from lib.utils.safe2bin import safecharencode
from lib.utils.timeout import timeout

def direct(query, content=True):
    select = True
    query = agent.payloadDirect(query)
    query = agent.adjustLateValues(query)
    threadData = getCurrentThreadData()

    if Backend.isDbms(DBMS.ORACLE) and query.upper().startswith("SELECT ") and " FROM " not in query.upper():
        query = "%s FROM DUAL" % query

    for sqlTitle, sqlStatements in SQL_STATEMENTS.items():
        for sqlStatement in sqlStatements:
            if query.lower().startswith(sqlStatement) and sqlTitle != "SQL SELECT statement":
                select = False
                break

    if select:
        if re.search(r"(?i)\ASELECT ", query) is None:
            query = "SELECT %s" % query

        if conf.binaryFields:
            for field in conf.binaryFields:
                field = field.strip()
                if re.search(r"\b%s\b" % re.escape(field), query):
                    query = re.sub(r"\b%s\b" % re.escape(field), agent.hexConvertField(field), query)

    logger.log(CUSTOM_LOGGING.PAYLOAD, query)

    output = hashDBRetrieve(query, True, True)
    start = time.time()

    if not select and re.search(r"(?i)\bEXEC ", query) is None:
        timeout(func=conf.dbmsConnector.execute, args=(query,), duration=conf.timeout, default=None)
    elif not (output and ("%soutput" % conf.tablePrefix) not in query and ("%sfile" % conf.tablePrefix) not in query):
        output, state = timeout(func=conf.dbmsConnector.select, args=(query,), duration=conf.timeout, default=None)
        if state == TIMEOUT_STATE.NORMAL:
            hashDBWrite(query, output, True)
        elif state == TIMEOUT_STATE.TIMEOUT:
            conf.dbmsConnector.close()
            conf.dbmsConnector.connect()
    elif output:
        infoMsg = "resumed: %s..." % getUnicode(output, UNICODE_ENCODING)[:20]
        logger.info(infoMsg)

    threadData.lastQueryDuration = calculateDeltaSeconds(start)

    if not output:
        return output
    elif content:
        if output and isListLike(output):
            if len(output[0]) == 1:
                output = [_[0] for _ in output]

        retVal = getUnicode(output, noneToNull=True)
        return safecharencode(retVal) if kb.safeCharEncode else retVal
    else:
        return extractExpectedValue(output, EXPECTED.BOOL)
