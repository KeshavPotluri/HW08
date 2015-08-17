#!/usr/bin/env python
# Exercise 1  
# Write a function that reads the words in words.txt and stores them as keys
# in a dictionary (returning the dictionary). It doesn't matter what the 
# values are. Then you can use the in operator as a fast way to check whether
# a string is in the dictionary.
##############################################################################

def store_to_dict():
    fin = open("words.txt", "r")
    dictionary = {}
    count = 0
    for line in fin:
    	dictionary[line.strip()] = count
    	count+=1 
    fin.close()
    return dictionary



##############################################################################
def main():  # DO NOT CHANGE BELOW
    words_dict = store_to_dict()
    if "this" in words_dict:
        print "Yup."
    if "qwertyuiop" in words_dict:
        print "Hmm."

if __name__ == '__main__':
    main()
