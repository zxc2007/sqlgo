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
SQL_STATEMENTS = {
    "SQL SELECT statement": (
        "select ",
        "show ",
        " top ",
        " distinct ",
        " from ",
        " from dual",
        " where ",
        " group by ",
        " order by ",
        " having ",
        " limit ",
        " offset ",
        " union all ",
        " rownum as ",
        "(case ",
    ),

    "SQL data definition": (
        "create ",
        "declare ",
        "drop ",
        "truncate ",
        "alter ",
    ),

    "SQL data manipulation": (
        "bulk ",
        "insert ",
        "update ",
        "delete ",
        "merge ",
        "load ",
    ),

    "SQL data control": (
        "grant ",
        "revoke ",
    ),

    "SQL data execution": (
        "exec ",
        "execute ",
        "values ",
        "call ",
    ),

    "SQL transaction": (
        "start transaction ",
        "begin work ",
        "begin transaction ",
        "commit ",
        "rollback ",
    ),

    "SQL administration": (
        "set ",
    ),
}