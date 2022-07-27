from Erorrs.exceptions import RepositoryError


class AssignmentRepo:
    def __init__(self):
        self.__assignments = []

    def __len__(self):
        return len(self.__assignments)

    def get_all_assignments(self):
        return self.__assignments[:]

    def add_assignment(self, assignment):
        for _assignment in self.__assignments:
            if _assignment == assignment:
                raise RepositoryError("Existing assignment!")
        self.__assignments.append(assignment)

    def remove_assignment(self, id_ass):
        ok = 1
        for i in range(len(self.__assignments)):
            if self.__assignments[i].get_id_ass() == id_ass:
                del self.__assignments[i]
                ok = 0
                return
        if ok == 1:
            raise RepositoryError("Inexisting assignment!")

    def update_assignment(self, assignment):
        ok = 1
        for i in range(len(self.__assignments)):
            if self.__assignments[i] == assignment:
                self.__assignments[i] = assignment
                ok = 0
                return
        if ok == 1:
            raise RepositoryError("Inexisting assignment!")

    def search_by_id(self, id_ass):
        ok = 1
        for assignment in self.__assignments:
            if assignment.get_id_ass() == id_ass:
                ok = 0
                return assignment
        if ok == 1:
            raise RepositoryError("Inexisting assignment!")