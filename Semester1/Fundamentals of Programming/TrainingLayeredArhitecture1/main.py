from Domain.entities import *
from Validation.validators import *
from Infrastructure.gradeRepo import GradeRepo
from Infrastructure.studentRepo import StudentRepo
from Infrastructure.assignmentRepo import AssignmentRepo
from Business.gradeService import GradeService
from Business.assignmentService import AssignmentService
from Business.studentService import StudentService
from Presentation.userInterface import Console


repo_student = StudentRepo()
repo_assignment = AssignmentRepo()
repo_grade = GradeRepo()

valid_student = StudentValidator()
valid_assignment = AssignmentValidator()
valid_grade = GradeValidator()

srv_student = StudentService(repo_student, valid_student)
srv_assignment = AssignmentService(repo_assignment, valid_assignment)
srv_grade = GradeService(repo_grade, repo_assignment, repo_student, valid_grade)

ui = Console(srv_assignment, srv_student, srv_grade)

ui.run()