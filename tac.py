"""Implementing the tac shell command in python."""

import sys
from lib.helper import tac, readfile
#sys is a module in library Python Runtime Services
# importing tac, readfile  from helper library 
TEXT = None
ARG_CNT = len(sys.argv) - 1
#TEXT is a variable assigned with null value
#sys.argv contains list of Command Line Arguments
#len(sys.argv) - it will find length of sys.argv
# ARG_CNT is a variable assigned with function len(sys.argv) minus integer one
if ARG_CNT == 0:
    TEXT = sys.stdin.read()
# If the condition (ARG_CNT is a variable that is equal to zero) is true then it will execute sys.stdin.read()
# sys.stdin.read() will read the input provided in command line
#  And then it will assigned to a variable called TEXT
if ARG_CNT == 1:
    filename = sys.argv[1]
    TEXT = readfile(filename)
# If condition (ARG_CNT is a variable that is equal to integer 1) is true then it will execute sys.argv[1] 
#  sys.argv[1] gives the first argument on the command line
#  and that is assigned to filename variable
#  readfile function will read the file and store in variable called TEXT
if ARG_CNT > 1:
    print(sys.argv[0], "doesn't handle more than one argument")
# If the  condition(ARG_CNT is greater than integer value 1) is true
#  Then it will print (sys.argv[0], "doesn't handle more than one argument")
#  sys.argv[0] gives the name of the current Python script
print(tac(TEXT))
# print the output of tac function
# Prints each line of a file starting from the bottom line and finishing on the top line 
