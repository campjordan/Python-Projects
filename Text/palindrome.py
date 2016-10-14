'''
Palindrome Checker
Checks if a string
entered by a user is
a palindrome.
'''

def check_palindrome(word):
    if word == word[::-1]:
        return True
    else:
        return False

def main():
    word = raw_input("Please enter a string. ")
    if check_palindrome(word):
        print "%s is a palindrome." % word
    else:
        print "%s is not a palindome. The reverse of %s is %s." % (word, word, word[::-1])

if __name__ == '__main__':
    main()
