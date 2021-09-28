# -*- coding: utf-8 -*-
"""
Created on Mon Sep 13 14:39:11 2021

@author: milan
"""

print("This Programm sums up all numbers from 0 to a (full) number you enter. Try it!")

num = int(input("enter number: "))
if num < 0:
    print("number must be positive")
elif num > 0:
    sum = 0 
    for i in range(1, num+1):
        sum += i
    print(sum)
else: 
    print("Unexpected Error. Please Contact my Creator")



print("\n\nThis does the same, but more elegant (what you can not see, of course) \n")
# faster: Gaußsche Summenformel
num = int(input("give me another number: "))
if num < 0:
    print("If you don't enter a valid number, we better end this now...")
elif num > 0:
    print(int((num**2+num)/2))
else: 
    print("Unexpected Error. Please Contact the Creator")


input("\n\nPress Enter to close")