"""Implementing the cat shell command in python."""

#sys is a module importing library Python Runtime Services#
# importing cat from helper library  to read the file#
import sys
from lib.helper import cat, readfile
#Text is a variable assigned with null value#
TEXT = None
ARG_CNT = len(sys.argv) - 1
# ARG_CNT is a variable assigned with function len(sys.argv) minus integer one
# if condition (ARG_CNT is a variable that is equal to zero) is true then it will execute sys.stdin.read()
#  and assigned to a variable called TEXT
if ARG_CNT == 0:
    TEXT = sys.stdin.read()
# If condition (ARG_CNT is a variable that is equal to integer 1) is true then it will execute sys.argv[1] 
# and that is assigned to filename variable
if ARG_CNT == 1:
    filename = sys.argv[1]
    TEXT = readfile(filename)
# If the  condition(ARG_CNT is greater than integer value 1) is true 
# then it will print (sys.argv[0], "doesn't handle more than one argument")
# sys.argv[0] gives the name of the current Python script
if ARG_CNT > 1:
    print(sys.argv[0], "doesn't handle more than one argument")
# if condition(ARG_CNT >1) is true then it will print the argv[0]#
print(cat(TEXT))
#  print the output of cat function .
