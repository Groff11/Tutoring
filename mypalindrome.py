# return True if palindrome, False if not
def help(word=''):
	first_word = word
	empty_string = ''
	while first_word != empty_string: # boolean expression - expression of True or False
		palindrome = 1 # don't know what this does yet
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
			return True
		else:
			return False
help("makem")
help("hannah")
help("dog")