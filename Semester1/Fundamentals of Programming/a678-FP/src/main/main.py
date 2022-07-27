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

if __name__ == "__main__":
    valid_student = ValidatorStudent
    valid_assignment = ValidatorAssignment
    valid_grade = ValidatorGrade

    repo_student = RepoStudent()
    repo_assignment = RepoAssignment()
    repo_grade = RepoGrade()

    srv_student = ServiceStudent(valid_student, repo_student)
    srv_assignment = ServiceAssignment(valid_assignment, repo_assignment)
    srv_grade = ServiceGrade(valid_student, valid_assignment, valid_grade, repo_student, repo_assignment, repo_grade)

    srv_undo = ServiceUndo(srv_student, srv_assignment, srv_grade)

    ui = Console(srv_student, srv_assignment, srv_grade, srv_undo)

    ui.run()
