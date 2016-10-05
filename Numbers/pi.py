'''
Find PI to the Nth Digit - Enter a number and have the program generate PI 
up to that many decimal places. Keep a limit to how far the program will go.
'''

def arctan(x, one=1000000):
    """
    Calculate arctan(1/x)

    arctan(1/x) = 1/x - 1/3*x**3 + 1/5*x**5 - ... (x >= 1)

    This calculates it in fixed point, using the value for one passed in
    """
    power = one // x            # the +/- 1/x**n part of the term
    total = power               # the total so far
    x_squared = x * x           # precalculate x**2
    divisor = 1                 # the 1,3,5,7 part of the divisor
    while 1:
        power = - power // x_squared
        divisor += 2
        delta = power // divisor
        if delta == 0:
            break
        total += delta
    return total

# Calculate pi
def pi(one):
	return 4*(12*arctan(18, one) + 8*arctan(57, one) - 5*arctan(239, one))

pi = str(pi(10000000000000000000000000000000000000000000000000000000000000000))
pi = pi[:1] + "." + pi[1:] # adds the decimal point

def get_pi(digit):
	if digit <=0 or digit > 64:
		print "Your number must be greater than 0 and no more than 64."
		get_pi()
	else:
		print pi[:digit + 1]
		
get_pi(int(raw_input("How many digits of pi would you like?")))
