import pickle
import os
from datetime import datetime

from src.domain.student import Student
from src.domain.assignment import Assignment
from src.domain.grade import Grade


class StudentDataAccess:
    """
    Methods for reading/writing student from/to files
    """

    @staticmethod
    def read_from_text_file(line):
        student_data = line.split(",")
        student = Student(int(student_data[0]),
                          student_data[1],
                          int(student_data[2].rstrip("\n")))
        return student

    @staticmethod
    def write_in_text_file(students, file_pointer):
        for i, student in enumerate(students):
            if i == 0:
                file_pointer.write(f"{student.get_id_stud()}, "
                                   f"{student.get_name()}, "
                                   f"{student.get_group()}")
            else:
                file_pointer.write(f"\n{student.get_id_stud()}, "
                                   f"{student.get_name()}, "
                                   f"{student.get_group()}")

    @staticmethod
    def read_from_binary_file(file_path):
        if os.path.getsize(file_path) == 0:
            return []
        with open(file_path, "rb") as file_pointer:
            data = pickle.load(file_pointer)
            return data

    @staticmethod
    def write_in_binary_file(file_path, data):
        with open(file_path, "wb") as file_pointer:
            pickle.dump(data, file_pointer)


class AssignmentDataAccess:
    @staticmethod
    def read_from_text_file(line):
        assignment_data = line.split(",")
        assignment = Assignment(int(assignment_data[0]),
                                assignment_data[1],
                                datetime.fromisoformat(assignment_data[2].rstrip("\n")).date())
        return assignment

    @staticmethod
    def write_in_text_file(assignments, file_pointer):
        for i, assignment in enumerate(assignments):
            if i == 0:
                file_pointer.write(f"{assignment.get_id_ass()},"
                                   f"{assignment.get_description()},"
                                   f"{assignment.get_deadline()}")
            else:
                file_pointer.write(f"\n{assignment.get_id_ass()}, "
                                   f"{assignment.get_description()},"
                                   f"{assignment.get_deadline()}")

    @staticmethod
    def read_from_binary_file(file_path):
        if os.path.getsize(file_path) == 0:
            return []
        with open(file_path, "rb") as file_pointer:
            data = pickle.load(file_pointer)
            return data

    @staticmethod
    def write_in_binary_file(file_path, data):
        with open(file_path, "wb") as file_pointer:
            pickle.dump(data, file_pointer)


class GradeDataAccess:
    @staticmethod
    def read_from_text_file(line):
        grade_data = line.split(",")
        grade = Grade(int(grade_data[0]),
                      int(grade_data[1]),
                      int(grade_data[2].rstrip("\n")))
        return grade

    @staticmethod
    def write_in_text_file(grades, file_pointer):
        for i, grade in enumerate(grades):
            if i == 0:
                file_pointer.write(f"{grade.get_id_ass_grade()}, "
                                   f"{grade.get_id_stud_grade()}, "
                                   f"{grade.get_value_grade()}")
            else:
                file_pointer.write(f"\n{grade.get_id_ass_grade()}, "
                                   f"{grade.get_id_stud_grade()}, "
                                   f"{grade.get_value_grade()}")

    @staticmethod
    def read_from_binary_file(file_path):
        if os.path.getsize(file_path) == 0:
            return []
        with open(file_path, "rb") as file_pointer:
            data = pickle.load(file_pointer)
            return data

    @staticmethod
    def write_in_binary_file(file_path, data):
        with open(file_path, "wb") as file_pointer:
            pickle.dump(data, file_pointer)



