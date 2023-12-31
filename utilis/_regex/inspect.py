import re

def id_parameter_extraction(string:str):

    matches = re.findall(r"id=([0-9]+)", string)

    for _match in matches:
        return _match

def admin_parameter_extraction(string:str):

    matches = re.findall(r"admin=([0-9]+)", string)

    for _match in matches:
        return _match


