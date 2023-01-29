#!/bin/python
# Author : Mickey Cyberkid 
###########################

import math

gold_set = []
robbers = 13

# 1.Loop for the right number that when divided
# by 13 will give a remainder of 3
# 2. Save that number in a variable called gold

# Looping through for the right number
for gold in range(1,700):
     # The each_share variable here is the number of golds each
     # robber get
     each_share = gold//robbers
     # gold variable is the number of golds
     gold = gold
     # Check if the remainder is 3
     if gold%robbers == 3:
        # if so reduce the number of robbers
        # since there would be confusion
        # kick one robber out
        robbers -=1
        # Try to print the number of robbers left
        # It will surely be 12 at this time 
        print("\033[1;31mRobbers left : {0}".format(robbers))
        print("\033[1;36mTotal num of gold : {0} \n\033[1;34mEach one got : {1}".format(gold,each_share))
        # save the new number of golds to be shared 
        # (the number of golds the one who recentlt left
        # got plus the remaining gold[3])
        # in a variable called left_gold
        left_gold = each_share+3
        # Print it to the screen {not necessary}
        print("\033[1;36m{0} more golds to top up ".format(gold))
        # now check the remainder of the new golds to be shared
        if left_gold%robbers == 5:
           # save the new number of golds to be shared
           # (the number of golds the one who recentlt left
           # got plus the remaining gold[5])
           # in a variable called left_gold
           left_gold = left_gold+5
           # kick one robber out
           robbers -=1
           print("\033[1;31mRobbers left : {0}".format(robbers))
           print("\033[1;31mRobbers left : {0}".format(robbers))
           print("\033[1;34mGolds left is : {0}".format(left_gold))
           got_in_addition = left_gold//robbers+5
           print("Each got {0} in addition".format(got_in_addition))
           print("Total num of gold : {0} \nEach one got : {1}".format(left_gold,got_in_addition))
           if left_gold%robbers:
              remain = left_gold%robbers
              print("\033[1;32mRemaining golds : ",remain)
