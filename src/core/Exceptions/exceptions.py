#!/usr/bin/env python
"""
# SQLGO License - Version 1.4

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
class SQlgoBasicException(Exception):
    pass

class SQLgoNoParameterFoundException(SQlgoBasicException):
    pass

class SQLgoWrongUrlException(SQlgoBasicException):
    pass

class SQLgoNoneKeyException(SQlgoBasicException):
    pass

class SQLgoKeyGenDictKeyException(SQlgoBasicException):
    pass

class SQLGOBeepSoundException(SQlgoBasicException):
    pass

class SQLGOStreamHandlerException(SQlgoBasicException):
    pass

class SQLGOFilePathException(SQlgoBasicException):
    pass

class SQLGOConnectionException(SQlgoBasicException):
    pass

class SQLGODataException(SQlgoBasicException):
    pass

class SQLGOFilePathException(SQlgoBasicException):
    pass