# -*- coding: utf-8 -*-
"""
Created on Mon Sep 27 15:22:03 2021

@author: milan
"""

def fib_recursive(n): 
    if n <= 2:
        return 1
    else:
        return fib_recursive(n-1) + fib_recursive(n-2)
        
print("recursive formula result: ", fib_recursive(7))

def fib_efficient(n):
    a, b = 0, 1
    for i in range(n):
        a, b = b, a + b
    return a
    
print ("for-loop result: ", fib_efficient(7))