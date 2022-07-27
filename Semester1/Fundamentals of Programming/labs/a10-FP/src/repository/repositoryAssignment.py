from src.errors.exceptions import RepositoryError
from src.domain.assignment import Assignment
from src.Iterable.Iterable import Iterable
import datetime
import random


class RepoAssignment:
    def __init__(self, assignments=None):
        """
        Here we have the init for the class RepoAssignment in which we initialize the list of assignments
        """
        if assignments == None:
            assignments = []
        if assignments is Iterable:
            self.__assignments = assignments
        else:
            self.__assignments = Iterable(assignments)

    def __len__(self):
        """
        Here we have function to determinate the length of the list of assignments
        :return: The length of the list of assignments
        """
        return len(self.__assignments)

    def add_assignment(self, assignment):
        """
        Here we add an Assignment to the list of assignments if the id isn't already in list
        :param assignment: An object from class Assignment
        :return: Nothing. It adds an Assignment to the list of assignments
        """
        for _assignment in self.__assignments:
            if _assignment.get_id_ass() == assignment.get_id_ass():
                raise RepositoryError("existing id!")
        self.__assignments.append(assignment)

    def remove_assignment_by_id(self, id_ass):
        """
        Here we remove an Assignment from the list of assignments if we can find it in the list
        :param id_ass: An id of an assignment
        :return: Nothing. It removes an Assignment from the list of assignments
        """
        ok = True
        for _assignment in self.__assignments:
            if _assignment.get_id_ass() == id_ass:
                self.__assignments.remove(_assignment)
                ok = False
        if ok:
            raise RepositoryError("inexisting id")

    def search_by_id_assignment(self, id_ass):
        """
        Here we search an Assignment in the list of assignments by his id
        :param id_ass: An id of an assignment
        :return: The assignment we were searching for if we find it, RepositoryError otherwise
        """
        ok = True
        for _assignment in self.__assignments:
            if _assignment.get_id_ass() == id_ass:
                return _assignment
        if ok:
            raise RepositoryError("inexisting id!")

    def update_by_id_assignment_description(self, id_ass, value):
        """
        Here we update an Assignment's description by its id
        :param id_ass: An id of an assignment
        :param value: The description we want to update with
        :return: Nothing. It sets the old description with the new description if the id exists
        """
        ok = False
        assignment_position = -1
        for position in range(self.__len__()):
            if self.__assignments[position].get_id_ass() == id_ass:
                assignment_position = position
                ok = True
        if not ok:
            raise RepositoryError("inexisting id!")
        else:
            self.__assignments[assignment_position].set_description(value)

    def update_by_id_assignment_deadline(self, id_ass, value):
        """
        Here we update an Assignment's deadline by its id
        :param id_ass: An id of an assignment
        :param value: The deadline we want to update with
        :return: Nothing. It sets the old deadline with the new deadline if the id exists
        """
        ok = False
        assignment_position = -1
        for position in range(self.__len__()):
            if self.__assignments[position].get_id_ass() == id_ass:
                assignment_position = position
                ok = True
        if not ok:
            raise RepositoryError("inexisting id!")
        else:
            self.__assignments[assignment_position].set_deadline(value)

    def get_all_assignments_repo(self):
        """
        Here we have a getter for the list of assignments
        :return: The list of assignments
        """
        return self.__assignments[:]

    def populate_assignment(self):
        """
        In this function we populate the list of assignments with 20 random Assignments
        :return: Nothing. We create a list with 20 entities
        """
        list_description = ["Assignment678: Problem statement 1.", "Assignment678: Problem statement 2.",
                            "Assignment678: Problem statement 3.", "Assignment678: Problem statement 4.",
                            "Assignment678: Problem statement 5.", "Assignment678: Problem statement 6.",
                            "Assignment678: Problem statement 7.", "Assignment678: Problem statement 8.",
                            "Assignment678: Problem statement 9.", "Assignment678: Problem statement 10."
        ]
        list_deadline = [datetime.date(2021, 11, 18), datetime.date(2021, 11, 19), datetime.date(2021, 11, 20),
                         datetime.date(2021, 11, 21), datetime.date(2021, 11, 22), datetime.date(2021, 11, 23),
                         datetime.date(2022, 12, 24), datetime.date(2022, 12, 25), datetime.date(2022, 12, 26),
                         datetime.date(2022, 12, 27), datetime.date(2022, 12, 28), datetime.date(2022, 12, 29),
                         datetime.date(2022, 12, 30)
        ]
        for i in range(20):
            self.__assignments.append(Assignment(i, random.choice(list_description), random.choice(list_deadline)))
