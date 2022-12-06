# MULTI DIMENSIONAL ARRAY - 2D & 3D using Ones()

# a = ones((3, 2), dtype=int)

from numpy import *
a = ones((3, 2), dtype=int)

# for r in a:
#     for c in r:
#         print(c)
#     print()


n = len(a)
i = 0
while(i<n):
    j = 0
    while (j<len(a[i])):
        print('index', i, j, "=", a[i][j])
        j+=1
    i+=1
    print()







