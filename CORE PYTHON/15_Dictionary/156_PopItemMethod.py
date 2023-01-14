# POP ITEM METHOD

# This method is used to remove the item which was last inserted into the dictionary.
# It returns the removed item in the form of tuple, Pairs are returned in LIFO order.

stu = {100: 'Harsh', 101: 'Sangam', 103:'Yadav'}
print("Original Dict: ")
print(stu)
print(id(stu))
print()

removed_item = stu.popitem()

print("After Removing Dict: ")
print(stu)
print(id(stu))
print("Removed Value: ", removed_item)
print()

