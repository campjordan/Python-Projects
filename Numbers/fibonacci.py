'''
Fibonacci Sequence
Enter a number and have the program 
generate the Fibonacci sequence to that 
number or to the Nth number.
'''

def get_fib(n):
    sequence = [0, 1]    # gives the sequence the first two numbers
    n = int(n)
    if n < 1:    # checks the value of the number
        print "Your number must be at least 1."
        n = int(raw_input("Please enter a new number."))    # if number is too small, give new one
        get_fib(n)
    else:
        while len(sequence) < n:
            sequence.append(sequence[len(sequence) - 1] + sequence[len(sequence) - 2])    # adds the last 2 digits
            																			                                        # and appends the sum
        else:
            print sequence    # prints the sequence when the sequence is long enough

get_fib(int(raw_input("Please enter how many numbers you would like.")))
