'''
Problem: Just like the previous problem, but with e instead of Pi.
Enter a number and have the program generate e up to that many decimal places.
Keep a limit to how far the program will go.
'''

from math import e

e = str(e)    # makes e a string so it can be indexed

decimal = int(raw_input("How many decimal places of e would you like?"))	# gets the decimal number as an int

while decimal > 11 or decimal <= 0:    #checks that the decimal is within parameters
	decimal = int(raw_input("Your number must be no more than 11 and greater than 0. Please insert a new number."))    # gets new number
else:
	print e[:decimal + 2]    # prints e to decimal + 2 to account for the "2."
