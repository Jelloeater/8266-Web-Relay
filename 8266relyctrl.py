import socket
import ure as re

# Standard socket stuff:
host = ''
port = 80
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind((host, port))
sock.listen(1) # don't queue up any requests


def run():
    while True:
        csock, caddr = sock.accept()
        print ("\nConnection from: " + str(caddr))
        req = csock.recv(1024) # get the request, 1kB max
        get_req=str(req).split('GET /')[1].split('HTTP')[0]
        print ('Req RAW:')
        print (req)
        output=parse_req(get_req)
        csock.sendall("""HTTP/1.0 200 OK
        Content-Type: text/html

        <html>
        <head>
        </head>
        <body>
        <form action="" method="get">
        <button name="pin1" value="True">P1-On</button>
        </form>
        <form action="" method="get">
        <button name="pin1" value="False">P1-Off</button>
        </form>
        <br>
        <form action="" method="get">
        <button name="pin2" value="True">P2-On</button>
        </form>
        <form action="" method="get">
        <button name="pin2" value="False">P2-Off</button>
        </form>
        <br>
        OUTPUT:
        {0}
        </body>
        </html>
        """.format(str(output)))
        csock.close()

def parse_req(get_req):
    print ('Get Req:')
    print(get_req)
    if 'favicon.ico' not in get_req:
        get_req=get_req[1:]
        data=get_req.split('=')
        print(data)
        return pin_logic(data)

def pin_logic(data):
    if 'pin1' in data[0]:
        print('yes') if 'True' in data[1] else print('no')

    if 'pin2' in data[0]:
        print('yes') if 'True' in data[1] else print('no')


run()
