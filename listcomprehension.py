# - assign a word (string)
words = "tacocat"

# - use list comprehennsion to compare first and last letter
if words[0] == words[-1]:
	# - if true:
	# 	- use list comprehension to exclude the first and last letter
	# 		- observe that a new string is created from the old string, excluding first and last
	print(words[1:-1])
	# 	- save a copy of the new string to the original variable
	words = words[1:-1]
print(len(words))

# put the above into a loop which ends when len(words) <= 1	