from src.repository.repositoryGrade import RepoGrade
from src.repository.dataAccesEntity import GradeDataAccess


class TextFileRepoGrade(RepoGrade):
    """
    Class for a grade repository specific to a text file
    """

    def __init__(self, file_path):
        super().__init__()
        self.__file_path = file_path
        self.__load_content()

    def __load_content(self):
        with open(self.__file_path) as file_pointer:
            for line in file_pointer:
                grade = GradeDataAccess.read_from_text_file(line)
                super().add_grade(grade)

    def __upload_content(self):
        with open(self.__file_path, "w") as file_pointer:
            GradeDataAccess.write_in_text_file(self.get_all_grades_repo(), file_pointer)

    def add_grade(self, grade):
        super().add_grade(grade)
        self.__upload_content()

    def update_grade(self, id_ass_grade, id_stud_grade, value):
        updated_grade = super().update_grade(id_ass_grade, id_stud_grade, value)
        self.__upload_content()
        return updated_grade

    def remove_assignment(self, id_stud):
        removed_assignment = super().remove_assignment(id_stud)
        self.__upload_content()
        return removed_assignment

    def remove_grade(self, id_ass):
        removed_grade = super().remove_grade(id_ass)
        self.__upload_content()
        return removed_grade

    def remove_grade_by_ids(self, id_stud, id_ass):
        removed_grade = super().remove_grade_by_ids(id_stud, id_ass)
        self.__upload_content()
        return removed_grade

    def set_value_grade_to_zero(self, id_stud, id_ass):
        set_grade = super().set_value_grade_to_zero(id_stud, id_ass)
        self.__upload_content()
        return set_grade