import os
import sys
import time
import warnings


sys.path.append(os.getcwd())

from lib.core.Exceptions.exceptions import SQLgoNoneKeyException
from lib.core.Exceptions.exceptions import SQLgoKeyGenDictKeyException
from lib.core._Warnings.warnings_ import KeyKeptTooLongWarning

class Keygendict(dict):
    """
    *Usage:
    setting some key and values
    >>> keygen = Keygendict()
    >>> keygen.add_cap('key1','value1')
    >>> keygen.add_cap('key2','value2')
    *Getting data
    >>> keygen.get_all_data()
    {'key1': 'value1', 'key2': 'value2'}
    NOTE: it is not recommended to remove the key and values by hand, instead the dict will remove the None key and values auto,however we have __delitem__ method but it might not work most of time
    *get capacity of the dict
    >>> keygen.dict_capacity_calculation()
    NOTE: read the methods docstring to see the order of returns
    >>> keygen.is_double()
    *return the duplicated keys


    """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.caps = {}
        self._keysum = None
        self._valuesum = None
        self._capacity = None
        self._start = time.monotonic()
        self.duplicate_keys = set()
        self.seen = set(key for key,_ in self.caps.items())

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
            self.dict_capacity_calculation()  
        else:
            raise SQLgoKeyGenDictKeyException
        
    def __getitem__(self,key):
        value = self.caps.get(key)
        if value is not None:
            return value
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
    
    def _trigger_warning_for_key(self):
        if self._calculate_time_of_key_value() == -1:
            pass
        else:
            if self._calculate_time_of_key_value() > 100:
                warnings.warn("You have kept the key too long in the Keygen dict, it is not recommended",category=KeyKeptTooLongWarning)
    
    def _identify_duplicated(self):
        for key in self.caps:
            if key in self.seen:
                self.duplicate_keys.add(key)
                return self.duplicate_keys
            else:
                self.seen.add(key)
                return self.seen
    
    def is_double(self):
        return self._identify_duplicated()
            
    def get_all_data(self):
        return self.caps

            
    



    

# diction = Keygendict()


# diction.add_cap("A",2)
# diction.add_cap("R","Hello")
# diction.add_cap("B",1)
# diction.add_cap("C",None)



# print(diction.dict_capacity_calculation())