import socket
from lib.core.parser.cmdline import time_out


def socket_init():

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(time_out)

    return s
