from Erorrs.exceptions import RepositoryError


class StudentRepo:
    def __init__(self):
        self.__students = []

    def __len__(self):
        return len(self.__students)

    def get_all_students(self):
        return self.__students[:]

    def add_student(self, student):
        for _student in self.__students:
            if _student == student:
                raise RepositoryError("Existing student!")
        self.__students.append(student)

    def remove_student(self, id_stud):
        ok = 1
        for i in range(len(self.__students)):
            if self.__students[i].get_id_stud() == id_stud:
                del self.__students[i]
                ok = 0
                return
        if ok == 1:
            raise RepositoryError("Inexisting student!")

    def update_student(self, student):
        ok = 1
        for i in range(len(self.__students)):
            if self.__students[i] == student:
                self.__students[i] = student
                ok = 0
                return
        if ok == 1:
            raise RepositoryError("Inexisting student!")

    def search_by_id(self, id_stud):
        ok = 1
        for student in self.__students:
            if student.get_id_stud() == id_stud:
                ok = 0
                return student
        if ok == 1:
            raise RepositoryError("Inexisting student!")




