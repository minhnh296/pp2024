import curses
import os
import zipfile
import pickle
from input import Smanagement, Cmanagement, Mmanagement
from output import main as outmain

class compress:
    def compression(names, dat):
        with zipfile.ZipFile(dat, "w") as zipf:
            for name in names:
                zipf.write(name, os.path.basename(name))
        with open(dat, 'wb') as f:
           pickle.dump(names, f)
        with open(dat, 'rb') as f:
           names = pickle.load(f)
    

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
    7. Feedback
    """)
        option = int(input("Your choice: "))  # Choose option from 0 -> n
        if option == 0:
            break
        elif option == 1:
            SM.Sinput()
            SM.Swrite()
            print("Adding successfully into the txt file")
        elif option == 2:
            CM.Cinput()
            CM.Cwrite()
            print("Adding successfully into the txt file")
        elif option == 3:
            MM.Minput(SM.students, CM.courses)
            MM.Mwrite()
            print("Adding successfully into the txt file")
        elif option == 4:
            SM.Slist()
        elif option == 5:
            CM.Clist()
        elif option == 6:
            MM.Mlist()
        elif option == 7:
            curses.wrapper(outmain)
        else:
            print("Invalid input. Please try again!")
names = [
    'pw5/input.py',
    'pw5/output.py',
    'pw5/main.py',
    'pw5/domains/student.py',
    'pw5/domains/course.py',
    'pw5/domains/mark.py'
]
dat = 'students.dat'
compress.compression(names, dat)
