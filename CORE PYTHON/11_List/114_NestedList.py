# # NESTED LIST 

# a = [10, 20, 30, 40, [50, 60]]

# print(a[0])
# print(a[1])
# print(a[2])
# print(a[3])
# print(a[4])
# print(a[4][0])
# print(a[4][1])




# y = [200, 300]
# x = [10, 20, 30 , y]

# print(x)





# k = [ [10, 20, 30], [40, 50, 60] ]
# print("k[0] : ", k[0])
# print("k[1] : ", k[1])

# print("k[0] : ", k[0][0])
# print("k[0] : ", k[0][1])
# print("k[0] : ", k[0][2])

# print("k[1] : ", k[1][0])
# print("k[1] : ", k[1][1])
# print("k[1] : ", k[1][2])




# ACCESSING NESTED LIST USING FOR LOOP

# a = [10, 20, 30, 40, [50, 60]]

# n = len(a)

# for i in range(n):
#     if type(a[i]) is list:
#         if len(a[i])>1:
#             m = len(a[i])
#             for j in range(m):
#                 print(i, j, a[i][j])
#     else:
#         print(i, a[i])







k = [ [10, 20, 30], [40, 50, 60] ]
print(k[0])
print(k[1])

# Without Index

for r in k:
    for c in r:
        print(c)
    print()


# With Index

k = [ [10, 20, 30], [40, 50, 60] ]

n = len(k)

for i in range(n):
    for j in range(len(k[i])):
        print(i, j, k[i][j])
    print()






# ACCESSING NESTED LIST USING WHILE LOOP

a = [10, 20, 30, 40, [50, 60, 70]]

n = len(a)
i = 0
while i<n:
    if type(a[i]) is list:
        if len(a[i])>1:
            j = 0
            m = len(a[i])
            while j<m:
                print(i, j, a[i][j])
                j += 1
            i += 1
    else:
        print(i, a[i])
        i += 1





m = [ [10, 20, 30], [40, 50, 60] ]

n = len(m)
i = 0
while i<n:
    j = 0
    while j<len(a[i]):
        print(i, j, a[i][j])
        j+=1
    i+=1


























