import socket
import struct
import threading


def worker(cs):
    counter = 0
    my_string = cs.recv(1024).decode('ascii')
    for character in my_string:
        if character == ' ':
            counter = counter + 1

    cs.send(struct.pack('!I', counter))
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
