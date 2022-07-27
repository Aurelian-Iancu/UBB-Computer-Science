from src.domain.student import Student, StudentGradeSort, StudentAverage
from src.domain.assignment import Assignment
from src.domain.grade import Grade

from src.validation.validatorStudent import ValidatorStudent
from src.validation.validatorAssignment import ValidatorAssignment
from src.validation.validatorGrade import ValidatorGrade

from src.errors.exceptions import ValidationError, RepositoryError

from src.repository.repositoryStudent import RepoStudent
from src.repository.repositoryAssignment import RepoAssignment
from src.repository.repositoryGrade import RepoGrade

from src.services.serviceStudent import ServiceStudent
from src.services.serviceAssignment import ServiceAssignment
from src.services.serviceGrade import ServiceGrade
from src.services.serviceUndo import ServiceUndo

import datetime
import unittest


class DomainAndValidatorsTests(unittest.TestCase):
    def test_create_student(self):
        student = Student(1, "Richard", 913)
        self.assertEqual(student.get_id_stud(), 1)
        self.assertEqual(student.get_name(), "Richard")
        self.assertEqual(student.get_group(), 913)
        self.assertEqual(str(student), "1. Richard from group 913")
        student.set_name("Robin")
        self.assertEqual(student.get_name(), "Robin")
        student.set_group(914)
        self.assertEqual(student.get_group(), 914)

        studentGradeSort = StudentGradeSort(1, "Richard", 913, 9)
        self.assertEqual(studentGradeSort.get_value_grade(), 9)
        self.assertEqual(str(studentGradeSort), "Student 1. Richard from group 913 with the grade 9")

        studentAverage = StudentAverage("Richard", 9.3)
        self.assertEqual(studentAverage.get_average(), 9.3)
        self.assertEqual(str(studentAverage), "Student Richard with average 9.3")

    def test_validation_student(self):
        student = Student(-1, "Richard", 913)
        self.assertRaises(ValidationError, ValidatorStudent.validate, student)
        student = Student(1, "", 913)
        self.assertRaises(ValidationError, ValidatorStudent.validate, student)
        student = Student(1, "Richard", 910)
        self.assertRaises(ValidationError, ValidatorStudent.validate, student)
        self.assertRaises(ValidationError, ValidatorStudent.validate_id_stud, -1)
        self.assertRaises(ValidationError, ValidatorStudent.validate_name, "")
        self.assertRaises(ValidationError, ValidatorStudent.validate_group, 900)

    def test_create_assignment(self):
        assignment = Assignment(1, "Assignment678", datetime.date(2021, 12, 30))
        self.assertEqual(assignment.get_id_ass(), 1)
        self.assertEqual(assignment.get_description(), "Assignment678")
        self.assertEqual(assignment.get_deadline(), datetime.date(2021, 12, 30))
        self.assertEqual(str(assignment), "1.You have the next assignment:\nAssignment678\nThe due date is: 2021-12-30")
        assignment.set_description("ABCD")
        self.assertEqual(assignment.get_description(), "ABCD")
        assignment.set_deadline(datetime.date(2020, 12, 30))
        self.assertEqual(assignment.get_deadline(), datetime.date(2020, 12, 30))

    def test_validation_assignment(self):
        assignment = Assignment(-1, "Assignment678", datetime.date(2021, 12, 30))
        self.assertRaises(ValidationError, ValidatorAssignment.validate, assignment)
        assignment = Assignment(1, "", datetime.date(2021, 12, 30))
        self.assertRaises(ValidationError, ValidatorAssignment.validate, assignment)
        self.assertRaises(ValidationError, ValidatorAssignment.validate_id_ass, -1)
        self.assertRaises(ValidationError, ValidatorAssignment.validate_description, "")

    def test_create_grade(self):
        grade = Grade(1, 2, 10)
        self.assertEqual(grade.get_id_ass_grade(), 1)
        self.assertEqual(grade.get_id_stud_grade(), 2)
        self.assertEqual(grade.get_value_grade(), 10)
        grade.set_value_grade(9)
        self.assertEqual(grade.get_value_grade(), 9)
        self.assertEqual(str(grade), "The grade for student with the id: 2 at the assignment with the id: 1 is 9")

    def test_validation_grade(self):
        grade = Grade(-1, 1, 10)
        self.assertRaises(ValidationError, ValidatorGrade.validate, grade)
        grade = Grade(1, -1, 10)
        self.assertRaises(ValidationError, ValidatorGrade.validate, grade)
        grade = Grade(1, 2, -1)
        self.assertRaises(ValidationError, ValidatorGrade.validate, grade)
        self.assertRaises(ValidationError, ValidatorGrade.validate_value_grade, 11)


