"""The python code helps to read the command line input for curl method."""

import sys
from lib.helper import curl
#sys is a module importing library Python Runtime Services#
# importing curl from helper library 

URL = None
ARG_CNT = len(sys.argv) - 1
#URL is a variable assigned with null value
#sys.argv contains list of Command Line Arguments
#len(sys.argv) - it will find length of sys.argv
# ARG_CNT is a variable assigned with function len(sys.argv) minus integer one

if ARG_CNT != 1:
    print('Usage: curl [URL]...')
# If condition (ARG_CNT is a variable that is not equal to integer value  1) is true then it will print 'Usage: curl [URL]...'

if ARG_CNT == 1:
    URL = sys.argv[1]
    if 'http' not in URL[:5]: # if http not in the given url then it will assign it 
        URL = "http://"+URL
    print(curl(URL))
# If the condition (ARG_CNT is a variable that is equal to integer value  1) is true then it will execute the next step.
# sys.argv[1] gives the first argument on the command line
# if http not in the given url then it will assign it 
# print the data present in that URL

