# How to take input in 2-D array using For Loop

from numpy import * 
m = int(input("Enter no. of rows : "))
n = int(input("Enter no. of column : "))
a = zeros( (m, n) )

u = len(a)

for i in range(u):
    for j in range(len(a[i])):
        x = int(input("Enter Element: "))
        a[i][j] = x


for i in range(u):
    for j in range(len(a[i])):
        print(a[i][j])
print(a)


for r in a:
    for c in r:
        print(c)
print(a)



