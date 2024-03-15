import curses

def main(stdscr):
    curses.init_pair(1, curses.COLOR_RED, curses.COLOR_BLACK)
    RED_AND_BLACK = curses.color_pair(1)
    
    stdscr.clear()
    stdscr.addstr(5, 5, "tu as été trompé, hahahahahahahahahahahahahahahahahahahaha", RED_AND_BLACK)
    stdscr.refresh()
    stdscr.getch()
