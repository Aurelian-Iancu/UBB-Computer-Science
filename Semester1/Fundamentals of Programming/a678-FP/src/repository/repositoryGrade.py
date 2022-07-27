from src.errors.exceptions import RepositoryError


class RepoGrade:
    def __init__(self):
        """
        Here we have the init for the class RepoGrade in which we initialize the list of grades
        """
        self.__grades = []

    def __len__(self):
        """
         Here we have function to determinate the length of the list of grades
        :return: The length of the list of grades
        """
        return len(self.__grades)

    def add_grade(self, grade):
        """
        Here we have a function that assigns an assignment to a student by grading it with 0
        :param grade: An object of type grade with value_grade = 0
        :return: Nothing. RepositoryError if the assignment was already assigned
        """
        for _grade in self.__grades:
            if _grade.get_id_ass_grade() == grade.get_id_ass_grade() and _grade.get_id_stud_grade() == grade.get_id_stud_grade():
                raise RepositoryError("The assignment was already assigned for the student!\n")
        self.__grades.append(grade)

    def update_grade(self, id_ass_grade, id_stud_grade, value):
        """
        Here we have a function that grades the assignment of a student by updating his value_grade
        :param id_ass_grade: An id of an assignment
        :param id_stud_grade: An id of a student
        :param value: The value you want to use to update the value_grade
        :return:Nothing. RepositoryError if the assignment was already graded or the student is non-existant
        """
        ok = False
        position = 0
        grade_position = -1
        for _grade in self.__grades:
            if _grade.get_id_ass_grade() == id_ass_grade and _grade.get_id_stud_grade() == id_stud_grade:
                if _grade.get_value_grade() != 0:
                    raise RepositoryError("The assignment was already graded for the student!\n")
                else:
                    grade_position = position
                    ok = True
            position += 1
        if not ok:
            raise RepositoryError("The student doesn't have such an assignment assigned!\n")
        else:
            self.__grades[grade_position].set_value_grade(value)

    def remove_assignment(self, id_stud):
        """
        Here we have a function that removes all the assignments assigned to a student in case we want to remove the student
        :param id_stud: The id of the student we removed
        :return: Nothing. RepositoryError if the student does not exist
        """
        ok = True
        length_list_grades = len(self.__grades)
        i = 0
        op_list = []
        try:
            while i <= length_list_grades:
                if self.__grades[i].get_id_stud_grade() == id_stud:
                    op_list.append(["delete", [self.__grades[i].get_id_ass_grade(), id_stud, self.__grades[i].get_value_grade()]])
                    del self.__grades[i]
                    i = i - 1
                    length_list_grades -= 1
                    ok = False
                i += 1
        except IndexError:
            pass
        if ok:
            raise RepositoryError("inexisting id!")
        return op_list

    def remove_grade(self, id_ass):
        """
        Here we have a function that removes all the assigments and the grades assigned to a student in case we want to remove an assignment
        :param id_ass: The id of the assignment we removed
        :return: Nothing. RepositoryError if the assignment does not exist
        """
        ok = True
        length_list_grades = len(self.__grades)
        i = 0
        op_list = []
        try:
            while i <= length_list_grades:
                if self.__grades[i].get_id_ass_grade() == id_ass:
                    op_list.append(["delete", [id_ass, self.__grades[i].get_id_stud_grade(), self.__grades[i].get_value_grade()]])
                    del self.__grades[i]
                    i = i - 1
                    length_list_grades -= 1
                    ok = False
                i += 1
        except IndexError:
            pass
        if ok:
                raise RepositoryError("inexisting id!")
        return op_list

    def remove_grade_by_ids(self, id_stud, id_ass):
        ok = True
        position = 0
        for _grade in self.__grades:
            if _grade.get_id_stud_grade() == id_stud and _grade.get_id_ass_grade() == id_ass:
                ok = False
                del self.__grades[position]
            position += 1
        if ok:
            raise RepositoryError("inexisting id!")

    def set_value_grade_to_zero(self, id_stud, id_ass):
        ok = True
        position = 0
        for _grade in self.__grades:
            if _grade.get_id_stud_grade() == id_stud and _grade.get_id_ass_grade() == id_ass:
                ok = False
                self.__grades[position].set_value_grade(0)
            position +=1
        if ok:
            raise RepositoryError("inexisting id!")

    def get_all_grades_repo(self):
        """
        Here we have a getter for the list of grades
        :return: The list of grades
        """
        return self.__grades[:]
