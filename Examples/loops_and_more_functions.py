# Loops and Functions

spam = 0

if spam < 5:
    print("in 'if' statement", spam)
    spam = spam + 1

while spam < 5: # Note how spam == 1 at start of loop
    print("in 'while' loop", spam)
    spam = spam + 1


x = "this could be anything"

while x != " ":
    print("Enter secret password to end annoyance")
    x = input()
    
print("Out of while loop")


while True: # Compare "True to random x variable
    print("What is 2 + 2?")
    answer = int(input())
    if answer == 4:
        break # When could this be used? (Show online compiler of cool program I did)
    
print("Out of loop")

import random, sys
# import sys
total = 0

for i in range(5):
    total = total + i # Compare to set integer
    print(total)
    if total > 3:
        sys.exit() # add this later, note code below doesn't work
                   # try break function, then observe below here
                   
print("Total = ", total)


import random

for x in range(0, 6, 2): # (start, stop, increment) note the start value included but not stop value
    print(random.randint(1, 10)) # prints random number between 1 and 10
    #print(x)



def try_example(divideby): # This is important to have in the back of your mind
    try:
        return 20 / divideby
    except ZeroDivisionError: # This is an error embedded in python, not imported
        print("Error: Invalid Argument")

print(try_example(2))
print(try_example(0))
print(try_example(5))
    








