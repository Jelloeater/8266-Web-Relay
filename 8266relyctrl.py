import socket
import ure as re

# Standard socket stuff:
host = ''
port = 80
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind((host, port))
sock.listen(1) # don't queue up any requests

# Loop forever, listening for requests:
while True:
    csock, caddr = sock.accept()
    print ("Connection from: " + str(caddr))
    req = csock.recv(1024) # get the request, 1kB max
    get_req=str(req).split('GET /')[1].split('HTTP/1')[0]
    print ('REQUEST RAW:\n')
    print(get_req)
    print ('GET URL:\n')
    print (req)

    csock.sendall("""HTTP/1.0 200 OK
    Content-Type: text/html

    <html>
    <head>
    </head>
    <body>
    {0}
    </body>
    </html>
    """.format(req))
    csock.close()
