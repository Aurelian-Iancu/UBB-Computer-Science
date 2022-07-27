from src.domain.assignment import Assignment


class ServiceAssignment:
    def __init__(self, valid_assignment, repo_assignment):
        """
        Here we have the init for the class ServiceAssignment in which we initialize the repository and the validator
        :param valid_assignment: The validator for assignments
        :param repo_assignment: The repository for assignments
        """
        self.__valid_assignment = valid_assignment
        self.__repo_assignment = repo_assignment

    def number_of_assignments(self):
        """
        Here we have the length of the repository
        :return: The length of the repository
        """
        return len(self.__repo_assignment)

    def add_assignment(self, id_ass, description, deadline):
        """
        Here we validate the assignment and we call the repo add instruction
        :param id_ass: An id of an Assignment
        :param description: A description of an Assignment
        :param deadline: A deadline of an Assignment
        :return: Nothing
        """
        assignment = Assignment(id_ass, description, deadline)
        self.__valid_assignment.validate(assignment)
        self.__repo_assignment.add_assignment(assignment)

    def remove_assignment(self, id_ass):
        """
        Here we validate the id of an assignment and we call the repo remove instruction
        :param id_ass: An id of an Assignment
        :return: Nothing
        """
        self.__valid_assignment.validate_id_ass(id_ass)
        self.__repo_assignment.remove_assignment_by_id(id_ass)

    def update_assignment_description(self, id_ass, description):
        """
        Here we validate the id of an assignment and the description and we call the repo update_description instruction
        :param id_ass: An id of an Assignment
        :param description: A description of an Assignment
        :return: Nothing
        """
        self.__valid_assignment.validate_id_ass(id_ass)
        self.__valid_assignment.validate_description(description)
        self.__repo_assignment.update_by_id_assignment_description(id_ass, description)

    def update_assignment_deadline(self, id_ass, deadline):
        """
        Here we validate the id of an assignment and the deadline and we call the repo update_deadline instruction
        :param id_ass: An id of an Assignment
        :param deadline: A deadline of an Assignment
        :return: Nothing
        """
        self.__valid_assignment.validate_id_ass(id_ass)
        self.__repo_assignment.update_by_id_assignment_deadline(id_ass, deadline)

    def get_all_assignments(self):
        """
        Here we call the repo instruction that returns the list of assignments
        :return: The list of assignments
        """
        return self.__repo_assignment.get_all_assignments_repo()

    def populate_assignment(self):
        """
        Here we call the repo instruction that populates the list of assignments
        :return: The populated list
        """
        return self.__repo_assignment.populate_assignment()