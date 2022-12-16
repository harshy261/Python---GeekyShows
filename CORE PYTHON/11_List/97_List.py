# LIST []

# List similar to Array but
# Array can store one type of element but list can store multiple type of arrays in a single list

# List are mutable object

# Dynamic in size , size not fixed


a = [10, 20, 10.45, -21, 'Harsh', 'sangam']

print(a)
print(a[0])
print(a[3])
print(a[-1])
print(a[-3])

a[3] = -40
print(a[3])
print(a, id(a))






# ACCESSING LIST USING FOR LOOP

a = [10, 20, 10.45, -21, 'Harsh', 'sangam']

for element in a:
    print(element)


n = len(a)

for i in range(n):
    print(i, a[i])





# ACCESSING LIST USING WHILE LOOP

a = [10, 20, 10.45, -21, 'Harsh', 'sangam']

n = len(a)
i = 0

while i<n:
    print(i, a[i])
    i+=1


















