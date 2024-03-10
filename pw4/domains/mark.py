import math

class Mark:
    # Constructor for the Mark class
    def __init__(self, student, course, score):
        self.student = student
        self.course = course
        self.score = math.ceil(float(score) * 10) / 10      # I change it to a decimal rounded to 1 digit when entered with math.ceil()
        self.gpa = self.score / course.credits

    # Function to provide a string representation of a student with mark using overriding  
    def __str__(self):
        return f"Student: {self.student.name}, Course: {self.course.name}, Score: {self.score}, GPA:{self.gpa}"
