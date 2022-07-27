from src.repository.repositoryStudent import RepoStudent
from src.repository.dataAccesEntity import StudentDataAccess
from src.domain.student import Student

class BinaryFileStudentRepository(RepoStudent):
    """
    Class for student repository saved in binary file
    """

    def __init__(self, file_path):
        super().__init__()
        self.__file_path = file_path
        self.__load_content()

    def __load_content(self):
        data = StudentDataAccess.read_from_binary_file(self.__file_path)
        for key in data:
            super().add_student(Student(key.get_id_stud(), key.get_name(), key.get_group()))

    def add_student(self, student):
        super().add_student(student)
        StudentDataAccess.write_in_binary_file(self.__file_path, self.get_all_students_repo())

    def delete_by_id(self, id_stud):
        deleted_student = super().remove_student_by_id(id_stud)
        StudentDataAccess.write_in_binary_file(self.__file_path, self.get_all_students_repo())
        return deleted_student

    def update_by_id_student_name(self, id_stud, value):
        updated_student = super().update_by_id_student_name(id_stud, value)
        StudentDataAccess.write_in_binary_file(self.__file_path, self.get_all_students_repo())
        return updated_student

    def update_by_id_student_group(self, id_stud, value):
        updated_student = super().update_by_id_student_group(id_stud, value)
        StudentDataAccess.write_in_binary_file(self.__file_path, self.get_all_students_repo())
        return updated_student