class RepoStudentTests(unittest.TestCase):
    def test_student_add_repo(self):
        repository = RepoStudent()
        self.assertEqual(len(repository.get_all_students_repo()), 0)
        repository.add_student(Student(1, "Richard", 913))
        self.assertEqual(len(repository.get_all_students_repo()), 1)
        self.assertEqual(repository.get_all_students_repo(), [Student(1, "Richard", 913)])
        repository.add_student(Student(2, "Robin", 913))
        self.assertEqual(repository.get_all_students_repo(), [Student(1, "Richard", 913), Student(2, "Robin", 913)])
        student = Student(1, "Duke", 913)
        self.assertRaises(RepositoryError, repository.add_student, student)

    def test_student_remove_repo(self):
        repository = RepoStudent()
        repository.add_student(Student(1, "Richard", 913))
        repository.add_student(Student(2, "Robin", 913))
        repository.remove_student_by_id(1)
        self.assertEqual(repository.get_all_students_repo(), [Student(2, "Robin", 913)])
        self.assertRaises(RepositoryError, repository.remove_student_by_id, 1)

    def test_student_update_name_repo(self):
        repository = RepoStudent()
        repository.add_student(Student(1, "Richard", 913))
        repository.update_by_id_student_name(1, "Duke")
        self.assertEqual(repository.get_all_students_repo(), [Student(1, "Duke", 913)])
        self.assertRaises(RepositoryError, repository.update_by_id_student_name, 2, "Vasile")

    def test_student_update_group_repo(self):
        repository = RepoStudent()
        repository.add_student(Student(1, "Richard", 913))
        repository.update_by_id_student_group(1, 911)
        self.assertEqual(repository.get_all_students_repo(), [Student(1, "Richard", 911)])
        self.assertRaises(RepositoryError, repository.update_by_id_student_group, 2, 911)

    def test_student_search_by_id_repo(self):
        repository = RepoStudent()
        repository.add_student(Student(1, "Richard", 913))
        self.assertEqual(repository.search_by_id_student(1), Student(1, "Richard", 913))
        self.assertRaises(RepositoryError, repository.search_by_id_student, 2)

    def test_student_populate(self):
        repository = RepoStudent()
        repository.populate_student()
        self.assertEqual(len(repository.get_all_students_repo()), 20)


