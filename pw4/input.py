from domains.student import Student
from domains.course import Course  
from domains.mark import Mark 
import numpy as np

class Smanagement:
    def __init__(self):
        self.students = []
    
    def Sinput(self):
        student_id = str(input("Enter student ID: "))
        name = input("Enter student name: ")
        dob = input("Enter student DoB: ")
        student = Student(student_id, name, dob)
        self.students.append(student)

    def Slist(self):
        for student in self.students:
            print(student)

class Cmanagement:
    def __init__(self):
        self.courses = []

    def Cinput(self):
        course_id = str(input("Enter course ID: "))
        name = input("Enter course name: ")
        credits = int(input("Enter credits "))
        course = Course(course_id, name, credits)
        self.courses.append(course)

    def Clist(self):
        for course in self.courses:
            print(course)

class Mmanagement:
    def __init__(self):
        self.marks = []

    def Minput(self, students, courses):
        student_id = input("Enter student ID: ")
        course_name = input("Enter course Name: ")

        student = next((s for s in students if s.id == student_id), None)
        course = next((c for c in courses if c.name == course_name), None)

        if student is not None and course is not None:
            score = input("Enter student score: ")
            mark = Mark(student, course, score)
            self.marks.append(mark)
        else:
            print("Invalid student ID or course name.")

    def Mlist(self):
        sortt = np.argsort([-mark.gpa for mark in self.marks])
        for index in sortt:
            print(self.marks[index])
