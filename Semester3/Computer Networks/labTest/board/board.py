from texttable import Texttable

class Board:
    def __init__(self):
        """
        Constructor class for board
        :param filename:
        """
        self._data = [[' ', ' ', ' '] for x in range(3)]


    def place(self, i, j, symbol):
        """
        Places a piece on the board
        :param owner:
        :param i:
        :param j:
        :return:
        """
        if self.is_occupied(i, j) == True:
            raise Exception(f"Position ({i}, {j}) is occupied!")

        self._data[i][j] = symbol

    def is_occupied(self, i, j):
        """
        Checks if a slot on board is occupied
        :param i:
        :param j:
        :return:
        """
        if self._data[i][j] != ' ':
            return True
        return False

    def __str__(self):
        """
        Returns the table in a pretty format :)
        :return:
        """
        t = Texttable()

        table_header = ['/']

        for i in range(3):
            table_header.append(i+1)

        t.header(table_header)

        for i in range(3):
            l = []
            l.append(i + 1)
            for j in range(3):
                l.append(self._data[i][j])
            t.add_row(l)

        return t.draw()