class RepoAssignmentTests(unittest.TestCase):
    def test_assignment_add_repo(self):
        repository = RepoAssignment()
        self.assertEqual(len(repository.get_all_assignments_repo()), 0)
        repository.add_assignment(Assignment(1, "Assignment678", datetime.date(2020, 11, 30)))
        repository.add_assignment(Assignment(2, "Assignment678", datetime.date(2021, 12, 15)))
        self.assertEqual(len(repository.get_all_assignments_repo()), 2)
        self.assertEqual(repository.get_all_assignments_repo(), [Assignment(1, "Assignment678", datetime.date(2020, 11, 30)), Assignment(2, "Assignment678", datetime.date(2021, 12, 15))])
        assignment = Assignment(1, "afsafs", datetime.date(2020, 11, 30))
        self.assertRaises(RepositoryError, repository.add_assignment, assignment)

    def test_assignment_remove_repo(self):
        repository = RepoAssignment()
        repository.add_assignment(Assignment(1, "Assignment678", datetime.date(2020, 11, 30)))
        repository.add_assignment(Assignment(2, "Assignment678", datetime.date(2021, 12, 15)))
        repository.remove_assignment_by_id(1)
        self.assertEqual(repository.get_all_assignments_repo(), [Assignment(2, "Assignment678", datetime.date(2021, 12, 15))])
        self.assertRaises(RepositoryError, repository.remove_assignment_by_id, 1)

    def test_assignment_update_description_repo(self):
        repository = RepoAssignment()
        repository.add_assignment(Assignment(1, "Assignment678", datetime.date(2020, 11, 30)))
        repository.update_by_id_assignment_description(1, "I don't know")
        self.assertEqual(repository.get_all_assignments_repo(), [Assignment(1, "I don't know", datetime.date(2020, 11, 30))])
        self.assertRaises(RepositoryError, repository.update_by_id_assignment_description, 2, "I don't know")

    def test_assignment_update_deadline_repo(self):
        repository = RepoAssignment()
        repository.add_assignment(Assignment(1, "Assignment678", datetime.date(2020, 11, 30)))
        repository.update_by_id_assignment_deadline(1, datetime.date(2021, 11, 30))
        self.assertEqual(repository.get_all_assignments_repo(), [Assignment(1, "Assignment678", datetime.date(2021, 11, 30))])
        self.assertRaises(RepositoryError, repository.update_by_id_assignment_deadline, 2, datetime.date(2022, 11, 30))

    def test_assignment_search_by_id_repo(self):
        repository = RepoAssignment()
        repository.add_assignment(Assignment(1, "Assignment678", datetime.date(2020, 11, 30)))
        self.assertEqual(repository.search_by_id_assignment(1), Assignment(1, "Assignment678", datetime.date(2020, 11, 30)))
        self.assertRaises(RepositoryError, repository.search_by_id_assignment, 2)

    def test_populate_assignment(self):
        repository = RepoAssignment()
        repository.populate_assignment()
        self.assertEqual(len(repository.get_all_assignments_repo()), 20)


class RepoGradeTests(unittest.TestCase):
    def test_grade_add_repo(self):
        repository = RepoGrade()
        self.assertEqual(len(repository.get_all_grades_repo()), 0)
        repository.add_grade(Grade(1, 1, 0))
        repository.add_grade(Grade(2, 2, 0))
        repository.add_grade(Grade(3, 3, 0))
        self.assertEqual(len(repository.get_all_grades_repo()), 3)
        self.assertEqual(repository.get_all_grades_repo(), [Grade(1, 1, 0), Grade(2, 2, 0), Grade(3, 3, 0)])
        grade = Grade(1, 1, 0)
        self.assertRaises(RepositoryError, repository.add_grade, grade)

    def test_grade_remove_repo(self):
        repository = RepoGrade()
        repository.add_grade(Grade(1, 1, 10))
        repository.add_grade(Grade(2, 2, 8))
        repository.add_grade(Grade(3, 3, 5))
        repository.remove_grade(1)
        self.assertEqual(repository.get_all_grades_repo(), [Grade(2, 2, 8), Grade(3, 3, 5)])
        repository.remove_assignment(2)
        self.assertEqual(repository.get_all_grades_repo(), [Grade(3, 3, 5)])
        self.assertRaises(RepositoryError, repository.remove_grade, 1)
        self.assertRaises(RepositoryError, repository.remove_assignment, 1)

    def test_grade_update_repo(self):
        repository = RepoGrade()
        repository.add_grade(Grade(1, 1, 0))
        repository.update_grade(1, 1, 10)
        self.assertEqual(repository.get_all_grades_repo(), [Grade(1, 1, 10)])
        self.assertRaises(RepositoryError, repository.update_grade, 1, 1, 10)
        self.assertRaises(RepositoryError, repository.update_grade, 2, 1, 10)
        self.assertRaises(RepositoryError, repository.update_grade, 1, 2, 10)

    def test_remove_grade_by_ids(self):
        repository = RepoGrade()
        repository.add_grade(Grade(1, 1, 0))
        repository.remove_grade_by_ids(1, 1)
        self.assertEqual(repository.get_all_grades_repo(), [])
        self.assertRaises(RepositoryError, repository.remove_grade_by_ids, 1, 1)

    def test_set_value_grade_to_zero(self):
        repository = RepoGrade()
        repository.add_grade(Grade(1, 1, 0))
        repository.update_grade(1, 1, 10)
        repository.set_value_grade_to_zero(1, 1)
        self.assertEqual(repository.get_all_grades_repo(), [Grade(1, 1, 0)])
        self.assertRaises(RepositoryError, repository.set_value_grade_to_zero, 2, 2)


