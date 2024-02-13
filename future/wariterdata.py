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
import io
import os
import sys
from src.core.Exceptions.exceptions import SQLGOStreamHandlerException
import io
from src.core.Exceptions.exceptions import SQLGOStreamHandlerException

class StreamReaderWriter:
    def __init__(self, stream, encoding='utf-8'):
        self._stream = stream
        self._encoding = encoding
        assert isinstance(self._stream, io.TextIOWrapper), repr(self._stream)

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        pass
        # No need to close the stream here, as it is managed by the 'with' statement

    def read(self, size=-1):
        return self._stream.read(size)

    def readline(self, size=-1):
        return self._stream.readline(size)

    def write(self, data):
        try:
            if not self._stream.closed:
                if isinstance(data, str):
                    self._stream.write(data)
                elif isinstance(data, bytes):
                    self._stream.write(data.decode(self._encoding))
                elif isinstance(data, dict):
                    for key, item in data.items():
                        self._stream.write(str(key))
                        self._stream.write(str(item))
        except Exception as e:
            raise SQLGOStreamHandlerException(f"Error in write: {e}")

    def writelines(self, lines):
        try:
            if not self._stream.closed:
                for line in lines:
                    self.write(line)
        except Exception as e:
            raise SQLGOStreamHandlerException(f"Error in writelines: {e}")

    def seek(self, offset, whence=0):
        self._stream.seek(offset, whence)

    def tell(self):
        return self._stream.tell()

    def __iter__(self):
        return iter(self._stream)


# Rest of your code
# file_path = '/Users/alimirmohammad/sqlgo/future/file.txt'
# file_stream = open(file_path, 'w+', encoding='utf-8')


# # Instantiate StreamReaderWriter
# with StreamReaderWriter(file_stream) as stream_wrapper:
#     # Use the instance for reading and writing
#     stream_wrapper.write("Hello, StreamWriterWriter!\n")
#     stream_wrapper.writelines(["Line 1\n", "Line 2\n"])

#     stream_wrapper.seek(0)  # Move the stream pointer to the beginning

#     for line in stream_wrapper:
#         print(line, end='')
