from src.repository.repositoryGrade import RepoGrade
from src.repository.dataAccesEntity import GradeDataAccess
from src.domain.grade import Grade


class BinaryFileRepoGrade(RepoGrade):
    """
    Class for a grade repository specific to a binary file
    """
    def __init__(self, file_path):
        super().__init__()
        self.__file_path = file_path
        self.__load_content()

    def __load_content(self):
        data = GradeDataAccess.read_from_binary_file(self.__file_path)
        for key in data:
            super().add_grade(Grade(key.get_id_ass_grade(), key.get_id_stud_grade(), key.get_value_grade()))

    def add_grade(self, grade):
        super().add_grade(grade)
        GradeDataAccess.write_in_binary_file(self.__file_path, self.get_all_grades_repo())

    def update_grade(self, id_ass_grade, id_stud_grade, value):
        updated_grade = super().update_grade(id_ass_grade, id_stud_grade, value)
        GradeDataAccess.write_in_binary_file(self.__file_path, self.get_all_grades_repo())
        return updated_grade

    def remove_assignment(self, id_stud):
        removed_assignment = super().remove_assignment(id_stud)
        GradeDataAccess.write_in_binary_file(self.__file_path, self.get_all_grades_repo())
        return removed_assignment

    def remove_grade(self, id_ass):
        removed_grade = super().remove_grade(id_ass)
        GradeDataAccess.write_in_binary_file(self.__file_path, self.get_all_grades_repo())
        return removed_grade

    def remove_grade_by_ids(self, id_stud, id_ass):
        removed_grade = super().remove_grade_by_ids(id_stud, id_ass)
        GradeDataAccess.write_in_binary_file(self.__file_path, self.get_all_grades_repo())
        return removed_grade

    def set_value_grade_to_zero(self, id_stud, id_ass):
        set_grade = super().set_value_grade_to_zero(id_stud, id_ass)
        GradeDataAccess.write_in_binary_file(self.__file_path, self.get_all_grades_repo())
        return set_grade