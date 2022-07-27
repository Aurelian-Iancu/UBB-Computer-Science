class Assignment:
    def __init__(self, id_ass, description, deadline):
        """
        Here we have the init for class Assignment
        :param id_ass: Assignment's id
        :param description: Assignment's description
        :param deadline: Assignment's deadline
        """
        self.__id_ass = id_ass
        self.__description = description
        self.__deadline = deadline

    def get_id_ass(self):
        """
        Getter for Assignment id
        :return: The Assignment id
        """
        return self.__id_ass

    def get_description(self):
        """
        Getter for Assignment description
        :return: The Assignment description
        """
        return self.__description

    def get_deadline(self):
        """
        Getter for Assignment deadline
        :return: The Assignment deadline
        """
        return self.__deadline

    def set_description(self, value):
        """
        Setter for Assignment description
        :param value: The value you want to set the description with
        :return: Nothing
        """
        self.__description = value

    def set_deadline(self, value):
        """
        Setter for Assignment deadline
        :param value: The value you want to set the deadline with
        :return: Nothing
        """
        self.__deadline = value

   # def __eq__(self, other):
    #    """
     #   In this function we check if 2 ids are equal
      #  :param other: Other id assignment
       # :return: True if the ids are equal, False if they are not equal
       # """
      #  return self.__id_ass == other.__id_ass

    def __str__(self):
        """
        In this function we initialize the format in which we want to print the assignments
        :return: The format in which you want to print the assignments
        """
        return str(self.__id_ass) + ".You have the next assignment:\n" + self.__description + "\n" + "The due date is: " + str(self.__deadline)
