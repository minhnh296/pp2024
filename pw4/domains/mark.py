import math

class Mark:
    def __init__(self, student, course, score):
        self.student = student
        self.course = course
        self.score = math.ceil(float(score) * 10) / 10
        self.gpa = self.score / course.credits

    def __str__(self):
        return f"Student: {self.student.name}, Course: {self.course.name}, Score: {self.score}, GPA:{self.gpa}"
