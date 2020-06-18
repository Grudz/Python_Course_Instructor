# Dungeon Game inventory system
# refer to: https://stackoverflow.com/questions/30208044/how-to-add-list-elements-into-dictionary

player_inventory = {"gold coin": 7, "sword": 1} # Dictionary {Key: Value}

def add_to_inventory(inventory, added_items): # Pass(Dictionary.list)
    for loot in added_items: # Loot is a new variable for each list item
        inventory.setdefault(loot, 0) # If the item in the list is not in the dictionary, then add it as a key to the dictionary - with a value of 1
        inventory[loot] = inventory[loot] + 1 # Note how Ruby = 1 because of this line

    return inventory # Print inv would be 0 without returning this dictionary

def display_inventory(inventory):
    print("\nInventory")
    item_total = 0 # Instantiate variable for number of key values that appear in inventory
    for k, v in inventory.items():
        print(str(v) + " " + k) # Print Value + Key
        item_total += v # Add value relative to key
    print("Total number of items: " + str(item_total))


print("\nIntial inventory")
print(player_inventory) # Displays intial loot

dragonloot = ["gold coin", "sword", "gold coin", "gold coin", "ruby"] # Loot from slaying dragon
player_inventory = add_to_inventory(player_inventory, dragonloot) # Setting player loot equal to ouput of function

print("\nUpdated inventory")
print(player_inventory) # Displays gained loot

display_inventory(player_inventory)
