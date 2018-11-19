#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Programa cliente que abre un socket a un servidor
"""

import socket
import sys

# Cliente UDP simple.

# Dirección IP del servidor.
try:
    METHOD = sys.argv[1]
    SIP_DIR = sys.argv[2][:sys.argv[2].find("@")]
    SERVER = sys.argv[2][sys.argv[2].find("@")+1:sys.argv[2].rfind(":")]
    PORT = int(sys.argv[2][sys.argv[2].rfind(":")+1:])
    LINE = (METHOD + " sip:" + sys.argv[2][:sys.argv[2].rfind(":")] + " SIP/2.0")
except IndexError:
    sys.exit("Usage: python3 client.py method receiver@IP:SIPport")

# Creamos el socket, lo configuramos y lo atamos a un servidor/puerto

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as my_socket:
    my_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    my_socket.connect((SERVER, PORT))
    
    if METHOD == "INVITE":
        print("Enviando: " + LINE)
        my_socket.send(bytes(LINE, 'utf-8') + b'\r\n')
        data = my_socket.recv(1024)
    
        print('Recibido -- ', data.decode('utf-8'))
        print("Terminando socket...")

print("Fin.")
