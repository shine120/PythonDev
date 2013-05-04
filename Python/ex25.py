def break_words(stuff):
	"""This fuction will break up words for us."""
	words = stuff.split(' ')
	return words

def sort_words(words):
	"""Sorts the World."""
	return sorted(words)

def print_first_word(words):
	"""Print the first word after poping it off"""
	word = words.pop(0)
	return word

def print_last_word():
	"""Print the first word after poping it off"""
	word = words.pop(-1)
	return word

def sort_sentence(sentence):
	words = break_words(sentence)
	return sort_words(words)


def print_first_and_last(sentence):
	words = break_words(sentence)
	print_first_word(words)
	print_last_word(words)

def print_first_and_last_sorted(sentence):
	words = sort_sentence(sentence)
	print_first_word(words)
	print_last_word(words)