# List examples

num_list = [1, 2, 3] # Note 0-index
print(num_list[1]) # Could use negative num for reverse selection

str_list = ['dog', 'pizza', 'pink']
print(str_list[0]) # This is called an index of a list
#print(str_list[7])

double_list = [['dog', 'pizza', 'pink'],[1, 2, 3]]
print(double_list[0])
print(double_list[1]) 
print(double_list[0][1])
print(double_list[1][2])


num_list = [1, 2, 3, 4] # Note same variable name (updated)
print(num_list[1:]) # This is called a slice (This includes 1 index, other doesn't)
print(num_list[:2]) # Print everything to the left of the second index
print(len(num_list))

total_list = num_list + str_list
print(total_list) # Combined into one (different types can be in one list)

total_list[0] = 7
print(total_list)

del total_list[0]
print(total_list)
