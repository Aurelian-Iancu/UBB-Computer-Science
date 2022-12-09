import socket
import struct

if __name__ == '__main__':
    try:
        s = socket.create_connection(('localhost', 1234))
    except socket.error as err:
        print('Error: ', err.strerror)
        exit(-1)

    string1 = str(input('Enter first string:'))
    string2 = str(input('Enter second string'))

    s.send(bytes(string1, 'ascii'))
    s.send(bytes(string2, 'ascii'))

    characterR = s.recv(1)
    character = characterR.decode('ascii')

    freqR = s.recv(4)
    freq = struct.unpack('!I', freqR)[0]

    print(character)
    print(freq)

    s.close()
