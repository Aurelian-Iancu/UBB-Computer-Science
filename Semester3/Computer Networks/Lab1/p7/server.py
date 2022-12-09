import socket
import threading
import struct

threads = []
string_s = ""


def worker(cs):

    my_string = cs.recv(1024).decode('ascii')
    start_r = cs.recv(4)
    start = struct.unpack('!I', start_r)[0]
    length_r = cs.recv(4)
    length = struct.unpack('!I', length_r)[0]

    string_ss = ""
    for character in my_string[start:start+length]:
        string_ss = string_ss + character

    cs.send(bytes(string_ss, 'ascii'))
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
