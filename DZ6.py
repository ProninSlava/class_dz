class Student:
    def __init__(self, name, surname, gender):             # Атрибуты
        self.name = name
        self.surname = surname
        self.gender = gender
        self.courses_in_progress = []
        self.grades = {}
        self.finished_courses = []

    # def insert_courses(self, course_name):                  # Курсы, которые учат
    #     self.courses_in_progress.append(course_name)

    def add_courses(self, course_name):                     # Курсы, которые закончили
        self.finished_courses.append(course_name)

    def grade_lecturer(self, lecturer, course, grade):      # Оценки лекторам
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def average_score(self):                                # Подсчет среднего балла за всю домашку одного студента
        total = 0
        total_len = 0
        for i in self.grades.values():
            total += sum(i)
        for i in self.grades.values():
            total_len += len(i)

        average = total / total_len
        return round(average, 1)

    def __lt__(self, other):                                # Сравнение студентов по среднему баллу
        if not isinstance(other, Student):
            return
        if self.average_score() < other.average_score():
            return (f'Cредняя оценка за домашние задания у студентов: {self.surname} ({self.average_score()}) < {other.surname} ({other.average_score()})')
        if self.average_score() > other.average_score():
            return (f'Cредняя оценка за домашние задания у студентов: {self.surname} ({self.average_score()}) > {other.surname} ({other.average_score()})')
    #__________________________________________________________
        # return self.average_score() < other.average_score()

    def __str__(self):                                       # Print
        a = ', '.join(self.finished_courses)
        b = ', '.join(self.courses_in_progress)

        return f'Студент\n------- \nИмя: {self.name} \nФамилия: {self.surname}' \
               f' \nКурсы в процессе изучения: {b}' \
               f'\nСредняя оценка: {self.average_score()}'\
               f'\nЗавершенные курсы: {a}'
#___________________________________________________________________________________
class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
#___________________________________________________________________________________
class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def average_score(self):                                 # Средний балл от учеников
        total = 0
        total_len = 0
        for i in self.grades.values():
            total += sum(i)
        for i in self.grades.values():
            total_len += len(i)

        average = total / total_len
        return round(average, 1)

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            return
        if self.average_score() < other.average_score():
            return (f'Cредняя оценка за лекции у лекторов: {self.surname} ({self.average_score()}) < {other.surname} ({other.average_score()})')
        if self.average_score() > other.average_score():
            return (f'Cредняя оценка за лекции у лекторов: {self.surname} ({self.average_score()}) > {other.surname} ({other.average_score()})')

    def __str__(self):                                        # Print
        return f'Лектор\n------ \nИмя: {self.name} \nФамилия: {self.surname}' \
               f'\nСредняя оценка за лекции: {self.average_score()}'
#_________________________________________________________________________
class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):                # Оценки студентам
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):                                          # Print
        return f'Эксперт \n-------\nИмя: {self.name} \nФамилия: {self.surname}'

#_________________________________________________
student1 = Student('Сергей', 'Петров', 'М')
student1.courses_in_progress += ['Python', 'Git']
student1.add_courses('Введение в программирование')

student2 = Student('Коля', 'Пупков', 'М')
student2.courses_in_progress += ['С++']
student2.add_courses('Введение в программирование')

student3 = Student('Женя', 'Дружини', 'М')
student3.courses_in_progress += ['С++']

student4 = Student('Петя', 'Крутов', 'М')
student4.courses_in_progress += ['Python', 'С++']

#_________________________________________________

lecturer1 = Lecturer('Олег','Рогожин')
lecturer1.courses_attached += ['С++', 'Python']

lecturer2 = Lecturer('Юра','Засовин')
lecturer2.courses_attached += ['Git', 'С++']
#_________________________________________________

reviewer1 = Reviewer('Василий', 'Уткин')
reviewer1.courses_attached += ['Python', 'Git']

reviewer2 = Reviewer('Валера', 'Хлопкин')
reviewer2.courses_attached += ['С++', 'Python']


reviewer1.rate_hw(student1, 'Python', 9)
reviewer1.rate_hw(student1, 'Python', 10)
reviewer1.rate_hw(student1, 'Python', 7)

reviewer2.rate_hw(student2, 'С++', 6)
reviewer2.rate_hw(student2, 'С++', 9)
reviewer2.rate_hw(student2, 'С++', 8)

reviewer2.rate_hw(student4, 'Python', 6)
reviewer2.rate_hw(student4, 'Python', 8)
reviewer2.rate_hw(student4, 'Python', 7)
reviewer2.rate_hw(student4, 'Python', 9)
reviewer2.rate_hw(student4, 'С++', 10)

#_________________________________________________

student2.grade_lecturer(lecturer1, 'С++', 7)
student3.grade_lecturer(lecturer1, 'С++', 6)
student4.grade_lecturer(lecturer1, 'С++', 9)
student4.grade_lecturer(lecturer1, 'Python', 8)

student2.grade_lecturer(lecturer2, 'С++', 7)
student3.grade_lecturer(lecturer2, 'С++', 7)
student4.grade_lecturer(lecturer2, 'С++', 10)
#_________________________________________________
print()

def evaluate_student(in_list, cours):                             # Средний балл за курс всех студентов
    total = 0
    for st in in_list:
        if cours in st.grades:
            suma = sum(st.grades[cours])
            total += suma/len(st.grades[cours])
    print(f'Cредняя оценка за домашнее задания по курсу "{cours}" по всем студентам: {round(total/len(in_list), 1)}')

#_________________________________________________
st_list = [student1, student4]
evaluate_student(st_list, "Python")
#_________________________________________________
print()

def evaluate_lecturer(in_list, cours):                             # Средний балл за курс всех лекторов
    total = 0
    for lect in in_list:
        if cours in lect.grades:
            suma = sum(lect.grades[cours])
            total += suma/len(lect.grades[cours])
    print(f'Cредняя оценка за лекции по курсу "{cours}" по всем лекторам: {round(total/len(in_list), 1)}')

#_________________________________________________
lect_list = [lecturer1, lecturer2]
evaluate_lecturer(lect_list, "С++")
#_________________________________________________

print()
print(reviewer1)
print()
print(lecturer1)
print()
print(lecturer2)
print()
print(student1)
print()
print(student2)
print()
print(student4)
print()
print(student1 < student2)
print(lecturer1 < lecturer2)

