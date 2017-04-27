#!/usr/bin/python

import sys
import re

def write_file(l, path):
    """
    This function will convert the list into a
    string and write to the file.
    """
    s = " ".join(l)
    try:
        with open(path, 'w') as o:
            o.write(s)
    except:
        print "incorrect output path at", path
        sys.exit()
        

def my_list_sort(l):
    """
    This function should take in an unsorted list,
    remove unwanted characters, and return sorted words
    and numbers as an list. 
    """
    is_num = []
    nums = []
    words = []
    pattern = re.compile("[^A-Za-z0-9-]")
    for i in l:
        s = pattern.sub("", i)
        try:
            nums.append(int(s))
            is_num.append(True)
        except:
            words.append(s.replace("", "-"))
            is_num.append(False)

    nums.sort(reverse=True)
    words.sort(reverse=True)

    result = []
    for i in is_num:
        if i:
            result.append(str(nums.pop()))
        else:
            result.append(words.pop())
    return result

def read_file(path):
    """
    This function should read the file and convert
    it to the a list. File might be empty!
    """
    try:
        with open(path, 'r') as f:
            return f.readline().split()
    except:
        print "No input file found at", path
        sys.exit()
        
if __name__ == "__main__":
    args = sys.argv
    if len(args) < 3:
        print "Not enough argument!"
        sys.exit()
    input_file = args[1]
    output_file = args[2]

    list2sort = read_file(input_file)
    sorted_list = my_list_sort(list2sort)
    write_file(sorted_list, output_file)    
