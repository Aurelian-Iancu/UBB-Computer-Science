from src.repository.repositoryAssignment import RepoAssignment
from src.repository.dataAccesEntity import AssignmentDataAccess
from src.domain.assignment import Assignment


class BinaryFileRepoAssignment(RepoAssignment):
    def __init__(self, file_path):
        super().__init__()
        self.__file_path = file_path
        self.__load_content()

    def __load_content(self):
        data = AssignmentDataAccess.read_from_binary_file(self.__file_path)
        for key in data:
            super().add_assignment(Assignment(key.get_id_ass(), key.get_description(), key.get_deadline()))

    def add_assignment(self, assignment):
        super().add_assignment(assignment)
        AssignmentDataAccess.write_in_binary_file(self.__file_path, self.get_all_assignments_repo())

    def remove_assignment_by_id(self, id_ass):
        deleted_assignment = super().remove_assignment_by_id(id_ass)
        AssignmentDataAccess.write_in_binary_file(self.__file_path, self.get_all_assignments_repo())
        return deleted_assignment

    def update_by_id_assignment_description(self, id_ass, value):
        updated_assignment = super().update_by_id_assignment_description(id_ass, value)
        AssignmentDataAccess.write_in_binary_file(self.__file_path, self.get_all_assignments_repo())
        return updated_assignment

    def update_by_id_assignment_deadline(self, id_ass, value):
        updated_assignment = super().update_by_id_assignment_deadline(id_ass, value)
        AssignmentDataAccess.write_in_binary_file(self.__file_path, self.get_all_assignments_repo())
        return updated_assignment