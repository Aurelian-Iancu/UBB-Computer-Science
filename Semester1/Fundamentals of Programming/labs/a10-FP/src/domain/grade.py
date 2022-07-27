class Grade:
    def __init__(self, id_ass, id_stud, value_grade):
        """
        Here we have the init for the class Grade
        :param id_ass: An Id of an Assignment
        :param id_stud: And Id of a Student
        :param grade: The value of the grade
        """
        self.__id_ass = id_ass
        self.__id_stud = id_stud
        self.__value_grade = value_grade

    def get_id_ass_grade(self):
        """
        Here we have a getter for the id_ass(id assignment)
        :return: The id_ass
        """
        return self.__id_ass

    def get_id_stud_grade(self):
        """
        Here we have a getter for the id_stud(id student)
        :return: The id_stud
        """
        return self.__id_stud

    def get_value_grade(self):
        """
        Here we have a getter for the grade
        :return: The value of the grade
        """
        return self.__value_grade

    def set_value_grade(self, value):
        """
        Here we have a setter for the grade
        :param value: The value you want to set the grade with
        :return: Nothing
        """
        self.__value_grade = value

    #def __eq__(self, other):
     #   """
      #  In this function we verify if 2 ids are equal
       # :param other: Other Student or other Assignment
        #:return: True if the ids are equal, false otherwise
        #"""
        #return self.__id_stud == other.__id_stud or self.__id_ass == other.__id_ass

    def __str__(self):
        """
        In this function we initialize the format in which we want to print the grades
        :return: The format in which you want to print the grades
        """
        return "The grade for student with the id: " + str(self.__id_stud) + " at the assignment with the id: " + str(self.__id_ass) + " is " + str(self.__value_grade)