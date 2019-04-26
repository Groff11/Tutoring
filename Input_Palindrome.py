#Why is this here?
def help():
	all_words = (input)
	while len(all_words) > 0:
		first_word = (all_words[0])
		Palindrome = (1)
		word = (all_words[0])#["M" "e" "r" "l" "i" "n"] Create A List Of Characters From #1 of All_Words
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
			print ("{0} Is A Palindrome".format(first_word))
		else:
			first_word = "".join(str(x) for x in first_word)
			print ("{0} Is Not A Palindrome".format(first_word))
help()
input()