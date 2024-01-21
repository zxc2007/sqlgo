import os
import sys
sys.path.append(os.getcwd())
from lib.datastruc.injectdict import AttribDict
from lib.core.parser.cmdline import port as _port
from lib.core.parser.cmdline import dbs,dbms
from lib.logger.log import logger
from lib.core.Exceptions.exceptions import SQLGOFilePathException
from abc import ABC,abstractmethod
from lib.core.enums.enums import DBMS
try:
    import pymysql
except:
    pass
username = None
password= None


conf = AttribDict()
conf.dbmsUser = username
conf.dbmsPass = password
conf.hostname = "localhost"
conf.dbms = dbms == DBMS.MYSQL or DBMS.MSSQL
class Connector(ABC):
    def __init__(self) -> None:
        self.connector = None
        self.cursor = None
        self.hostname = None
    
    def initconnection(self):
        try:
            self.user = conf.dbmsUser or ""
            self.password = conf.dbmsPass or ""
            self.hostname = conf.hostname
            self.port = conf.port or _port
            self.db = conf.dbmsDb or dbs
        
        except AttributeError:
            self.user = "root"
            self.password = "alimirmohammad"
            self.hostname = "localhost"
            self.port = 3306
            self.db = "ali"
    def print_connected(self):
        self.port = 3306
        if self.hostname and self.port:
            infoMsg = "connection to %s server '%s:%d' established" % (conf.dbms, self.hostname, self.port)
            logger.info(infoMsg)
        
        self.connector = None
        self.cursor = None

    def init_cursor(self):
        if not hasattr(self,'cursor'):
            self.connector = pymysql.connect(
                    host=self.hostname,
                    user=self.user,
                    passwd=self.password,
                    db=self.db,
                    port=self.port,
                    connect_timeout=5,
                    use_unicode=True
                )
            self.cursor = self.connector.cursor()
    
    def close(self):
        try:
            if self.cursor:
                self.cursor.close()
            if self.connector:
                self.connector.close()
        except Exception as ex:
            logger.debug(ex)
        finally:
            self.closed()
    
    def checkFileDb(self):
        if not os.path.exists(self.db):
            errMsg = "the provided database file '%s' does not exist" % self.db
            raise SQLGOFilePathException(errMsg)
    
    @abstractmethod
    def select(self):
        pass

    @abstractmethod
    def execute(self):
        pass

    @abstractmethod
    def fetchall(self):
        pass

    @abstractmethod
    def connect(self):
        pass
    

