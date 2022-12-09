import socket
import struct
import pickle

if __name__ == '__main__':
    try:
        s = socket.create_connection(('localhost', 1234))
    except socket.error as err:
        print('Error: ', err.strerror)
        exit(-1)

    n = int(input('Enter the integer: '))

    s.send(struct.pack('!I', n))

    data = s.recv(4098)
    arr = pickle.loads(data)
    print(arr)

    s.close()
