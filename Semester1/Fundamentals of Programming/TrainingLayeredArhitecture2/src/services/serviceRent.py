class ServiceRent:
    def __init__(self, rent_repo):
        self.__rent_repo = rent_repo

    def get_all_rents(self):
        return self.__rent_repo.get_all_rents()


