import socket
import struct

server_address = '192.168.1.248'
server_port = 1234

server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.bind((server_address, server_port))

while True:
    # Receive sensor data
    data, address = server_socket.recvfrom(1024)
    ax, ay, az = struct.unpack('hhh', data)
    print('Received data: ax={}, ay={}, az={}'.format(ax, ay, az))
    ##print('ax={}, ay={}, az={}'.format(ax, ay, az))