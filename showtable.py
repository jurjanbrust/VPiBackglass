#!/usr/bin/env python3
import socket
import re


HOST = '192.168.1.210'  # The server's hostname or IP address
PORT = 8001  # The port used by the server

tableRegex = re.compile(r'with ROM=\'(\w+)\'')

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    print('connecting to: ' + HOST)
    try:
        s.connect((HOST, PORT))
    except:
        print('socket: ' + s)
    while True:
        data = s.recv(1024)
        match = tableRegex.search(repr(data))
        if (match != None):
            tableName = match.group(1)
            print(tableName)
