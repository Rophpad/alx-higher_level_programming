#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    import sys
    ops = len(sys.argv) - 1
    if (ops == 3):
        a = int(sys.argv[1])
        b = int(sys.argv[3])
        operator = sys.argv[2]
        if (operator == '+'):
            print("{} {} {} = {}".format(a, operator, b, add(a, b)))
        elif (operator == '-'):
            print("{} {} {} = {}".format(a, operator, b, sub(a, b)))
        elif (operator == '*'):
            print("{} {} {} = {}".format(a, operator, b, mul(a, b)))
        elif (operator == "/"):
            print("{} {} {} = {}".format(a, operator, b, div(a, b)))
        else:
            print("Unknown operator. Available operators: +, -, * and /")
            sys.exit(1)
    else:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)
