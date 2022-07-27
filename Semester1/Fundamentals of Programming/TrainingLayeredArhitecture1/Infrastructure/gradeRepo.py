from Erorrs.exceptions import RepositoryError


class GradeRepo:
    def __init__(self):
        self.__grades = []

    def __len__(self):
        return len(self.__grades)

    def get_all_grades(self):
        return self.__grades[:]

    def add_grade(self, grade):
        for _grade in self.__grades:
            if _grade == grade:
                raise RepositoryError("Existing grade!")
        self.__grades.append(grade)

    def remove_grade(self, id_grade):
        ok = 1
        for i in range(len(self.__grades)):
            if self.__grades[i].get_id_grade() == id_grade:
                del self.__grades[i]
                ok = 0
                return
        if ok == 1:
            raise RepositoryError("Inexisting grade!")

    def update_grade(self, grade):
        ok = 1
        for i in range(len(self.__grades)):
            if self.__grades[i] == grade:
                self.__grades[i] = grade
                ok = 0
                return
        if ok == 1:
            raise RepositoryError("Inexisting grade!")

    def search_by_id(self, id_grade):
        ok = 1
        for grade in self.__grades:
            if grade.get_id_grade() == id_grade:
                ok = 0
                return grade
        if ok == 1:
            raise RepositoryError("Inexisting grade!")