# MULTI DIMENSIONAL ARRAY - 2D & 3D using Zeros()

# a = zeros(( row, col ))

from numpy import *
# a = zeros((3, 2))
a = zeros((3, 2), dtype=int)
print(a)

# for r in a:
#     for c in r:
#         print(c)
#     print()


n = len(a)
print(n)
for i in range(n):
    for j in range(len(a[i])):
        print('index', i, j, "=", a[i][j])
    print()







# While Loop

from numpy import *
a = zeros((3,2), dtype=int)
print(a)

n = len(a)
i = 0
while(i<n):
    j = 0
    while (j<len(a[i])):
        print('index', i, j, "=", a[i][j])
        j+=1
    i+=1
    print()




