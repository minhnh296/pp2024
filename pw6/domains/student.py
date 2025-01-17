class Student:
    def __init__(self, student_id, name, dob):
        # Constructor for the Student class
        self.id = student_id
        self.name = name
        self.dob = dob
        self.gpa = 0
    
    # Function to provide a string representation of a student object using overriding
    def __str__(self):
        return f"Id: {self.id}, Name: {self.name}, Dob: {self.dob}"
