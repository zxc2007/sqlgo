#!/usr/bin/env python
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
import hashlib

class Hash(object):
    def __init__(self,plainText):
        self.plainText = plainText
    
    def sha256(self):
        return hashlib.sha256(self.plainText.encode('utf-8')).hexdigest()

    def sha512(self):
        return hashlib.sha512(self.plainText.encode('utf-8')).hexdigest()

    def md5(self):
        return hashlib.md5(self.plainText.encode('utf-8')).hexdigest()

    def sha1(self):
        return hashlib.sha1(self.plainText.encode('utf-8')).hexdigest()

    def sha224(self):
        return hashlib.sha224(self.plainText.encode('utf-8')).hexdigest()

    def sha384(self):
        return hashlib.sha384(self.plainText.encode('utf-8')).hexdigest()
    