#!/usr/bin/env python
import sys, getopt

# Defining Python Command Line Arguments
def main(argv):
	jumbled_word = ''

	# Getting command line argument
	try:
		opts, args = getopt.getopt(argv,"hj:",["jword="])
	except getopt.GetoptError:
		print 'usage : python %s -j <jumbled word>'%(__file__)
		sys.exit(2)

	# Iterating command line argument
	for opt, arg in opts:
		# Help Text
		if opt == '-h':
			print 'usage : python %s -j <jumbled word>'%(__file__)
			sys.exit()
		# Jumbled Word Text
		elif opt in ("-j", "--jword"):
			jumbled_word = arg

	if jumbled_word == "":
		print 'usage : python %s -j <jumbled word>'%(__file__)
		sys.exit()
	else:
		print 'Jumbled Word:', jumbled_word
		print longest(jumbled_word)

# Defining longest Function
from collections import Counter
def longest(jumbled_word):
	words = open('enable1.txt','r').read().split('\r\n')
	target = jumbled_word
	match_list = [word for word in words if not Counter(word) - Counter(target)]
	try:
		longest_word = max(match_list, key=len)
		return longest_word
	except ValueError:
		return "No matches found!"

if __name__ == "__main__":
   main(sys.argv[1:])