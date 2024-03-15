from domains.student import Student
from domains.course import Course  
from domains.mark import Mark 
import numpy as np

class Smanagement(Student):
    def __init__(self):
        # Encapsulation data in the student class
        self.students = []
    
    # Function to input student details and add them to the list
    def Sinput(self):
        student_id = str(input("Enter student ID: "))
        name = input("Enter student name: ")
        dob = input("Enter student DoB: ")
        student = Student(student_id, name, dob)
        self.students.append(student)

    # Function to list all students
    def Slist(self):
        for student in self.students:
            print(student)

class Cmanagement(Course):
    def __init__(self):
        # Encapsulation data in the course class
        self.courses = []

    # Function to input course details and add them to the list    
    def Cinput(self):
        course_id = str(input("Enter course ID: "))
        name = input("Enter course name: ")
        credits = int(input("Enter credits "))
        course = Course(course_id, name, credits)
        self.courses.append(course)

    # Function to list all courses    
    def Clist(self):
        for course in self.courses:
            print(course)
            
class Mmanagement(Mark):
    def __init__(self):
        # Encapsulation data in the Mark class
        self.marks = []

    # Function to input mark details and add them to the list
    def Minput(self, students, courses):
        student_id = input("Enter student ID: ")
        course_name = input("Enter course Name: ")

    # Check if the entered student and course exist
        student = next((s for s in students if s.id == student_id), None)
        course = next((c for c in courses if c.name == course_name), None)

        if student is not None and course is not None:
            score = input("Enter student score: ")
            mark = Mark(student, course, score)
            self.marks.append(mark)
        else:
            print("Invalid student ID or course name.")

    # Function to list all student, course and mark
    def Mlist(self):
        sortt = np.argsort([-mark.gpa for mark in self.marks])
        for index in sortt:
            print(self.marks[index])