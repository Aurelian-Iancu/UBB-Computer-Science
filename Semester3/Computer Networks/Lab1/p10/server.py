import socket
import threading
import struct

threads = []


def worker(cs):
    string1R = cs.recv(1024)
    string2R = cs.recv(1245)
    string1 = string1R.decode('ascii')
    string2 = string2R.decode('ascii')

    my_dic = {}
    max_freq = 0
    found_char = 'Not found'

    if len(string1) < len(string2):
        for pos in range(0, len(string1)):
            if string1[pos] == string2[pos]:
                if string1[pos] in my_dic:
                    my_dic[string1[pos]] += 1
                else:
                    my_dic[string1[pos]] = 1
    else:
        for pos in range(0, len(string2)):
            if string1[pos] == string2[pos]:
                if string1[pos] in my_dic:
                    my_dic[string1[pos]] += 1
                else:
                    my_dic[string1[pos]] = 1

    for key in my_dic:
        if my_dic[key] > max_freq:
            max_freq = my_dic[key]
            found_char = key

    print(my_dic)

    cs.send(bytes(found_char, 'ascii'))
    cs.send(struct.pack('!I', max_freq))

    cs.close()


if __name__ == '__main__':
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.bind(('0.0.0.0', 1234))
        s.listen(5)

    except socket.error as err:
        print('Error: ', err.strerror)
        print(-1)

    client_socket, client_addr = s.accept()

    t = threading.Thread(target=worker, args=(client_socket,))
    t.start()

    for th in threads:
        t.join()
