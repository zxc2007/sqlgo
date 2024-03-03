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
# import os
# import sys
# from src.core.dumper.dump import dumper
# from src.datastruc.tree import Tree,root
# from src.core.tester.injector.injections import make_set_injection_func
# from src.core.tester.injector.injections import time_based_injection_func
# from src.core.tester.injector.injections import error_based_INJECTION
# from src.core.tester.injector.injections import union_based_injection_function
# from src.core.tester.injector.injections import mysql_blind_based_function
# from src.core.tester.injector.injections import postgre_sql_function
# from src.core.converts.tree2dict import tree_to_dict
# from src.datastruc.magiclist import Magiclist




# class DumpAll:
#     def __init__(self,_node=None) -> None:
#         self._convert = tree_to_dict(node=_node)
#         self._magic_list = Magiclist()
        
    
#     def _tree2dict(self,*args):
#         for arg in args:
#             self._convert = tree_to_dict(node=arg if isinstance(arg,Tree) else None)
#             return self._convert
    

#     def convert_all_to(self):
#         make = make_set_injection_func()
#         time = time_based_injection_func()
#         error = error_based_INJECTION()
#         union = union_based_injection_function()
#         mysql = mysql_blind_based_function()
#         postgres = postgre_sql_function()
#         self._magic_list.append(make,time,error,union,mysql,postgres)
#         for _ in self._magic_list:
#             retval = tree_to_dict(_)
#             return retval
    

# def dumping():
#     obj = DumpAll()
#     _ = obj.convert_all_to()
#     dumper.dbTableColumn(_)
#     dumper.dbColumns(_)
#     dumper.DbTableCount(_)
#     dumper.dbs(_)


# # obj = DumpAll()
# # print(obj.convert_all_to())

