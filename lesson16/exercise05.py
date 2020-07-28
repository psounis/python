from random import randrange, seed
from datetime import datetime


class Student:
    def __init__(self, full_name):
        self.full_name = full_name
        self.grade = -1


def grade_student(student):
    student.grade = randrange(0,11)


def average(students):
    s = 0
    for student in students:
        s += student.grade

    print("Average: " + str(s/len(students)))

seed(datetime.now())

names = ["Kirk Bowman",
"Bear Byers",
"Kurtis Macias",
"Maximus Preece",
"Cecily Ray",
"Cade Parry",
"Jordyn Pitts",
"Liya Christian",
"Ceri Orr",
"Mekhi Hahn"]

students = [Student(names[i]) for i in range(len(names))]

for student in students:
    grade_student(student)

average(students)