import os
import sys

def read_common_tables():
    """
    >>> _ = read_common_tables()

    >>> for i in _:
        ... for j in i:
            ... print(j)
    """
    cwd = os.getcwd()
    targetdir = cwd+"/data/txt/common-tables.txt"
    with open(targetdir, 'r') as f:
        payload = f.read() 
        rows = payload.split("\n") 
        sorted_rows = sorted(rows)
        sorted_payload = "\n".join(sorted_rows) 
        yield sorted_payload.split("\n")