class ServiceStudentTests(unittest.TestCase):
    def setUp(self):
        self.repo_student = RepoStudent()
        self.valid_student = ValidatorStudent
        self.srv_student = ServiceStudent(self.valid_student, self.repo_student)

    def test_student_add_service(self):
        self.assertEqual(len(self.srv_student.get_all_students()), 0)
        self.srv_student.add_student(1, "Richard", 913)
        self.srv_student.add_student(2, "Robin", 914)
        self.assertEqual(len(self.srv_student.get_all_students()), self.srv_student.number_of_students())
        self.assertEqual(self.srv_student.get_all_students(), [Student(1, "Richard", 913), Student(2, "Robin", 914)])

    def test_student_remove_service(self):
        self.srv_student.add_student(1, "Richard", 913)
        self.srv_student.add_student(2, "Robin", 914)
        self.srv_student.remove_student(1)
        self.assertEqual(self.srv_student.get_all_students(), [Student(2, "Robin", 914)])

    def test_student_update_name_service(self):
        self.srv_student.add_student(1, "Richard", 913)
        self.srv_student.update_student_name(1, "Robin")
        self.assertEqual(self.srv_student.get_all_students(), [Student(1, "Robin", 913)])

    def test_student_update_group_service(self):
        self.srv_student.add_student(1, "Richard", 913)
        self.srv_student.update_student_group(1, 911)
        self.assertEqual(self.srv_student.get_all_students(), [Student(1, "Robin", 911)])

    def test_student_populate_service(self):
        self.srv_student.populate_student()
        self.assertEqual(len(self.srv_student.get_all_students()), 20)


class ServiceAssignmentTests(unittest.TestCase):
    def setUp(self):
        self.repo_assignment = RepoAssignment()
        self.valid_assignment = ValidatorAssignment
        self.srv_assignment = ServiceAssignment(self.valid_assignment, self.repo_assignment)

    def test_assignment_add_service(self):
        self.assertEqual(len(self.srv_assignment.get_all_assignments()), 0)
        self.srv_assignment.add_assignment(1, "Assignment678", datetime.date(2020, 11, 11))
        self.assertEqual(len(self.srv_assignment.get_all_assignments()), 1)
        self.assertEqual(len(self.srv_assignment.get_all_assignments()), self.srv_assignment.number_of_assignments())
        self.assertEqual(self.srv_assignment.get_all_assignments(), [Assignment(1, "Assignment678", datetime.date(2020, 11, 11))])

    def test_assignment_remove_service(self):
        self.srv_assignment.add_assignment(1, "Assignment678", datetime.date(2020, 11, 11))
        self.srv_assignment.remove_assignment(1)
        self.assertEqual(self.srv_assignment.get_all_assignments(), [])

    def test_assignment_update_description_service(self):
        self.srv_assignment.add_assignment(1, "Assignment678", datetime.date(2020, 11, 11))
        self.srv_assignment.update_assignment_description(1, "Assignment5")
        self.assertEqual(self.srv_assignment.get_all_assignments(), [Assignment(1, "Assignment5", datetime.date(2020, 11, 11))])

    def test_assignment_update_deadline_service(self):
        self.srv_assignment.add_assignment(1, "Assignment678", datetime.date(2020, 11, 11))
        self.srv_assignment.update_assignment_deadline(1, datetime.date(2021, 11, 11))
        self.assertEqual(self.srv_assignment.get_all_assignments(), [Assignment(1, "Assignment678", datetime.date(2021, 11, 11))])

    def test_assignment_populate_service(self):
        self.srv_assignment.populate_assignment()
        self.assertEqual(len(self.srv_assignment.get_all_assignments()), 20)


