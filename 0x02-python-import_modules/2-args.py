#!/usr/bin/python3
from sys import argv
if __name__ == "__main__":
    i = len(sys.argv) - 1
    if i == 0:
        print("{} arguments.".format(i))
    elif i == 1:
        print("{} argument:".format(i))
        print("{}: {}".format(i, argv))
    else:
        print("{} arguments:".format(i))
        if i >= 1:
            i = 0
            for arg in sys.argv:
                if i != 0:
                    print("{}: {}".format(i, arg))
                    i += 1
