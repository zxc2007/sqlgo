_VERSION = "1.1.4.8"
VERSION_TYPE = "#dev" if _VERSION.count('.') > 2 and _VERSION.split('.')[-1] != '0' else "#stable"
VERSION = _VERSION+VERSION_TYPE