'''
Reverse a String
Enter a string and 
the program will reverse
it and print it out.
'''

def reverse(word):
    return word[::-1]

def main():
    word = raw_input("Please enter a string to reverse. ")
    print reverse(word)

if __name__ == '__main__':
    main()
