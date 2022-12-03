# Getting Input from User in Numpy 1-D Array

'''
# 1st 
from numpy import *

n = int((input("Enter Number of Elements: ")))
a = zeros(n, dtype = int)
print(a)
'''



'''
# 2nd 
from numpy import *

n = int(input("Enter Number of Elements: "))
a = zeros(n, dtype = int)
a[0] = 10
a[1] = 20
print(a)

'''






# 3rd 
from numpy import *

n = int(input("Enter Number of Elements: "))
a = zeros(n, dtype = int)

#input
for i in range(len(a)):
    x = int(input("Enter Element: "))
    a[i] = x


print(a)        # Print in form of array

# output

for i in range(len(a)):
    print(a[i])             # print one by one





