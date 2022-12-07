#!/usr/bin/python3
"""Print all names defined by hidden_4 module."""
import hidden_4
if __name__ == "__main__":
    for i in dir(hidden_4):
        if i[0:2] != "__":
            print("{:s}".format(i))
