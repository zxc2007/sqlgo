from sqlmap.lib.core.data import conf,kb
from src.core.parser.cmdline import dbms
from src.logger.log import logger
from src.core.Exceptions.exceptions import SQLGOFilePathException
from utilis.readfile import ReadFile
import os
import sys
import platform
import subprocess


__tool__ = "hydra"

class Hydra(object):
    def __init__(self,userfile,passfile,host):
        try:
            self.userfile = conf.Userfile or userfile
            self.passfile = conf.Passfile or passfile
            self.host = conf.hostname or host
            self.dbms = conf.dbms or dbms or "mysql"
            self.mysql_scheme = "mysql://"
            self.hydra_command = f"hydra -l {self.userfile} -p {self.passfile} {self.mysql_scheme}{self.host}"

        
        except AttributeError:
            self.userfile = userfile
            self.passfile = passfile
            self.host = host
            self.dbms = dbms
            self.mysql_scheme = "mysql://"
            self.hydra_command = f"hydra -l {self.userfile} -p {self.passfile} {self.mysql_scheme}{self.host}"
    
    def _check_hydra(self):
        try:
            command = os.system(__tool__)
            if "Hydra" in str(command):
                logger.info("hydra installed on your system!")
                return True
        except Exception as ex:
            logger.error("Error occurred: %s"%ex)
        
    
    def _check_file_paths(self):
        if not os.path.exists(self.userfile) or not os.path.exists(self.passfile):
            errMsg = "the provided file paths '%s' and '%s' do not exist" % (self.userfile, self.passfile)
            raise SQLGOFilePathException(errMsg)
        else:
            return True
    
    def run_hydra(self):
        if self._check_file_paths():
            os.system(self.hydra_command)
            



            
