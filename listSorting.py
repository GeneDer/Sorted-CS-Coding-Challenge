#!/usr/bin/python

import sys

def my_list_sort(l):
    """
    This function should take in an unsorted list,
    remove unwanted characters, and return sorted words
    and numbers as an list. 
    """
    pass

def read_file(path):
    """
    This function should read the file and convert
    it to the a list. File might be empty!
    """
    try:
        with open(path, 'r') as f:
            return f.readline().split()
    except:
        print "No file found at", path
        sys.exit()
        
if __name__ == "__main__":
    args = sys.argv
    if len(args) < 3:
        print "Not enough argument!"
        sys.exit()
    input_file = args[1]
    output_file = args[2]

    print read_file(input_file)
    print read_file("input/empty.txt")