class ServiceGradeTests(unittest.TestCase):
    def setUp(self):
        self.repo_student = RepoStudent()
        self.repo_assignment = RepoAssignment()
        self.repo_grade = RepoGrade()
        self.validate_student = ValidatorStudent
        self.validate_assignment = ValidatorAssignment
        self.validate_grade = ValidatorGrade
        self.srv_grade = ServiceGrade(self.validate_student, self.validate_assignment, self.validate_grade, self.repo_student,
                                      self.repo_assignment, self.repo_grade)
        self.srv_student = ServiceStudent(self.validate_student, self.repo_student)
        self.srv_assignment = ServiceAssignment(self.validate_assignment, self.repo_assignment)

    def test_add_assignment_to_student_service(self):
        self.srv_student.add_student(1, "Richard", 913)
        self.srv_assignment.add_assignment(1, "Assignment678", datetime.date(2020, 11, 11))
        self.assertEqual(len(self.srv_grade.get_all_grades()), 0)
        self.srv_grade.add_assignment_to_student(1, 1)
        self.assertEqual(len(self.srv_grade.get_all_grades()), 1)
        self.assertEqual(len(self.srv_grade.get_all_grades()), self.srv_grade.number_of_grades())
        self.assertEqual(self.srv_grade.get_all_grades(), [Grade(1, 1, 0)])

    def test_add_assignment_to_group_service(self):
        self.srv_student.add_student(1, "Richard", 913)
        self.srv_student.add_student(2, "Robin", 913)
        self.srv_assignment.add_assignment(1, "Assignment678", datetime.date(2020, 11, 11))
        self.srv_grade.add_assignment_to_group(1, 913)
        self.assertEqual(self.srv_grade.get_all_grades(), [Grade(1, 1, 0), Grade(1, 2, 0)])

    def test_add_grade_to_assignment_service(self):
        self.srv_student.add_student(1, "Richard", 913)
        self.srv_assignment.add_assignment(1, "Assignment678", datetime.date(2020, 11, 11))
        self.srv_grade.add_assignment_to_student(1, 1)
        self.srv_grade.add_grade_to_assignment(1, 1, 10)
        self.assertEqual(self.srv_grade.get_all_grades(), [Grade(1, 1, 10)])

    def test_remove_all_assignments_service(self):
        self.srv_student.add_student(1, "Richard", 913)
        self.srv_student.add_student(2, "Robin", 911)
        self.srv_assignment.add_assignment(1, "Assignment678", datetime.date(2020, 11, 11))
        self.srv_assignment.add_assignment(2, "Assignment678", datetime.date(2020, 12, 12))
        self.srv_grade.add_assignment_to_student(1, 1)
        self.srv_grade.add_assignment_to_student(1, 2)
        self.srv_grade.add_grade_to_assignment(1, 1, 10)
        self.srv_grade.remove_all_assignments(1)
        self.assertEqual(self.srv_grade.get_all_grades(), [Grade(1, 2, 0)])

    def test_remove_all_grades_service(self):
        self.srv_student.add_student(1, "Richard", 913)
        self.srv_student.add_student(2, "Robin", 911)
        self.srv_assignment.add_assignment(1, "Assignment678", datetime.date(2020, 11, 11))
        self.srv_assignment.add_assignment(2, "Assignment678", datetime.date(2020, 12, 12))
        self.srv_grade.add_assignment_to_student(1, 1)
        self.srv_grade.add_assignment_to_student(1, 2)
        self.srv_grade.add_grade_to_assignment(1, 1, 10)
        self.srv_grade.remove_all_grades(1)
        self.assertEqual(self.srv_grade.get_all_grades(), [])

    def test_remove_grade_by_ids(self):
        self.srv_student.add_student(1, "Richard", 913)
        self.srv_student.add_student(2, "Robin", 911)
        self.srv_assignment.add_assignment(1, "Assignment678", datetime.date(2020, 11, 11))
        self.srv_assignment.add_assignment(2, "Assignment678", datetime.date(2020, 12, 12))
        self.srv_grade.add_assignment_to_student(1, 1)
        self.srv_grade.remove_grade(1, 1)
        self.assertEqual(self.srv_grade.get_all_grades(), [])

    def test_set_value_grade_to_zero(self):
        self.srv_student.add_student(1, "Richard", 913)
        self.srv_student.add_student(2, "Robin", 911)
        self.srv_assignment.add_assignment(1, "Assignment678", datetime.date(2020, 11, 11))
        self.srv_assignment.add_assignment(2, "Assignment678", datetime.date(2020, 12, 12))
        self.srv_grade.add_assignment_to_student(1, 1)
        self.srv_grade.add_grade_to_assignment(1, 1, 10)
        self.srv_grade.remove_grade_graded(1, 1)
        self.assertEqual(self.srv_grade.get_all_grades(), [Grade(1, 1, 0)])

    def test_first_statistic_service(self):
        self.srv_student.add_student(1, "Richard", 913)
        self.srv_student.add_student(2, "Robin", 911)
        self.srv_student.add_student(3, "Rudolf", 916)

        self.srv_assignment.add_assignment(1, "Assignment678", datetime.date(2020, 11, 11))
        self.srv_assignment.add_assignment(2, "Assignment678", datetime.date(2020, 12, 12))
        self.srv_assignment.add_assignment(3, "Assignment678", datetime.date(2021, 1, 1))

        self.srv_grade.add_assignment_to_student(1, 1)
        self.srv_grade.add_assignment_to_student(1, 2)
        self.srv_grade.add_assignment_to_student(1, 3)

        self.srv_grade.add_grade_to_assignment(1, 1, 10)
        self.srv_grade.add_grade_to_assignment(1, 2, 8)
        self.srv_grade.add_grade_to_assignment(1, 3, 9)

        self.assertEqual(len(self.srv_grade.first_statistic(1)), 3)

    def test_second_statistic_service(self):
        self.srv_student.add_student(1, "Richard", 913)

        self.srv_assignment.add_assignment(1, "Assignment678", datetime.date(2020, 11, 11))
        self.srv_assignment.add_assignment(2, "Assignment678", datetime.date(2020, 12, 12))
        self.srv_assignment.add_assignment(3, "Assignment678", datetime.date(2022, 1, 1))

        self.srv_grade.add_assignment_to_student(1, 1)
        self.srv_grade.add_assignment_to_student(2, 1)
        self.srv_grade.add_assignment_to_student(3, 1)

        self.srv_grade.add_grade_to_assignment(2, 1, 8)
        self.srv_grade.add_grade_to_assignment(3, 1, 9)

        self.assertEqual(len(self.srv_grade.second_statistic()), 1)
        self.assertEqual(self.srv_grade.second_statistic(), [Student(1, "Richard", 913)])

    def test_third_statistic_service(self):
        self.srv_student.add_student(1, "Richard", 913)
        self.srv_student.add_student(2, "Robin", 911)
        self.srv_student.add_student(3, "Rudolf", 916)

        self.srv_assignment.add_assignment(1, "Assignment678", datetime.date(2020, 11, 11))
        self.srv_assignment.add_assignment(2, "Assignment678", datetime.date(2020, 12, 12))
        self.srv_assignment.add_assignment(3, "Assignment678", datetime.date(2021, 1, 1))

        self.srv_grade.add_assignment_to_student(1, 1)
        self.srv_grade.add_assignment_to_student(1, 2)
        self.srv_grade.add_assignment_to_student(2, 1)

        self.srv_grade.add_grade_to_assignment(1, 1, 10)
        self.srv_grade.add_grade_to_assignment(2, 1, 8)
        self.srv_grade.add_grade_to_assignment(1, 2, 9)

        self.assertEqual(len(self.srv_grade.third_statistic()), 2)


