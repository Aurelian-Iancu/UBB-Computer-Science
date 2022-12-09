import socket
import threading
import struct

my_lock = threading.Lock()


def worker(css):

    arr1 = css.recv(125).decode('ascii')
    arr2 = css.recv(125).decode('ascii')

    print(arr1)
    print(arr2)

    my_lock.acquire()
    arr1 = arr1 + arr2
    my_lock.release()

    arr1 = sorted(arr1)
    res = ""
    for i in arr1:
        res = res + i

    css.send(bytes(res, 'ascii'))

    css.close()


if __name__ == '__main__':
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.bind(('0.0.0.0', 1234))
        s.listen(5)

    except socket.error as err:
        print('Error', err.strerror)
        exit(-1)

    cs, addr = s.accept()

    t = threading.Thread(target=worker, args=(cs,))
    t.start()
    t.join()
