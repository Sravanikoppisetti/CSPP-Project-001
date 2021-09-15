"""Implementing the wc shell command in python."""
#sys is a module importing library Python Runtime Services#
# importing wc from helper library  to read the file#
import sys

from lib.helper import wc, readfile
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
response = wc(TEXT)
#we are creating response variable and saving function wc which will return the value which has an argument text
print(" " + str(response[0]) + "  " + str(response[1]) + " " + str(response[2]))
#print the  string responses by concatenating  with space.
