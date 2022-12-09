import socket
import struct
import threading

threads = []


def worker(cs):
    my_string = cs.recv(1024).decode('ascii')
    character = cs.recv(1).decode('ascii')

    print(my_string)
    print(character)

    positions = []

    for i in range(len(my_string)):
        if my_string[i] == character:
            positions.append(i)

    nr = len(positions)
    cs.send(struct.pack('!I', nr))

    for pos in positions:
        cs.send(struct.pack('!I', pos))

    cs.close()


if __name__ == '__main__':
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.bind(('0.0.0.0', 1234))
        s.listen(5)
    except socket.error as err:
        print('Error: ', err.strerror)
        exit(-1)

    client_socket, addr = s.accept()

    t = threading.Thread(target=worker, args=(client_socket,))
    t.start()
    threads.append(t)

    for th in threads:
        t.join()