import os
import hashlib
import sys
import threading
sys.path.append(os.getcwd())
from lib.conf.conf import data_to_std_out
from future.wariterdata import StreamReaderWriter
from lib.logger.log import logger
from lib.core.Exceptions.exceptions import SQLGOStreamHandlerException
from lib.core.common.common import IsListLike
import lib.core.setting.setting as settings
from lib.datastruc.tree import Tree


class Dump(object):

    def __init__(self, file_path, write_line=False,sensitive=False):
        self._lock = threading.Lock()
        self.file_path = os.path.abspath(file_path)
        self.write_line = write_line
        self.file_stream = open(self.file_path, "w+", encoding="utf-8")
        self.output_file = None
        self.sensitive = sensitive

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
    
    def set_output_file(self, content:str):
        self._write(content=content)
     
    def string(self,data):
        if IsListLike(data) and len(data) == 0:
            return data if isinstance(data,(tuple,list,set)) else None
        
        if self.sensitive:
            self._flush()
            self._write(data=data)
            
            return

        self._write(data=data)

    def lister(self, header, elements, content_type=None, sort=True):
        if elements and sort:
            try:
                elements = set(elements)
                elements = list(elements)
                elements.sort(key=lambda _: _.lower() if hasattr(_, "lower") else _)
            except:
                pass



        if elements:
            self._write("%s [%d]:" % (header, len(elements)))

        for element in elements:
            if isinstance(element, str):
                self._write("[*] %s" % element)
            elif IsListLike(element):
                self._write("[*] " + ", ".join(e for e in element))

        if elements:
            self._write("")

    
    def table_info(self,tables):
        if IsListLike(tables):
            for table in tables:
                if "\n" in table or "\n" in tables:
                    self._write("Table: %s | count %d"%(table,_ for _ in range(10000,0,-1)))
    
    def dbs(self,dbs):
        self.lister("available databases",dbs,content_type=settings.ContentType.TABLE)
    
    def DBTables(self,table):
        if isinstance(table,dict):
            for table_name in table.keys():
                self._write("Table: %s | count %d"%(table_name,_ for _ in range(10000,0,-1)))
                return
        
        elif isinstance(table,Tree):
            #TODO:need to be improved
            for table_name in table.print_child():
                self._write("Table: %s | count %d"%(table_name,_ for _ in range(10000,0,-1)))
                return
    
        self._write("Table: %s | count %d"%(table_name,_ for _ in range(10000,0,-1)))
        

# Instantiate Dump class
# dumper = Dump(file_path="/Users/alimirmohammad/sqlgo/future/file.txt")  
# print(dumper._write("hello "))