from src.errors.exceptions import RepositoryError
from src.domain.student import Student
from src.Iterable.Iterable import *
import random


class RepoStudent:
    def __init__(self, students=None):
        """
        Here we have the init for the class RepoStudent in which we initialize the list of students
        """
        if students == None:
            students = []
        if students is Iterable:
            self.__students = students
        else:
            self.__students = Iterable(students)

    def __len__(self):
        """
        Here we have function to determinate the length of the list of students
        :return: The length of the list of students
        """
        return len(self.__students)

    def add_student(self, student):
        """
        Here we add a Student to the list of students if the id isn't already in list
        :param student: An object from class Student
        :return: Nothing. It adds a Student to the list of students
        """
        for _student in self.__students:
            if _student.get_id_stud() == student.get_id_stud():
                raise RepositoryError("existing id!")
        self.__students.append(student)

    def remove_student_by_id(self, id_stud):
        """
        Here we remove a Student from the list of students if we can find it in the list
        :param id_stud: An id of a student
        :return: Nothing. It removes a Student from the list of students
        """
        ok = True
        for _student in self.__students:
            if _student.get_id_stud() == id_stud:
                self.__students.__delitem__(_student)
                ok = False
        if ok:
            raise RepositoryError("inexisting id")

    def search_by_id_student(self, id_stud):
        """
        Here we search a Student in the list of students by his id
        :param id_stud: An id of a student
        :return: The student we were searching for if we find it, RepositoryError otherwise
        """
        ok = True
        for _student in self.__students:
            if _student.get_id_stud() == id_stud:
                return _student
        if ok:
            raise RepositoryError("inexisting id!")

    def update_by_id_student_name(self, id_stud, value):
        """
        Here we update a Student's description by its id
        :param id_stud: An id of a student
        :param value: The name we want to update with
        :return: Nothing. It sets the old name with the new name if the id exists
        """
        ok = False
        student_position = -1
        for position in range(self.__len__()):
            if self.__students[position].get_id_stud() == id_stud:
                student_position = position
                ok = True
        if not ok:
            raise RepositoryError("inexisting id!")
        else:
            self.__students[student_position].set_name(value)

    def update_by_id_student_group(self, id_stud, value):
        """
        Here we update a Student's group by its id
        :param id_stud: An id of a student
        :param value: The group we want to update with
        :return: Nothing. It sets the old group with the new group if the id exists
        """
        ok = False
        student_position = -1
        for position in range(self.__len__()):
            if self.__students[position].get_id_stud() == id_stud:
                student_position = position
                ok = True
        if not ok:
            raise RepositoryError("inexisting id!")
        else:
            self.__students[student_position].set_group(value)

    def get_all_students_repo(self):
        """
         Here we have a getter for the list of students
        :return: The list of students
        """
        return self.__students[:]

    def populate_student(self):
        """
        In this function we populate the list of students with 20 random Students
        :return: Nothing. We create a list with 20 entities
        """
        list_name =[
                    "Gligor Pașcu Ovidiu", "Goia Alexia Maria", "Grab Andrei", "Groza Iulia-Diana",
                    "Groza Vlad-Andrei", "Guceanu George-Marian", "Guia Alex", "Gulei-Grădinaru Daniel-Andrei",
                    "GyÖrgy Ferenc", "Halmagyi-Filip Nicholas", "Haranguș Dan-Ioan", "Haranguș Robert-Adrian",
                    "Havîrneanu Albert-Andrei", "Hideg Paul", "Hognogi Ana-Maria Cristina",
                    "Homescu Monica Daniella", "Hornea Dorian-Alexandru", "Horvath David-Cristian",
                    "Horvath Krisztina-Aliz", "Hoszu Bernadett-Sabrina", "Hudema Dana",
                    "Iaguța Alen-Mihael", "Iakab Alex-Edward", "Iancu Gheorghe-Aurelian", "Ifrim Cristian",
                    "Ilie Oana-Andreea", "Iliescu Andrei", "Iliesi Antonia-Catrinel", "Ion Bogdan"
                    ]
        for i in range(20):
            self.__students.append(Student(i, random.choice(list_name), random.randint(911, 917)))
        return self.__students