'''
Calculator
A simple calculator to
do simple operators.
'''

def calc(a, b, op):

    if op == "+":
        return a + b
    if op == "-":
        return a - b
    if op == "*":
        return a * b
    if op == "/":
        return a / b

def main():
    while True:
        a = raw_input("Please enter the first number. ")
        op = raw_input("Please enter the operator. Use either +, -, *, or /. ")
        b = raw_input("Please enter the second number. ")

        if a.isdigit() and op in "+-*/" and b.isdigit():
            break

    print calc(float(a), op, float(b))

if __name__ == '__main__':
    main()
