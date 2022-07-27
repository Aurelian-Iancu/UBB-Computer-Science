from board.exceptions import MoveError
from board.point import Point


class Board:
    def __init__(self, rows, columns):
        self.__rows = rows
        self.__columns = columns
        self.__board = []
        self._turn = "first"

    def get_turn(self):
        return self._turn

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
        self._turn = turn

    def set_move(self, point):
        x = point.get_x
        y = point.get_y
        if self._turn == "first":
            self.__board[x][y] = 'X'
            self.set_turn("second")
        else:
            self.__board[x][y] = 'O'
            self.set_turn("first")

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

    def potential_move_is_valid(self, point):
        """
        function that checks whether a potential move is valid
        :param point: the move
        :return: boolean value depending on the truth value of the validity
        """
        x = int(point.get_x())
        y = int(point.get_y())
        if x > self.get_rows() - 1 or x < 0 or y > self.get_columns() - 1 or y < 0:
            return False
        if self.__board[x][y] != '.':
            return False
        return True

    def validate_move(self, point):
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

    def mark_borders_of_move(self, point):
        """
        function that boards the map around the point that we read
        :param point: the point around which we want to board
        :return: None
        """
        x = point.get_x
        y = point.get_y
        if x - 1 >= 0 and y - 1 >= 0 and self.__board[x - 1][y - 1] == '.':  # upper left corner
            self.__board[x - 1][y - 1] = '*'
        if x - 1 >= 0 and self.__board[x - 1][y] == '.':  # directly above the move
            self.__board[x - 1][y] = '*'
        if x - 1 >= 0 and y + 1 < self.get_columns() and self.__board[x - 1][y + 1] == '.':  # upper right corner
            self.__board[x - 1][y + 1] = '*'
        if y - 1 >= 0 and self.__board[x][y - 1] == '.':  # in the left of the move
            self.__board[x][y - 1] = '*'
        if y + 1 < self.get_columns() and self.__board[x][y + 1] == '.':  # in the right of the move
            self.__board[x][y + 1] = '*'
        if x + 1 < self.get_rows() and y - 1 >= 0 and self.__board[x + 1][y - 1] == '.':  # lower left corner
            self.__board[x + 1][y - 1] = '*'
        if x + 1 < self.get_rows() and self.__board[x + 1][y] == '.':  # directly under the move
            self.__board[x + 1][y] = '*'
        if x + 1 < self.get_rows() and y + 1 < self.get_columns() and self.__board[x + 1][y + 1] == '.': #lower right corner
            self.__board[x+1][y+1] = "*"

    def execute_move(self, point):
        """
        the function that executes a move on the board
        :param point: the move to be executed, represented by its coordinates
        :return: None
        """
        self.validate_move(point)
        self.set_move(point)
        self.mark_borders_of_move(point)

    def get_move_list(self):
        """
        in this function we get the list of available moves
        :return: list of moves
        """
        m = []
        rows = self.get_rows()
        columns = self.get_columns()
        for row in range(rows):
            for column in range(columns):
                if self.__board[row][column] == '.':
                    m.append(Point(row, column))
        return m

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



