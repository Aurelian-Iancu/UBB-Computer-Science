from src.configuration.configurationSettings import Settings
from src.ui.user_interface import Console

from src.services.serviceStudent import ServiceStudent
from src.services.serviceAssignment import ServiceAssignment
from src.services.serviceGrade import ServiceGrade
from src.services.serviceUndo import ServiceUndo

from src.repository.repositoryStudent import RepoStudent
from src.repository.repositoryAssignment import RepoAssignment
from src.repository.repositoryGrade import RepoGrade

from src.validation.validatorStudent import ValidatorStudent
from src.validation.validatorAssignment import ValidatorAssignment
from src.validation.validatorGrade import ValidatorGrade

from src.repository.textRepository.textFileRepoStudent import TextFileRepoStudent
from src.repository.textRepository.textFileRepoAssignment import TextFileRepoAssignment
from src.repository.textRepository.textFileRepoGrade import TextFileRepoGrade

from src.repository.binaryRepository.binaryFileRepoStudent import BinaryFileRepoStudent
from src.repository.binaryRepository.binaryFileRepoAssignment import BinaryFileRepoAssignment
from src.repository.binaryRepository.binaryFileRepoGrade import BinaryFileRepoGrade

# repository = inmemory
# students = ""
# assignments = ""
# grades = ""


# repository = textfiles
# students = "../data/textFileStudent.txt"
# assignments = "../data/textFileAssignment.txt"
# grades = "../data/textFileGrade.txt"

# repository = binaryfiles
# students = "../data/binaryFileStudent.bin"
# assignments = "../data/binaryFileAssignment.bin"
# grades = "../data/binaryFileGrade.bin"


def repositories(settings):
    if settings.repository == "inmemory":
        return RepoStudent(), RepoAssignment(), RepoGrade()

    elif settings.repository == "textfiles":
        return TextFileRepoStudent(settings.students_path), TextFileRepoAssignment(settings.assignments_path), \
                TextFileRepoGrade(settings.grades_path)

    elif settings.repository == "binaryfiles":
        return BinaryFileRepoStudent(settings.students_path), BinaryFileRepoAssignment(settings.assignments_path), \
               BinaryFileRepoGrade(settings.grades_path)


if __name__ == "__main__":
    settings = Settings()
    valid_student = ValidatorStudent
    valid_assignment = ValidatorAssignment
    valid_grade = ValidatorGrade
    repo_student, repo_assignment, repo_grade = repositories(settings)

    srv_student = ServiceStudent(valid_student, repo_student)
    srv_assignment = ServiceAssignment(valid_assignment, repo_assignment)
    srv_grade = ServiceGrade(valid_student, valid_assignment, valid_grade, repo_student, repo_assignment, repo_grade)
    srv_undo = ServiceUndo(srv_student, srv_assignment, srv_grade)

    ui = Console(srv_student, srv_assignment, srv_grade, srv_undo)

    ui.run()


