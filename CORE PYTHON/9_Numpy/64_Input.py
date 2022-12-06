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





'''
# 3rd 
from numpy import *

n = int(input("Enter Number of Elements: "))
a = zeros(n, dtype = int)

#input
for i in range(len(a)):
    x = int(input("Enter Element: "))
    a[i] = x

# output

print(a)        # Print in form of array


for i in range(len(a)):
    print(a[i])             # print one by one

'''





# 4rth
from numpy import *

n = int(input("Enter Number of Elements: "))
a = zeros(n, dtype = int)

x = len(a)
i = 0
j = 0

while i < x:
    k = int(input("Enter Element: "))
    a[i] = k
    i+=1

print(a)            # in form of array
print(type(a))

while j < len(a):
    print(a[j])         # print one by one 
    j+=1













