import re

pattern = re.compile("\d+[+\-*\/\^]\d+")

equation = raw_input("What would you like to calculate?")

while True:
    if pattern.match(equation):
        break

    print "Not a valid input."


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
    print int(equation[0]) / int(equation[1])

elif "^" in equation:
    equation = equation.split("^")
    print int(equation[0]) ** int(equation[1])
