'''
Tax Calculator
Asks the user to enter a cost
and either a country or state 
tax. It then returns the tax 
plus the total cost with tax.
'''

calc = lambda c, t: c * (1 + (t / 100.0))

def main():
    c = float(raw_input("Please enter the cost. "))
    t = int(raw_input("Please enter the tax rate as a percentage. "))
    print "The total cost of a $%.2f purchase with a %i%% tax rate is $%.2f." % (c, t, calc(c, t))

if __name__ == '__main__':
    main()
