from src.domain.student import Student


class ServiceStudent:
    def __init__(self, valid_student, repo_student):
        """
        Here we have the init for the class ServiceStudent in which we initialize the repository and the validator
        :param valid_student: The validator for students
        :param repo_student: The repository for students
        """
        self.__valid_student = valid_student
        self.__repo_student = repo_student

    def number_of_students(self):
        """
        Here we have the length of the repository
        :return: The length of the repository
        """
        return len(self.__repo_student)

    def add_student(self, id_stud, name, group):
        """
        Here we validate the student and we call the repo add instruction
        :param id_stud: An id of a Student
        :param name: A name of a Student
        :param group: A group of a Student
        :return: Nothing
        """
        student = Student(id_stud, name, group)
        self.__valid_student.validate(student)
        self.__repo_student.add_student(student)

    def remove_student(self, id_stud):
        """
        Here we validate if the id of a student is valid and we call the repo remove instruction
        :param id_stud: An id of a Student
        :return: Nothing
        """
        self.__valid_student.validate_id_stud(id_stud)
        self.__repo_student.remove_student_by_id(id_stud)

    def update_student_name(self, id_stud, name):
        """
        Here we validate if the id and the name of a Student are valid and we call the repo update_name instruction
        :param id_stud: An id of a Student
        :param name: A name of a Student
        :return: Nothing
        """
        self.__valid_student.validate_id_stud(id_stud)
        self.__valid_student.validate_name(name)
        self.__repo_student.update_by_id_student_name(id_stud, name, )

    def update_student_group(self, id_stud, group):
        """
        Here we validate if the id and the group of a Student are valid and we call the repo update_group instruction
        :param id_stud: An id of a Student
        :param group: A group of a Student
        :return: Nothing
        """
        self.__valid_student.validate_id_stud(id_stud)
        self.__valid_student.validate_group(group)
        self.__repo_student.update_by_id_student_group(id_stud, group)

    def get_all_students(self):
        """
        Here we call the repo instruction that returns the list of students
        :return: The list of students
        """
        return self.__repo_student.get_all_students_repo()

    def populate_student(self):
        """
        Here we call the repo instruction that populates the list of students
        :return: The populated list
        """
        return self.__repo_student.populate_student()
