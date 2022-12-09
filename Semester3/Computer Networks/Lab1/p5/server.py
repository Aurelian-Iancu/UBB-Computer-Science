import socket
import pickle
import struct
import threading

threads = []


def worker(cs):
    client_number = cs.recv(4)
    client_number = struct.unpack('!I', client_number)[0]
    div_array = []

    for d in range(1, client_number):
        if d * d > client_number:
            break
        if client_number % d == 0:
            div_array.append(d)
            div_array.append(int(client_number / d))

    div_array.sort()

    data_to_send = pickle.dumps(div_array)
    cs.send(data_to_send)

    cs.close()


if __name__ == '__main__':
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.bind(('0.0.0.0', 1234))
        s.listen(5)

    except socket.error as err:
        print(err.strerror)
        exit(-1)

    client_socket, client_addr = s.accept()

    t = threading.Thread(target=worker, args=(client_socket,))
    threads.append(t)
    t.start()

    for th in threads:
        th.join()