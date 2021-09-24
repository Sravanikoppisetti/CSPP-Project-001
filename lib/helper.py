"""Implementing the helper functions in python."""

import sys
import requests

def curl(url):
    """
        url will be passed as parameter to the wget function
        if given url is valid, function will download the content from url
        downloaded content will be written into file index.html
    """
    try:
        response = requests.get(url)
        return response.text
    except:
        return "curl: unable to resolve host address " + url

def cat(text):
    """
        Implementing the cat command functionality by defining a function
    """
    result = ""
    # result variable is assigned with empty string
    lines = text.splitlines()
    #Text file is splitted line wise and stored in variable called lines.
    
    for i in range(len(lines)):
     # after splitting lines , length of each lines is find using length function 
     #length of lines assigned as stopping condition for range.
    
        result += lines[i] + "\n"
      # list containing lines is appended to result variable one after another.
      
    return result[:-1]
       #result[:-1]- will exclude last element in list i.e \n
      # return function will return the result and display it when you call that function



def tac(text):
    """
        Implementing the tac command functionality by defining a function
    """
    result = ""
    # result variable is assigned with empty string
    lines = text.splitlines()
    #Text file is splitted line wise and stored in variable called lines.
    for i in range(len(lines)-1, -1, -1):
        # after splitting lines , length of each lines is find using length function 
     #(length of lines-1 is assigned as start condition),(stop condition as-1) and (step by -1) for the above range.

        result += lines[i] + "\n"
         # list containing lines is appended to result variable one after another.
    return result[:-1]
     #result[:-1]- will exclude last element in list i.e \n
      # return function will return the result and display it when you call that function




def tail(text, n_lines=10):
    """
        Implementing the tail command functionality by defining a function
    """
    if text:
        lines = text.splitlines()
        lines = lines[-n_lines:]
        return "\n".join(lines)
    return None

def head(text, n_lines=10):
    """
        Implementing the head command functionality by defining a function
    """
    if text:
        lines = text.splitlines()
        lines = lines[:n_lines]
        return "\n".join(lines)
    return None

def wc(text):
    """
        will create a function of wc which takes text(i.e., content of the entire file)
        as a parameter
    """
    word_count = word_counts(text)
    char_count = char_counts(text)
    line_count = line_counts(text)
    byte_count = byte_counts(text)
    return [line_count, word_count, byte_count, char_count]

def word_counts(text):
    """
        returns the count of words a given file
    """
    list_of_words = text.split()
    return len(list_of_words)

def line_counts(text):
    """
        returns the count of lines a given file
    """
    list_of_lines = text.split("\n")
    return len(list_of_lines) - 1

def char_counts(text):
    """
        returns the count of character a given file
    """
    return len(text)

def byte_counts(text):
    """
        returns the count of bytes a given file
    """
    return len(text.encode('utf-8'))


def is_valid_file():
    """
        Check the file validations
    """
    try:
        file = open(sys.argv[-1], "r")
        file.close()
        return True
    except:
        print("cut: "+sys.argv[-1]+": No such file or directory")
        return False

def readfile(filename):
    """
        Reading the contents of a given file
    """
    try:
        file = open(filename)
        text = file.read()
        return text
    except FileNotFoundError:
        print("tail: cannot open", filename, "for reading: No such file or directory")
