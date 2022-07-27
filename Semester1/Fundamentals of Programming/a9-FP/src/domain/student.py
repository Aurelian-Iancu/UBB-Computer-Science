class Student:

    def __init__(self, id_stud, name, group):
        """
        Here we have the init for class Student. We also have a list __assignment for when we want to assign an assignment to a student
        :param id_stud: Student's id
        :param name: Student's name
        :param group: Student's group
        """
        self.__id_stud = id_stud
        self.__name = name
        self.__group = group

    def get_id_stud(self):
        """
        Getter for Student id
        :return: The Student id
        """
        return self.__id_stud

    def get_name(self):
        """
        Getter for Student name
        :return: The Student name
        """
        return self.__name

    def get_group(self):
        """
        Getter for Student group
        :return: The Student group
        """
        return self.__group

    def set_name(self, value):
        """
        Setter for Student's name
        :param value: The value you want to set the name with
        :return: Nothing
        """
        self.__name = value

    def set_group(self, value):
        """
        Setter for Student's group
        :param value: The value you want to set the group with
        :return: Nothing
        """
        self.__group = value

    def __eq__(self, other):
        """
        In this function we check if 2 ids are equal
        :param other: Other Student
        :return: True if the ids are equal, False if they are not equal
        """
        return self.__id_stud == other.__id_stud

    def __str__(self):
        """
        In this function we initialize the format in which we want to print the students
        :return: The format in which you want to print the students
        """
        return str(self.__id_stud) + ". " + self.__name + " from group " + str(self.__group)


class StudentGradeSort:
    """
    This class is created in order to print the students for the first statistic in the way we want
    """
    def __init__(self, id_stud, name, group, value_grade):
        """
        Constructor for the class StudentGradeSort
        :param id_stud: The id of a student
        :param name: The name of the student
        :param group: The group of a student
        :param value_grade: The value of the grade he got at a given assignment
        """
        self.__id_stud = id_stud
        self.__name = name
        self.__group = group
        self.__value_grade = value_grade

    def get_value_grade(self):
        """
        Getter for the value_grade
        :return: The value_grade
        """
        return self.__value_grade

    def __str__(self):
        """
        In this function we initialize the format in which we want to print the students
        :return: The format in which we want to print the students
        """
        return f"Student {str(self.__id_stud)}. {self.__name} from group {str(self.__group)} with the grade {str(self.__value_grade)}"


class StudentAverage:
    def __init__(self, name, average):
        """
        This class is created in order to print the students for the third statistic in the way we want
        :param name: The name of the student
        :param average: The average score of the student
        """
        self.__name = name
        self.__average = average

    def get_average(self):
        """
        Getter for the average score
        :return: The average score
        """
        return self.__average

    def __str__(self):
        """
        In this function we initialize the format in which we want to print the students
        :return: The format in which we want to print the students
        """
        return f"Student {self.__name} with average {str(self.__average)}"