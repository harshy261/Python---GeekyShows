# SET DEFAULT METHOD

# This method returns the value of specified key.
# If key is not found then it inserts key with specified value.


stu = {100: 'Harsh', 101: 'Sangam', 103:'Yadav'}
print("Original Dict: ")
print(stu)
print(id(stu))
print()

returned_value = stu.setdefault(109, 'Python')

print("After SetDefault Dict: ")
print(stu)
print(id(stu))
print("Returned Value: ", returned_value)
print()
