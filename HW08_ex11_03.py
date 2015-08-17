#!/usr/bin/env python
# Exercise 3  
# Dictionaries have a method called keys that returns the keys of the 
# dictionary, in no particular order, as a list.

# (1) Modify print_hist_old to print the keys and their values in alphabetical 
# order.

# (2) Paste in your completed functions from HW08_ex_11_02.py

# (3) Within main() make the appropriate function calls to print the
# alphabetical histogram of pledge.txt
##############################################################################

import re

def print_hist_old(h):
    for c in h:
        print c, h[c]


def print_hist_new(h):
	for c in sorted(h):
		print c, h[c]

##############################################################################
################### INSERT COMPLETED CODE FROM 11_02 BELOW: ##################
##############################################################################

def histogram_new(s):
    d = dict()
    for c in s:
        d[c] = d.get(c,0) + 1
    return d

def get_pledge_list():
    """ Opens pledge.txt and converts to a list, each item is a word in 
    the order it appears in the original file. returns the list.
    """
    # Your code here.
    pledge_list = []
    fin = open("pledge.txt", "r")
    text = fin.read()
    pledge_list = re.findall(r"[\w']+", text)
    fin.close()
    return pledge_list


##############################################################################
################### INSERT COMPLETED CODE FROM 11_02 ABOVE: ##################
##############################################################################
##############################################################################
def main():
    """ Calls print_hist_new with the appropriate arguments to print the 
    histogram of pledge.txt.
    """
    print_hist_new(histogram_new(get_pledge_list()))

if __name__ == '__main__':
    main()
