import unittest
from board.board import Board
from board.exceptions import MoveError
from board.point import Point


class  TestBoard(unittest.TestCase):

    def setUp(self) -> None:
        self.__board = Board(4, 3)

    def test_for_getters_and_setters(self):
        self.__board.set_rows(5)
        self.assertEqual(self.__board.get_rows(), 5)
        self.__board.set_columns(8)
        self.assertEqual(self.__board.get_columns(), 8)
        self.assertEqual(self.__board.get_board(), [])

    def test_create_board(self):
        self.__board.create_board()
        self.assertEqual(str(self.__board),
                         "\nx\n0 ['.', '.', '.']\n1 ['.', '.', '.']\n2 ['.', '.', '.']\n3 ['.', '.', '.']\n    0    1    2    y")
        turn = self.__board.get_turn()
        self.assertEqual(turn, "first")

    def test_moves(self):
        self.__board.create_board()
        self.assertEqual(self.__board.available_moves(), 12)
        self.__board.execute_move(Point(1, 1))
        self.__board.execute_move(Point(3, 1))
        self.assertEqual(str(self.__board),
                             "\nx\n0 ['*', '*', '*']\n1 ['*', 'X', '*']\n2 ['*', '*', '*']\n3 ['*', 'O', '*']\n    0    1    2    y")
        with self.assertRaises(MoveError):
            self.__board.execute_move(Point("a", 1))
        with self.assertRaises(MoveError):
            self.__board.execute_move(Point(1, 1))
        with self.assertRaises(MoveError):
            self.__board.execute_move(Point(7, 7))
        self.assertEqual(self.__board.available_moves(), 0)

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

