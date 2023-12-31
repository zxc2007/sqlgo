import socket
import sys


class Get:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self._socket = None

    def _header_prep(self):
        header = f"GET / HTTP/1.1\r\nHost: {self.host}\r\n\r\n"
        return header

    def _connect(self):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((self.host, self.port))
        return s

    def _send(self):
        s = self._connect()
        header = self._header_prep()
        s.sendall(header.encode())
        s.close()

    def _response(self):
        _response = b""
        s = self._connect()
        while True:
            chunk = s.recv(4096)
            if not chunk:
                break
            _response += chunk
        s.close()
        return _response

    def get_send(self):
        self._send()
        response = self._response()
        print(response.decode())
    
    def using_requests(self):
        try:
            import requests
            res = requests.get(self.host)
        except ImportError:
            sys.exit("[!]requests library is not installed,exiting...")

# obj = Get("http://testfire.net/index.jsp?content=business_deposit.htm", 80)
# obj.using_requests()
