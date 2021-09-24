"""Implementing the wc shell command in python."""
import sys

from lib.helper import wc, readfile
#sys is a module in library Python Runtime Services
# importing  wc, readfile  from helper library 

TEXT = None
ARG_CNT = len(sys.argv) - 1
#text is a variable assigned with null value
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
response = wc(TEXT)
#we are creating response variable and saving function wc which will return the value which has an argument text
print(" " + str(response[0]) + "  " + str(response[1]) + " " + str(response[2]))
#print the  string responses by concatenating  with space.
