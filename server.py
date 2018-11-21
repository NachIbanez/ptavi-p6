#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Clase (y programa principal) para un servidor de eco en UDP simple
"""

import socketserver
import sys
import os


class EchoHandler(socketserver.DatagramRequestHandler):
    """
    Echo server class
    """

    def handle(self):
        # Escribe dirección y puerto del cliente (de tupla client_address)
        while 1:
            # Leyendo línea a línea lo que nos envía el cliente
            line = self.rfile.read()
            line = line.decode('utf-8')
            method = line[:line.find(" ")]
            if method == "INVITE":
                print("El cliente nos manda " + line)
                if not "@" in line or not ":" in line:
                    self.wfile.write(b'SIP/2.0 400 Bad Request')
                else:
                    self.wfile.write(b'SIP/2.0 100 Trying\r\n'
                                     b'SIP/2.0 180 Ringing\r\n'
                                     b'SIP/2.0 200 OK\r\n')
            elif method == "ACK":
                print("El cliente nos manda " + line)
                aEjecutar = './mp32rtp -i 127.0.0.1 -p 23032 < ' + AUDIO
                os.system(aEjecutar)
            elif line[:line.find(" ")] == "BYE":
                print("El cliente nos manda " + line)
                if not "@" in line or not ":" in line:
                    self.wfile.write(b'SIP/2.0 400 Bad Request\r\n')
                else:
                    self.wfile.write(b'SIP/2.0 200 OK\r\n')
            elif line and method != "INVITE" and method != "BYE" and method != "ACK":
                self.wfile.write(b'SIP/2.0 405 Method Not Allowed\r\n')

            # Si no hay más líneas salimos del bucle infinito
            if not line:
                break

if __name__ == "__main__":
    # Creamos servidor de eco y escuchamos
    try:
        IP = sys.argv[1]
        PORT = sys.argv[2]
        AUDIO = sys.argv[3]
    except Index_Error:
        sys.exit("Usage: python3 server.py IP port audio_file")

    serv = socketserver.UDPServer(('', 6001), EchoHandler)
    print("Listening")
    serv.serve_forever()
