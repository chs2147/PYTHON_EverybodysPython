import socket

# create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:

    # connect the socket to the port where the server is listening
    server_address = ('localhost', 8888)
    print('connecting to %s port %s' % server_address)
    sock.connect(server_address)

    # send data
    message = 'This is the message. It will be repeated.'
    print('sending "%s"' % message)
    sock.sendall(message.encode())

    # look for the response
    amount_received = 0
    amount_expected = len(message)

    while amount_received < amount_expected:
        data = sock.recv(16)
        amount_received += len(data)
        print('received "%s"' % data)

except socket.error as msg:
    print('No echo server: ' + str(msg))

finally:
    print('closing socket')
    sock.close()
