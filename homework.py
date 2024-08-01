class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = []

    def rate_lecturer(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached:
            if course in lecturer.courses_attached:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        return (f'Имя: {self.name}'
                f'Фамилия: {self.surname}'
                f'Средняя оценка за домашние задания: {self.}'
                f'Курсы в процессе изучения: {self.courses_in_progress}'
                f'Завершенные курсы: {", ".join(self.finished_courses)}')


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname, courses_attached, courses_in_progress, grades):
        Mentor.__init__(self, name, surname)
        self.courses_attached = []
        self.courses_in_progress = []
        self.grades = []

    def __str__(self):
        return (f'Имя: {self.name}'
                f'Фамилия: {self.surname}'
                f'Средняя оценка за лекции: {self.}')


class Reviewer(Lecturer):
    def __init__(self, name, surname, courses_attached, courses_in_progress):
        Mentor.__init__(self, name, surname)
        self.courses_attached = []
        self.courses_in_progress = []

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        return (f'Имя: {self.name}'
                f'Фамилия: {self.surname}')

student1 = Student('Ruoy','Eman', 'boy')
student2 = Student('Kate', 'Brown', 'girl')
lecturer1 = Lecturer('Band', 'Keyge', 'Python', '', 0)
lecturer2 = Lecturer('Fard', 'Hold', 'Git', '', 0)
reviewer1 = Reviewer('Hitten', 'Dons', 'Python', '')
reviewer2 = Reviewer('Jake', 'Lows', 'Python', '')

Student.rate_lecturer(student1, lecturer1, 'Python', 5)
Student.rate_lecturer(student2, lecturer1, 'Python', 10)
Student.rate_lecturer(student1, lecturer2, 'Python', 6)
Student.rate_lecturer(student2, lecturer2, 'Python', 10)

print(student1)
print(student2)
print(lecturer1)
print(lecturer2)

Reviewer.rate_hw(reviewer1, student1, 'Python', 8)
Reviewer.rate_hw(reviewer1, student2, 'Python', 10)
Reviewer.rate_hw(reviewer2, student1, 'Python', 2)
Reviewer.rate_hw(reviewer2, student2, 'Python', 5)

print(reviewer1)
print(reviewer2)

def all_students = []
# не понимаю как записать и как реализовать две функции

best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python']

cool_mentor = Mentor('Some', 'Buddy')
cool_mentor.courses_attached += ['Python']


print(best_student.grades)