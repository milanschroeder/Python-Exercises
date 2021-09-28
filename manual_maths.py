# -*- coding: utf-8 -*-
"""
Created on Mon Sep 20 14:18:55 2021

@author: milan
"""

population_ages = [81, 100, 1, 9, 49, 64, 4, 9, 16, 25, 36]

# w/o packages
# mean

addedup = 0
for i in population_ages:
    addedup += i
    mean = addedup/len(population_ages)
print ("mean = ", mean, end="\n\n")


# only works if one mode, else override
mode = []
modecount = 0
for i in population_ages:
    modecount = max(population_ages.count(i), modecount)
for i in population_ages:
    if population_ages.count(i) == modecount and i not in mode:
        mode.append(i)
print("mode = ", mode, end="\n\n")


# median
population_ages.sort()
print("ordered sequences: ",population_ages, end="\n\n")
# even number:
if len(population_ages) % 2:
   medpos_high = int(len(population_ages)/2)
   high = population_ages[medpos_high]
   medpos_low = int(len(population_ages)/2) - 1
   low = population_ages[medpos_low]
   median = (high + low)/2
   print("median = ", median, end="\n\n")
# odd number
else:
   medpos = int(len(population_ages)/2+1)
   median = population_ages[medpos]                
   print("median = ", median, end="\n\n")
    