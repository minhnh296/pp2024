import numpy as np
from domains.student import Student
from domains.course import Course  
from domains.mark import Mark 

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
    
    # Function to list the student into txt file
    def Swrite(self):
        with open('students.txt', 'w') as x:
            for student in self.students:
                x.write(f"Id: {student.id}, Name: {student.name}, Dob: {student.dob}\n")
                

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
            
    # Function to list the course into txt file
    def Cwrite(self):
        with open('courses.txt', 'w') as x:
            for course in self.courses:
                x.write(f"Id: {course.id}, Name: {course.name}, Credits: {course.credits}\n")

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

    # Function to list all student, course and mark into txt file
    def Mwrite(self):
        with open('marks.txt', 'w') as x:
            for mark in self.marks:
                x.write(f"Student ID: {mark.student.id}, D/O/B: {mark.student.dob}, Student: {mark.student.name}, Course: {mark.course.name}, Score: {mark.score}, GPA:{mark.gpa}\n")
