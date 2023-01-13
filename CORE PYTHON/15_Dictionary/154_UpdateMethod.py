# UPDATE METHOD

# This method is used to update the dict with specified key value pairs.

stu = {100: 'Harsh', 101: 'Sangam', 103:'Yadav'}
print("Original Dict: ")
print(stu)
print()

stu.update({104:'Python'})

vals = {'name': 'Kashish', 'address': 'Noida', 105: 'Youtube'}
stu.update(vals)

print("Updated Dict: ")
print(stu)
print(id(stu))
print()

