from src.errors.exceptions import ValidationError


class ValidatorStudent:
    @staticmethod
    def validate(student):
        """
        Here we validate a student
        :param student: A Student
        :return: Nothing. Validation error if the student isn't valid
        """
        errors = ""
        if student.get_id_stud() < 0 or float(student.get_id_stud()) != int(student.get_id_stud()):
            errors += "invalid id!\n"
        if student.get_name() == "":
            errors += "invalid name!\n"
        if student.get_group() < 911 or student.get_group() > 917 or float(student.get_group()) != int(student.get_group()):
            errors += "invalid group!\n"
        if len(errors) > 0:
            raise ValidationError(errors)

    @staticmethod
    def validate_id_stud(id_stud):
        """
        Here we validate an id of a student
        :param id_stud: An id of a student
        :return: Nothing. Validation error if the student isn't valid
        """
        errors = ""
        if id_stud < 0 or float(id_stud) != int(id_stud):
            errors += "invalid id!\n"
        if len(errors) > 0:
            raise ValidationError(errors)

    @staticmethod
    def validate_name(name):
        """
        Here we validate a name of a student
        :param name: A name of a student
        :return: Nothing. Validation error if the student isn't valid
        """
        errors = ""
        if name == "":
            errors += "invalid name!\n"
        if len(errors) > 0:
            raise ValidationError(errors)

    @staticmethod
    def validate_group(group):
        """
        Here we validate a group of a student
        :param group: A group of a student
        :return: Nothing. Validation error if the student isn't valid
        """
        errors = ""
        if group < 911 or group > 917 or float(group) != int(group):
            errors += "invalid group!\n"
        if len(errors) > 0:
            raise ValidationError(errors)
