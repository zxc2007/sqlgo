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
class SQlgoBasicException(Exception):
    """
    A class that Defines SQLGO Basic Exception(Parent exception)
    """
    pass

class SQLgoNoParameterFoundException(SQlgoBasicException):
    """
    A class that defines SQLGO exception where should be raised when no GET parameter provided
    """
    pass

class SQLgoWrongUrlException(SQlgoBasicException):
    """
    An exception will be raised when there is an issue with the entered url
    """
    pass

class SQLgoNoneKeyException(SQlgoBasicException):
    """
    An exception will be raised when there is an issue with the entered key of the Magic dict data type
    """
    pass

class SQLgoKeyGenDictKeyException(SQlgoBasicException):
    """
    An exception will be raised when there is an issue with the entered key of the Magic dict data type
    """
    pass

class SQLGOBeepSoundException(SQlgoBasicException):
    """
    An exception will be raised when got issue with beep sound (--beep)
    """
    pass

class SQLGOStreamHandlerException(SQlgoBasicException):
    """
    An exception will be raised when got issue with stream handler
    """
    pass

class SQLGOFilePathException(SQlgoBasicException):
    """
    An exception will be raised when got issue with file path
    """
    pass

class SQLGOConnectionException(SQlgoBasicException):
    """
    An exception will be raised when got issue with connection
    """
    pass

class SQLGODataException(SQlgoBasicException):
    """
    An exception will be raised when got issue with data
    """
    pass

class SQLGOFilePathException(SQlgoBasicException):
    """
    An exception will be raised when got issue with file path
    """
    pass