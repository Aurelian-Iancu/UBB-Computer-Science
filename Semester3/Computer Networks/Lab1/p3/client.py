import socket


if __name__ == '__main__':
    try:
        s = socket.create_connection(('localhost', 1234))
    except socket.error as err:
        print('error', err.strerror)
        exit(-1)

    my_string = str(input('Enter string:\n'))
    s.send(bytes(my_string, 'ascii'))

    data = s.recv(1024).decode('ascii')
    print(data)

    s.close()
