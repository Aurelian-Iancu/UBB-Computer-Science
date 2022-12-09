import socket
import threading
import struct


def worker(cs):
    nr_r = cs.recv(4)
    nr = struct.unpack('!I', nr_r)[0]
    my_sum = 0

    for i in range(nr):
        x_r = cs.recv(4)
        x = struct.unpack('!I', x_r)[0]
        print(x_r)
        my_sum = my_sum + x

    cs.send(struct.pack('!I', my_sum))
    cs.close()


if __name__ == '__main__':
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.bind(('0.0.0.0', 1234))
        s.listen(5)
    except socket.error as err:
        print('Error ', err.strerror)
        exit(-1)

    client_socket, addr = s.accept()

    t = threading.Thread(target=worker, args=(client_socket,))
    t.start()
    t.join()
