from Domain.entities import StudentAverageDTO


class GradeService:
    def __init__(self, repo_grade, repo_assignment, repo_student, valid_grade):
        self.__repo_grade = repo_grade
        self.__repo_assignment = repo_assignment
        self.__repo_student = repo_student
        self.__valid_grade = valid_grade

    def top_30_percent_bosses(self):
        grades = self.__repo_grade.get_all_grades()
        school_situation = {}
        for grade in grades:
            student_id = grade.get_id_stud()
            if student_id not in school_situation:
                school_situation[student_id] = []
            school_situation[student_id].append(grade.get_value_grade())
        res = []
        for student_id in school_situation:
            student_name = self.__repo_student.search_by_id(student_id)
            student_average = sum(school_situation[student_id]) / len(school_situation[student_id])
            student_averageDTO = StudentAverageDTO(student_name, student_average)
            res.append(student_averageDTO)
        res.sort(key=lambda x: x.get_average(), reverse=True)
        return res[:len(res)//3]
