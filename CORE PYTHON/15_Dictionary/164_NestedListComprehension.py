# NESTED LIST COMPREHENSION



# Normal Way ---> 
lst = [ [24, 14, 45], [16, 46, 88] ]

for i in range(6,8):
    for j in range(4,7):
        pass

print(lst)
print()






# List Comprehension Way --> 
new_lst = [ [i*j for j in range(4,7)] for i in range(6,8) ]
print(new_lst)





