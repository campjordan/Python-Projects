'''
Factorial Finder
Finds the factorial
of a positive integer.
'''

def factorial(num):
	if num == 0 or num == 1:
		return 1
	else:
		i = 1
		result = num
		while i < num:
			result *= num - i
			i += 1
		return result

def main():
    num = int(raw_input("Please enter a number. "))
    print factorial(num)

if __name__ == '__main__':
    main()
