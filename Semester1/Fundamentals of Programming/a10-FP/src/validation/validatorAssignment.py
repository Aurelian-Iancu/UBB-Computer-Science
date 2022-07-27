from src.errors.exceptions import ValidationError
import datetime


class ValidatorAssignment:
    @staticmethod
    def validate(assignment):
        """
        Here we validate an assignment
        :param assignment: An assignment
        :return: Nothing. Validation error if the assignment isn't valid
        """
        errors = ""
        if assignment.get_id_ass() < 0 or float(assignment.get_id_ass()) != int(assignment.get_id_ass()):
            errors += "Invalid id!\n"
        if assignment.get_description() == "":
            errors += "Invalid description!\n"
        if len(errors) > 0:
            raise ValidationError(errors)

    @staticmethod
    def validate_id_ass(id_ass):
        """
        Here we validate an id of an assignment
        :param id_ass: An id of an Assignment
        :return: Nothing. Validation error if the assignment isn't valid
        """
        errors = ""
        if id_ass < 0 or float(id_ass) != int(id_ass):
            errors += "invalid id!\n"
        if len(errors) > 0:
            raise ValidationError(errors)

    @staticmethod
    def validate_description(description):
        """
        Here we validate a description of an assignment
        :param description: A description of an Assignment
        :return: Nothing. Validation error if the assignment isn't valid
        """
        errors = ""
        if description == "":
            errors += "invalid description!\n"
        if len(errors) > 0:
            raise ValidationError(errors)
