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

from src.configuration.Setting import Settings

from src.repository.textRepository.textFileGradeRepository import TextFileGradeRepository
from src.repository.textRepository.textFileStudentRepository import TextFileStudentRepository
from src.repository.textRepository.textFileAssignmentRepository import TextFileAssignmentRepository

from src.repository.binaryRepository.binaryFileGradeRepository import BinaryFileGradeRepository
from src.repository.binaryRepository.binaryFileStudentRepository import BinaryFileStudentRepository
from src.repository.binaryRepository.binaryFileAssignmentRepository import BinaryFileAssignmentRepository


def repositories(settings):
    if settings.repository == "inmemory":
        return RepoStudent(),  RepoAssignment(), RepoGrade()

    elif settings.repository == "textfiles":
        return TextFileStudentRepository(settings.students_path), \
               TextFileAssignmentRepository(settings.assignments_path), \
               TextFileGradeRepository(settings.grades_path)

    elif settings.repository == "binaryfiles":
        return BinaryFileStudentRepository(settings.students_path),\
               BinaryFileAssignmentRepository(settings.assignments_path), \
               BinaryFileGradeRepository(settings.grades_path)


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
