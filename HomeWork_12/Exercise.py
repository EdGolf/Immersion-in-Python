from Students import Student
from random import randint, choice

COUNT_GRADES = 30
COUNT_TESTS = 50

if __name__ == '__main__':
    student = Student("Петр", "Петров", "Петрович")
    for _ in range(COUNT_GRADES):
        student.add_grade(choice(student.subjects), randint(Student.GRADE_MIN, Student.GRADE_MAX))
    for _ in range(COUNT_TESTS):
        student.add_test_result(choice(student.subjects), randint(Student.TEST_RESULT_MIN, Student.TEST_RESULT_MAX))
    print(student)