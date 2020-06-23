# Random Python Art Program
# Author: Ben Grudzien
#
# Link: https://github.com/sepandhaghighi/art#font-modes
# Import install doc: https://stackoverflow.com/questions/31661694/import-module-works-in-terminal-but-not-in-idle
# Import install doc2: https://stackoverflow.com/questions/23708898/pip-is-not-recognized-as-an-internal-or-external-command

from art import *
import random

def random_art(random_num):
    
    if random_num == 1:
        print("Alpha Text\n")
        tprint("Ben", "alpha")
    if random_num == 2:
        print("Chiseled Text\n")
        tprint("R o c k", "chiseled")
    if random_num == 3:
        print("Fancy58 Text\n")
        tprint("Follow me for more crazy vids!!!", "fancy58")
    if random_num == 4:
        print("finger2 Art\n")
        aprint("finger2")
    if random_num == 5:
        print("Table Flip Art\n")
        aprint("table flip")
    if random_num == 6:
        print("Real Face Art\n")
        aprint("real face")
    if random_num == 7:
        print("Ping Pong Art\n")
        aprint("ping pong")
    if random_num == 8:
        print("American Money3 Art\n")
        aprint("american money3")
    
tprint("Python  Art  :)")
previous_number = 0

while True:

    input("\n~~~ Press ENTER to see random ART! ~~~\n")
    rand_num = random.randint(1, 8) # Select random number
        
    if previous_number == rand_num: #Avoid repeating art
        print("\n- Encountered Repeating Random Number\n")
        for i in range(1, 9): # COuld have used a while loop
            # rand_num = i # Technically whats here could fail, but unlikely
            rand_num = random.randint(1, 8)
            if previous_number != rand_num:
                print("- New Number Picked!\n")
                break
            else:
                rand_num = random.randint(1, 8)              
        
    random_art(rand_num)
    previous_number = rand_num
    







