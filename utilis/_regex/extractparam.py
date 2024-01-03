import re
import os
import sys
sys.path.append(os.getcwd())
from lib.core.Exceptions.exceptions import SQLgoNoParameterFoundException
from lib.core.payloads.makesetsqlpayload import classify,_sorted
from utilis.colorago.colorago import Fore

def replace_url_parameter(url, new_value):
    """
    >>> url = "www.example.com?id=1&name=John&age=25"
    >>> new_value = input("Enter the new value: ")

    >>> replaced_url = replace_url_parameter(url, new_value)
    >>> print(replaced_url)
    NOTE: return would be url,parameter
    """
    pattern = r"(\?|\&)([^=]+)=[^&]*"
    replaced_url = re.sub(pattern, rf"\1\2={new_value}", url)
    extracted_value = re.search(pattern, url).group()
    if not replace_url_parameter:
        raise SQLgoNoParameterFoundException
    return replaced_url,Fore.BRIGHT_CYAN+str(extracted_value)

#http://testfire.net/index.jsp?content=business_deposit.htm



# print(replace_url_parameter(url="http://testfire.net/index.jsp?content=business_deposit.htm",new_value=_sorted))


