class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

        

    def rete_lc(self,lecturer,course,grade):
      if isinstance (lecturer,Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress :
        if course in lecturer.grades:
          lecturer.grades[course] += [grade]
        else:
          lecturer.grades[course] = [grade] 
      else:
        return "Ошибка" 

    def __average_ball (self):
      self.midl_ball = [grade for grades in self.grades.values() for grade in grades]
      if self.midl_ball:
        self.midl_grade = (sum(self.midl_ball)/len(self.midl_ball)) 
        return self.midl_grade
      else:
        return ("Пока нет оценок")

      

    def __str__(self):
        return (f"Имя Студента : {self.name} \nФамилия Студента : {self.surname} \nСредний балл за ДЗ : {self.__average_ball()} \nКурсы в процессе изучени :{self.courses_in_progress} \nЗавершенные курсы : {self.finished_courses} ")
        
       
  
    def __eq__(self, other):
        if not isinstance (other,Student):
          print ("Ошибка : сравнивать можно только студентов")
          return
        elif isinstance (self,Student):
          return self.__average_ball() == other.__average_ball

    def __lt__(self, other):
        if not isinstance (other,Student):
          print ("Ошибка : сравнивать можно только студентов")
          return
        elif isinstance (self,Student):
          return self.__average_ball() < other.__average_ball

    def __gt__(self, other):
        if not isinstance (other,Student):
          print ("Ошибка : сравнивать можно только студентов")
          return
        elif isinstance (self,Student):
          return self.__average_ball() > other.__average_ball 

 

class Mentor:
  def __init__(self,name,surname):
    self.name = name
    self.surname = surname
    self.courses_attached = []


class Lecturer(Mentor):
  def __init__(self,name,surname):
    super().__init__(name,surname)
    self.courses_attached = []
    self.grades = {}

       
    

  def __average_ball (self):
    self.midl_ball = [grade for grades in self.grades.values() for grade in grades]
    if self.midl_ball:
      self.midl_grade = sum(self.midl_ball) / len(self.midl_ball)
      return self.midl_grade
    else:
      return "Пока нет оценок"
        
       
  
  
  def __str__(self):
    return (f"Имя Лектора : {self.name} \nФамилия Лектора : {self.surname} \nСредний балл : {self.__average_ball()}")
      


  def __eq__(self, other):
        if not isinstance (other,Lecturer):
          print ("Ошибка : сравнивать можно только Лекторов")
          return
        elif isinstance (self,Lecturer):
          return self.__average_ball() == other.__average_ball()

  def __lt__(self, other):
        if not isinstance (other,Lecturer):
          print ("Ошибка : сравнивать можно только Лекторов")
          return
        elif isinstance (self,Lecturer):
          return self.__average_ball() < other.__average_ball()

  def __gt__(self, other):
        if not isinstance (other,Lecturer):
          print ("Ошибка : сравнивать можно только Лекторов")
          return
        elif isinstance (self,Lecturer):
          return self.__average_ball() > other.__average_ball()
  
           
          

class Reviewer(Mentor):
  def __init__(self,name,surname,):
    super(). __init__(name,surname,)
    self.courses_attached = []

        
  
  def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'  


        

  def __str__(self):
    return f" Имя и Фамилия Ревьюера : {self.name} {self.surname}"


    
          

Student1 = Student("Maria","Petrova","woman")
Student1.courses_in_progress += ["Python", "Java"]
Student1.finished_courses += ["Git"]

Student2 = Student("Emma","Still","woman")
Student2.courses_in_progress += ["Python", "Java"]
Student2.finished_courses += ["Git"]

Reviewer1 = Reviewer ("Bill","Stoke")
Reviewer1.courses_attached += ["Java","Python","Git"]
Reviewer2 = Reviewer ("Eddy","Koks")
Reviewer2.courses_attached += ["Java","Python","Git"]

Reviewer1.rate_hw(Student2,"Java",7)
Reviewer1.rate_hw(Student2,"Java",7)
Reviewer1.rate_hw(Student2,"Java",8)

Reviewer1.rate_hw(Student1,"Java",10)
Reviewer1.rate_hw(Student1,"Java",10)
Reviewer1.rate_hw(Student1,"Java",9)

Reviewer2.rate_hw(Student2,"Python", 5)
Reviewer2.rate_hw(Student2,"Python", 10)
Reviewer2.rate_hw(Student2,"Python", 10)

Reviewer2.rate_hw(Student1,"Python",8)
Reviewer2.rate_hw(Student1,"Python",10)
Reviewer2.rate_hw(Student1,"Python",9)


Lecturer1 = Lecturer ("Max","Brown")
Lecturer1.courses_attached += ["Java", "Python"]


Student1.rete_lc(Lecturer1,"Java", 7)
Student1.rete_lc(Lecturer1,"Java", 7)
Student1.rete_lc(Lecturer1,"Java", 9) 

Student2.rete_lc(Lecturer1,"Python", 6)
Student2.rete_lc(Lecturer1,"Python", 10)
Student2.rete_lc(Lecturer1,"Python", 10) 

Lecturer2 = Lecturer ("Rita", "Smirnova")
Lecturer2.courses_attached += ["Java", "Python"]

Student1.rete_lc(Lecturer2,"Java", 7)
Student1.rete_lc(Lecturer2,"Java", 8)
Student1.rete_lc(Lecturer2,"Java", 10) 

Student2.rete_lc(Lecturer2,"Python", 7)
Student2.rete_lc(Lecturer2,"Python", 8)
Student2.rete_lc(Lecturer2,"Python", 6) 


print (f'Список студентов и средний бал за Домашнее задание по их курсу : \n{Student1} \n{Student2}')
print ()
print (f' Список Лекторов и средние оценки за лекцию : \n{Lecturer1} \n{Lecturer2}')
print ()
print (f'Список проверяющих Домашние задания : \n{Reviewer1} \n{Reviewer2}')



Student_list = [Student1,Student2]
Lecturer_list = [Lecturer1,Lecturer2]

def course_m_grade_stud (Student_list,course):
  midl_grade = []
  for student in Student_list:
    if course in student.grades:
      midl_grade += student.grades[course]
  if midl_grade:
    return sum(midl_grade) / len(midl_grade)
      

def course_m_grade_lect (Lecturer_list,course):
  midl_grade = []
  for lecturer in Lecturer_list:
    if course in lecturer.grades:
      midl_grade += lecturer.grades[course]
  if midl_grade:
    return sum(midl_grade) / len(midl_grade)  



