from src.errors.exceptions import ValidationError, RepositoryError, UndoError

from src.domain.student import Student
from src.domain.assignment import Assignment
import datetime


class Console:
    def __init__(self, srv_student, srv_assignment, srv_grade, srv_undo):
        self.__srv_student = srv_student
        self.__srv_assignment = srv_assignment
        self.__srv_grade = srv_grade
        self.__srv_undo = srv_undo

    @staticmethod
    def __ui_print_menu():
        print("\t Student Lab Assignment Manager:")
        print("To use a command for students enter: S")
        print("To use a command for assignments enter: A")
        print("To add an assignment to a student enter: AS")
        print("To add an assignment to a group of students enter: AG")
        print("To print the list of assignments assigned to students enter: PA")
        print("To add a grade to an assignment enter: G")
        print("To print the list of grades enter: PG")
        print("To choose a command for statistics enter: STATS")
        print("To undo the last command enter: UNDO")
        print("To redo the last command enter: REDO")

    @staticmethod
    def __ui_print_menu_student():
        print("\tTo add a student enter: add")
        print("\tTo print the list of students enter: print")
        print("\tTo remove a student enter: remove")
        print("\tTo update the student's name enter: update_name")
        print("\tTo update the student's group enter: update_group")

    @staticmethod
    def __ui_print_menu_assignment():
        print("\tTo add an assignment enter: add")
        print("\tTo print the list of assignments enter: print")
        print("\tTo remove an assignment enter: remove")
        print("\tTo update the assignment's description enter: update_description")
        print("\tTo update the assignment's deadline enter: update_deadline")

    @staticmethod
    def __ui_print_menu_stats():
        print("\tTo print the first statistic enter: 1")
        print("\tTo print the second statistic: 2")
        print("\tTo print the third statistic: 3")

    def __ui_add_student(self):
        try:
            id_stud = int(input("Id student:"))
        except ValueError:
            print("Invalid numerical id")
            return
        name = input("Name:")
        try:
            group = int(input("Group(it has to be between 911-917):"))
        except ValueError:
            print("Invalid numerical group")
            return
        self.__srv_student.add_student(id_stud, name, group)
        self.__srv_undo.add_command_to_stack("sAdd", Student(id_stud, name, group))
        print("Student succesfully added")

    def __ui_print_students(self):
        number_of_students = self.__srv_student.number_of_students()
        if number_of_students == 0:
            print("No students present in list!")
            return
        all_students = self.__srv_student.get_all_students()
        for student in all_students:
            print(student)

    def __ui_remove_student(self):
        try:
            id_stud = int(input("Id student:"))
        except ValueError:
            print("Invalid numerical id")
            return
        all_students = self.__srv_student.get_all_students()
        all_grades = self.__srv_grade.get_all_grades()
        ok = True
        for grade in all_grades:
            if grade.get_id_stud_grade() == id_stud:
                ok = False
        op_list = []
        if not ok:
            for student in all_students:
                if student.get_id_stud() == id_stud:
                    op_list = self.__srv_grade.remove_all_assignments(id_stud)
                    self.__srv_student.remove_student(id_stud)
                    op_list.append(["sRemove", Student(id_stud, student.get_name(), student.get_group())])

                    self.__srv_undo.add_command_to_stack("cascade", op_list)
        else:
            for student in all_students:
                if student.get_id_stud() == id_stud:
                    self.__srv_student.remove_student(id_stud)
                    op_list.append(["sRemove", Student(id_stud, student.get_name(), student.get_group())])
                    self.__srv_undo.add_command_to_stack("cascade", op_list)

    def __ui_update_student_name(self):
        try:
            id_stud = int(input("Id student:"))
        except ValueError:
            print("Invalid numerical id")
            return
        name = input("Name:")
        all_students = self.__srv_student.get_all_students()
        for student in all_students:
            if student.get_id_stud() == id_stud:
                self.__srv_undo.add_command_to_stack("sUpdate", [1, id_stud, student.get_name(), name])
                self.__srv_student.update_student_name(id_stud, name)


    def __ui_update_student_group(self):
        try:
            id_stud = int(input("Id student:"))
        except ValueError:
            print("Invalid numerical id")
            return
        try:
            group = int(input("Group:"))
        except ValueError:
            print("Invalid group")
            return
        all_students = self.__srv_student.get_all_students()
        for student in all_students:
            if student.get_id_stud() == id_stud:
                self.__srv_undo.add_command_to_stack("sUpdate", [2, id_stud, student.get_group(), group])
                self.__srv_student.update_student_group(id_stud, group)

    #   Assignments
    def __ui_add_assignment(self):
        try:
            id_ass = int(input("Id assignment:"))
        except ValueError:
            print("Invalid numerical id")
            return
        description = input("Description:")
        try:
            print("Enter a deadline for the assignment: ")
            year = int(input('Enter a year:'))
            month = int(input('Enter a month:'))
            day = int(input('Enter a day:'))
            deadline = datetime.date(year, month, day)
        except ValueError:
            print("Invalid deadline!")
            return
        self.__srv_assignment.add_assignment(id_ass, description, deadline)
        self.__srv_undo.add_command_to_stack("aAdd", Assignment(id_ass, description, deadline))
        print("Assignment succesfully added")

    def __ui_print_assignments(self):
        number_of_assignments = self.__srv_assignment.number_of_assignments()
        if number_of_assignments == 0:
            print("No assignments present in list!")
            return
        all_assignments = self.__srv_assignment.get_all_assignments()
        for assignment in all_assignments:
            print(assignment)

    def __ui_remove_assignment(self):
        try:
            id_ass = int(input("Id assignment:"))
        except ValueError:
            print("Invalid numerical id")
            return
        all_assignments = self.__srv_assignment.get_all_assignments()
        all_grades = self.__srv_grade.get_all_grades()
        ok = True
        for grade in all_grades:
            if grade.get_id_stud_grade() == id_ass:
                ok = False
        op_list = []
        if not ok:
            for assignment in all_assignments:
                if assignment.get_id_ass() == id_ass:
                    op_list = self.__srv_grade.remove_all_grades(id_ass)
                    op_list.append(["aRemove", Assignment(id_ass, assignment.get_description(), assignment.get_deadline())])
                    self.__srv_assignment.remove_assignment(id_ass)
                    self.__srv_undo.add_command_to_stack("cascade", op_list)
        else:
            for assignment in all_assignments:
                if assignment.get_id_ass() == id_ass:
                    self.__srv_assignment.remove_assignment(id_ass)
                    op_list.append(["aRemove", Assignment(id_ass, assignment.get_description(), assignment.get_deadline())])
                    self.__srv_undo.add_command_to_stack("cascade", op_list)

    def __ui_update_assignment_description(self):
        try:
            id_ass = int(input("Id assignment:"))
        except ValueError:
            print("Invalid numerical id")
            return
        description = input("Description:")
        all_assignments = self.__srv_assignment.get_all_assignments()
        for assignment in all_assignments:
            if assignment.get_id_ass() == id_ass:
                self.__srv_undo.add_command_to_stack("aUpdate", [1, id_ass, assignment.get_description(), description])
                self.__srv_assignment.update_assignment_description(id_ass, description)

    def __ui_update_assignment_deadline(self):
        try:
            id_ass = int(input("Id assignment:"))
        except ValueError:
            print("Invalid numerical id")
            return
        try:
            print("Enter a deadline for the assignment:")
            year = int(input('Enter a year:'))
            month = int(input('Enter a month:'))
            day = int(input('Enter a day:'))
            deadline = datetime.date(year, month, day)
        except ValueError:
            print("Invalid deadline! It has to be after the actual date!")
            return
        all_assignments = self.__srv_assignment.get_all_assignments()
        for assignment in all_assignments:
            if assignment.get_id_ass() == id_ass:
                self.__srv_undo.add_command_to_stack("aUpdate", [2, id_ass, assignment.get_deadline(), deadline])
                self.__srv_assignment.update_assignment_deadline(id_ass, deadline)

