from random import randint

answer = str(randint(1000, 10000))

def game(num):
	correct = 0
	i = 0
	while i < 4:
		if len(num) != 4:
			break
		
		if num[i] == answer[i]:
			correct += 1
		i += 1
	print "*" * correct
		
def main():
	print "Try to guess the 4-digit number.\nThe number of correct numbers will be printed."
	tries = 0
	
	while True:
		num = str(raw_input())
		tries +=1
		game(num)
		
		if num == answer:
			print "It took you %i tries." % tries
			break
		
main()
