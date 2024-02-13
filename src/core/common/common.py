import os
import sys
import re
import random
import string

sys.path.append(os.getcwd())


class _IOFileReader(object):
    def __init__(self, to_write, to_read) -> None:
        self.__os = os
        self.__sys = sys
        self._payload_dir = os.path.join(self.__os.getcwd(), "data", "payloads", f"{to_read}.txt")
        self.__paylods_dir = os.path.join(self.__os.getcwd(), "data", "payloads", f"{to_write}.txt")
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
    
    @classmethod
    def payload(cls,_file):   
        with open(os.getcwd()+"/data/payloads/"+_file, "r") as file: 
            payload = file.read() 
            rows = payload.split("\n") 
            sorted_rows = sorted(rows) 
            sorted_payload = "\n".join(sorted_rows) 
            return sorted_payload

# IOFileReader.payload("inline.txt")