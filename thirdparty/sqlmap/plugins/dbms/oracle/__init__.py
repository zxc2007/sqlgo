#!/usr/bin/env python

"""
Copyright (c) 2006-2024 sqlmap developers (https://sqlmap.org/)
See the file 'LICENSE' for copying permission
"""

from src.core.enums import DBMS
from lib.core.settings import ORACLE_SYSTEM_DBS
from lib.core.unescaper import unescaper
from _plugins.dbms.oracle.enumeration import Enumeration
from _plugins.dbms.oracle.filesystem import Filesystem
from _plugins.dbms.oracle.fingerprint import Fingerprint
from _plugins.dbms.oracle.syntax import Syntax
from _plugins.dbms.oracle.takeover import Takeover
from plugins.generic.misc import Miscellaneous

class OracleMap(Syntax, Fingerprint, Enumeration, Filesystem, Miscellaneous, Takeover):
    """
    This class defines Oracle methods
    """

    def __init__(self):
        self.excludeDbsList = ORACLE_SYSTEM_DBS

        for cls in self.__class__.__bases__:
            cls.__init__(self)

    unescaper[DBMS.ORACLE] = Syntax.escape
