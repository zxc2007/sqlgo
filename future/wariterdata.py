import io
import os
import sys
sys.path.append(os.getcwd())
from lib.core.Exceptions.exceptions import SQLGOStreamHandlerException
class StreamReaderWriter:
    def __init__(self, stream, encoding='utf-8'):
        self._stream = stream
        self._encoding = encoding
        assert type(self._stream) == io.TextIOWrapper,repr(self._stream)

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self._stream.close()

    def read(self, size=-1):
        return self._stream.read(size)

    def readline(self, size=-1):
        return self._stream.readline(size)

    def write(self, data):
        if isinstance(data, str):
            self._stream.write(data)
        elif isinstance(data, bytes):
            self._stream.write(data.decode(self._encoding))
        else:
            raise SQLGOStreamHandlerException("Data must be str or bytes")
        

    def writelines(self, lines):
        for line in lines:
            self.write(line)

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
