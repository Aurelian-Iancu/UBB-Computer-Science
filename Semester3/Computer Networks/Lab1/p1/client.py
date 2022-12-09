import socket
import struct

if __name__ == '__main__':
    try:
        s = socket.create_connection(('localhost', 1234))
    except socket.error as err:
        print('Error', err.strerror)
        exit(-1)

    n = int(input('Enter nr of elems:\n'))
    my_arr = []

    for i in range(n):
        x = int(input('Elem: '))
        my_arr.append(x)

    s.send(struct.pack('!I', n))
    for nr in my_arr:
        s.send(struct.pack('!I', nr))

    sum_r = s.recv(4)
    sum_to_print = struct.unpack('!I', sum_r)[0]

    print('Sum of the sent nr is: ', sum_to_print)
    s.close()


