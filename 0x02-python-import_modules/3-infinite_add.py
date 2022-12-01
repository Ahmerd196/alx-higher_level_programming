#!/usr/bin/python3
import argv from sys
if __name__ == "__main__":
    result = 0
    if len(argv) == 1:
        print("0")
    else:
        for i in range(1, len(argv)):
            result += int(argv[i])
            print(result)
