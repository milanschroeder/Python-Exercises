# -*- coding: utf-8 -*-
"""
Created on Mon Sep 13 15:31:06 2021

@author: milan
"""

# A Game of Nim
## version 1.0: (randomly) silly opponent

import random
sticks = 12

print("The game Nim starts out with", sticks, "sticks on the table. Each player takes turns picking up 1, 2 or 3 sticks and cannot pass. Whoever picks up the last stick wins.")

# who start's: Head or tail
headTail = input("First we need to determine who starts. So head or tail? \n")
head = headTail
while not head == 1 or head ==2:
    if headTail.lower() == "tail": 
        head = 1
    elif headTail.lower() == "head": 
        head = 2
    else: 
        headTail = input("I'll ask you again: HEAD or TAIL \n")

random = random.randint(1,2)
if random == head:
    print("It's", headTail + "! \nLucky you!")
else: 
    # if opponent starts
    print("It's", headTail + "\nSo the GREAT INTELLIGENCE starts!")
    pc = random.randint(1,3)
    sticks -= pc 
    print("The GREAT INTELLIGENCE picks", pc, end = " \n")
    if sticks > 0:
        print(sticks, "left \nNow it's your turn!")

while sticks > 0:
    #if player starts
    turn = int(input("How many sticks do you take? \n"))
    if 0 < turn < 4:
        print("\nYou draw", turn, end = " \n")
        sticks -= turn
    else:
        print("\nThat's not a valid number. You can pick either 1, 2, or 3.'  \n")
        continue
    if sticks > 0:
        print(sticks, "left \n")
    else :
        print("\nThere are no more sticks. \n\nYOU WIN")
        break
    
    pc = random.randint(1,3)
    sticks -= pc 
    print("\nThe GREAT INTELLIGENCE picks", pc, end = " \n\n")
    if sticks > 0:
        print(sticks, "left \n")
    else:
        print("\nThere are no more sticks. \n\nThe GREAT INTELLIGENCE WINS")
        break
    

input("\n\nPress Enter to close")