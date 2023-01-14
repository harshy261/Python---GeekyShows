# POP METHOD

# This Method is used to remove the item with specified keys.
# It returns the removed item's value
# If key is not found then the default value is returned
# If the key is not found and default value is not given then shows KeyAError.

stu = {100: 'Harsh', 101: 'Sangam', 103:'Yadav'}
print("Original Dict: ")
print(stu)
print(id(stu))
print()

# removed_value = stu.pop(102)
removed_value = stu.pop(101)

print("After Removing Dict: ")
print(stu)
print(id(stu))
print("Removed Value: ", removed_value)
print()







