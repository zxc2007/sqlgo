
from sqlmap.lib.core.enums import DBMS
from sqlmap.lib.core.settings import MYSQL_SYSTEM_DBS
from sqlmap.lib.core.unescaper import unescaper
from sqlmap.plugins.dbms.mysql.enumeration import Enumeration
from sqlmap.plugins.dbms.mysql.filesystem import Filesystem
from sqlmap.plugins.dbms.mysql.fingerprint import Fingerprint
from sqlmap.plugins.dbms.mysql.syntax import Syntax
from sqlmap.plugins.dbms.mysql.takeover import Takeover
from sqlmap.plugins.generic.misc import Miscellaneous

class MySQLMap(Syntax, Fingerprint, Enumeration, Filesystem, Miscellaneous, Takeover):
    """
    This class defines MySQL methods
    """

    def __init__(self):
        self.excludeDbsList = MYSQL_SYSTEM_DBS
        self.sysUdfs = {
            # UDF name: UDF return data-type
            "sys_exec": {"return": "int"},
            "sys_eval": {"return": "string"},
            "sys_bineval": {"return": "int"}
        }

        for cls in self.__class__.__bases__:
            cls.__init__(self)

    unescaper[DBMS.MYSQL] = Syntax.escape
