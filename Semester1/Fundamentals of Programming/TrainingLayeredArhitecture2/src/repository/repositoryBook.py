from src.domain.book import Book


class BookRepoTextFile:
    def __init__(self, file_path):
        self._file_path = file_path
        self._list_of_books = []
        self._read_all_from_file()

    def _read_all_from_file(self):
        self._list_of_books.clear()
        with open(self._file_path, "r") as f:
            lines = f.readlines()
            for line in lines:
                line = line.strip()
                if line !="":
                    line = line.split(",")
                    book = Book(int(line[0]), line[1], line[2], int(line[3]))
                    self._list_of_books.append(book)

    def __len__(self):
        return len(self._list_of_books)

    def get_all_books(self):
        return self._list_of_books
