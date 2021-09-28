# -*- coding: utf-8 -*-
"""
Created on Mon Sep 13 14:59:11 2021

@author: milan
"""

n = input("Counts to from 1 to a selected (full) number, but replaces multiples of 3 with Fizz, and those of 5 with Buzz (and multiples of both with FizzBuzz). Select a number:\n\n")
while n:
    if n.isdigit():
        n = int(n)
    else:
        n = 100
        print("\nInvalid input. selected number set to 100 by default:\n")
        
    string = ""
    for i in range(1, n+1):
        if i % 3 == 0:
            string += "Fizz"
        if i % 5 == 0:
            string += "Buzz"
        if i % 3 != 0 and i % 5 != 0:
            string += str(i)
        if i < n: 
            string += ", "
    print(string)
    
    n = None
    n = input("\n\nPress Enter to close or enter another (full) number to repeat: ")