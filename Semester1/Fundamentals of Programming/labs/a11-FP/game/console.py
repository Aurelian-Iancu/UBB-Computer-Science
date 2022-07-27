from board.board import Board
from board.point import Point
from board.exceptions import MoveError
from strategy.strategy import Strategy


class Console:
    def __init__(self, rows, columns, mode, turn):
        self.__mode = mode
        self.__rows = rows
        self.__columns = columns
        self.__turn = turn
        self.__game_board = Board(rows, columns)
        if self.__turn is True:
            self.__game_board.set_turn("second")
        self.__game_board.create_board()
        self.__game_running = True
        self.__strategy = Strategy()

    def print_board(self):
        print(self.__game_board)

    def print_turn(self):
        if self.__mode == "player":
            if self.__game_board.get_turn() == "first":
                print("\nCurrent player: Player 1.\n")
            else:
                print("\nCurrent player: Player 2.\n")
        else:
            if self.__turn is False:
                print("\nYour turn\n")

    def game_over(self):
        self.__game_running = False

    def start(self):
        if self.__mode == "player":
            while self.__game_running:
                self.print_board()
                self.print_turn()
                try:
                    x = int(input("Enter the first coordinate for ur move:"))
                    y = int(input("Enter the second coordinate for ur move:"))
                    point = Point(x, y)
                    self.__game_board.execute_move(point)
                    if self.__game_board.available_moves() == 0:
                        self.game_over()
                        self.print_board()
                        if self.__game_board.get_turn() == "first":
                            print("\nPlayer 2 wins!")
                        else:
                            print("\nPlayer 1 wins!")
                except ValueError:
                    print("Invalid move!Coordinate should be integers and should fit in the map!")
                except MoveError as me:
                    print(me)
        else:
            while self.__game_running is True:
                if self.__turn is False: # if it's user's turn
                    try:
                        self.print_board()
                        self.print_turn()
                        x = int(input("Enter the first coordinate for ur move:"))
                        y = int(input("Enter the second coordinate for ur move:"))
                        point = Point(x, y)
                        self.__game_board.execute_move(point)
                        self.__turn = not self.__turn
                        if self.__game_board.available_moves() == 0:
                            self.game_over()
                            self.print_board()
                            print("\nYou win!")
                    except ValueError:
                        print("Invalid move!Coordinate should be integers and should fit in the map!")
                    except MoveError as me:
                        print(me)
                else:
                    move = self.__strategy.get_input(self.__game_board)
                    self.__game_board.execute_move(move)
                    self.__turn = not self.__turn
                    if self.__game_board.available_moves() == 0:
                        self.game_over()
                        self.print_board()
                        print("\nComputer win!")


if __name__ == "__main__":
    ok = True
    turn = -1
    while ok is True:
        try:
            turn = int(input("1 if you want to start, 2 if you want the other player/computer to start:"))
        except ValueError:
            print("Invalid numerical number!")
            continue
        if turn != 1 and turn != 2:
            print("Invalid command! You can choose between 1 and 2")
            continue
        ok = False
    if turn == 1:
        turn = False
    else:
        turn = True

    mode = ""
    ok = True
    while ok is True:
        mode = input("Enter the mode you want to play:(vs computer/ vs another_player(player)")
        if mode == "player":
            ok = False
        elif mode == "computer":
            ok = False
        else:
            print("Try again! player or computer")

    rows = 0
    columns = 0
    while True:
        try:
            rows = int(input("The number of rows for the map:"))
            columns = int(input("The number of columns for the map:"))
        except ValueError:
            print("Invalid command! They must be integers")
            continue
        break

    ui = Console(rows, columns, mode, turn)
    ui.start()


