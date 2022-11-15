import socket
from board.board import Board


if __name__ == "__main__":
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect(('127.0.0.1', 1234))
    except socket.error as se:
        print("Error: ", se.strerror)
        exit(-1)


    table = Board()

    server_message = "continue"

    while(server_message != "over"):
        
        print(table)
        print()

        try:
            x = int(input("Enter X coordinate: "))
            if x not in [1, 2, 3]:
                print("Please enter a valid X coordinate(1 <= x <= 3).")
                continue

            y = int(input("Enter Y coordinate: "))
            if y not in [1, 2, 3]:
                print("Please enter a valid coordinate(1 <= y <= 3).")
                continue
              
        except ValueError:
            print("Please enter only numbers!")
            continue


        try:
            table.place(x - 1, y - 1, 'X')
        except Exception as e:
            print(e)
            continue
        
        print(f"You have placed your piece on ({x}, {y}).")
        
        s.send((x).__str__().encode())
        s.send((y).__str__().encode())

        sv_position_x = int(s.recv(1).decode())
        sv_position_y = int(s.recv(1).decode())

        if sv_position_x == 5:
            break
            
        table.place(sv_position_x - 1, sv_position_y - 1, 'O')
        print(f"Server has placed it's piece on ({sv_position_x}, {sv_position_y}).")
        print()

        server_message = s.recv(1024).decode()


    print(table)
    game_over_string = s.recv(1024).decode()
    print(game_over_string)

    s.close()