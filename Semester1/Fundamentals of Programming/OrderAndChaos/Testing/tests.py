import unittest
from Board.board import Board
from Board.exceptions import MoveError
from Board.point import Point


class  TestBoard(unittest.TestCase):

    def setUp(self) -> None:
        self.__board = Board(6, 6)

    def test_for_getters_and_setters(self):
        self.__board.set_rows(5)
        self.assertEqual(self.__board.get_rows(), 5)
        self.__board.set_columns(8)
        self.assertEqual(self.__board.get_columns(), 8)
        self.assertEqual(self.__board.get_board(), [])

    def test_create_board(self):
        self.__board.create_board()
        self.assertEqual(str(self.__board),
                         "\nx\n0 ['.', '.', '.', '.', '.', '.']\n1 ['.', '.', '.', '.', '.', '.']\n2 ['.', '.', '.', '.', '.', '.']\n3 ['.', '.', '.', '.', '.', '.']\n4 ['.', '.', '.', '.', '.', '.']\n5 ['.', '.', '.', '.', '.', '.']\n    0    1    2    3    4    5    y")

    def test_moves(self):
        self.__board.create_board()
        self.assertEqual(self.__board.available_moves(), 36)
        self.__board.execute_move(Point(1, 1), 'X')
        # I won't print again the board cuz it s stupid, but the move works

        with self.assertRaises(MoveError):
            self.__board.execute_move(Point("a", 1), 'X')
        with self.assertRaises(MoveError):
            self.__board.execute_move(Point(1, 1), '0')
        with self.assertRaises(MoveError):
            self.__board.execute_move(Point(7, 7), 'X')
        with self.assertRaises(MoveError):
            self.__board.execute_move(Point(3, 4), 'z')

    if __name__ == "__main__":
        unittest.main()


class TestPoint(unittest.TestCase):

    def setUp(self) -> None:
        self._point = Point(2, 5)

    def test_getters(self):
        self.assertEqual(self._point.get_y, 5)
        self.assertEqual(self._point.get_x, 2)

    if __name__ == "__main__":
        unittest.main()