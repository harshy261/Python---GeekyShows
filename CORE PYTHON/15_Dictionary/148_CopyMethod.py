# COPY METHOD

stu = {100: 'Harsh', 101: 'Sangam', 103:'Yadav'}

print("Original Dictionary: ")
print(stu)
print(id(stu))
print()

new_stu = stu.copy()
print("Copied Dictionary: ")
print(new_stu)
print(id(new_stu))
print()



stu[102] = 'Python'

print(stu)
print(new_stu)







