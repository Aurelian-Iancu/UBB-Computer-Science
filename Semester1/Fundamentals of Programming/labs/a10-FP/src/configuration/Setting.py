class Settings:
    def __init__(self):
        self.__repository = ""
        self.__students_path = ""
        self.__assignments_path = ""
        self.__grades_path = ""
        self.__load_data()

    def __load_data(self):
        with open("../configuration/settings.properties") as file_pointer:
            line = file_pointer.readline()
            tokens = line.split("=")
            self.__repository = tokens[1].strip()
            line = file_pointer.readline()
            tokens = line.split("=")
            self.__students_path = tokens[1].strip().strip('"')
            line = file_pointer.readline()
            tokens = line.split("=")
            self.__assignments_path = tokens[1].strip().strip('"')
            line = file_pointer.readline()
            tokens = line.split("=")
            self.__grades_path = tokens[1].strip().strip('"')

    @property
    def repository(self):
        return self.__repository

    @property
    def students_path(self):
        return self.__students_path

    @property
    def assignments_path(self):
        return self.__assignments_path

    @property
    def grades_path(self):
        return self.__grades_path