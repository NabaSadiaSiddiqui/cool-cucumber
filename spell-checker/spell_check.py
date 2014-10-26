#!/usr/bin/python

import sys

"""
	Reads from /usr/share/dict/words
	Checks validity of user-entered word
"""

if len(sys.argv) != 2:
	raise SyntaxError("This program takes a single word from commandline")


"""
	words is a standard Unix file which contains a newline-delimited
	list of dictionary words
"""
word = sys.argv[1]
src = '/usr/share/dict/words'
f = open(src, 'r')
_dict = f.read().split("\n")
res = "valid" if word in _dict else "invalid"

msg = "The word '" + word + "' is " + res

print msg
