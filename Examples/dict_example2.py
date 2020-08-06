# First cover help ('modules')

# Second do this dictionary stuff
'''


mouse_time = {'Mouse 1': [5, 2, 4], # Comment on format and space in key name
              'Mouse 2': [7, 10, 4],
              'Mouse 3': [13, 45, 8]
              }

print(mouse_time)
print(mouse_time['Mouse 1'][0]) # Explain how you refer to key then list index
print(mouse_time['Mouse 2'][2])

def print_dictionary():
    for i in range(len(mouse_time['Mouse 3'])):
        print('Index ' + str(i) + ' in ' + str(mouse_time['Mouse 3'][i]))

print_dictionary()

mouse_stats = {'Mouse 1': {"trait": "fat", 'color': "white"}, # Comment on format and space in key name
              'Mouse 2': {"trait": "skinny", 'color': "grey"},
              'Mouse 3': {"trait": "smol", 'color': "yellow"}
              }
print(mouse_stats)
print(mouse_stats['Mouse 1']['trait'])

# Third do function stuff

def some_func(local_x):
    local_x += 5
    return local_x

global_x = 0

for i in range(3):
    print("Before function call", global_x)
    some_func(global_x)
    #global_x = some_func(global_x)
    print("After function call", global_x) # Note if same or different

'''
# Now string manipulation

fact = 'Ben is super cool'

print(fact)
print(fact.lower())
print(fact.upper())

print(fact) # Note how not permanatly updated

fact = fact.lower()

print(fact) # Now its updated
print(fact.islower()) # Also isupper, numbers are niether

# On your own review isaplha(), isalnum, isdeicmal, istitle()
# Page 129 and 130

fact2 = 'Ben is super strong'
print(fact2.startswith('Ben')) # This is case sensitive, also endswith()
print(fact2.split()) # Makes list


bens_stats = ["strong", "cool", "funny"]
stats = ' '.join(bens_stats) # Concatenates words with ' '
print(stats)

print('Ben'.rjust(20)) # Formats ouput
print('Ben'.ljust(20))
print('Ben'.center(20, '*'))

# Look up stip(), rstrip(), and lstrip() (They take away whitespace) page 134
# Mention pyperclip module to copy and paste
# Refernce "if in some_list" function














