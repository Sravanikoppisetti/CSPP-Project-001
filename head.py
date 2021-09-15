"""Implementing the head shell command in python."""
#sys is a module importing library Python Runtime Services#
# importing head from helper library  to read the file#
import sys
from lib.helper import head, readfile
#text is a variable assigned with null value#
TEXT = None
ARG_CNT = len(sys.argv) - 1
# ARG_CNT is a variable assigned with function len(sys.argv) minus integer one
# If condition (ARG_CNT is a variable that is equal to zero) is true then it will execute sys.stdin.read()
# sys.stdin.read() will read from standard input using the sys module
#  and result will be assigned to a variable called TEXT
if ARG_CNT == 0:
    TEXT = sys.stdin.read()
# If condition (ARG_CNT is a variable that is equal to integer 1) is true then it will execute sys.argv[1] 
# sys.argv[1] gives the first argument on the command line
# And that result is assigned to filename variable
# Readfile function will read the filename and assigned it to TEXT variable
if ARG_CNT == 1:
    filename = sys.argv[1]
    TEXT = readfile(filename)
# If the  condition(ARG_CNT is greater than integer value 1) is true then it will print "Usage: head.py <file>"
if ARG_CNT > 1:
    print("Usage: head.py <file>")

print(head(TEXT))
# print the output of head function
#print the top 10 lines of the file 