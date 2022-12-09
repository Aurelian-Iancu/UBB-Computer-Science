import socket
import threading
import struct

threads = []
string_s = ""


def worker(cs):
    nr_r = cs.recv(4)
    nr = struct.unpack('!I', nr_r)[0]
    data1 = []
    data2 = []
    data_final = []

    for i in range(nr):
        x_r = cs.recv(4)
        x = struct.unpack('!I', x_r)[0]
        data1.append(x)

    nr_rr = cs.recv(4)
    nr2 = struct.unpack('!I', nr_rr)[0]
    for i in range(nr2):
        x_r = cs.recv(4)
        x = struct.unpack('!I', x_r)[0]
        data2.append(x)

    print(data1)
    print(data2)

    freq = {}

    for x in data1:
        if x not in freq:
            freq[x] = 1

    for x in data2:
        if x in freq:
            data_final.append(x)

    nr = len(data_final)
    cs.send(struct.pack('!I', nr))
    for x in data_final:
        cs.send(struct.pack('!I', x))

    cs.close()


if __name__ == '__main__':
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.bind(('0.0.0.0', 1234))
        s.listen(5)
    except socket.error as err:
        print('Error', err.strerror)
        exit(-1)

    client_socket, addr = s.accept()
    t = threading.Thread(target=worker, args=(client_socket,))
    t.start()
    threads.append(t)

    for th in threads:
        th.join()

    s.close()
