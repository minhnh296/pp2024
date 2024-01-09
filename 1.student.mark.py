# Function to get the number of students
def NumOfStudents():
    s = int(input("Number of students is: "))
    return s

# Function to get the list of students
def Slist():
    num_students = NumOfStudents()
    stulist = []
    for i in range(num_students):
        print(f"\nStudent {i + 1}:")
        Sid = input("ID: ")       
        Sname = input("Name: ")
        Sdob = input("DOB(dd/mm/yy): ")
        student_info = {"ID": Sid, "Name": Sname, "DOB": Sdob}
        stulist.append(student_info)
    return stulist

# Function to get the number of courses
def NumOfCourse():
    c = int(input("Number of courses is: "))
    return c

# Function to get the list of courses
def Clist():
    num_courses = NumOfCourse()
    courselist = []
    for n in range(num_courses):
        print(f"\nCourse {n + 1}:")
        Cid = input("ID: ")
        Cname = input("Name: ")
        course_info = {"ID": Cid, "Name": Cname}
        courselist.append(course_info)
    return courselist

# function to input marks for student in the course
def inputmarks(student, course):
    mark = float(input(f"Enter the mark for ID: {student['ID']} in the course name: {course['Name']}: "))
    return {"course": course, "student": student, "mark": mark}

# Function to display the list of the student
def Sdisplay(students):
    print("\nStudents List:")
    for student in students:
        print(f"ID: {student['ID']} - Name: {student['Name']} - DOB: {student['DOB']}")
        
# Function to display the list of the course
def Cdisplay(courses):
    print("\nCourse List:")
    for course in courses:
        print(f"ID: {course['ID']} - Name: {course['Name']}")

# Function to display the list of mark
def inputDisplay(marks):
    print("\n input mark list")
    for mark in marks:
        print(f"Student ID: {mark['student']['ID']} - Name: {mark['student']['Name']} - Dob: {mark['student']['DOB']} - Course: {mark['course']['Name']} - Mark: {mark['mark']}")

def main():
    # Initialize the list for DATA option
    students = []
    courses = []
    marks = []

    while True:
        print("""
    0. Exit
    1. Add student
    2. Add course
    3. Input marks
    4. Students list
    5. Courses list
    6. Display marks
    
    """)
        option = int(input("Your choice: "))  # Choose option from 0 -> n
        if option == 0:
            break
        elif option == 1:
            students.extend(Slist()) 
        elif option == 2:
            courses.extend(Clist())
        elif option == 3:
            for student in students:
                for course in courses:
                    mark = inputmarks(student, course)
                    marks.append(mark)
                    print(f"Mark entered: {mark['mark']}")

        elif option == 4:
            Sdisplay(students)
        elif option == 5:
            Cdisplay(courses)
        elif option == 6:
            inputDisplay(marks)
        else:
            print("Invalid input. Please try again!")

# Call the main function
if __name__ == "__main__":
    main()
