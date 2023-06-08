#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    add = 0
for numbers in argv[1:]:
    add += int(numbers)
print("{:d}".format(add))
