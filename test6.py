import mysql.connector

# Replace this value with your own
host = 'testfire.net'

# Connect to the MySQL server
cnx = mysql.connector.connect(host=host)

# Get the list of databases
cursor = cnx.cursor()
cursor.execute("SELECT SCHEMA_NAME FROM information_schema.SCHEMATA")
databases = [i[0] for i in cursor.fetchall()]

# Iterate through the databases
for database in databases:
    print(f"Database: {database}")
    cursor.execute(f"USE {database}")
    
    # Get the list of tables in the database
    cursor.execute("SELECT TABLE_NAME FROM information_schema.TABLES WHERE TABLE_SCHEMA = SCHEMA_NAME")
    tables = [i[0] for i in cursor.fetchall()]

    # Iterate through the tables
    for table in tables:
        print(f"Table: {table}")

        # Get the list of columns in the table
        cursor.execute(f"SELECT COLUMN_NAME FROM information_schema.COLUMNS WHERE TABLE_SCHEMA = SCHEMA_NAME AND TABLE_NAME = '{table}'")
        columns = [i[0] for i in cursor.fetchall()]
        print(f"Columns: {', '.join(columns)}")