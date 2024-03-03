#!/usr/bin/env python
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
import argparse
import os
try:
    from urllib.parse import urlparse
except:
    from urlparse import urlparse

import sys
import sys

import extras.version
from src.datastruc.attrdict import api
from src.data import arg
from src.core.common.common import _listTamperingFunctions




class Cmdline(argparse.ArgumentParser):
    def __init__(self):
        super(Cmdline, self).__init__(description="sqlgo")

        self.add_argument("-o", "--output", help="Get output file as result",required=False)
        self.add_argument("--verbose", action="store", help="Enable verbose mode and set the range of(default is 1)",type=int,required=False,default=1)
        self.add_argument("--version",action="version",version="SQLgo version: "+extras.version.VERSION)
        self.add_argument("--url","-u",help="Give the program url of the target",required=False,default=3306)
        self.add_argument("--port","-p",help="Specify the port for the injection",required=False,type=int)
        self.add_argument("--inspect","-insp",help="Inspect the target response",required=False)
        self.add_argument("--column","-C",help="Specify the database possible column",required=False)
        self.add_argument("--table","-T",help="Specify the database possible table",required=False)
        self.add_argument("--dbms",help="Specify the DBMS of the server",required=False,type=str,default="mysql")
        self.add_argument("--db","-d",help="Specify the database name",required=False,action="store_true")
        self.add_argument("-dbs",help="Enumerate the DBMS databases",required=False,action="store_true")
        self.add_argument("-tables",help="Enumerate the DBMS tables",required=False,action="store_true")
        self.add_argument("--columns",help="Enumerate the DBMS columns",required=False,action="store_true")
        self.add_argument("--random-agent",help="Use random user agents",required=False,action="store_true")
        self.add_argument("--user-agent",help="Specify the user agent",required=False)
        self.add_argument("--dump",help="Dump the databases and show user",required=False,action="store_true")
        self.add_argument("--dump-table",help="Dump the tables and show user",required=False,action="store_true")
        self.add_argument("--dump-column",help="Dump the columns and show user",required=False,action="store_true")
        self.add_argument("--dump-user",help="Dump the users",required=False,action="store_true")
        self.add_argument("--dump-password",help="Dump the passwords",required=False,action="store_true")
        self.add_argument("--time-out",help="Set timeout amount",type=int,required=False)
        self.add_argument("--attack",help="Specify the attack type",default="normal",type=str,required=False)
        self.add_argument("--install-dependent",help="install the required modules for sqlgo to be executed",action="store_true",required=False)
        self.add_argument("--disable-warning",help="disable the ssl warning",action="store_true",required=False)
        self.add_argument("--payload",help="send you own payload",required=False,action="store_true")
        self.add_argument("--proxy-server",help="specify the proxyserver",type=str,required=False)
        self.add_argument("--proxy-port",help="specify proxy port ",action="store",type=int,required=False)
        self.add_argument("--proxy",help="use proxy servers",required=False,action="store_true")
        self.add_argument("--level",help="increase the level of performing tests(from range 1-5 default is 1 )",type=int,default=1,required=False)
        self.add_argument("--tamper",help="use tampers for specifying the payloads specific changes,eg: --tamper space2plus",required=False,type=str)
        self.add_argument("--time-based-t",help="specify the treshold of the time base injection (only for the time based injection,default = 0.5)",type=float,required=False)
        self.add_argument("--crawl",help="add crawling tests",action="store_true",required=False)
        self.add_argument("--shell", help="execute sqlgo in shell environment", required=False,action="store_true")
        self.add_argument("--update", help="update sqlgo", required=False,action="store_true")
        self.add_argument("--beep", help="beep when vulnerability info appeared.", required=False,action="store_true")
        self.add_argument("--no-prompt", help="do not show user any prompt unless found important info.", required=False,action="store_true")
        self.add_argument("--username",help="Specify the DBMS username",required=False)
        self.add_argument("--password",help="Specify the DBMS password",required=False)
        self.add_argument("--username-wordlist",help="use wordlist to specify the brute force attack",required=False)
        self.add_argument("--password-wordlist",help="use wordlist to specify the brute force attack",required=False)
        self.add_argument("--dbs-port",help="specify the DBMS port",required=False)
        self.add_argument("--dbs-timeout",help="specify the timeout amount for the connection to DBMS",default=10)
        self.add_argument("--dbms-user",help="specify the DBMS possible username",required=False)
        self.add_argument("--dbms-pass",help="specify the DBMS possible password",required=False)
        self.add_argument("--hydra",help="use hydra for brute force attack",required=False,action="store_true")
        self.add_argument("--user-file",help="specify the username file for hydra",required=False)
        self.add_argument("--pass-file",help="specify the password file for hydra",required=False)
        self.add_argument("--delay-time",help="specify the time of delay whenever found potential SQL injection vulnerability",required=False,type=int,default=10)
        self.add_argument("--accept-cookie",help="Accept the cookies by the server by default",action="store_true")
        self.add_argument("--list-tampers",help="list all available tamper functions",action="store_true")
        self.add_argument("--skip-basic",help="skip basic tests",action="store_true",required=False)
        self.add_argument("--batch",help="batch mode,never ask user for any input.",action="store_true",required=False)






    



