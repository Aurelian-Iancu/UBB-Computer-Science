import socket
import threading
from random import randint
from board.ServerBoard import ServerBoard

threads = []
string_s = ""



def play_game(cs):

    table = ServerBoard()
    game_stop = 'c'
    server_msg = "continue"
    while(game_stop == 'c'):

        x = cs.recv(1)
        y = cs.recv(1)

        client_position_x = int(x.decode())
        client_position_y = int(y.decode())

        table.place(client_position_x - 1, client_position_y - 1, 'X')

        game_stop = table.check_if_game_over()

        if game_stop != 'c':
            server_position_x = 5
            server_position_y = 5

            cs.send((server_position_x).__str__().encode())
            cs.send((server_position_y).__str__().encode())

            break

        server_position_x, server_position_y = table.find_best_move()

        table.place(server_position_x, server_position_y, 'O')

        cs.send((server_position_x + 1).__str__().encode())
        cs.send((server_position_y + 1).__str__().encode())

        game_stop = table.check_if_game_over()

        if game_stop != 'c':
            server_msg = "over"
        
        cs.send(server_msg.encode())

        #print(table)


    if(game_stop == 'O'):
        string_ss = "Game over! You lost."
        cs.send(string_ss.encode())
    elif(game_stop == '-'):
        string_ss = "Game over! It's a draw."
        cs.send(string_ss.encode())
    else:
        string_ss = "Game over! You won."
        cs.send(string_ss.encode())

    cs.close()


if __name__ == '__main__':
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.bind(('127.0.0.1', 1234))
        s.listen(5)
    except socket.error as err:
        print('Error', err.strerror)
        exit(-1)

    client_socket, addr = s.accept()
    t = threading.Thread(target=play_game, args=(client_socket,))
    t.start()
    threads.append(t)

    for th in threads:
        th.join()

    #
    # play_game(client_socket)

    s.close()