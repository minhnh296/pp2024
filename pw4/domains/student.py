class Student:
    def __init__(self, student_id, name, dob):
        self.id = student_id
        self.name = name
        self.dob = dob
        self.gpa = 0
    
    def describe(self):
        print("Id: ", self.id)
        print("Name: ", self.name)
        print("DoB: ", self.dob)

    def __str__(self):
        return f"Id: {self.id}, Name: {self.name}, Dob: {self.dob}"
