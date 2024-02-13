"""
# SQLGO License - Version 1.1

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
import hashlib
import sys
import threading
from src.conf.conf import data_to_std_out
from future.wariterdata import StreamReaderWriter
from src.logger.log import logger
from src.core.Exceptions.exceptions import SQLGOStreamHandlerException
from src.core.common.common import IsListLike

class Dump(object):

    def __init__(self, file_path, write_line=False):
        self._lock = threading.Lock()
        self.file_path = os.path.abspath(file_path)
        self.write_line = write_line
        self.file_stream = open(self.file_path, "w+", encoding="utf-8")
        self.output_file = None

    def _write(self, content):
        try:
            # content = data_to_std_out(content if not is)

            with StreamReaderWriter(self.file_stream) as streamer:
                content = str(content) if not isinstance(content,str) else str(content)
                self._lock.acquire()
                streamer.write(str(content))
                if self.write_line:
                    streamer.writelines([content, '\n'])
                    streamer.seek(0)
                    for line in streamer:
                        logger.debug(line)
                
        except IOError as ex:
            raise SQLGOStreamHandlerException(f"IOError: {ex}")
        finally:
            self._lock.release()
        return content
    
    def _flush(self):
        try:
            self.file_stream.flush()
        except IOError:
            pass
    
    def set_output_file(self, content):
        self._write(content=content)
     
    def string(self,data):
        if IsListLike(data) and len(data) == 0:
            return data if isinstance(data,(tuple,list,set)) else None
        self._write(data=data)

# Instantiate Dump class
# dumper = Dump(file_path="/Users/alimirmohammad/sqlgo/future/file.txt")  
# print(dumper._write("hello "))