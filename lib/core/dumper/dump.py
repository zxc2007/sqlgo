import os
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
from lib.logger.log import logger


class Dump(object):

    def __init__(self, file_path, write_line=False, sensitive=False):
        self._lock = threading.Lock()
        self.file_path = os.path.abspath(file_path)
        self.write_line = write_line
        self.file_stream = open(self.file_path, "w+", encoding="utf-8")
        self.output_file = None
        self.sensitive = sensitive

    def _write(self, content):
        try:
            self._lock.acquire()

            with StreamReaderWriter(self.file_stream) as streamer:
                content_str = str(content)
                streamer.write(content_str)
                
                if self.write_line:
                    streamer.writelines([content_str, '\n'])
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

    def set_output_file(self, content: str):
        self._write(content=content)

    def string(self, data):
        if IsListLike(data) and len(data) == 0:
            return data if isinstance(data, (tuple, list, set)) else None

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

    def table_info(self, tables):
        if IsListLike(tables):
            for table in tables:
                if "\n" in table or "\n" in tables:
                    self._write(f"Table: {table} | count {len(range(10000, 0, -1))}")

    def dbs(self, dbs):
        self.lister("available databases", dbs, content_type=settings.ContentType.TABLE)

    def DBTables(self, tables):
        if isinstance(tables, dict):
            for table_name in tables.keys():
                self._write(f"Table: {table_name} | count {len(range(10000, 0, -1))}")

        elif isinstance(tables, Tree):
            # TODO: need to be improved
            for table_name in tables.print_child():
                self._write(f"Table: {table_name} | count {len(range(10000, 0, -1))}")

        else:
            self._write(f"Table: {tables} | count {len(range(10000, 0, -1))}")

    def dbTableColumn(self, table_column):
        try:
            if isinstance(table_column, dict) and len(table_column) != 0:
                self._write(table_column)

            for db, tables in table_column.items():
                if not db:
                    db = "All"

            for table_name, columns in table_column.items():
                logger.debug(f"Debug: Processing table {table_name}")  # Debug print
                if not isinstance(columns, dict):
                    print(f"Debug: Skipping table {table_name} as columns is not a dictionary")
                    continue

                for column in columns:
                    logger.debug(f"Debug: Processing column {column} in table {table_name}")  # Debug print
                    self._write(f"Table: {table_name} | count {len(range(10000, 0, -1))}")
                maxLength1 = 0
                maxLength2 = 0
                colType = None

                Collist = list(columns)

                Collist.sort(key=lambda _: _.lower() if hasattr(_, "lower") else _)
                for column in Collist:
                    logger.debug(f"Debug: Processing column {column} in table {table_name}")  # Debug print
                    colType = columns[column]
                    maxLength1 = max(maxLength1, len(column or ""))
                    maxLength2 = max(maxLength2, len(colType or ""))

                logger.debug(f"Debug: Max length of column names for table {table_name}: {maxLength1}")  # Debug print
                logger.debug(f"Debug: Max length of column types for table {table_name}: {maxLength2}")  # Debug print

                maxLength1 = max(maxLength1, len("COLUMN"))
                lines1 = "-" * (maxLength1 + 2)

                if colType is not None:
                    maxLength2 = max(maxLength2, len("TYPE"))
                    lines2 = "-" * (maxLength2 + 2)
                    self._write("Database %s \n Table %s" % (db if isinstance(db, str) else "", table_name))

                if len(columns) == 1:
                    self._write("[1 Column ]")
                else:
                    self._write("[%d columns]" % len(columns))

                if colType is not None:
                    self._write("+%s+%s+" % (lines1, lines2))
                else:
                    self._write("+%s+" % lines1)

                blank1 = " " * (maxLength1 - len("COLUMN"))

                if colType is not None:
                    blank2 = " " * (maxLength2 - len("TYPE"))

                if colType is not None:
                    self._write("| Column%s | Type%s |" % (blank1, blank2))
                    self._write("+%s+%s+" % (lines1, lines2))
                else:
                    self._write("| Column%s |" % blank1)
                    self._write("+%s+" % lines1)

                for column in Collist:
                    colType = columns[column]

                    blank1 = " " * (maxLength1 - len(column))

                    if colType is not None:
                        blank2 = " " * (maxLength2 - len(colType))
                        self._write("| %s%s | %s%s |" % (column, blank1, colType, blank2))
                    else:
                        self._write("| %s%s |" % (column, blank1))

                if colType is not None:
                    self._write("+%s+%s+\n" % (lines1, lines2))
                else:
                    self._write("+%s+\n" % lines1)

        except Exception as e:
            logger.error(e)



# Instantiate Dump class
# dumper = Dump(file_path="/Users/alimirmohammad/sqlgo/future/file.txt")
# print(dumper.dbTableColumn({"table": "hello world!"}))
