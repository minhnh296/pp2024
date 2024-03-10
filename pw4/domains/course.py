class Course:
    def __init__(self, course_id, name, credits):
        # Constructor for the Course class
        self.id = course_id
        self.name = name
        self.credits = credits
                    
    # Method to print the details of a course
    def describe(self):
        print("Id: ", self.id)
        print("Name: ", self.name)
        print("Credits:", self.credits)
        
    # Function to provide a string representation of a Course object using overriding
    def __str__(self):
        return f"Course Id: {self.id}, Course name: {self.name}, Credits: {self.credits}"