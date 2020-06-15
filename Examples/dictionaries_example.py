myCat = {"size": "fat", "color": "gray", "trait": "loud"} # size = key, fat = value
print(myCat["size"])

myDog = {"color": "gray", "size": "fat", "trait": "loud"}
print(myCat == myDog) # A list of order would return false
# There is no myDog[0]


social_media_accounts = {"kylie": "insta", "tyga": "twitter", "j cole": "insta"}
'''
while 1:
    print("Enter a name: (blank to quite)")
    name = input()
    if name == '':
        break

    if name in social_media_accounts: # If key in dictionary
        print(name + " has a " + social_media_accounts[name] + " page\n")
    else:
        print("What is their social_media page?")
        social_media = input()
        social_media_accounts[name] = social_media # Changing values
        print("database updated\n")

# All these dictionary data is forgotten after program ran

'''
spam = {"color": "blue", "age": "34"}

# Shows the difference between values, items, and keys
for i in spam.values():
    print(i)

for i in spam.items():
    print(i)

for i in spam.keys():
    print(i)

dict_list_conv = list(spam.keys()) # Convert dict to list
print(dict_list_conv[0])

for k, v in spam.items():
    print("key: " + k + " Value: " + str(v))

pantry = {"cereal": 4, "soup": 7}
print("In my pantry there is " + str(pantry.get("soup", 0)) + " soups.")
# ^^^ .get(key, default value if key not found)
print("In my pantry there is " + str(pantry.get("bagel", 0)) + " bagels.")

''' 
if "bagel" not in pantry:
    pantry["bagel"] = 5

print(pantry)
'''

# Same as above line, similar to .append

print(pantry.setdefault("bagel", 5)) # This prints bagel value
print(pantry) # Demonstrates updated dictionary

import pprint # pretty print
# Verically prints dictionary in better way than regular print

message = "Hey, how are ya?"
count = {}

for character in message:
    count.setdefault(character, 0) # Sets character as key
    count[character] = count[character] + 1

pprint.pprint(count) # Outputs the number of times a certain char is used











