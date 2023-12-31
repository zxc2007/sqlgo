import re

def space_comment(string:str):

    modified_string = re.sub(r"\s", "--", string)
    return modified_string
