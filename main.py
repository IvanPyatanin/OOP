class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lecturer(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def average_rating(self):
        count = 0
        sum_ = 0
        for course in self.grades.values():
            sum_ += sum(course)
            count += len(course)
        return round(sum_ / count, 2)

    def __lt__(self, other_student):
        if not isinstance(other_student, Student):
            return
        else:
            compare = self.average_rating() > other_student.average_rating()

            if compare:
                print(f"У {self.name} {self.surname} оценка лучше чем, у {other_student.name} {other_student.surname}")
            else:
                print(f"У {other_student.name} {other_student.surname} оценка лучше чем, у {self.name} {self.surname}")

    def __str__(self):
        prog_courses = ','.join(self.courses_in_progress)
        fin_courses = ','.join(self.finished_courses)
        return f"Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашнеее задание: {self.average_rating}\nКурсы в процессе изучения: {prog_courses}\nЗавершенные курсы: {fin_courses}"

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def average_rating(self):
        count = 0
        sum_ = 0
        for course in self.grades.values():
            sum_ += sum(course)
            count += len(course)
        return round(sum_ / count, 2)

    def __lt__(self, other_lecturer):
        if not isinstance(other_lecturer, Lecturer):
            return
        else:
            compare = self.average_rating() > other_lecturer.average_rating()

            if compare:
                print(f"У {self.name} {self.surname} оценка лучше чем, у {other_lecturer.name} {other_lecturer.surname}")
            else:
                print(f"У {other_lecturer.name} {other_lecturer.surname} оценка лучше чем, у {self.name} {self.surname}")

    def __str__(self):
        return f"Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекцию: {self.average_rating()}"


class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        return f"Имя: {self.name}\nФамилия: {self.surname}"

def averege_stident_grade(students, course):
    sum_ = 0
    for student in students:
        sum_ +=sum(student.grades[course]) / len(student.grades[course])
    return sum_ / len(students)

def averege_lecturer_garde(lecturers, course):
    sum_ = 0
    for lecturer in lecturers:
        sum_ += sum(lecturer.grades[course]) / len(lecturer.grades[course])
    return sum_ / len(lecturers)

some_student = Student('Ruoy', 'Eman', 'your_gender')
some_student.courses_in_progress += ['Python']
some_student.courses_in_progress += ['Git']
some_student.finished_courses += ['Введение в программирование']

some_lecturer = Lecturer('Some', 'Buddy')
some_lecturer.courses_attached += ['Python']
some_lecturer.courses_attached += ['Git']

some_reviewer = Reviewer('Some','Buddy')