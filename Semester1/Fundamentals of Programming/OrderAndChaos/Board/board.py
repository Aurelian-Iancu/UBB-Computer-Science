import random

from Board.exceptions import MoveError
from Board.point import Point


class Board:
    def __init__(self, rows, columns):
        self.__rows = rows
        self.__columns = columns
        self.__board = []
        self.__turn = "first"

    def get_turn(self):
        return self.__turn

    def get_rows(self):
        return self.__rows

    def get_columns(self):
        return self.__columns

    def get_board(self):
        return self.__board

    def set_columns(self, columns):
        self.__columns = columns

    def set_rows(self, rows):
        self.__rows = rows

    def set_turn(self, turn):
        self.__turn = turn

    def get_board_pos(self, x, y):
        return self.__board[x][y]

    def set_move(self, point, c):
        x = point.get_x
        y = point.get_y
        character = c
        self.__board[x][y] = character

    def create_board(self):
        """
        in this function we initiate the board
        :return: None
        """
        for row in range(self.get_rows()):
            work_list = []
            for column in range(self.get_columns()):
                work_list.append('.')
            self.__board.append(work_list)

    def validate_move(self, point, c):
        """
        in this function we validate if a move is correct
        :param point: the point we try to put on the board
        :return: None
        """
        try:
            x = int(point.get_x)
            y = int(point.get_y)
        except ValueError:
            raise MoveError("Invalid move! Coordinates should be integers")
        if x > self.get_rows() - 1 or x < 0 or y > self.get_columns() - 1 or y < 0:
            raise MoveError("Invalid move! You are outside the board")
        if self.__board[x][y] != '.':
            raise MoveError("Invalid move! You can't move there")
        if c != 'X' and c != '0':
            raise MoveError("Invalid move! You can have only X and O")

    def available_moves(self):
        """
        in this function we count the number of moves we can do
        :return: number_of_available_moves = number of available moves
        """
        number_of_available_moves = 0
        rows = self.get_rows()
        columns = self.get_columns()
        for row in range(rows):
            for column in range(columns):
                if self.__board[row][column] == '.':
                    number_of_available_moves += 1
        return number_of_available_moves

    def get_move_list(self):
        """
        in this function we get the list of available moves
        :return: list of moves
        """
        m = []
        characters = ['X', '0']
        rows = self.get_rows()
        columns = self.get_columns()
        for row in range(rows):
            for column in range(columns):
                if self.__board[row][column] == '.':
                    point = Point(row, column)
                    m.append([point, 'X'])
                    m.append([point, '0'])
        return m

    def execute_move(self, point, c):
        """
        the function that executes a move on the board
        :param point: the move to be executed, represented by its coordinates
        :return: None
        """
        self.validate_move(point, c)
        self.set_move(point, c)

    def is_game_won(self):
        """
        Here we verify is the game is won by someone
        :return: True if the game is won, false if not
        """
        # Is game won on a row
        for row in range(6):
            if self.get_board_pos(row, 0) in ['X', '0'] and self.get_board_pos(row, 0) == self.get_board_pos(row, 1) == \
               self.get_board_pos(row, 2) == self.get_board_pos(row, 3) == self.get_board_pos(row, 4):
                return True
        for row in range(6):
            if self.get_board_pos(row, 1) in ['X', '0'] and self.get_board_pos(row, 1) == self.get_board_pos(row, 2) == \
               self.get_board_pos(row, 3) == self.get_board_pos(row, 4) == self.get_board_pos(row, 5):
                return True
        # Is game won on a column
        for column in range(6):
            if self.get_board_pos(0, column) in ['X', '0'] and self.get_board_pos(0, column) == self.get_board_pos(1, column)\
                    == self.get_board_pos(2, column) == self.get_board_pos(3, column) == self.get_board_pos(4, column):
                return True
            if self.get_board_pos(1, column) in ['X', '0'] and self.get_board_pos(1, column) == self.get_board_pos(2, column)\
                    == self.get_board_pos(3, column) == self.get_board_pos(4, column) == self.get_board_pos(5, column):
                return True
        # Is game won for main diagonal
        if self.get_board_pos(1, 0) in ['X', '0'] and self.get_board_pos(1, 0) == self.get_board_pos(2, 1) == \
                self.get_board_pos(3, 2) == self.get_board_pos(4, 3) == self.get_board_pos(5, 4):
            return True
        if self.get_board_pos(0, 1) in ['X', '0'] and self.get_board_pos(0, 1) == self.get_board_pos(1, 2) == \
                self.get_board_pos(2, 3) == self.get_board_pos(3, 4) == self.get_board_pos(4, 5):
            return True
        if self.get_board_pos(0, 0) in ['X', '0'] and self.get_board_pos(0, 0) == self.get_board_pos(1, 1) == \
                self.get_board_pos(2, 2) == self.get_board_pos(3, 3) == self.get_board_pos(4, 4):
            return True
        if self.get_board_pos(1, 1) in ['X', '0'] and self.get_board_pos(1, 1) == self.get_board_pos(2, 2) == \
                self.get_board_pos(3, 3) == self.get_board_pos(4, 4) == self.get_board_pos(5, 5):
            return True
        # Is game won for secondary diagonal
        if self.get_board_pos(0, 4) in ['X', '0'] and self.get_board_pos(0, 4) == self.get_board_pos(1, 3) == \
                self.get_board_pos(2, 2) == self.get_board_pos(3, 1) == self.get_board_pos(4, 0):
            return True
        if self.get_board_pos(1, 5) in ['X', '0'] and self.get_board_pos(1, 5) == self.get_board_pos(2, 4) == \
                self.get_board_pos(3, 3) == self.get_board_pos(4, 2) == self.get_board_pos(5, 1):
            return True
        if self.get_board_pos(0, 5) in ['X', '0'] and self.get_board_pos(0, 5) == self.get_board_pos(1, 4) == \
                self.get_board_pos(2, 3) == self.get_board_pos(3, 2) == self.get_board_pos(4, 1):
            return True
        if self.get_board_pos(1, 4) in ['X', '0'] and self.get_board_pos(1, 4) == self.get_board_pos(2, 3) == \
                self.get_board_pos(3, 2) == self.get_board_pos(4, 1) == self.get_board_pos(5, 0):
            return True

    def symbol_with_most_apparitions(self):
        """
        In this function we compute the max between the number of Xs and the number of 0s
        :return: X if there are more Xs than 0 or 0 otherwise
        """
        number_of_x = 0
        number_of_0 = 0
        for row in range(6):
            for column in range(6):
                if self.get_board_pos(row, column) == 'X':
                    number_of_x += 1
                if self.get_board_pos(row, column) == '0':
                    number_of_0 += 1
        if number_of_x > number_of_0:
            return [number_of_x, 'X']
        else:
            return [number_of_0, '0']

    def __str__(self):
        """
        format for the board
        :return: the format of the board
        """
        s = "\nx\n"
        row = 0
        for element in self.__board:
            s += f"{row} {element}\n"
            row += 1
        row = self.__board[0]
        s += "  "
        for column in range(0, len(row)):
            s += f"  {column}  "
        s += "  y"
        return s
