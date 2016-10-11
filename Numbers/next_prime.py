'''
Next Prime Number
Generate prime numbers until
the user chooses to stop.
'''

def is_prime(n):
    if n == 2:
        return True

    i = 2
    while i < n:
        if n % i == 0:
            return False
            break
        else:
            i += 1
    else:
        return True

def gen_next_prime(current):
    i = current + 1
    while not is_prime(i):
        i += 1
    else:
        return i

def main():
    current = 2
    print current

    while True:
        choice = raw_input("Would you like to generate a new prime number? (y/n)")
        if choice.lower() == "y":
            current = gen_next_prime(current)
            print current
        else:
            break

if __name__ == '__main__':
    main()
