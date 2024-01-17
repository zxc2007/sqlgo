

import hashlib
import os
import re
import shutil
import tempfile
import threading
import sys


# Importing from built-in modules
import six
import mimetypes

class Dump(object):
    """
    This class defines methods used to parse and output the results
    of SQL injection actions
    """

    def __init__(self):
        self._outputFile = None
        self._outputFP = None
        self._lock = threading.Lock()

    def _write(self, data, newline=True, console=True, content_type=None):
        text = "%s%s" % (data, "\n" if newline else " ")

        if conf.api:
            dataToStdout(data, contentType=content_type, status=CONTENT_STATUS.COMPLETE)
        elif console:
            dataToStdout(text)

        if self._outputFP:
            multiThreadMode = kb.multiThreadMode
            if multiThreadMode:
                self._lock.acquire()

            try:
                self._outputFP.write(text)
            except IOError as ex:
                errMsg = "error occurred while writing to log file ('%s')" % getSafeExString(ex)
                raise SqlmapGenericException(errMsg)

            if multiThreadMode:
                self._lock.release()

        kb.dataOutputFlag = True

    def flush(self):
        if self._outputFP:
            try:
                self._outputFP.flush()
            except IOError:
                pass

    def setOutputFile(self):
        if conf.noLogging:
            self._outputFP = None
            return

        self._outputFile = os.path.join(conf.outputPath, "log")
        try:
            self._outputFP = openFile(self._outputFile, "ab" if not conf.flushSession else "wb")
        except IOError as ex:
            errMsg = "error occurred while opening log file ('%s')" % getSafeExString(ex)
            raise SqlmapGenericException(errMsg)

    def singleString(self, data, content_type=None):
        self._write(data, content_type=content_type)

    # ... (rest of the class methods, unchanged)
