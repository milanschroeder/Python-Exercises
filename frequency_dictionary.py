# -*- coding: utf-8 -*-
"""
Created on Mon Sep 20 15:19:41 2021

@author: milan
"""

# read user input
text = input("Sentence, please: ")

# turn string into list

words = text.lower().split(" ") # make it lowercase and split by spaces
print(words)

# count of each element frequency
# ... and store as dictionary
freq = {}
for word in words:
    freq[word] = words.count(word)
print(freq)


