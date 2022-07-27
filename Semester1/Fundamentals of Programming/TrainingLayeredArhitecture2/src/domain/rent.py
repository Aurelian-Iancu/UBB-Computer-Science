class Rent:
    def __init__(self, id_rent, id_book, rent_date, rent_time):
        self.__id_rent = id_rent
        self.__id_book = id_book
        self.__rent_date = rent_date
        self.__rent_time = rent_time

    @property
    def get_id_rent(self):
        return self.__id_rent

    @property
    def get_id_book(self):
        return self.__id_book

    @property
    def get_rent_date(self):
        return self.__rent_date

    @property
    def get_rent_time(self):
        return self.__rent_time

    def set_rent_date(self, new_rent_date):
        self.__rent_date = new_rent_date

    def set_rent_time(self, new_rent_time):
        self.__rent_time = new_rent_time

    def __str__(self):
        return f"{self.__id_rent}, {self.__id_book}, {self.__rent_date}, {self.__rent_time}"
