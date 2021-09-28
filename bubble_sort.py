# -*- coding: utf-8 -*-
"""
Created on Mon Sep 20 15:32:00 2021

@author: milan
"""

# Bubble SOrt

ages = [81, 100, 1, 9, 49, 64, 4, 9, 16, 25, 36]

#for all elements in list
ordered = []
for i in ages:
    for index, i in enumerate(ages):
        # compare
        # if larger: swap
        if  ages[index-1] > ages[index]:
            ages[index-1], ages[index] = ages[index], ages[index-1]
        else:
            continue
print(ages)
    # otherwise: do nothing