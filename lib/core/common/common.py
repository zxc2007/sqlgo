import os
import sys
sys.path.append(os.getcwd())
from lib.logger.log import logger
from lib.decorators import cachedmethod
from lib.datastruc.injectdict import AttribDict

kb = AttribDict

@cachedmethod
def aliasToDbmsEnum(dbms):
    """
    Returns major DBMS name from a given alias

    >>> aliasToDbmsEnum('mssql')
    'Microsoft SQL Server'
    """

    retVal = None

    if dbms:
        for key, item in DBMS_DICT.items():
            if dbms.lower() in item[0] or dbms.lower() == key.lower():
                retVal = key
                break

    return retVal



def IsListLike(value):
    return isinstance(value,(set,tuple,list))
class Backend(object):
    @staticmethod
    def setDbms(dbms):
        dbms = aliasToDbmsEnum(dbms)

        if dbms is None:
            return None

        # Little precaution, in theory this condition should always be false
        elif kb.dbms is not None and kb.dbms != dbms:
            warnMsg = "there appears to be a high probability that "
            warnMsg += "this could be a false positive case"
            logger.warning(warnMsg)

            msg = "sqlmap previously fingerprinted back-end DBMS as "
            msg += "%s. However now it has been fingerprinted " % kb.dbms
            msg += "as %s. " % dbms
            msg += "Please, specify which DBMS should be "
            msg += "correct [%s (default)/%s] " % (kb.dbms, dbms)

            while True:
                choice = readInput(msg, default=kb.dbms)

                if aliasToDbmsEnum(choice) == kb.dbms:
                    kb.dbmsVersion = []
                    kb.resolutionDbms = kb.dbms
                    break
                elif aliasToDbmsEnum(choice) == dbms:
                    kb.dbms = aliasToDbmsEnum(choice)
                    break
                else:
                    warnMsg = "invalid value"
                    logger.warning(warnMsg)

        elif kb.dbms is None:
            kb.dbms = aliasToDbmsEnum(dbms)

        return kb.dbms

    @staticmethod
    def setVersion(version):
        if isinstance(version, six.string_types):
            kb.dbmsVersion = [version]

        return kb.dbmsVersion

    @staticmethod
    def setVersionList(versionsList):
        if isinstance(versionsList, list):
            kb.dbmsVersion = versionsList
        elif isinstance(versionsList, six.string_types):
            Backend.setVersion(versionsList)
        else:
            logger.error("invalid format of versionsList")

    @staticmethod
    def forceDbms(dbms, sticky=False):
        if not kb.stickyDBMS:
            kb.forcedDbms = aliasToDbmsEnum(dbms)
            kb.stickyDBMS = sticky

    @staticmethod
    def flushForcedDbms(force=False):
        if not kb.stickyDBMS or force:
            kb.forcedDbms = None
            kb.stickyDBMS = False

    @staticmethod
    def setOs(os):
        if os is None:
            return None

        # Little precaution, in theory this condition should always be false
        elif kb.os is not None and isinstance(os, six.string_types) and kb.os.lower() != os.lower():
            msg = "sqlmap previously fingerprinted back-end DBMS "
            msg += "operating system %s. However now it has " % kb.os
            msg += "been fingerprinted to be %s. " % os
            msg += "Please, specify which OS is "
            msg += "correct [%s (default)/%s] " % (kb.os, os)

            while True:
                choice = readInput(msg, default=kb.os)

                if choice == kb.os:
                    break
                elif choice == os:
                    kb.os = choice.capitalize()
                    break
                else:
                    warnMsg = "invalid value"
                    logger.warning(warnMsg)

        elif kb.os is None and isinstance(os, six.string_types):
            kb.os = os.capitalize()

        return kb.os

    @staticmethod
    def setOsVersion(version):
        if version is None:
            return None

        elif kb.osVersion is None and isinstance(version, six.string_types):
            kb.osVersion = version

    @staticmethod
    def setOsServicePack(sp):
        if sp is None:
            return None

        elif kb.osSP is None and isinstance(sp, int):
            kb.osSP = sp

    @staticmethod
    def setArch():
        msg = "what is the back-end database management system architecture?"
        msg += "\n[1] 32-bit (default)"
        msg += "\n[2] 64-bit"

        while True:
            choice = readInput(msg, default='1')

            if hasattr(choice, "isdigit") and choice.isdigit() and int(choice) in (1, 2):
                kb.arch = 32 if int(choice) == 1 else 64
                break
            else:
                warnMsg = "invalid value. Valid values are 1 and 2"
                logger.warning(warnMsg)

        return kb.arch

    # Get methods
    @staticmethod
    def getForcedDbms():
        return aliasToDbmsEnum(conf.get("forceDbms")) or aliasToDbmsEnum(kb.get("forcedDbms"))

    @staticmethod
    def getDbms():
        return aliasToDbmsEnum(kb.get("dbms"))

    @staticmethod
    def getErrorParsedDBMSes():
        """
        Returns array with parsed DBMS names till now

        This functions is called to:

        1. Ask user whether or not skip specific DBMS tests in detection phase,
           lib/controller/checks.py - detection phase.
        2. Sort the fingerprint of the DBMS, lib/controller/handler.py -
           fingerprint phase.
        """

        return kb.htmlFp if kb.get("heuristicTest") == HEURISTIC_TEST.POSITIVE else []

    @staticmethod
    def getIdentifiedDbms():
        """
        This functions is called to:

        1. Sort the tests, getSortedInjectionTests() - detection phase.
        2. Etc.
        """

        dbms = None

        if not kb:
            pass
        elif not kb.get("testMode") and conf.get("dbmsHandler") and getattr(conf.dbmsHandler, "_dbms", None):
            dbms = conf.dbmsHandler._dbms
        elif Backend.getForcedDbms() is not None:
            dbms = Backend.getForcedDbms()
        elif Backend.getDbms() is not None:
            dbms = Backend.getDbms()
        elif kb.get("injection") and kb.injection.dbms:
            dbms = unArrayizeValue(kb.injection.dbms)
        elif Backend.getErrorParsedDBMSes():
            dbms = unArrayizeValue(Backend.getErrorParsedDBMSes())
        elif conf.get("dbms"):
            dbms = conf.get("dbms")

        return aliasToDbmsEnum(dbms)

    @staticmethod
    def getVersion():
        versions = filterNone(flattenValue(kb.dbmsVersion)) if not isinstance(kb.dbmsVersion, six.string_types) else [kb.dbmsVersion]
        if not isNoneValue(versions):
            return versions[0]
        else:
            return None

    @staticmethod
    def getVersionList():
        versions = filterNone(flattenValue(kb.dbmsVersion)) if not isinstance(kb.dbmsVersion, six.string_types) else [kb.dbmsVersion]
        if not isNoneValue(versions):
            return versions
        else:
            return None

    @staticmethod
    def getOs():
        return kb.os

    @staticmethod
    def getOsVersion():
        return kb.osVersion

    @staticmethod
    def getOsServicePack():
        return kb.osSP

    @staticmethod
    def getArch():
        if kb.arch is None:
            Backend.setArch()
        return kb.arch

    # Comparison methods
    @staticmethod
    def isDbms(dbms):
        if not kb.get("testMode") and all((Backend.getDbms(), Backend.getIdentifiedDbms())) and Backend.getDbms() != Backend.getIdentifiedDbms():
            singleTimeWarnMessage("identified ('%s') and fingerprinted ('%s') DBMSes differ. If you experience problems in enumeration phase please rerun with '--flush-session'" % (Backend.getIdentifiedDbms(), Backend.getDbms()))
        return Backend.getIdentifiedDbms() == aliasToDbmsEnum(dbms)

    @staticmethod
    def isFork(fork):
        return hashDBRetrieve(HASHDB_KEYS.DBMS_FORK) == fork

    @staticmethod
    def isDbmsWithin(aliases):
        return Backend.getDbms() is not None and Backend.getDbms().lower() in aliases

    @staticmethod
    def isVersion(version):
        return Backend.getVersion() is not None and Backend.getVersion() == version

    @staticmethod
    def isVersionWithin(versionList):
        if Backend.getVersionList() is None:
            return False

        for _ in Backend.getVersionList():
            if _ != UNKNOWN_DBMS_VERSION and _ in versionList:
                return True

        return False

    @staticmethod
    def isVersionGreaterOrEqualThan(version):
        retVal = False

        if all(_ not in (None, UNKNOWN_DBMS_VERSION) for _ in (Backend.getVersion(), version)):
            _version = unArrayizeValue(Backend.getVersion())
            _version = re.sub(r"[<>= ]", "", _version)

            try:
                retVal = LooseVersion(_version) >= LooseVersion(version)
            except:
                retVal = str(_version) >= str(version)

        return retVal

    @staticmethod
    def isOs(os):
        return Backend.getOs() is not None and Backend.getOs().lower() == os.lower()
    

