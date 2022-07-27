from src.repository.repositoryStudent import RepoStudent
from src.repository.dataAccesEntity import StudentDataAccess


class TextFileRepoStudent(RepoStudent):
    """
    Class for a student repository specific to a text file
    """
    def __init__(self, file_path):
        super().__init__()
        self. __file_path = file_path
        self.__load_content()

    def __load_content(self):
        with open(self.__file_path) as file_pointer:
            for line in file_pointer:
                student = StudentDataAccess.read_from_text_file(line)
                super().add_student(student)

    def __upload_content(self):
        with open(self.__file_path, "w") as file_pointer:
            StudentDataAccess.write_in_text_file(self.get_all_students_repo(), file_pointer)

    def add_student(self, student):
        super().add_student(student)
        self.__upload_content()

    def remove_student_by_id(self, id_stud):
        deleted_student = super().remove_student_by_id(id_stud)
        self.__upload_content()
        return deleted_student

    def update_by_id_student_name(self, id_stud, value):
        updated_student = super(). update_by_id_student_group(id_stud, value)
        self.__upload_content()
        return updated_student

    def update_by_id_student_group(self, id_stud, value):
        updated_student = super(). update_by_id_student_group(id_stud, value)
        self.__upload_content()
        return updated_student

