import socket
import struct

data = []

if __name__ == '__main__':
    try:
        s = socket.create_connection(('localhost', 1234))
    except socket.error as err:
        print('Error', err.strerror)
        exit(-1)

    my_string = str(input('Enter a string: '))
    character = str(input('Enter character: '))

    s.send(bytes(my_string, 'ascii'))
    s.send(bytes(character, 'ascii'))

    nr_r = s.recv(4)
    nr = struct.unpack('!I', nr_r)[0]

    for i in range(nr):
        x_r = s.recv(4)
        x = struct.unpack('!I', x_r)[0]
        data.append(x)

    print(data)
    s.close()