def extract():
    obj = Cmdline()
    args = obj.parse_args()
    output = args.output
    verbose = args.verbose
    url = args.url
    port = args.port
    inspect = args.inspect
    column = args.column
    table = args.table
    dbms = args.dbms
    db = args.db
    dbs = args.dbs
    tables = args.tables
    columns = args.columns
    random_agent = args.random_agent
    user_agent = args.user_agent
    dump = args.dump
    dump_table = args.dump_table
    dump_column = args.dump_column
    dump_user = args.dump_user
    dump_password = args.dump_password
    time_out = args.time_out
    attack = args.attack
    install = args.install_dependent
    warning_dis = args.disable_warning
    payload = args.payload
    Proxy_server = args.proxy_server
    Proxy_port = args.proxy_port
    user_proxy = args.proxy
    level = args.level
    tamper = args.tamper
    time_based_treshold = args.time_based_t
    crawl = args.crawl
    shell = args.shell
    update = args.update
    beep = args.beep
    no_prompt = args.no_prompt
    username = args.username
    password = args.password
    username_wordlist = args.username_wordlist
    password_wordlist = args.password_wordlist
    dbs_port = args.dbs_port
    dbs_timeout = args.dbs_timeout
    dbms_user = args.dbms_user
    dbms_pass = args.dbms_pass
    user_file = args.user_file
    pass_file = args.pass_file
    hydra = args.hydra
    delay_time = args.delay_time
    accept_cookie = args.accept_cookie
    list_tampers = args.list_tampers
    skip_basic = args.skip_basic
    batch = args.batch
    return (
        output,
        verbose,
        url,
        port,
        inspect,
        column,
        table,
        dbms,
        db,
        dbs,
        tables,
        columns,
        random_agent,
        user_agent,
        dump,
        dump_table,
        dump_column,
        dump_user,
        dump_password,
        time_out,
        attack,
        install,
        warning_dis,
        payload,
        Proxy_server,
        Proxy_port,
        user_proxy,
        level,
        tamper,
        time_based_treshold,
        crawl,
        shell,
        update,
        beep,
        no_prompt,
        username,
        password,
        username_wordlist,
        password_wordlist,
        dbs_port,
        dbs_timeout,
        dbms_user,
        dbms_pass,
        user_file,
        pass_file,
        hydra,
        delay_time,
        accept_cookie,
        list_tampers,
        skip_basic,
        batch
    )


try:
    result = extract()
    output = result[0]
    verbose = result[1]
    url = result[2]
    port = result[3]
    inspect = result[4]
    column = result[5]
    table = result[6]
    dbms = result[7]
    db = result[8]
    dbs = result[9]
    tables = result[10]
    columns = result[11]
    random_agent = result[12]
    user_agent = result[13]
    dump = result[14]
    dump_table = result[15]
    dump_column = result[16]
    dump_user = result[17]
    dump_password = result[18]
    time_out = result[19]
    attack = result[20]
    install_dep = result[21]
    warning_disable = result[22]
    payload = result[23]
    proxy_server = result[24]
    proxy_port = result[25]
    user_proxy = result[26]
    level = result[27]
    tamper = result[28]
    time_based_tres = result[29]
    crawl = result[30]
    shell = result[31]
    update = result[32]
    beep = result[33]
    no_prompt = result[34]
    username = result[35]
    password = result[36]
    username_wordlist = result[37]
    password_wordlist = result[38]
    dbs_port = result[39]
    dbs_timeout = result[40]
    dbms_user = result[41]
    dbms_pass = result[42]
    user_file = result[43]
    pass_file = result[44]
    hydra = result[45]
    delay_time = result[46]
    accept_cookie = result[47]
    list_tampers = result[48]


    arg.output = result[0]
    arg.verbose = result[1]
    arg.url = result[2]
    arg.port = result[3]
    arg.inspect = result[4]
    arg.column = result[5]
    arg.table = result[6]
    arg.dbms = result[7]
    arg.db = result[8]
    arg.dbs = result[9]
    arg.tables = result[10]
    arg.columns = result[11]
    arg.random_agent = result[12]
    arg.user_agent = result[13]
    arg.dump = result[14]
    arg.dump_table = result[15]
    arg.dump_column = result[16]
    arg.dump_user = result[17]
    arg.dump_password = result[18]
    arg.time_out = result[19]
    arg.attack = result[20]
    arg.install_dep = result[21]
    arg.warning_disable = result[22]
    arg.payload = result[23]
    arg.proxy_server = result[24]
    arg.proxy_port = result[25]
    arg.user_proxy = result[26]
    arg.level = result[27]
    arg.tamper = result[28]
    arg.time_based_tres = result[29]
    arg.crawl = result[30]
    arg.shell = result[31]
    update = result[32]
    arg.beep = result[33]
    arg.no_prompt = result[34]
    arg.username = result[35]
    arg.password = result[36]
    arg.username_wordlist = result[37]
    arg.password_wordlist = result[38]
    arg.dbs_port = result[39]
    arg.dbs_timeout = result[40]
    arg.dbms_user = result[41]
    arg.dbms_pass = result[42]
    arg.user_file = result[43]
    arg.pass_file = result[44]
    arg.hydra = result[45]
    arg.delay_time = result[46]
    arg.accept_cookie = result[47]
    arg.listTamper = result[48]
    arg.skipBasic = result[49]
    arg.batch = result[50]
except MemoryError:
    print("Could not allocate memory for the args namepace, exiting...")

if arg.listTamper:
    _listTamperingFunctions()
    raise SystemExit


if update:
    api.updates = True
else:
    api.updates = False


# conf.dbmsUser = dbms_user or ""
# conf.dbmsPass = dbms_pass or ""
# conf.hostname = urlparse(url).hostname
# conf.port = 3306 if dbms == "mysql" and dbms is not None else ""
# conf.dbmsDb = dbs or ""
# conf.dbms = dbms or "mysql"
# kb.timeout = dbs_timeout
# conf.timeout = dbs_timeout
# conf.dbmsHandler = "f"