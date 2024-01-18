import os
import sys
sys.path.append(os.getcwd())
from lib.core.dumper.dump import dumper
from lib.datastruc.tree import Tree,root
from lib.core.tester.injector.injections import make_set_injection_func
from lib.core.tester.injector.injections import time_based_injection_func
from lib.core.tester.injector.injections import error_based_INJECTION
from lib.core.tester.injector.injections import union_based_injection_function
from lib.core.tester.injector.injections import mysql_blind_based_function
from lib.core.tester.injector.injections import postgre_sql_function
from lib.core.converts.tree2dict import tree_to_dict
from lib.datastruc.magiclist import Magiclist




class DumpAll:
    def __init__(self,_node=None) -> None:
        self._convert = tree_to_dict(node=_node)
        self._magic_list = Magiclist()
        
    
    def _tree2dict(self,*args):
        for arg in args:
            self._convert = tree_to_dict(node=arg if isinstance(arg,Tree) else None)
            return self._convert
    

    def convert_all_to(self):
        make = make_set_injection_func()
        time = time_based_injection_func()
        error = error_based_INJECTION()
        union = union_based_injection_function()
        mysql = mysql_blind_based_function()
        postgres = postgre_sql_function()
        self._magic_list.append(make,time,error,union,mysql,postgres)
        for _ in self._magic_list:
            retval = tree_to_dict(_)
            return retval
    

def dumping():
    obj = DumpAll()
    _ = obj.convert_all_to()
    dumper.dbTableColumn(_)
    dumper.dbColumns(_)
    dumper.DbTableCount(_)
    dumper.dbs(_)


# obj = DumpAll()
# print(obj.convert_all_to())

