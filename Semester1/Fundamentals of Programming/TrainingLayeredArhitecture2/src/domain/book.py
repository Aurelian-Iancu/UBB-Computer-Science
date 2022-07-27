class Book:
    def __init__(self, id_book, name, author, year):
        self.__id_book = id_book
        self.__name = name
        self.__author = author
        self.__year = year

    @property
    def get_id_book(self):
        return self.__id_book

    @property
    def get_name(self):
        return self.__name

    @property
    def get_author(self):
        return self.__author

    @property
    def get_year(self):
        return self.__year

    def set_name(self, new_name):
        self.__name = new_name

    def set_author(self, new_author):
        self.__author = new_author

    def set_year(self, new_year):
        self.__year = new_year

    def __str__(self):
        return f"{self.__id_book}, {self.__name}, {self.__author}, {self.__year}"
