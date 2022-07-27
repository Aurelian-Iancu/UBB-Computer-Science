class Student:
    def __init__(self, id_stud, name, group):
        self.__id_stud = id_stud
        self.__name = name
        self.__group = group

    def get_id_stud(self):
        return self.__id_stud

    def get_name(self):
        return self.__name

    def get_group(self):
        return self.__group

    def set_name(self, value):
        self.__name = value

    def set_group(self, value):
        self.__group = value

    def __eq__(self, other):
        return self.__id_stud == other.__id_stud

    def __str__(self):
        return f"{str(self.__id_stud)}, {self.__name}, {str(self.__group)}"


class Assignment:
    def __init__(self, id_ass, description, deadline):
        self.__id_ass = id_ass
        self.__description = description
        self.__deadline = deadline

    def get_id_ass(self):
        return self.__id_ass

    def get_description(self):
        return self.__description

    def get_deadline(self):
        return self.__deadline

    def set_description(self, value):
        self.__description = value

    def set_deadline(self, value):
        self.__deadline = value

    def __eq__(self, other):
        return self.__id_ass == other.__id_ass

    def __str__(self):
        return f"{str(self.__id_ass)}, {self.__description}, {str(self.__deadline)}"


class Grade:
    def __init__(self, id_grade, id_ass, id_stud, value_grade):
        self.__id_grade = id_grade
        self.__id_ass = id_ass
        self.__id_stud = id_stud
        self.__value_grade = value_grade

    def get_id_grade(self):
        return self.__id_grade

    def get_id_ass(self):
        return self.__id_ass

    def get_id_stud(self):
        return self.__id_stud

    def get_value_grade(self):
        return self.__value_grade

    def set_value_grade(self, value):
        self.__value_grade = value

    def __eq__(self, other):
        return self.__id_grade == other.__id_grade

    def __str__(self):
        return f"{str(self.__id_grade)}, {str(self.__id_ass)}, {str(self.__id_stud)}, {str(self.__value_grade)}"


class StudentAverageDTO:
    def __init__(self, name, average):
        self.__name = name
        self.__average = average

    def get_average(self):
        return self.__average

    def __str__(self):
        return f"Student {self.__name} with average {str(self.__average)}"