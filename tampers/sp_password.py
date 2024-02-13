
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
def tamper(payload, **kwargs):
    """
    Appends (MsSQL) function 'sp_password' to the end of the payload for automatic obfuscation from DBMS logs

    Requirement:
        * MSSQL

    Notes:
        * Appending sp_password to the end of the query will hide it from T-SQL logs as a security measure
        * Reference: http://websec.ca/kb/sql_injection

    >>> tamper('1 AND 9227=9227-- ')
    '1 AND 9227=9227-- sp_password'
    """

    retVal = ""

    if payload:
        retVal = "%s%ssp_password" % (payload, "-- " if not any(_ if _ in payload else None for _ in ('#', "-- ")) else "")

    return retVal