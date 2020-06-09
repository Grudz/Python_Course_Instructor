#!/usr/bin/env python3

# MAGIC 8-BALL HOMEWORK

import random

history = ["History:"]

def magiceightball(random_number):    
   if random_number == 1:
       result = "Yes!"
   if random_number == 2:
       result = "No."
   if random_number == 3:
       result = "Maybe."
   if random_number == 4:
       result = "Possibly."
   if random_number == 5: 
       result = "You may rely on it."
   if random_number == 6: 
       result = "Try Again."
   history.append(result)
   print(result)
     
print("---- Welcome to the Magic 8 Ball! -----\n")

while True: 
    print("What is your Question?\n")
    question = input()
    history.append(question)
    
    answer = random.randint(1,6)
    magiceightball(answer)

    print("Press H to see History, Press E to Exit, Press Enter to Ask Again\n")
    decision = input()
    if decision == "E":
        break
    if decision == "H":
        print(history)
        input("Press ENTER to Ask Again")

        
