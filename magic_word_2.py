#!/usr/bin/env python
import sys, getopt

# Defining Python Command Line Arguments
def main(argv):
	wildcard_word = ''
	proper_word = ''

	# Getting command line argument
	try:
		opts, args = getopt.getopt(argv,"hw:p:",["wword=","pword="])
	except getopt.GetoptError:
		print 'usage : python %s -w <wildcard word> -p <proper word>'%(__file__)
		sys.exit(2)

	# Iterating command line argument
	for opt, arg in opts:
		# Help Text
		if opt == '-h':
			print 'usage : python %s -w <wildcard word> -p <proper word>'%(__file__)
			sys.exit()
		# Wildcard Word Text
		elif opt in ("-w", "--wword"):
			wildcard_word = arg
		# Proper Word Text
		elif opt in ("-p", "--pword"):
			proper_word = arg

	if wildcard_word == "" or proper_word == "":
		print 'usage : python %s -w <wildcard word> -p <proper word>'%(__file__)
		sys.exit()
	else:
		print 'Wildcard Word:', wildcard_word
		print 'Proper Word:', proper_word
		print wildcard(wildcard_word, proper_word)

# Defining wild card function
import fnmatch
def wildcard(wildcard_word, proper_word):
	wc = wildcard_word
	word = [proper_word]
	matches = fnmatch.filter(word, wc)
	if matches != []:
		msg = "Yes, '%s' can be created."%(proper_word)
	else:
		msg = "No, '%s' can not be created."%(proper_word)
	return msg

if __name__ == "__main__":
   main(sys.argv[1:])