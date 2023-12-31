import argparse

class Cmdline(argparse.ArgumentParser):
    def __init__(self):
        super().__init__(description="sqlgo")

        self.add_argument("-o", "--output", help="Get output file as result",required=False)
        self.add_argument("--verbose", action="store_true", help="Enable verbose mode")
        self.add_argument("--url","-u",help="Give the program url of the target",required=True)
        self.add_argument("--port","-p",help="Specify the port for the injection",required=False)
        self.add_argument("--inspect","-insp",help="Inspect the target response",required=False)
        self.add_argument("--column","-C",help="Specify the database possible column",required=False)
        self.add_argument("--table","-T",help="Specify the database possible table",required=False)
        self.add_argument("--dbms",help="Specify the DBMS of the server",required=False)
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



    

# if __name__ == "__main__":
#     parser = Cmdline()
#     args = parser.parse_args()
    
#     # Use the parsed arguments as needed
#     print(args.file)
#     print(args.output)
#     print(args.verbose)

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
        time_out
    )

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



