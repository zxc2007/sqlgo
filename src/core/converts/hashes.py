#!/usr/bin/env python
"""
# SQLGO License - Version 1.4

Copyright (C) 2023-2024 AliMirmohammad

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
    """
    A class that defines hashing methods for string in order to bypass WAF/IPS and other security mechanisms.
    Usage:
    >>> foo = Hash("foo")
    >>> foo.sha256()
    'acbd18db4cc2f85cedef654fccc4a4d8'
    >>> foo.md5()
    '37b51d13a48edebd814e87b6b855b6f6'
    >>> foo.sha1()
    '2aae6c35c94fcfb415dbe95f408b9ce91ee846ed'
    >>> foo.sha224()
    '23097d223405d8228642a477bda255b32aadbce4bda0b3f7e36c9da7'
    >>> foo.sha384()
    '9d0e1809716474cb086e2aa9ed0e91e80cfaf1cb771a4b1ae4ce2d951e0a7a8a413aa107ab7281a6c3d23e11ebcdb1cd4b8c0fc44b70e057f97cd982efe419'
    """
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
    