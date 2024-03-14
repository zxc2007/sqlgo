#!/usr/bin/env python
"""
# SQLGO License - Version 1.3

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
import sqlite3
import os

class Replication:
    """
    This class holds all methods/classes used for database
    replication purposes.
    """

    def __init__(self, dbpath):
        try:
            self.dbpath = dbpath
            self.connection = sqlite3.connect(dbpath)
            self.connection.isolation_level = None
            self.cursor = self.connection.cursor()
            # Create a new database file if it doesn't exist
            self.create_database()
        except sqlite3.OperationalError as ex:
            errMsg = "Error occurred while opening a replication "
            errMsg += f"file '{dbpath}' ('{ex}')"
            raise errMsg

    def create_database(self):
        """
        Create a new SQLite database file if it doesn't exist.
        """
        if not os.path.exists(self.dbpath):
            try:
                open(self.dbpath, 'w').close()  # Create an empty file
                print(f"SQLite database created at {self.dbpath}")
            except Exception as ex:
                errMsg = f"Error creating SQLite database: {ex}"
                raise errMsg

    class DataType:
        """
        Using this class we define auxiliary objects
        used for representing sqlite data types.
        """

        def __init__(self, name):
            self.name = name

        def __str__(self):
            return self.name

        def __repr__(self):
            return f"<DataType: {self}>"

    class Table:
        """
        This class defines methods used to manipulate table objects.
        """

        def __init__(self, parent, name, columns=None, create=True, typeless=False):
            self.parent = parent
            self.name = name
            self.columns = columns
            if create:
                try:
                    self.execute(f'DROP TABLE IF EXISTS "{self.name}"')
                    if not typeless:
                        self.execute(f'CREATE TABLE "{self.name}" ({",".join(f"{colname} {coltype}" for colname, coltype in self.columns)})')
                    else:
                        self.execute(f'CREATE TABLE "{self.name}" ({",".join(f"{colname}" for colname in self.columns)})')
                except Exception as ex:
                    errMsg = f"Problem occurred ('{ex}') while initializing the SQLite database "
                    errMsg += f"located at '{self.parent.dbpath}'"
                    raise errMsg

        def insert(self, values):
            if len(values) == len(self.columns):
                self.execute(f'INSERT INTO "{self.name}" VALUES ({",".join(["?"] * len(values))})', values)
            else:
                errMsg = "Wrong number of columns used in replicating insert"
                raise errMsg

        def execute(self, sql, parameters=None):
            try:
                try:
                    self.parent.cursor.execute(sql, parameters or [])
                    self.parent.connection.commit()  # Commit changes to the database
                    return self.parent.cursor  # Return the cursor for SELECT operations
                except sqlite3.OperationalError as ex:
                    errMsg = f"Error during execution of SQL query ('{ex}')"
                    raise errMsg
                except Exception as ex:
                    errMsg = f"Unexpected error during execution ('{ex}')"
                    raise errMsg
            except sqlite3.OperationalError as ex:
                errMsg = f"Problem occurred ('{ex}') while accessing SQLite database "
                errMsg += f"located at '{self.parent.dbpath}'. Please make sure that "
                errMsg += "it's not used by some other program"
                raise errMsg

        def begin_transaction(self):
            """
            Great speed improvement can be gained by using explicit transactions around multiple inserts.
            Reference: http://stackoverflow.com/questions/4719836/python-and-sqlite3-adding-thousands-of-rows
            """
            self.execute('BEGIN TRANSACTION')

        def end_transaction(self):
            self.execute('END TRANSACTION')

        def select(self, condition=None):
            """
            This function is used for selecting row(s) from the current table.
            """
            _ = f'SELECT * FROM {self.name}'
            if condition:
                _ += f' WHERE {condition}'
            result = self.execute(_)
            if result:
                return result.fetchall()
            else:
                print("Error during SELECT operation.")
                return None

    def create_table(self, tblname, columns=None, typeless=False):
        """
        This function creates a Table instance with current connection settings.
        """
        return Replication.Table(parent=self, name=tblname, columns=columns, typeless=typeless)

    def __del__(self):
        self.cursor.close()
        self.connection.close()

    # SQLite data types
    NULL = DataType('NULL')
    INTEGER = DataType('INTEGER')
    REAL = DataType('REAL')
    TEXT = DataType('TEXT')
    BLOB = DataType('BLOB')

# Example Usage:
# db_path = 'database.db'

# # Create a Replication instance and a new database
# replication_instance = Replication(db_path)

# # Create a table
# table = replication_instance.create_table('example_table', columns=[('id', Replication.INTEGER), ('name', Replication.TEXT)])

# # Insert a row into the table
# table.insert([1, 'John Doe'])

# # Select all rows from the table
# result = table.select()
# if result:
#     print(result)
# else:
#     print("Error occurred during SELECT operation.")

# # Cleanup
# del replication_instance
