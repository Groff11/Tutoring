#random_words = ['tacocat','eye','fire','kayak','racecar']
#while (len(random_words) > 0):
#	print (random_words)
#	random_words.pop()
def help():
	all_words = ["Merlin","tacocat","racecar","lol","leg"]
	while len(all_words) > 0:
		Palindrome = (1)
		word = list(all_words[0])#["M" "e" "r" "l" "i" "n"] Create A List Of Characters From #1 of All_Words
		while len(word) > 1:
			first = word[0]
			last = word[len(word)-1]
			if first != last:
				Palindrome = (0)
				break
			else:
				Palindrome = (1)
				del word[0]
				word.pop()
		del all_words[0]
		if Palindrome == (1):
			print ("This Is A Palindrome")
		else:
			print ("This Is Not A Palindrome")
help()
input()