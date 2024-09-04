import functools
from functools import total_ordering
from pprint import pprint


class Student:
    def get_average_grade(self, course):
        if course in self.grades:
            return round(sum(self.grades[course]) / len(self.grades[course]), 2)
        else:
            return 0

    def __lt__(self, other):
        if not isinstance(other, Student):
            return NotImplemented
        return self.get_average_grade('Python') < other.get_average_grade('Python')
        
    def __gt__(self, other):
        if not isinstance(other, Student):
            return NotImplemented
        return self.get_average_grade('Python') > other.get_average_grade('Python')
        
    def __eq__(self, other):
        if not isinstance(other, Student):
            return NotImplemented
        return self.get_average_grade('Python') == other.get_average_grade('Python')
        
    def __init__(self, name, surname, gender, finished_courses, courses_in_progress):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = finished_courses
        self.courses_in_progress = courses_in_progress
        self.grades = {} 
        self.avg_student = {}

    def rate_lecturer(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        return (f'Имя: {self.name} ' 
                f'Фамилия: {self.surname} ' 
                f'Средняя оценка за домашние задания: {self.avg_student} '
                f'Курсы в процессе изучения: {self.courses_in_progress} '
                f'Завершенные курсы: {self.finished_courses}')


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname, courses_attached, courses_in_progress, grades):
        super().__init__(name, surname) 
        self.courses_attached = courses_attached
        self.courses_in_progress = courses_in_progress
        self.grades = {}
        self.avg_lecturer = {}  

    def get_average_grade(self, course):
        if course in self.grades:
            return round(sum(self.grades[course]) / len(self.grades[course]), 2)
        else:
            return 0

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            return NotImplemented
        return self.avg_lecturer['Python'] < other.avg_lecturer['Python']
        
    def __gt__(self, other):
        if not isinstance(other, Lecturer):
            return NotImplemented
        return self.avg_lecturer['Python'] > other.avg_lecturer['Python']
        
    def __eq__(self, other):
        if not isinstance(other, Lecturer):
            return NotImplemented
        return self.avg_lecturer['Python'] == other.avg_lecturer['Python']

    def __str__(self):
        return (f'Имя: {self.name} '
                f'Фамилия: {self.surname} '
                f'Средняя оценка за лекции: {self.avg_lecturer}')


class Reviewer(Mentor):
    def __init__(self, name, surname, courses_attached, courses_in_progress):
        super().__init__(name, surname)
        self.courses_attached = courses_attached
        self.courses_in_progress = courses_in_progress

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        return (f'Имя: {self.name} '
                f'Фамилия: {self.surname}')

student1 = Student('Ruoy', 'Eman', 'boy','Введение в программирование, Git', 'Python')
student2 = Student('Kate', 'Brown', 'girl', 'Git', 'Python')
student_list = [student1, student2]

lecturer1 = Lecturer('Band', 'Keyge', 'Python', '', {}) 
lecturer2 = Lecturer('Fard', 'Hold', 'Python', '', {})
lecturer_list = [lecturer1, lecturer2]

reviewer1 = Reviewer('Hitten', 'Dons', 'Python', '')
reviewer2 = Reviewer('Jake', 'Lows', 'Python', '')

def count_grade(student_list, course):
    for student in student_list:
        if course in student.grades:
            student.avg_student[course] = round(sum(student.grades[course]) / len(student.grades[course]), 2)
        else:
            student.avg_student[course] = 0
    return student_list

def count_grade_l(lecturer_list, course):
    for lecturer in lecturer_list:
        if course in lecturer.grades:
            lecturer.avg_lecturer[course] = round(sum(lecturer.grades[course]) / len(lecturer.grades[course]), 2)
        else:
            lecturer.avg_lecturer[course] = 0 
    return lecturer_list


Student.rate_lecturer(student1, lecturer1, 'Python', 5)
Student.rate_lecturer(student2, lecturer1, 'Python', 10)
Student.rate_lecturer(student1, lecturer2, 'Python', 6)
Student.rate_lecturer(student2, lecturer2, 'Python', 10)


Reviewer.rate_hw(reviewer1, student1, 'Python', 8)
Reviewer.rate_hw(reviewer1, student2, 'Python', 10)
Reviewer.rate_hw(reviewer2, student1, 'Python', 2)
Reviewer.rate_hw(reviewer2, student2, 'Python', 5)


print(reviewer1)
print(reviewer2)

count_grade(student_list, 'Python')
count_grade_l(lecturer_list, 'Python')

print(lecturer1)
print(lecturer2)
print(student1)
print(student2)

count_grade_l([lecturer1, lecturer2], 'Python')
count_grade([student1, student2], 'Python')

print(lecturer1 < lecturer2)
print(lecturer1 > lecturer2)
print(lecturer1 == lecturer2)
print(student1 < student2) 
print(student1 > student2) 
print(student1 == student2)
