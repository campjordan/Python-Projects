import re

pattern = re.compile("\d+[+\-*\/\^]\d+")

while True:
    equation = raw_input("What would you like to calculate?\n")
    if pattern.match(equation):
        break
    else:
        print "Not a valid input.\n"


if "+" in equation:
    equation = equation.split("+")
    print int(equation[0]) + int(equation[1])
    
elif "-" in equation:
    equation = equation.split("-")
    print int(equation[0]) - int(equation[1])
    
elif "*" in equation:
    equation = equation.split("*")
    print int(equation[0]) * int(equation[1])
    
elif "/" in equation:
    equation =equation.split("/")
    print float(equation[0]) / float(equation[1])

elif "^" in equation:
    equation = equation.split("^")
    print int(equation[0]) ** int(equation[1])
