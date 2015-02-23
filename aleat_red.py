#!/usr/bin/python

#!/usr/bin/python
# -*- coding: utf-8 -
import socket
import random
import time

mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mySocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
mySocket.bind(('localhost', 1234))

# Queue a maximum of 5 TCP connection requests

mySocket.listen(5)


try:
    while True:
        print 'Waiting for connections'
        (recvSocket, address) = mySocket.accept()
        print 'HTTP request received:'
        peticion= recvSocket.recv(1024)
        print peticion
        num = str(random.randint(1, 10000000))
        recvSocket.send('HTTP/1.1 302 Found\r\nLocation: http://localhost:1234/'+num+'\r\n\r\n' + '<html><head> Server-Url-Aleatorias </head><body><h1>Redirigiendo  </h1></body></html>'+'\r\n')
        time.sleep(1)
        recvSocket.close()
except KeyboardInterrupt:
    print "Closing binded socket"
    mySocket.close()
