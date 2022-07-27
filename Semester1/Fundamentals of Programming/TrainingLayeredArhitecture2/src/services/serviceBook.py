class ServiceBook:
    def __init__(self, book_repo):
        self.__book_repo = book_repo

    def get_all_books(self):
        return self.__book_repo.get_all_books()
