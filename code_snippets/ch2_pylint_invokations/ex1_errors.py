# pylint: disable=R,C
import sys


def mispellings():
    my_str = "Hello, PyGDA!"
    print(my_st)  # misspelled variable
    sys.stout.write(my_str)  # misspelled attribute


def bad_except_order():
    try:
        return mispellings()
    except ValueError:
        pass
    except UnicodeError:
        # never reached, superclass is caught first
        pass
