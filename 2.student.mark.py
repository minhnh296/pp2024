class Student:
    def __init__(self, student_id, name, dob):
        # Constructor for the Student class
        self.id = student_id
        self.name = name
        self.dob = dob
    
    # Function to provide a string representation of a student object using overriding
    def __str__(self):
        return f"Id: {self.id} - Name: {self.name} - Dob: {self.dob}"

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

class Course:
    def __init__(self, course_id, name):
        # Constructor for the Course class
        self.id = course_id
        self.name = name
    
    # Function to provide a string representation of a Course object using overriding
    def __str__(self):
        return f"Course Id: {self.id}, Course name: {self.name}"

class Cmanagement(Course):
    def __init__(self):
        # Encapsulation data in the course class
        self.courses = []

    # Function to input course details and add them to the list    
    def Cinput(self):
        course_id = str(input("Enter course ID: "))
        name = input("Enter course name: ")
        course = Course(course_id, name)
        self.courses.append(course)

    # Function to list all courses    
    def Clist(self):
        for course in self.courses:
            print(course)

class Mark:
    # Constructor for the Mark class
    def __init__(self, student, course, score):
        self.student = student
        self.course = course
        self.score = score

    # Function to provide a string representation of a student with mark using overriding  
    def __str__(self):
        return f"Student: {self.student.name}, Course: {self.course.name}, Score: {self.score}"

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
        for mark in self.marks:
            print(mark)

# Create instances of the management classes
if __name__ == "__main__": 
    SM = Smanagement()
    CM = Cmanagement()
    MM = Mmanagement()

    while True:
        print("""
    0. Exit
    1. Add student
    2. Add course
    3. Input mark
    4. Students list
    5. Courses list
    6. Mark list
    """)
        option = int(input("Your choice: "))  # Choose option from 0 -> n
        if option == 0:
            break
        elif option == 1:
            SM.Sinput()
        elif option == 2:
            CM.Cinput()
        elif option == 3:
            MM.Minput(SM.students, CM.courses)
        elif option == 4:
            SM.Slist()
        elif option == 5:
            CM.Clist()
        elif option == 6:
            MM.Mlist()
        else:
            print("Invalid input. Please try again!")
