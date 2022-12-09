import socket
import struct

data = []

if __name__ == '__main__':
    try:
        s = socket.create_connection(('localhost', 1234))
    except socket.error as err:
        print('Error', err.strerror)
        exit(-1)

    n = int(input('Enter a nr: '))
    s.send(struct.pack('!I', n))
    for i in range(n):
        x = int(input('Enter elem: '))
        s.send(struct.pack('!I', x))

    m = int(input('Enter a nr: '))
    s.send(struct.pack('!I', m))
    for i in range(m):
        x = int(input('Enter elem: '))
        s.send(struct.pack('!I', x))

    nr_r = s.recv(4)
    nr = struct.unpack('!I', nr_r)[0]
    for i in range(nr):
        x_r = s.recv(4)
        x = struct.unpack('!I', x_r)[0]
        data.append(x)

    print(data)
    s.close()

