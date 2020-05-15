# Function Example - By: Ben Grudzien
# (Use a hastag for comments and remember to use them in your code)
# Note how to do block comments (google that too)

def function(): # Could name anything
    print("l") # 4 spaces to show part of function
    print("l2")
    
print("out of function")
# function() # Doesn't display unless called

def pen(x):
    return 2*x

var_passed_to_function = pen(7)
print(var_passed_to_function)

def logibear(x, y): # 2 is not the limit
    print("still in function")
    return x + y # return so function done
    #print("is this still in function?")
    
double_variable = logibear(1, 2)
print(double_variable)
    #print("Okay maybe here, is this still in function?")

def new_func(z): # Can pass any type here
    print(z)
    
new_func(69)
new_func("Some string")
new_func(69.72)

# Could use tab instead of 4 spaces, could also do 2 spaces if consistent

print("How old are you?")
age = int(input()) # This is normally a string
# don't make this int part at first, demonstrate googling stuff
def age_func(age):
    if age >= 18:
        print("You are legal for stuff!")
    else:
        print("No 18+ stuff for you")

# Could I move age input here? or could it (not) be below function call?
age_func(age)






        
