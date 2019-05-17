import socket
import sys

# create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# bind the socket to the port
server_address = ('localhost', 10000)

print('starting up on %s port %s' % server_address)

try:
    sock.bind(server_address)
except socket.error as msg:
    print('Address bind error: ' + str(msg))
    sys.exit()

print('socket bind complete')

# listen for incoming connections
sock.listen(1)

while True:
    # wait for a connection
    print('waiting for a connection')

    connection, client_address = sock.accept()

    try:
        print('connection from \'{0}\''.format(client_address))

        # receive the data in small chunks and retransmit it
        while True:
            data = connection.recv(16)
            print('received "%s"' % data)

            if data:
                print('sending data back to the client')
                connection.sendall(data)
            else:
                print('no more data from \'{0}\''.format(client_address))
                break

    finally:
        # clean up the connection
        connection.close()
