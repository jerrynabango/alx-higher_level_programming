#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    from calculator_1 import add, sub, mul, div
    argc = len(argv)
    if argc != 4:
        print('Usage: {} <a> <operator> <b>'.format(argv[0]))
        exit(1)
    ops = {'+': add,
                '-': sub,
                '*': mul,
                '/': div
               }
    if argv[2] in ops:
        integer1 = int(argv[1])
        integer2 = int(argv[3])
        operation = ops[argv[2]]
        result = ops(integer1, integer2)
        print('{:d} {:s} {:d} = {:d}'.format(integer1, argv[2], integer2, result))
    else:
        print('Unknown operator. Available operators: +, -, * and /')
        exit(1)
    exit(0)
