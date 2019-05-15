# return True if palindrome, False if not
def help(word=''):
	first_word = word
	empty_string = ''
	while first_word != empty_string: # boolean expression - expression of True or False
		palindrome = 1
		while len(first_word) > 1:
			first = first_word[0]
			last = first_word[len(first_word)-1]
			if first != last:
				palindrome = 0
				break
			else:
				palindrome = 1
				del first_word (0)
				first_word.pop()
		first_word = empty_string
		if palindrome == 1:
			first_word = "".join(str(x) for x in first_word)
			print ("{0} is a palindrome".format(first_word))
			return content, status.HTTP_200_OK
		else:
			first_word = "".join(str(x) for x in first_word)
			print ("{0} is not a palindrome".format(first_word))
			return content, status.HTTP_406_NOT_ACCEPTABLE
help("makem")
help("hannah")
help("dog")