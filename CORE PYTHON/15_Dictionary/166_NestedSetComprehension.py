# NESTED SET COMPREHENSION


# Normal Way ---> 
set = [ [24, 14, 45], [16, 46, 88] ]

for i in range(6,8):
    for j in range(4,7):
        pass

print(set)
print()






# List Comprehension Way --> 
new_set = { (i*j) for j in range(4,7) for i in range(6,8) }
print(new_set)
print(type(new_set))





