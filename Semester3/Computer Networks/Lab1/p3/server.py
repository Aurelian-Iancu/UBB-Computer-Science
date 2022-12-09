import socket
import threading


def worker(cs):
    my_string = cs.recv(1024).decode('ascii')
    i = 0
    j = len(my_string) - 1
    print(my_string)

    my_string_send = my_string[::-1]

    cs.send(bytes(my_string_send, 'ascii'))
    cs.close()


if __name__ == '__main__':
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.bind(('0.0.0.0', 1234))
        s.listen(5)

    except socket.error as err:
        print('Error', err.strerror)
        exit(-1)

    css, add = s.accept()
    t = threading.Thread(target=worker, args=(css,))
    t.start()
    t.join()
