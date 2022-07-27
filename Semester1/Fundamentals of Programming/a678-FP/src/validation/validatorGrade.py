from src.errors.exceptions import ValidationError


class ValidatorGrade:
    @staticmethod
    def validate(grade):
        errors = ""
        if grade.get_id_ass_grade() < 0 or float(grade.get_id_ass_grade()) != int(grade.get_id_ass_grade()):
            errors += "invalid id assignment!\n"
        if grade.get_id_stud_grade() < 0 or float(grade.get_id_stud_grade()) != int(grade.get_id_stud_grade()):
            errors += "invalid id student!\n"
        if grade.get_value_grade() < 0 or grade.get_value_grade() > 10 or float(grade.get_value_grade()) != int(grade.get_value_grade()):
            errors += "invalid value grade"
        if len(errors) > 0:
            raise ValidationError(errors)

    @staticmethod
    def validate_value_grade(value_grade):
        errors = ""
        if value_grade < 0 or value_grade > 10 or float(value_grade) != int(value_grade):
            errors += "invalid value grade"
        if len(errors) > 0:
            raise ValidationError(errors)