from src.errors.exceptions import UndoError


class ServiceUndo:
    """
    Class for the undo/redo functionality
    """
    def __init__(self, srv_student, srv_assignment, srv_grade):
        self.__srv_student = srv_student
        self.__srv_assignment = srv_assignment
        self.__srv_grade = srv_grade

        self.__commandStackTop = -1
        self.__commandStack = []


        self.__undoDict = {
            "sAdd": self.undo_add_student,
            "sRemove": self.undo_remove_student,
            "sUpdate": self.undo_update_student,
            "aAdd": self.undo_add_assignment,
            "aRemove": self.undo_remove_assignment,
            "aUpdate": self.undo_update_assignment,
            "delete": self.undo_remove_grade,
            "cascade": self.undo_cascade_remove,
            "addAssignmentToStudent": self.undo_assign_assignment_to_student,
            "addAssignmentToGroup": self.undo_cascade_assign_student_group,
            "addGradeToAssignment": self.undo_add_grade_to_assignment
        }

        self.__redoDict = {
            "sAdd": self.redo_add_student,
            "sRemove": self.redo_remove_student,
            "sUpdate": self.redo_update_student,
            "aAdd": self.redo_add_assignment,
            "aRemove": self.redo_remove_assignment,
            "aUpdate": self.redo_update_assignment,
            "delete": self.redo_remove_grade,
            "cascade": self.redo_cascade_remove,
            "addAssignmentToStudent": self.redo_assign_assignment_to_student,
            "addAssignmentToGroup": self.redo_cascade_assign_student_group,
            "addGradeToAssignment": self.redo_add_grade_to_assignment
        }

    """
    Undo functionalities
    """
    def get_stack(self):
        return self.__commandStack

    def add_command_to_stack(self, action, object):
        self.__commandStackTop += 1
        self.__commandStack.insert(self.__commandStackTop, [action, object])
        del self.__commandStack[self.__commandStackTop + 1:]

    def get_last_operation(self):
        operation = self.__commandStack[self.__commandStackTop]
        self.__commandStackTop -= 1
        return operation

    def get_last_operation_command(self, operation):
        return operation[0]

    def get_last_operation_oject(self, operation):
        return operation[1]

    def get_next_operation(self):
        operation = self.__commandStack[self.__commandStackTop + 1]
        self.__commandStackTop += 1
        return operation

    def call_undo(self):
        if self.__commandStackTop == -1:
            raise UndoError("There is nothing to undo.")
        last_operation = self.get_last_operation()
        action = self.get_last_operation_command(last_operation)
        object = self.get_last_operation_oject(last_operation)
        self.__undoDict[action](object)

    def undo_add_student(self, student):
        """
        Undoes the action of adding a student
        """
        self.__srv_student.remove_student(student.get_id_stud())

    def undo_remove_student(self, student):
        """
        Undoes the action of removing a student
        """
        self.__srv_student.add_student(student.get_id_stud(), student.get_name(), student.get_group())

    def undo_cascade_remove(self, operations):
        """
        Undoes the cascade removal of a student or an assignment
        """
        new_operations = operations[:]
        while len(new_operations) > 0:
            operation = new_operations.pop()
            action = self.get_last_operation_command(operation)
            object = self.get_last_operation_oject(operation)
            self.__undoDict[action](object)

    def undo_cascade_assign_student_group(self, operations):
        """
        Undoes the assigning of an assignment to a group of students
        """
        new_operations = operations[:]
        while len(new_operations) > 0:
            operation = new_operations.pop()
            action = self.get_last_operation_command(operation)
            object = self.get_last_operation_oject(operation)
            self.__undoDict[action](object)

    def undo_update_student(self, student):
        """
        Undoes the action of updating a student
        """
        if student[0] == 1:
            self.__srv_student.update_student_name(student[1], student[2])
        if student[0] == 2:
            self.__srv_student.update_student_group(student[1], student[2])

    def undo_add_assignment(self, assignment):
        """
        Undoes the action of adding an assignment
        """
        self.__srv_assignment.remove_assignment(assignment.get_id_ass())

    def undo_remove_assignment(self, assignment):
        """
        Undoes the action of removing an assignment
        """
        self.__srv_assignment.add_assignment(assignment.get_id_ass(), assignment.get_description(), assignment.get_deadline())

    def undo_update_assignment(self, assignment):
        """
        Undoes the action of updating an assignment
        """
        if assignment[0] == 1:
            self.__srv_assignment.update_assignment_description(assignment[1], assignment[2])
        if assignment[0] == 2:
            self.__srv_assignment.update_assignment_deadline(assignment[1], assignment[2])

    def undo_assign_assignment_to_student(self, params):
        """
        Undoes the action of assigning an assignment to a student
        """
        self.__srv_grade.remove_grade(params[1], params[0])

    def undo_add_grade_to_assignment(self, params):
        """
        Undoes the action of grading an assignment
        """
        self.__srv_grade.remove_grade_graded(params[1], params[0])

    def undo_remove_grade(self, grade):
        """
        grade[0] --> id_ass
        grade[1] --> id_stud
        grade[2] --> value_grade
        """
        self.__srv_grade.add_assignment_to_student(grade[0], grade[1])
        self.__srv_grade.add_grade_to_assignment(grade[0], grade[1], grade[2])
    """
    Redo functionalities
    """
    def call_redo(self):
        if self.__commandStackTop == len(self.__commandStack) - 1:
            raise UndoError("There is nothing to redo!")
        next_operation = self.get_next_operation()
        action = self.get_last_operation_command(next_operation)
        object = self.get_last_operation_oject(next_operation)
        self.__redoDict[action](object)

    def redo_add_student(self, student):
        self.undo_remove_student(student)

    def redo_remove_student(self, student):
        self.undo_add_student(student)

    def redo_cascade_remove(self, operations):
        for item in operations:
            action = self.get_last_operation_command(item)
            object = self.get_last_operation_oject(item)
            self.__redoDict[action](object)

    def redo_cascade_assign_student_group(self, operations):
        for item in operations:
            action = self.get_last_operation_command(item)
            object = self.get_last_operation_oject(item)
            self.__redoDict[action](object)

    def redo_update_student(self, student):
        if student[0] == 1:
            self.__srv_student.update_student_name(student[1], student[3])
        if student[0] == 2:
            self.__srv_student.update_student_group(student[1], student[3])

    def redo_add_assignment(self, assignment):
        self.undo_remove_assignment(assignment)

    def redo_remove_assignment(self, assignment):
        self.undo_add_assignment(assignment)

    def redo_update_assignment(self, assignment):
        if assignment[0] == 1:
            self.__srv_assignment.update_assignment_description(assignment[1], assignment[3])
        if assignment[0] == 2:
            self.__srv_assignment.update_assignment_deadline(assignment[1], assignment[3])

    def redo_assign_assignment_to_student(self, params):
        self.__srv_grade.add_assignment_to_student(params[0], params[1])

    def redo_add_grade_to_assignment(self, params):
        self.__srv_grade.add_grade_to_assignment(params[0], params[1], params[2])

    def redo_remove_grade(self, grade):
        self.__srv_grade.remove_grade(grade[1], grade[0])






