import socket

def socket_init():

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    return s
