import copy
import types
import os
import sys
sys.path.append(os.getcwd())
from lib.datastruc.magiclist import Magiclist
class AttribDict(dict):
    """
    This class defines the dictionary with added capability to access members as attributes

    >>> foo = AttribDict()
    >>> foo.bar = 1
    >>> foo.bar
    1
    """

    def __init__(self, indict=None, attribute=None, keycheck=True):
        if indict is None:
            indict = {}

        # Set any attributes here - before initialisation
        # these remain as normal attributes
        self.attribute = attribute
        self.keycheck = keycheck
        dict.__init__(self, indict)
        self.__initialised = True

        # After initialisation, setting attributes
        # is the same as setting an item

    def __getattr__(self, item):
        """
        Maps values to attributes
        Only called if there *is NOT* an attribute with this name
        """

        try:
            return self.__getitem__(item)
        except KeyError:
            if self.keycheck:
                raise AttributeError("unable to access item '%s'" % item)
            else:
                return None

    def __delattr__(self, item):
        """
        Deletes attributes
        """

        try:
            return self.pop(item)
        except KeyError:
            if self.keycheck:
                raise AttributeError("unable to access item '%s'" % item)
            else:
                return None

    def __setattr__(self, item, value):
        """
        Maps attributes to values
        Only if we are initialised
        """

        # This test allows attributes to be set in the __init__ method
        if "_AttribDict__initialised" not in self.__dict__:
            return dict.__setattr__(self, item, value)

        # Any normal attributes are handled normally
        elif item in self.__dict__:
            dict.__setattr__(self, item, value)

        else:
            self.__setitem__(item, value)

    def __getstate__(self):
        return self.__dict__

    def __setstate__(self, dict):
        self.__dict__ = dict

    def __deepcopy__(self, memo):
        retVal = self.__class__()
        memo[id(self)] = retVal

        for attr in dir(self):
            if not attr.startswith('_'):
                value = getattr(self, attr)
                if not isinstance(value, (types.BuiltinFunctionType, types.FunctionType, types.MethodType)):
                    setattr(retVal, attr, copy.deepcopy(value, memo))

        for key, value in self.items():
            retVal.__setitem__(key, copy.deepcopy(value, memo))

        return retVal

class InjectionDict(AttribDict):
    """
    >>> foo = AttribDict()
    >>> foo.bar = 1
    >>> print(foo.bar)  # Output: 1

    # Creating an instance of InjectionDict
    >>> injection_data = InjectionDict()
    >>> injection_data.place = "example"
    >>> injection_data.parameter = "param"
    >>> injection_data.data.example = "example_data"
    >>> print(injection_data.place)  # Output: example
    >>> print(injection_data.data.example)  # Output: example_data
    """
    def __init__(self):
        AttribDict.__init__(self)

        self.place = None
        self.parameter = None
        self.ptype = None
        self.prefix = None
        self.suffix = None
        self.clause = None
        self.notes = []  # Note: https://github.com/sqlmapproject/sqlmap/issues/1888

        # data is a dict with various stype, each which is a dict with
        # all the information specific for that stype
        self.data = AttribDict()

        # conf is a dict which stores current snapshot of important
        # options used during detection
        self.conf = AttribDict()

        self.dbms = None
        self.dbms_version = None
        self.os = None
        self.general = Magiclist()
    
    def add_data(self,*args):
        for arg in args:
            self.general.append(arg)
    
    def add_dbms(self,*args):
        self.dbms = Magiclist()
        for arg in args:
            self.dbms.append(arg)
    def extra_data(self,*args):
        self.dbms = Magiclist()
        for arg in args:
            self.data.extra.append(arg)
    

injeciondict = InjectionDict()


# # Creating an instance of AttribDict
# foo = AttribDict()
# foo.bar = 1
# print(foo.bar)  # Output: 1

# # Creating an instance of InjectionDict
# injection_data = InjectionDict()
# injection_data.place = "example"
# injection_data.parameter = "param"
# injection_data.data.example = "example_data"
# print(injection_data.place)  # Output: example
# print(injection_data.data.example)  # Output: example_data

def extract_injection():
    print(injeciondict.data.example)
