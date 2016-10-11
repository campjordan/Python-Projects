'''
Binary to Decimal and Back Converter
Develop a converter to convert a decimal number to 
binary or a binary number to its decimal equivalent.
'''

n = ""

def get_number():
    global n
    n = str(raw_input("Please enter the number you want to convert."))
    if not n.isdigit():
        print "Please input a number."
        get_number()

get_number()

def convert():
    global n
    mode = raw_input("Type b or d to convert to binary or decimal.")
    if mode not in "bd":
        print "Please enter either b or d."
        convert()
    elif mode == "b":
        n = bin(int(n))[2:]
        print n
    else:
        for i in n:
            if i not in "10":
                print "This number is not binary!"
                get_number()
                convert()
                break
        else:
            n = int(n, 2)
            print n
                        
convert()
