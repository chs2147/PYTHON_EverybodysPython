"""
    Simple socket server using threads
"""

import socket
import sys
from threading import *

server_address = ('localhost', 8888)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print('socket created')

# bind socket to local host and port
try:
    s.bind(server_address)
except socket.error as msg:
    print(msg)
    sys.exit()

print('socket bind complete')

# start listening on socket
s.listen(10)
print('socket now listening')


# function for handling connections.
# this will be used to create threads
def client_thread(tid, conn):

    print('New thread started with thread-id: ' + tid)

    try:

        # sending message to connected client
        message = 'Welcome to the server. Type something and hit enter\n'
        conn.send(message.encode())

        # infinite loop so that function do not terminate and thread do not end
        while True:

            # receiving from client
            data = conn.recv(1024)
            reply = 'OK...' + data.decode()

            if not data:
                break

            conn.sendall(reply.encode())

    finally:
        conn.close()
        print("%s terminated." % tid)


# now keep talking with the client
thread_name_prefix = 'THREAD-'
thread_count = 0

while True:
    # wait to accept a connection - blocking call
    connection, address = s.accept()
    print('connected with %s:%s' % address)

    # start new thread takes 1st argument as a function name to be run
    thread_count += 1
    thread_id = thread_name_prefix + str(thread_count).rjust(4, '0')

    t = Thread(target=client_thread, args=(thread_id, connection))
    t.start()
