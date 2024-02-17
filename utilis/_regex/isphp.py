"""
# SQLGO License - Version 1.1

Copyright (C) 2023-2024 Heisenberg

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.


"""
import re
import os
import sys
from src.core.parser.cmdline import url as _url
from src.logger.log import logger

def _isphp(url=_url):
    return bool(re.search(r"\.php", url))

def isphp():
    if _isphp() is True:
        logger.info("target:%s backend is designed with php.this site might be vulnerable to XSS(cross site scripting)"%_url)
        return True
    