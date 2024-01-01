import os
import sys
import time


sys.path.append(os.getcwd())

from lib.core.Exceptions.exceptions import SQLgoNoneKeyException
from lib.core.Exceptions.exceptions import SQLgoKeyGenDictKeyException

class Keygendict(dict):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.caps = {}
        self._keysum = None
        self._valuesum = None
        self._capacity = None
        self._start = time.monotonic()

    def _rm_None(self):
        keys_to_remove = []
        for key, value in self.caps.items():
            if value is None:
                keys_to_remove.append(key)

        for key in keys_to_remove:
            del self.caps[key]
    
    def _add_key_caps(self,key,value):
        self.caps[key] = value
        self._rm_None()
    
    def add_cap(self,key,value):
        _retval = None
        _ = self._add_key_caps(key=key,value=value)
        for _key,_value in self.items():
            if _key is None:
                raise SQLgoNoneKeyException
            
            elif _value is None:
                self._rm_None()

        _retval = _
        return _retval
    
    def __len__(self) -> int:
        return super().__len__()
    
    def __delitem__(self,key) -> None:
        if key in self.caps:
            del self.caps[key]
        else:
            raise SQLgoKeyGenDictKeyException
        
    def __getitem__(self,key):
        if key in self.items:
            return self.caps[key]
        else:
            raise SQLgoKeyGenDictKeyException
    
    def dict_capacity_calculation(self):
        """
        NOTE:capacity,keysum,valuesum
        """
        _retval = None
        self._keysum = sum(len(str(key)) for key in self.caps.keys())
        self._valuesum = sum(len(str(value)) for value in self.caps.values())
        self._capacity = self._keysum + self._valuesum
        _retval = (self._capacity,
                self._keysum,
                self._valuesum)
        return _retval
    
    def _calculate_time_of_key_value(self):
        if self._start is not None:
            duration = time.monotonic() - self._start
            return duration
        else:
            return -1

            
    



    

diction = Keygendict()


diction.add_cap("A",None)
diction.add_cap("B",45)

print(diction._calculate_time_of_key_value())