import socket
import struct


if __name__ == '__main__':
    try:
        s = socket.create_connection(('localhost', 1234))
    except socket.error as err:
        print('Error', err.strerror)
        exit(-1)

    my_string = str(input('Enter a string: '))
    s.send(bytes(my_string, 'ascii'))

    count_spaces_r = s.recv(4)
    count_spaces = struct.unpack('!I', count_spaces_r)[0]

    print('Nr of spaces in the sent string:', count_spaces)

    s.close()
