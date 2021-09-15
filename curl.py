"""The python code helps to read the command line input for curl method."""
#sys is a module importing library Python Runtime Services#
# importing curl from helper library  
import sys
from lib.helper import curl
#URL is a variable assigned with null value
# ARG_CNT is a variable assigned with function len(sys.argv) minus integer one
URL = None
ARG_CNT = len(sys.argv) - 1
# If condition (ARG_CNT is a variable that is not equal to integer value  1) is true then it will print 'Usage: curl [URL]...'
if ARG_CNT != 1:
    print('Usage: curl [URL]...')

# If condition (ARG_CNT is a variable that is equal to integer value  1) is true then it will execute next step.
#sys.argv[1] gives the first argument on the command line
if ARG_CNT == 1:
    URL = sys.argv[1]
    if 'http' not in URL[:5]: # if http not in the given url then it will assign it 
        URL = "http://"+URL
    print(curl(URL))
# print the data present in that URL