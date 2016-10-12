'''
Coin Flip Simulation 
Write some code that simulates flipping
a single coin however many times the user decides.
The code should record the outcomes and count the 
number of tails and heads.
'''

from random import randint

def flip():
    result = randint(0, 2)
    if result == 1:
        return True
    else:
        return False

def main():
    while True:
        times = raw_input("How many times would you like to flip the coin?")
        if times.isdigit():
            break
    heads = 0
    tails = 0
    for i in range(int(times)):
        if flip():
            heads += 1
        else:
            tails += 1
    print "The number of heads is %i." % heads
    print "The number of tails is %i." % tails

main()
