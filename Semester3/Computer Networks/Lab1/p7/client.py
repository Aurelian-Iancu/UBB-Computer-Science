import socket
import struct


if __name__ == '__main__':
    try:
        s = socket.create_connection(('localhost', 1234))
    except socket.error as err:
        print('Error', err.strerror)
        exit(-1)

    my_string = str(input('Enter a string: '))
    start = int(input('Enter starting pos: '))
    length = int(input('Enter length: '))

    s.send(bytes(my_string, 'ascii'))
    s.send(struct.pack("!I", start))
    s.send(struct.pack("!I", length))

    my_string = s.recv(1024).decode('ascii')
    print(my_string)
    s.close()

