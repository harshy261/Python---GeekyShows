# # MODIFICATION

# stu = {100: 'Harsh', 101: 'Sangam', 103:'Yadav'}

# print("Before Modification: ")
# print(stu)
# print(id(stu))
# print()

# stu[100] = 'Python'
# print("After Modification: ")
# print(stu)
# print(id(stu))
# print()





# # Adding / Inserting Item 

# stu = {100: 'Harsh', 101: 'Sangam', 103:'Yadav'}

# print("Before Addition: ")
# print(stu)
# print(id(stu))
# print()

# stu[104] = 'Java'
# stu[105] = 'Python'
# print("After Addition: ")
# print(stu)
# print(id(stu))
# print()




# Deleting Dict Items


stu = {100: 'Harsh', 101: 'Sangam', 103:'Yadav'}

print("Before Deletion: ")
print(stu)
print(id(stu))
print()

del stu[101]
print("After Deletion: ")
print(stu)
print(id(stu))
print()


stu1 = {105: 'Rahul', 110: 'Simran', 115:'Raj'}
del stu1
print(stu1)



# Clear Method remove all the elements from the dictionary

stu = {100: 'Harsh', 101: 'Sangam', 103:'Yadav'}

print("Before Clearing: ")
print(stu)
print()

stu.clear()
print("After Clearing: ")
print(stu)
print()



