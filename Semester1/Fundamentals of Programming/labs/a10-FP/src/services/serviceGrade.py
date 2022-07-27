from src.domain.grade import Grade
from src.domain.student import StudentGradeSort, StudentAverage
from src.Iterable.Iterable import *
import datetime


class ServiceGrade:
    def __init__(self, valid_student, valid_assignment, valid_grade, repo_student, repo_assignment, repo_grade):
        """
        Here we have the init for the class ServiceGrade in which we initialize all the repos and the validators because it is the connection class
        :param valid_student: The validator for student
        :param valid_assignment: The validator for assignment
        :param valid_grade: The validator for grade
        :param repo_student: The repository for student
        :param repo_assignment: The repository for assignment
        :param repo_grade: The repository for grade
        """
        self.__valid_student = valid_student
        self.__valid_assignment = valid_assignment
        self.__valid_grade = valid_grade
        self.__repo_student = repo_student
        self.__repo_assignment = repo_assignment
        self.__repo_grade = repo_grade

    def number_of_grades(self):
        """
        Here we have the length of the repository
        :return: The length of the repository
        """
        return len(self.__repo_grade)

    def add_assignment_to_student(self, id_ass, id_stud):
        """
        Here we validate if the ids of the student and assignment and if they exist and they are valid we call the repo.add_grade
        :param id_ass: An id of an assignment
        :param id_stud: An id of a student
        :return: Nothing
        """
        grade = Grade(id_ass, id_stud, value_grade=0)
        self.__valid_assignment.validate_id_ass(id_ass)
        self.__valid_student.validate_id_stud(id_stud)
        ok_ass = False
        ok_stud = False
        for student in self.__repo_student.get_all_students_repo():
            if student.get_id_stud() == id_stud:
                ok_stud = True
        for assignment in self.__repo_assignment.get_all_assignments_repo():
            if assignment.get_id_ass() == id_ass:
                ok_ass = True
        if ok_ass and ok_stud:
            self.__repo_grade.add_grade(grade)

    def add_assignment_to_group(self, id_ass, group):
        """
        For every student from the choosen group we validate the id_ass and call the repo.add_grade
        :param id_ass: An id of an assignment
        :param group: A group of students
        :return: Nothing
        """
        for student in self.__repo_student.get_all_students_repo():
            if student.get_group() == int(group):
                grade = Grade(id_ass, student.get_id_stud(), value_grade=0)
                self.__valid_student.validate_group(group)
                self.__valid_grade.validate(grade)
                self.__repo_grade.add_grade(grade)

    def add_grade_to_assignment(self, id_ass, id_stud, value_grade):
        """
        Here we validate the id_ass, id_stud, value_grade, then we call the repo.update_grade function
        :param id_ass: An id of an assignment
        :param id_stud: An id of a student
        :param value_grade: A value of a grade
        :return: Nothing
        """
        self.__valid_assignment.validate_id_ass(id_ass)
        self.__valid_student.validate_id_stud(id_stud)
        self.__valid_grade.validate_value_grade(value_grade)
        self.__repo_grade.update_grade(id_ass, id_stud, value_grade)

    def remove_all_assignments(self, id_stud):
        """
        Here we validate the id_stud, then we call the repo.remove_assignment function
        :param id_stud:
        :return:
        """
        self.__valid_student.validate_id_stud(id_stud)
        return self.__repo_grade.remove_assignment(id_stud)

    def remove_all_grades(self, id_ass):
        """
        Here we validate the id_ass, then we call the repo.remove_grade function
        :param id_ass:
        :return:
        """
        self.__valid_assignment.validate_id_ass(id_ass)
        return self.__repo_grade.remove_grade(id_ass)

    def remove_grade(self, id_stud, id_ass):
        self.__valid_student.validate_id_stud(id_stud)
        self.__valid_assignment.validate_id_ass(id_ass)
        self.__repo_grade.remove_grade_by_ids(id_stud, id_ass)

    def remove_grade_graded(self, id_stud, id_ass):
        self.__valid_student.validate_id_stud(id_stud)
        self.__valid_assignment.validate_id_ass(id_ass)
        self.__repo_grade.set_value_grade_to_zero(id_stud, id_ass)

    def get_all_grades(self):
        """
        Here we call the repo function that gets the list of grades
        :return:
        """
        return self.__repo_grade.get_all_grades_repo()

    def first_statistic(self, id_ass):
        grades = self.__repo_grade.get_all_grades_repo()
        school_situation = {}
        for grade in grades:
            student_id = grade.get_id_stud_grade()
            if grade.get_id_ass_grade() == id_ass and grade.get_value_grade() != 0:
                school_situation[student_id] = grade.get_value_grade()
        res = []
        for student_id in school_situation:
            student = self.__repo_student.search_by_id_student(student_id)
            student_name = student.get_name()
            student_group = student.get_group()
            student_value_grade = school_situation[student_id]
            student_grade_sort = StudentGradeSort(student_id, student_name, student_group, student_value_grade)
            res.append(student_grade_sort)
        res = Iterable.sort(res, lambda x, y: x.get_value_grade() < y.get_value_grade())
        return res

    def second_statistic(self):
        current_time_year = datetime.datetime.now().year
        current_time_month = datetime.datetime.now().month
        current_time_day = datetime.datetime.now().day
        current_time = datetime.date(current_time_year, current_time_month, current_time_day)
        assignments = self.__repo_assignment.get_all_assignments_repo()
        #print(assignments)
        #for assignment in assignments:
            #if assignment.get_deadline() < current_time:
             #   list_of_assignments_passed_deadline.append(assignment.get_id_ass())
        list_of_assignments_passed_deadline = Iterable.filter(assignments, lambda assignment: assignment.get_deadline() < current_time)
        ids_of_assignments_passed_deadline = []
        for assignment in list_of_assignments_passed_deadline:
            ids_of_assignments_passed_deadline.append(assignment.get_id_ass())
        grades = self.__repo_grade.get_all_grades_repo()
        school_situation = {}
        for grade in grades:
            student_id = grade.get_id_stud_grade()
            if grade.get_id_ass_grade() in ids_of_assignments_passed_deadline and grade.get_value_grade() == 0:
                school_situation[student_id] = student_id
        res = []
        for student_id in school_situation:
            student = self.__repo_student.search_by_id_student(student_id)
            res.append(student)
        return res

    def third_statistic(self):
        grades = self.__repo_grade.get_all_grades_repo()
        school_situation = {}
        for grade in grades:
            student_id = grade.get_id_stud_grade()
            if student_id not in school_situation:
                school_situation[student_id] = []
            school_situation[student_id].append(grade.get_value_grade())
        res = []
        for student_id in school_situation:
            student_name = self.__repo_student.search_by_id_student(student_id)
            student_average = sum(school_situation[student_id]) / len(school_situation[student_id])
            student_averageDTO = StudentAverage(student_name, student_average)
            res.append(student_averageDTO)
        #res.sort(key=lambda x: x.get_average(), reverse=True)
        res = Iterable.sort(res, lambda x, y: x.get_average() < y.get_average())
        return res
