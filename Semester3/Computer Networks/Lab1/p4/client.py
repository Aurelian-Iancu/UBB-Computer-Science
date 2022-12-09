import socket
import struct

if __name__ == '__main__':
    try:
        s = socket.create_connection(('localhost', 1234))
    except socket.error as err:
        print('Error', err.strerror)
        exit(-1)

    arr1 = str(input('Enter string:\n'))
    arr2 = str(input('Enter string:\n'))

    s.send(bytes(arr1, 'ascii'))
    s.send(bytes(arr2, 'ascii'))
    result = s.recv(256).decode()
    print(result)

    s.close()