#----------------------------------------------------------------------------------------------------------------------

    def __ui_add_assignment_to_student(self):
        try:
            id_ass = int(input("Id assignment:"))
        except ValueError:
            print("Invalid numerical id!")
            return
        try:
            id_stud = int(input("Id student:"))
        except ValueError:
            print("Invalid numerical id!")
            return
        self.__srv_grade.add_assignment_to_student(id_ass, id_stud)
        self.__srv_undo.add_command_to_stack("addAssignmentToStudent", [id_ass, id_stud])

    def __ui_add_assignment_to_group(self):
        try:
            id_ass = int(input("Id assignment:"))
        except ValueError:
            print("Invalid numerical id")
            return
        try:
            group = int(input("Group:"))
        except ValueError:
            print("Invalid numerical id")
            return
        op_list = []
        all_students = self.__srv_student.get_all_students()
        self.__srv_grade.add_assignment_to_group(id_ass, group)
        for student in all_students:
            if student.get_group() == group:
                op_list.append(["addAssignmentToStudent", [id_ass, student.get_id_stud()]])
        self.__srv_undo.add_command_to_stack("addAssignmentToGroup", op_list)




    def __ui_print_list_of_assignments_assigned_to_students(self):
        number_of_grades = self.__srv_grade.number_of_grades()
        if number_of_grades == 0:
            print("No assignments assigned!")
            return
        all_grades = self.__srv_grade.get_all_grades()
        for grade in all_grades:
            print("For student " + str(grade.get_id_stud_grade()) + " was assigned the assignment number " + str(grade.get_id_ass_grade()))

    def __ui_print_list_of_assignments_to_be_graded(self):
        all_grades = self.__srv_grade.get_all_grades()
        all_students = self.__srv_student.get_all_students()
        for student in all_students:
            ok = False
            for grade in all_grades:
                if student.get_id_stud() == grade.get_id_stud_grade() and grade.get_value_grade() == 0:
                    if not ok:
                        print("For the student " + str(student.get_id_stud()) + " we have the next assignments ungraded:")
                        ok = True
                    print("Assignment " + str(grade.get_id_ass_grade()))

    def __ui_add_grade_to_assignment(self):
        self.__ui_print_list_of_assignments_to_be_graded()
        if self.__srv_grade.number_of_grades() == 0:
            print("There are no assignments to grade!")
            return
        try:
            id_ass = int(input("Id assignment:"))
        except ValueError:
            print("Invalid numerical id!")
            return
        try:
            id_stud = int(input("Id student:"))
        except ValueError:
            print("Invalid numerical id!")
            return
        try:
            value_grade = int(input("Value grade:"))
        except ValueError:
            print("Invalid value grade!")
            return
        self.__srv_grade.add_grade_to_assignment(id_ass, id_stud, value_grade)
        self.__srv_undo.add_command_to_stack("addGradeToAssignment", [id_ass, id_stud, value_grade])

    def __ui_print_list_of_grades(self):
        number_of_grades = self.__srv_grade.number_of_grades()
        if number_of_grades == 0:
            print("No grades in list!")
            return
        all_grades = self.__srv_grade.get_all_grades()
        for grade in all_grades:
            if grade.get_value_grade() != 0:
                print("The student " + str(grade.get_id_stud_grade()) + " was graded at the assignment " + str(grade.get_id_ass_grade())
                      + " with the grade " + str(grade.get_value_grade()))

    def __ui_print_assignment_descending_by_grade(self):
        try:
            id_ass = int(input("Id assignment"))
        except ValueError:
            print("Invalid numerical id!")
            return
        list_of_students = self.__srv_grade.first_statistic(id_ass)
        if len(list_of_students) == 0:
            print("There is no student graded at this assignment!")
            return
        print(f"For the assignment {id_ass} we had the next grades in descending order:")
        for student in list_of_students:
            print(student)

    def __ui_print_students_with_deadline_passed(self):
        list_of_students_with_deadline_passed = self.__srv_grade.second_statistic()
        if len(list_of_students_with_deadline_passed) == 0:
            print("All students finished their assignments in time!")
            return
        print("The next students are late with at least one assignment:")
        for student in list_of_students_with_deadline_passed:
            print(student)

    def __ui_print_students_best_school_situation(self):
        list_of_students_by_average_score = self.__srv_grade.third_statistic()
        print("Here we have the classament of the students:")
        for student in list_of_students_by_average_score:
            print(student)

    def run(self):
        self.__ui_print_menu()
        self.__srv_student.populate_student()
        self.__srv_assignment.populate_assignment()
        while True:
            cmd1 = input(">>>")
            if cmd1 == "exit":
                return
            elif cmd1 == "S":
                self.__ui_print_menu_student()
                cmd2 = input(">>>")
                try:
                    if cmd2 == "add":
                        self.__ui_add_student()
                    elif cmd2 == "remove":
                        self.__ui_remove_student()
                    elif cmd2 == "update_name":
                        self.__ui_update_student_name()
                    elif cmd2 == "update_group":
                        self.__ui_update_student_group()
                    elif cmd2 == "print":
                        self.__ui_print_students()
                except ValidationError as ve:
                    print("Validation error: " + str(ve))
                except RepositoryError as re:
                    print("Repository error: " + str(re))
            elif cmd1 == "A":
                self.__ui_print_menu_assignment()
                cmd2 = input(">>>")
                try:
                    if cmd2 == "add":
                        self.__ui_add_assignment()
                    elif cmd2 == "remove":
                        self.__ui_remove_assignment()
                    elif cmd2 == "update_description":
                        self.__ui_update_assignment_description()
                    elif cmd2 == "update_deadline":
                        self.__ui_update_assignment_deadline()
                    elif cmd2 == "print":
                        self.__ui_print_assignments()
                except ValidationError as ve:
                    print("Validation error: " + str(ve))
                except RepositoryError as re:
                    print("Repository error: " + str(re))
            elif cmd1 == "AS":
                try:
                    self.__ui_add_assignment_to_student()
                except ValidationError as ve:
                    print("Validation error: " + str(ve))
                except RepositoryError as re:
                    print("Repository error: " + str(re))
            elif cmd1 == "AG":
                try:
                    self.__ui_add_assignment_to_group()
                except ValidationError as ve:
                    print("Validation error: " + str(ve))
                except RepositoryError as re:
                    print("Repository error: " + str(re))
            elif cmd1 == "PA":
                try:
                    self.__ui_print_list_of_assignments_assigned_to_students()
                except ValidationError as ve:
                    print("Validation error: " + str(ve))
                except RepositoryError as re:
                    print("Repository error: " + str(re))
            elif cmd1 == "G":
                try:
                    self.__ui_add_grade_to_assignment()
                except ValidationError as ve:
                    print("Validation error: " + str(ve))
                except RepositoryError as re:
                    print("Repository error: " + str(re))

            elif cmd1 == "PG":
                try:
                    self.__ui_print_list_of_grades()
                except ValidationError as ve:
                    print("Validation error: " + str(ve))
                except RepositoryError as re:
                    print("Repository error: " + str(re))
            elif cmd1 == "STATS":
                self.__ui_print_menu_stats()
                cmd2 = input(">>>")
                try:
                    if cmd2 == "1":
                        self.__ui_print_assignment_descending_by_grade()
                    elif cmd2 == "2":
                        self.__ui_print_students_with_deadline_passed()
                    elif cmd2 == "3":
                        self.__ui_print_students_best_school_situation()
                except ValidationError as ve:
                    print("Validation error: " + str(ve))
                except RepositoryError as re:
                    print("Repository error: " + str(re))
            elif cmd1 == "UNDO":
                try:
                    self.__srv_undo.call_undo()
                    print("Undo operation went succesfully!")
                except UndoError as ue:
                    print("UndoError: " + str(ue))
            elif cmd1 == "REDO":
                try:
                    self.__srv_undo.call_redo()
                    print("Redo operation went succesfully!")
                except UndoError as ue:
                    print("UndoError: " + str(ue))
            elif cmd1 == "":
                continue
            else:
                print("Invalid command")
