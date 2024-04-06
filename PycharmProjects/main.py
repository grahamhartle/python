import curses
from curses import wrapper


def main(stdscr):
    stdscr.clear()
    stdscr.addstr(10, 25, "Hello World!", curses.A_BOLD)
    stdscr.addstr(12, 0, "Press any key to continue...")
    stdscr.refresh()
    stdscr.getch()


wrapper(main)
