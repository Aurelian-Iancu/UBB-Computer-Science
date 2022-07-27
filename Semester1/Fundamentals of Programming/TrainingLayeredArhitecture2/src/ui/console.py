class Console:
    def __init__(self, book_service, rent_service):
        self.__book_service = book_service
        self.__rent_service = rent_service

    def check_if_two_strings_have_the_same_last_two_letters(self, string1, string2):
        if string1.endswith() == string2.endswith():
            return True
        return False

    def __ui_print_sorted(self, ending):
        books = self.__book_service.get_all_books()
        good_endings = []
        for book in books:
            if book.get_name.endswith(ending):
                good_endings.append(book)
        good_endings.sort(key=lambda x: x.get_year)
        for book in good_endings:
            print(book)

    def __ui_print_rented_books(self, rent_time):
        rents = self.__rent_service.get_all_rents()
        good_rents = []
        if rent_time == "-1" or rent_time == "abc":
            print("Special message")
            return
        for rent in rents:
            if rent.get_rent_time == int(rent_time):
                good_rents.append(rent)
        if len(good_rents) == 0:
            print("There are no books rented for such time!")
        else:
            for rent in good_rents:
                print(rent)


    def print_menu(self):
        print("1. To print the list of that end in some message descendent by year")
        print("2. To print the rents with a specified number of days rented")

    def start(self):
        self.print_menu()
        while True:
            cmd = input(">>>")
            if cmd == "exit":
                return
            if cmd == "1":
                print("what sequence should be at the end of the strings:")
                ending = input(">>>")
                self.__ui_print_sorted(ending)
            if cmd == "2":
                print("What time should the book be rented:")
                rent_time = input(">>>")
                self.__ui_print_rented_books(rent_time)