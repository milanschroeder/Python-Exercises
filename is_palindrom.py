# -*- coding: utf-8 -*-
"""
Created on Mon Sep 27 14:40:01 2021

@author: milan
"""


def is_palindrom(text):
    """ tests if string is a palindrom?"""
    
    
    original = text.lower()[:]
    desrever = original[::-1]
    
    # could also try for-loop
    
    if original == desrever:
        return True
    else:
        return False

print(is_palindrom("A man, a plan, a canal: Panama"))
print(is_palindrom("Saippuakivikauppias"))

input("\n\nPress Enter to close")