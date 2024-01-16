_VERSION = "1.1.5.6"
VERSION_TYPE = "#dev" if _VERSION.count('.') > 2 and _VERSION.split('.')[-1] != '0' else "#stable"
VERSION = _VERSION+VERSION_TYPE
