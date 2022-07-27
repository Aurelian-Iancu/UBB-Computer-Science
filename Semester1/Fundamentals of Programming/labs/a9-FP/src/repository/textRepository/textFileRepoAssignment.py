from src.repository.repositoryAssignment import RepoAssignment
from src.repository.dataAccesEntity import AssignmentDataAccess


class TextFileRepoAssignment(RepoAssignment):
    """
    Class for assignment repository specific to a text file.
    """
    def __init__(self, file_path):
        super().__init__()
        self.__file_path = file_path
        self.__load_content()

    def __load_content(self):
        with open(self.__file_path) as file_pointer:
            for line in file_pointer:
                assignment = AssignmentDataAccess.read_from_text_file(line)
                super().add_assignment(assignment)

    def __upload_content(self):
        with open(self.__file_path, "w") as file_pointer:
            AssignmentDataAccess.write_in_text_file(self.get_all_assignments_repo(), file_pointer)

    def add_assignment(self, assignment):
        super().add_assignment(assignment)
        self.__upload_content()

    def remove_assignment_by_id(self, id_ass):
        deleted_assignment = super().remove_assignment_by_id(id_ass)
        self.__upload_content()
        return deleted_assignment

    def update_by_id_assignment_description(self, id_ass, value):
        updated_assignment = super().update_by_id_assignment_description(id_ass, value)
        self.__upload_content()
        return updated_assignment

    def update_by_id_assignment_deadline(self, id_ass, value):
        updated_assignment = super().update_by_id_assignment_deadline(id_ass, value)
        self.__upload_content()
        return updated_assignment
