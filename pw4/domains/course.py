class Course:
    def __init__(self, course_id, name, credits):
        self.id = course_id
        self.name = name
        self.credits = credits
        
    def describe(self):
        print("Id: ", self.id)
        print("Name: ", self.name)
        print("Credits:", self.credits)
    
    def __str__(self):
        return f"Course Id: {self.id}, Course name: {self.name}, Credits: {self.credits}"
