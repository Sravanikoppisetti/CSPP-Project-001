"""Implementing the tac shell command in python."""
#sys is a module importing library Python Runtime Services#
# importing tac from helper library  to read the file#
import sys
from lib.helper import tac, readfile
#Text is a variable assigned with null value
# ARG_CNT is a variable assigned with function len(sys.argv) minus integer one
TEXT = None
ARG_CNT = len(sys.argv) - 1
# If condition (ARG_CNT is a variable that is equal to zero) is true then it will execute sys.stdin.read()
# sys.stdin.read() will read from standard input using the sys module
#  And result will be assigned to a variable called TEXT
if ARG_CNT == 0:
    TEXT = sys.stdin.read()
# If condition (ARG_CNT is a variable that is equal to integer 1) is true then it will execute sys.argv[1] 
# sys.argv[1] gives the first argument on the command line
# And that result is assigned to filename variable
# Readfile function will read the filename and assigned it to TEXT variable
if ARG_CNT == 1:
    filename = sys.argv[1]
    TEXT = readfile(filename)
# If the  condition(ARG_CNT is greater than integer value 1) is true
#  Then it will print (sys.argv[0], "doesn't handle more than one argument")
# sys.argv[0] gives the name of the current Python script
if ARG_CNT > 1:
    print(sys.argv[0], "doesn't handle more than one argument")

print(tac(TEXT))
# print the output of tac function
# Prints each line of a file starting from the bottom line and finishing on the top line 
