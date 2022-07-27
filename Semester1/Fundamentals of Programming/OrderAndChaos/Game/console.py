from Board.board import Board
from Board.point import Point
from Board.exceptions import MoveError
from Strategy.strategy import Strategy


class Console:
    def __init__(self, rows, columns, turn):
        self.__rows = rows
        self.__columns = columns
        self.__turn = turn
        self.__game_board = Board(rows, columns)
        self.__game_board.create_board()
        self.__game_running = True
        self.__strategy = Strategy()

    def print_board(self):
        print(self.__game_board)

    def game_over(self):
        self.__game_running = False

    def print_turn(self):
        if self.__turn is False:
            print("\nYour turn!!\n")

    def start(self):
        self.print_board()
        while self.__game_running:
            if self.__turn is False: #it's user's turn
                try:
                    self.print_board()
                    self.print_turn()
                    x = int(input("Enter the first coordinate for ur move:"))
                    y = int(input("Enter the second coordinate for ur move:"))
                    character = input("Enter the character you want to put on the map:")
                    point = Point(x, y)
                    self.__game_board.execute_move(point, character)
                    self.__turn = not self.__turn
                    if self.__game_board.is_game_won():
                        print("\nOrder wins!")
                        self.game_over()
                    if self.__game_board.available_moves() == 0:
                        self.game_over()
                        self.print_board()
                        print("\nChaos wins!")
                except ValueError:
                    print("Invalid move!Coordinate should be integers and should fit in the map!")
                except MoveError as me:
                    print(me)
            else:
                move = self.__strategy.get_input(self.__game_board)
                print(self.__game_board.symbol_with_most_apparitions())
                try:
                    self.__game_board.execute_move(move[0], move[1])
                    self.__turn = not self.__turn
                    if self.__game_board.is_game_won():
                        print("\nOrder wins!")
                        self.game_over()
                        self.print_board()
                    if self.__game_board.available_moves() == 0:
                        self.game_over()
                        self.print_board()
                        print("\nChaos wins!")
                except MoveError as me:
                    print(me)


if __name__ == "__main__":
    rows = 6
    columns = 6
    turn = True
    ui = Console(rows, columns, turn)
    ui.start()