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
import os
import sys
import re
import random
import string
import glob
import os
import re
from sqlmap.lib.core.common import setColor
from src.data import arg,config
from src.core.enums.enums import DBMS
from src.core.enums.enums import Hashes
from src.data import gen


class _IOFileReader(object):
    def __init__(self, to_write, to_read):
        self.__os = os
        self.__sys = sys
        self._payload_dir = os.path.join(self.__os.getcwd(), "data", "payloads", "%s.txt"%to_read)
        self.__paylods_dir = os.path.join(self.__os.getcwd(), "data", "payloads", "%s.txt"%to_write)
        self.__regex = re
        self.__numeric_pattern = re.compile(r'\[RANDNUM\]|\[RANDNUM1\]|\[INFERENCE\]|\[RANDNUM2\]|\[SLEEPTIME\]')
        self.__string_pattern = re.compile(r'\[RANDSTR\]|\[RANDSTR1\]|\[GENERIC_SQL_COMMENT\]|\[ORIGVALUE\]|\[DELIMITER_START\]|\[QUERY\]')
        self.__string = string
        self.__files = [
            "error_boolean.txt"
        ]

    def __enter__(self):
        with open(self._payload_dir, "r") as file:
            content = file.read()
            if re.search(self.__numeric_pattern, content) or re.search(self.__string_pattern, content):
                content = re.sub(self.__numeric_pattern, lambda x: str(random.randint(0, 100)), content)
                content = re.sub(self.__string_pattern,
                                 lambda x: ''.join(random.choice(self.__string.ascii_letters + str(self.__string.digits)) for _ in range(len(x.group(0)))), content)
                return content
            else:
                return content

    def __exit__(self, exc_type, exc_value, exc_traceback):
        pass

    def replace(self):
        with open(self._payload_dir, "r") as file:
            content = file.read()
            if re.search(self.__numeric_pattern, content) or re.search(self.__string_pattern, content):
                for file_name in self.__files:
                    replaced_content = re.sub(self.__numeric_pattern, lambda x: str(random.randint(0, 100)), content)
                    replaced_content = re.sub(self.__string_pattern,
                                               lambda x: ''.join(
                                                   random.choice(self.__string.ascii_letters + str(self.__string.digits)) for _ in range(len(x.group(0)))), replaced_content)
                    with open(self.__paylods_dir, "w") as out_file:  # Open outside loop
                        lines = replaced_content.split(";")
                        out_file.write("\n".join(lines))
            return content



class IOFileReader(object):
    """
    Reads the payloads file and returns the content of the payloads file
    Usage:
    >>> with open(IOFileReader("error_boolean.txt")) as file:
        ... 'AND 1=1'

    """
    
    @classmethod
    def payload(cls,_file):   
        with open(os.getcwd()+"/data/payloads/"+_file, "r") as file: 
            payload = file.read() 
            rows = payload.split("\n") 
            sorted_rows = sorted(rows) 
            sorted_payload = "\n".join(sorted_rows) 
            return sorted_payload
    @classmethod
    def generic(cls,path):
        with open(os.getcwd()+path, "r") as file: 
            payload = file.read() 
            rows = payload.split("\n") 
            sorted_rows = sorted(rows) 
            sorted_payload = "\n".join(sorted_rows) 
            return sorted_payload



def _listTamperingFunctions():
    """
    Lists available tamper functions
    """

    infoMsg = "listing available tamper scripts\n"
    print(infoMsg)

    for script in sorted(glob.glob(os.path.join(os.getcwd(), "tampers", "*.py"))):
        if os.path.basename(script) == 'maintamper.py' or os.path.basename(script) == '__init__.py':
            continue
        with open(script, "r") as file:
            content = file.read()
            match = re.search(r'(?s).+"""(.+)"""', content)
            if match:
                comment = match.group(1).strip()
                print("* %s - %s\n" % (setColor(os.path.basename(script), "yellow"), re.sub(r" *\n *", " ", comment.split("\n\n")[0].strip())))

def readInput(msg, default=None, boolean=False,options=[]):
    """
    A function to read input from the stream.
    *Note:first option of the list the the default value 
    """
    if not options:
        options = ["y", "n"]
    retVal = None
    if arg.batch:
        retVal = default
        return True

    if default is not None:
        msg += " [%s/%s]" % (default[0].upper()+default[1:] or options[0],options[1])

    while retVal is None:
        retVal = input(msg).strip().lower()

        if retVal == '' and default is not None:
            retVal = default
        elif retVal == '0' and boolean:
            retVal = False
        elif retVal == '1' and boolean:
            retVal = True
        elif retVal == options[0] or retVal == default:
            retVal = True
        elif retVal == options[1]:
            retVal = False

        try:
            if boolean:
                retVal = bool(int(retVal))
            else:
                retVal = int(retVal)

        except ValueError:
            pass

    return retVal

def whatDbms(response):
    """
    Tries to guess the DBMS by checking the response headers
    Usage:
    >>> whatDbms(response)
    'MySQL'
    """
    try:
        dbmsVars = vars(DBMS)
        for dbmsVar in dbmsVars.values():
            if re.search(dbmsVar, response, re.IGNORECASE):
                return dbmsVar
    
    except TypeError:
        return
        

def _wizardInterfaceSetup():
    """
    Setup wizard interface
    """
    print("starting wizard interface")
    inputMsg = "Please enter full target url(-u/--url)"
    url = readInput(inputMsg, default=arg.url)
    if url is not None:
        arg.url = url
    difMsg = "Injection difficulty (--level). Please choose:"
    level = readInput(difMsg, default=arg.level)
    if level is not None:
        arg.level = level
    
    enumerationMsg = "Enumeration (--banner/--current-user/etc). Please choose:"
    enumeration = readInput(enumerationMsg, default="tables")
    if enumeration is not None:
        if enumeration == "tables":
            arg.tables = True
        elif enumeration == "columns":
            arg.columns = True
        elif enumeration == "dbs":
            arg.dbs = True
        elif enumeration == "schema":
            arg.schema = True
        elif enumeration == "dump":
            arg.dump = True
            

def isHash(string):
    """
    A function determines whether the string retrieved from database is hashed or not
    """
    for hashType, length in Hashes.__members__.items():
        if len(string) == length.value:
            if re.match(r'^[a-fA-F0-9]+$', string):
                return True, hashType
    return False, ""

def genDataInit():
    """
    Function that initiates the knowledge based attributes
    """
    gen.basePath = os.getcwd() + "/data"
    gen.hashDir = gen.basePath + glob.glob("/txt/%s.txt" % gen.hashType)
    gen.originHash = gen.basePath + "/txt/plainpassword.txt"


def isListLike(value):
    """
    Checks if the value is list like
    >>> isListLike([1, 2, 3])
    True
    """
    return isinstance(value, (list, tuple, set))

def findPlainPassword(hashed, hashType="md5"):
    """
    A function to perform rainbow attack on the hashed database passwords
    >>> foo = findPlainPassword("5f4dcc3b5aa765d61d8327deb882cf99")
    >>> foo
    'password'
    """
    originFile = gen.hashDir
    path = gen.hashDir

    with open(path[0] if isListLike(path) else path, "r") as hashedFile:
        with open(originFile, "r") as originFile:
            for hashed_password in hashedFile:
                hashed_password = hashed_password.strip()
                plain_password = next(originFile).strip()
                if hashed_password == hashed:
                    return plain_password

    return
