#!/usr/bin/env python
"""
# SQLGO License - Version 1.4

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

_errors = """
root
dbms
error
SQL syntax.*?MySQL
Warning.*?\Wmysqli?_
MySQLSyntaxErrorException
valid MySQL result
check the manual that (corresponds to|fits) your MySQL server version
check the manual that (corresponds to|fits) your MariaDB server version
_fork MariaDB
check the manual that (corresponds to|fits) your Drizzle server version
_fork Drizzle
Unknown column '[^ ]+' in 'field list'
MySqlClient\.
com\.mysql\.jdbc
Zend_Db_(Adapter|Statement)_Mysqli_Exception
Pdo[./_\\]Mysql
MySqlException
SQLSTATE\[\d+\]: Syntax error or access violation
MemSQL does not support this type of query
_fork MemSQL
is not supported by MemSQL
_fork MemSQL
unsupported nested scalar subselect
_fork MemSQL
you have an error in your sql syntax;
_fork MemSQL
_value MySQL
error
PostgreSQL.*?ERROR
Warning.*?\Wpg_
valid PostgreSQL result
Npgsql\.
PG::SyntaxError:
org\.postgresql\.util\.PSQLException
ERROR:\s\ssyntax error at or near
ERROR: parser: parse error at or near
PostgreSQL query failed
org\.postgresql\.jdbc
Pdo[./_\\]Pgsql
PSQLException
_value PostgreSQL
error
Driver.*? SQL[\-\_\ ]*Server
OLE DB.*? SQL Server
\bSQL Server[^<"]+Driver
Warning.*?\W(mssql|sqlsrv)_
\bSQL Server[^<"]+[0-9a-fA-F]{8}
System\.Data\.SqlClient\.(SqlException|SqlConnection\.OnError)
(?s)Exception.*?\bRoadhouse\.Cms\.
Microsoft SQL Native Client error '[0-9a-fA-F]{8}
\[SQL Server\]
ODBC SQL Server Driver
ODBC Driver \d+ for SQL Server
SQLServer JDBC Driver
com\.jnetdirect\.jsql
macromedia\.jdbc\.sqlserver
Zend_Db_(Adapter|Statement)_Sqlsrv_Exception
com\.microsoft\.sqlserver\.jdbc
Pdo[./_\\](Mssql|SqlSrv)
SQL(Srv|Server)Exception
Unclosed quotation mark after the character string
_value Microsoft SQL Server
error
Microsoft Access (\d+ )?Driver
JET Database Engine
Access Database Engine
ODBC Microsoft Access
Syntax error \(missing operator\) in query expression
_value Microsoft Access
error
\bORA-\d{5}
Oracle error
Oracle.*?Driver
Warning.*?\W(oci|ora)_
quoted string not properly terminated
SQL command not properly ended
macromedia\.jdbc\.oracle
oracle\.jdbc
Zend_Db_(Adapter|Statement)_Oracle_Exception
Pdo[./_\\](Oracle|OCI)
OracleException
_value Oracle
error
CLI Driver.*?DB2
DB2 SQL error
\bdb2_\w+\(
SQLCODE[=:\d, -]+SQLSTATE
com\.ibm\.db2\.jcc
Zend_Db_(Adapter|Statement)_Db2_Exception
Pdo[./_\\]Ibm
DB2Exception
ibm_db_dbi\.ProgrammingError
_value IBM DB2
error
Warning.*?\Wifx_
Exception.*?Informix
Informix ODBC Driver
ODBC Informix driver
com\.informix\.jdbc
weblogic\.jdbc\.informix
Pdo[./_\\]Informix
IfxException
_value Informix
error
Dynamic SQL Error
Warning.*?\Wibase_
org\.firebirdsql\.jdbc
Pdo[./_\\]Firebird
_value Firebird
error
SQLite/JDBCDriver
SQLite\.Exception
(Microsoft|System)\.Data\.SQLite\.SQLiteException
Warning.*?\W(sqlite_|SQLite3::)
\[SQLITE_ERROR\]
SQLite error \d+:
sqlite3.OperationalError:
SQLite3::SQLException
org\.sqlite\.JDBC
Pdo[./_\\]Sqlite
SQLiteException
_value SQLite
error
SQL error.*?POS([0-9]+)
Warning.*?\Wmaxdb_
DriverSapDB
-3014.*?Invalid end of SQL statement
com\.sap\.dbtech\.jdbc
\[-3008\].*?: Invalid keyword or missing delimiter
_value SAP MaxDB
error
Warning.*?\Wsybase_
Sybase message
Sybase.*?Server message
SybSQLException
Sybase\.Data\.AseClient
com\.sybase\.jdbc
_value Sybase
error
Warning.*?\Wingres_
Ingres SQLSTATE
Ingres\W.*?Driver
com\.ingres\.gcf\.jdbc
_value Ingres
error
Exception (condition )?\d+\. Transaction rollback
com\.frontbase\.jdbc
Syntax error 1. Missing
(Semantic|Syntax) error [1-4]\d{2}\.
_value FrontBase
error
Unexpected end of command in statement \[
Unexpected token.*?in statement \[
org\.hsqldb\.jdbc
_value HSQLDB
error
org\.h2\.jdbc
\[42000-192\]
_value H2
error
![0-9]{5}![^\n]+(failed|unexpected|error|syntax|expected|violation|exception)
\[MonetDB\]\[ODBC Driver
nl\.cwi\.monetdb\.jdbc
_value MonetDB
error
Syntax error: Encountered
org\.apache\.derby
ERROR 42X01
_value Apache Derby
error
, Sqlstate: (3F|42).{3}, (Routine|Hint|Position):
/vertica/Parser/scan
com\.vertica\.jdbc
org\.jkiss\.dbeaver\.ext\.vertica
com\.vertica\.dsi\.dataengine
_value Vertica
error
com\.mckoi\.JDBCDriver
com\.mckoi\.database\.jdbc
<REGEX_LITERAL>
_value Mckoi
error
com\.facebook\.presto\.jdbc
io\.prestosql\.jdbc
com\.simba\.presto\.jdbc
UNION query has different number of fields: \d+, \d+
_value Presto
error
Altibase\.jdbc\.driver
_value Altibase
error
com\.mimer\.jdbc
Syntax error,[^\n]+assumed to mean
_value MimerSQL
error
io\.crate\.client\.jdbc
_value CrateDB
error
encountered after end of query
A comparison operator is required here
_value Cache
error
-10048: Syntax error
rdmStmtPrepare\(.+?\) returned
_value Raima Database Manager
error
SQ074: Line \d+:
SR185: Undefined procedure
SQ200: No table 
Virtuoso S0002 Error
\[(Virtuoso Driver|Virtuoso iODBC Driver)\]\[Virtuoso Server\]
_value Virtuoso

"""

error_lines = _errors.splitlines()



errors = [error_lines]