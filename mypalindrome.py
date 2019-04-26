# rewrite this function so it takes a string argument
# determine if that string is a palindrome
# return True if palindrome, False if not
def help():
	all_words = ["makem","tacocat","racecar","lol","leg"]
	while len(all_words) > 0:
		first_word = list(all_words[0])
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
			first_word = "".join(str(x) for x in first_word)
			print ("{0} is a palindrome".format(first_word))
			return "{0} is a palindrome".format(first_word)
		else:
			first_word = "".join(str(x) for x in first_word)
			print ("{0} is not a palindrome".format(first_word))
help()