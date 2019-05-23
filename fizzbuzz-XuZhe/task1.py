import string
punctuation =string.punctuation

def textcode():
	filename = input("Please tell me the filename:")
	pagenumber = int(input("Please tel me the pagenumber:"))
	fin = open(filename,'r')
	linenumber = pagenumber * 25
	print("line number is:",linenumber)
	count1 = 0
	count2 = 0
	count3 = 0
	for i in range(linenumber):
		line = fin.readline()
		for word in line.split():
			word = word.strip(punctuation)
			count3 += 1
			if word[-2:] == 'er':
				word = word[:-2] + 'xor'
			word1 = list(word)
			for element in word1:
				if element.isdigit():
					count1 += 1
				else:
					count2 += 1
			for index in range(len(word1)):
				if word1[index] == 'o' or word1[index] == 'O':
					word1[index] = '0'
				elif word1[index] == 'a' or word1[index] == 'A':
                               	        word1[index] = '4'
				elif word1[index] == 'e' or word1[index] == 'E': 
					word1[index] = '3'
				elif word1[index] == 'i' or word1[index] == 'I':
					word1[index] = '1'
					word = ''.join(word1)
					print(word)
	print("the word number is:",count3)
	print("the alphabetic characters number is:",count2)
	print("the digit number is:",count1)

textcode()
