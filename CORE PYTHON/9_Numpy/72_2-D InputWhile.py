# How to take input in 2-D array using While Loop

from numpy import * 
m = int(input("Enter no. of rows : "))
n = int(input("Enter no. of column : "))
a = zeros( (m, n) )

u = len(a)
i = 0
while(i<u):
    j = 0
    while(j<len(a[i])):
        x = int(input("Enter Element: "))
        a[i][j] = x
        j += 1
    i += 1

i = 0

while i<u:
    j = 0
    while (j<len(a[i])):
        print('index', i, j, "=", a[i][j] )
        j += 1
    i += 1

print(a)





