import curses
from input import Smanagement, Cmanagement, Mmanagement
from output import main as outmain

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
        elif option == 7:
            curses.wrapper(outmain)
        else:
            print("Invalid input. Please try again!")
