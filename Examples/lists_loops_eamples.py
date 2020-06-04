# -*- coding: utf-8 -*-
"""
Created on Wed Jun  3 16:02:43 2020

@author: Ben

This covers the rest of lists, dictionaries, and explores loops some more

"""

food = ["hotdog", "milk", "fries"]
#food = ["hotdog", "milk"] # This is why you don't give variables the same name
print(len(food)) # Equals number of entries in list

#food[1] = food[2]
food[2] = food[0]
print(food)

del food[2]
print(food)

for i in range(4): # Note how this loop and the loop below have same output
    print(i)

for i in [0, 1, 2, 3]:
    print(i)
    

fake_sports = ["soccer", "croquet", "footsie"]

for i in range(len(fake_sports)): # This is a common way to iterate over lists
    print("Index " + str(i) + " in fake_sports is " + fake_sports[i]) # Note the error message w/o str(i)
    
if "milk" in food:# Compare with 'not in' statement
    print("That is true!")
else:
    print("it's not true :(")
    
    

toolstuff = ["hammer", "wrench", "nails", "screw"]
print(toolstuff.index("wrench"))
toolstuff.append("wood pencil") # COuld also pass an integer to it (also .remove function which is same as del)
print(toolstuff)
toolstuff.sort()
print(toolstuff)

num = [400, 18, 3, 9000]
num.sort()
print(num)

rows = 5
for i in range(0, rows):
    for j in range(0, rows - i - 1):
        print(end = " ")
    for j in range(0, i + 1):
        print("*", end = " ")
    print() #prints a new line
        











