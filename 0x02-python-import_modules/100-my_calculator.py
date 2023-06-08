#!/usr/bin/python3
    from sys import argv
    from calculator_1 import add, sub, mul, div
    def calculate_result(num1, operator, num2):
    if operator == '+':
        return add(num1, num2)
    elif operator == '-':
        return sub(num1, num2)
    elif operator == '*':
        return mul(num1, num2)
    elif operator == '/':
        if num2 == 0:
            raise ZeroDivisionError("Division by zero is not allowed.")
        return div(num1, num2)
    else:
        raise ValueError("Unknown operator. Available operators: +, -, * and /")
        
if __name__ == "__main__":
    if len(argv) != 4:
        print('Usage: {} <a> <operator> <b>'.format(argv[0]))
        exit(1)

    num1 = int(argv[1])
    operator = argv[2]
    num2 = int(argv[3])

    try:
        result = calculate_result(num1, operator, num2)
        print('{:d} {:s} {:d} = {:d}'.format(num1, operator, num2, result))
    except (ValueError, ZeroDivisionError) as e:
        print(str(e))
        exit(1)

    exit(0)
