class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lec(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.courses_attached and course in lecturer.grades:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        res = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашние задания: {self.grades}\nКурсы в процессе изучения: {self.courses_in_progress}\nЗавершённые курсы: {self.finished_courses}'
        return res
    
    def __lt__(self, other):

        if not isinstance(other, Lecturer):
            print('Можно сравнивать только Лекторов!')
            return
        elif self.rate_lec() > other.rate_lec():
            return f'\n{self.name} {self.surname} имеет среднюю оценку за лекции выше чем {other.name} {other.surname}'
        else:
            return f'\n{other.name} {other.surname} имеет среднюю оценку за лекции выше чем {self.name} {self.surname}'
    
    
class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

class Lecturer(Mentor):
    def __init__(self):
        self.grades = {}
    def __str__(self):
        res = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self.grades}'
        return res
    
class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'
    
    def __lt__(self, other):

        if not isinstance(other, Student):
            print('Можно сравнивать только студентоп!')
            return
        elif self.rate_hw() > other.rate_hw():
            return f'\n{self.name} {self.surname} имеет среднюю оценку за ДЗ выше чем {other.name} {other.surname}'
        else:
            return f'\n{other.name} {other.surname} имеет среднюю оценку за ДЗ выше чем {self.name} {self.surname}'

    def __str__(self):
        res = f'Имя: {self.name}\nФамилия: {self.surname}'
        return res

students_list = []
lecturer_list = []


stud1 = Student('Ruoy', 'Eman', 'M')
stud1.finished_courses += ['Введение в программирование', 'Основы Python']
stud1.courses_in_progress += ['Python']
stud1.grades = [9.8]
students_list.append(stud1)

stud2 = Student('Vincent', 'Flow', 'M')
stud1.finished_courses += ['Основы Python']
stud2.courses_in_progress += ['Python']
stud1.grades += [9.7]
students_list.append(stud2)

lec1 = Lecturer('Ivan', 'Fank')
lec1.courses_attached += ['Python']
lec1.grades += [7.5]
lecturer_list.append(lec1)

lec2 = Lecturer('John', 'Sirius')
lec2.courses_attached += ['Python']
lec2.grades += [8.4]
lecturer_list.append(lec2) 

rew1 = Reviewer('Some', 'Buddy')
rew1.courses_attached += ['Python']

rew2 = Reviewer('Solc', 'Sins')
rew2.courses_attached += ['Python'] 
# cool_mentor.rate_hw(best_student, 'Python', 10)
# cool_mentor.rate_hw(best_student, 'Python', 10)
# cool_mentor.rate_hw(best_student, 'Python', 10)
 
# print(best_student.grades)