class ServiceUndoTests(unittest.TestCase):
    def setUp(self):
        self.repo_student = RepoStudent()
        self.repo_assignment = RepoAssignment()
        self.repo_grade = RepoGrade()
        self.validator_student = ValidatorStudent
        self.validator_assignment = ValidatorAssignment
        self.validator_grade = ValidatorGrade
        self.srv_student = ServiceStudent(self.validator_student, self.repo_student)
        self.srv_assignment = ServiceAssignment(self.validator_assignment, self.repo_assignment)
        self.srv_grade = ServiceGrade(self.validator_student, self.validator_assignment, self.validator_grade,
                                      self.repo_student, self.repo_assignment, self.repo_grade)
        self.srv_undo = ServiceUndo(self.srv_student, self.srv_assignment, self.srv_grade)

    def test_add_command_to_stack(self):
        self.srv_undo.add_command_to_stack("addCommand", [1, 1])
        self.assertEqual(self.srv_undo.get_stack(), [["addCommand", [1, 1]]])

    def test_getters(self):
        self.srv_undo.add_command_to_stack("addCommand", [1, 1])
        self.assertEqual(self.srv_undo.get_last_operation(), ["addCommand", [1, 1]])
        self.assertEqual(self.srv_undo.get_last_operation_command(["addCommand", [1, 1]]), "addCommand")
        self.assertEqual(self.srv_undo.get_last_operation_oject(["addCommand", [1, 1]]), [1, 1])

    def test_undo_redo_add_student(self):
        self.srv_student.add_student(1, "Aurelian", 913)
        self.assertEqual(self.repo_student.get_all_students_repo(), [Student(1, "Aurelian", 913)])
        self.srv_undo.undo_add_student(Student(1, "Aurelian", 913))
        self.assertEqual(self.repo_student.get_all_students_repo(), [])
        self.srv_undo.redo_add_student(Student(1, "Aurelian", 913))
        self.assertEqual(self.repo_student.get_all_students_repo(), [Student(1, "Aurelian", 913)])

    def test_undo_redo_remove_student(self):
        self.srv_student.add_student(1, "Aurelian", 913)
        self.assertEqual(self.repo_student.get_all_students_repo(), [Student(1, "Aurelian", 913)])
        self.srv_student.remove_student(1)
        self.assertEqual(self.repo_student.get_all_students_repo(), [])
        self.srv_undo.undo_remove_student(Student(1, "Aurelian", 913))
        self.assertEqual(self.repo_student.get_all_students_repo(), [Student(1, "Aurelian", 913)])
        self.srv_undo.redo_remove_student(Student(1, "Aurelian", 913))
        self.assertEqual(self.repo_student.get_all_students_repo(), [])

    def test_undo_redo_update_student(self):
        self.srv_student.add_student(1, "Aurelian", 913)
        self.assertEqual(self.repo_student.get_all_students_repo(), [Student(1, "Aurelian", 913)])
        self.srv_student.update_student_name(1, "Gheorghe")
        self.assertEqual(self.repo_student.get_all_students_repo(), [Student(1, "Gheorghe", 913)])
        self.srv_undo.undo_update_student([1, 1, "Aurelian", None])
        self.assertEqual(self.repo_student.get_all_students_repo(), [Student(1, "Aurelian", 913)])
        self.srv_undo.redo_update_student([1, 1, None, "Gheorghe"])
        self.srv_undo.undo_update_student([1, 1, "Aurelian", None])

        self.srv_student.update_student_group(1, 911)
        self.assertEqual(self.repo_student.get_all_students_repo(), [Student(1, "Aurelian", 911)])
        self.srv_undo.undo_update_student([2, 1, 913, None])
        self.assertEqual(self.repo_student.get_all_students_repo(), [Student(1, "Aurelian", 913)])
        self.srv_undo.undo_update_student([2, 1, 911, 911])
        self.assertEqual(self.repo_student.get_all_students_repo(), [Student(1, "Aurelian", 911)])

    def test_undo_redo_add_assignment(self):
        self.srv_assignment.add_assignment(1, "Assignment", datetime.date(2020, 11, 11))
        self.assertEqual(self.repo_assignment.get_all_assignments_repo(), [Assignment(1, "Assignment", datetime.date(2020, 11, 11))])
        self.srv_undo.undo_add_assignment(Assignment(1, "Assignment", datetime.date(2020, 11, 11)))
        self.assertEqual(self.repo_assignment.get_all_assignments_repo(), [])
        self.srv_undo.redo_add_assignment(Assignment(1, "Assignment", datetime.date(2020, 11, 11)))
        self.assertEqual(self.repo_assignment.get_all_assignments_repo(), [Assignment(1, "Assignment", datetime.date(2020, 11, 11))])













