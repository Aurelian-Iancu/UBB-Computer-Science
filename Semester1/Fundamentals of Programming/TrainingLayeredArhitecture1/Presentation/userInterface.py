from Erorrs.exceptions import ValidationError, RepositoryError


class Console:
    def __init__(self, srv_assignment, srv_student, srv_grade):
        self.__srv_assignment = srv_assignment
        self.__srv_student = srv_student
        self.__srv_grade = srv_grade

    def run(self):
        while True:
            cmd = input(">>>")
            if cmd == "exit":
                return
            if cmd == "":
                continue
            if cmd == "add_stud":
                try:
                    self.__ui_add_stud()
                except ValidationError as ve:
                    print(ve)
                except RepositoryError as re:
                    print(re)
            else:
                print("Invalid command!")

    def __ui_add_stud(self):
        print("We entered in the ui add_stud function")
