#!/usr/bin/env python
import sys, getopt

# Defining Python Command Line Arguments
def main(argv):
	jumbled_word = ''
	proper_word = ''

	# Getting command line argument
	try:
		opts, args = getopt.getopt(argv,"hj:p:",["jword=","pword="])
	except getopt.GetoptError:
		print 'usage : python %s -j <jumbled word> -p <proper word>'%(__file__)
		sys.exit(2)

	# Iterating command line argument
	for opt, arg in opts:
		# Help Text
		if opt == '-h':
			print 'usage : python %s -j <jumbled word> -p <proper word>'%(__file__)
			sys.exit()
		# Jumbled Word Text
		elif opt in ("-j", "--jword"):
			jumbled_word = arg
		# Proper Word Text
		elif opt in ("-p", "--pword"):
			proper_word = arg

	if jumbled_word == "" or proper_word == "":
		print 'usage : python %s -j <jumbled word> -p <proper word>'%(__file__)
		sys.exit()
	else:
		print 'Jumbled Word:', jumbled_word
		print 'Proper Word:', proper_word
		print magic(jumbled_word, proper_word)

# Defining Magic Function
from collections import Counter
def magic(jumbled_word, proper_word):
	if not Counter(proper_word) - Counter(jumbled_word):
		msg = "Yes, '%s' can be created."%(proper_word)
	else:
		msg = "No, '%s' can not be created."%(proper_word)
	return msg

if __name__ == "__main__":
   main(sys.argv[1:])