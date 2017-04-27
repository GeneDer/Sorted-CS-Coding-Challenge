#!/usr/bin/python

import sys
import re


def my_list_sort(l):
    """
    This function should take in an unsorted list,
    remove unwanted characters, and return sorted words
    and numbers as an list. 
    """
    is_num = []
    nums = []
    words = []
    pattern = re.compile("[^A-Za-z0-9]")
    for i in l:
        s = pattern.sub("", i)
        try:
            nums.append(int(s))
            is_num.append(True)
        except:
            words.append(s)
            is_num.append(False)

    print is_num, nums, words

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

    list2sort = read_file(input_file)
    
    print my_list_sort(list2sort)
