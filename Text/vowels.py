'''
Count Vowels
Returns the total
number of vowels and
the amount of each.
'''

vowel_dict = {
"a" : 0,
"e" : 0,
"i" : 0,
"o" : 0,
"u" : 0
}

vowels = 0

def count(word):
    global vowel_dict, vowels
    for n in word:
        if n in vowel_dict:
            vowels += 1
            vowel_dict[n] += 1

def main():
    word = raw_input("Please enter your text. ")
    count(word)
    print "\nThere are %i vowels in '%s'. \n" % (vowels, word)
    for key in vowel_dict:
        if vowel_dict[key] > 0:
            print "%s: %i" % (key, vowel_dict[key])

if __name__ == '__main__':
    main()
