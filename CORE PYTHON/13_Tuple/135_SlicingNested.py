# SLICING NESTED TUPLE 

x = ( (10, 20, 30),
      (40, 50, 60), 
      (70, 80, 90), 
      (11, 22, 33), 
      (44, 55, 66), 
      (77, 88, 99), )

print("Original Tuple")
print(x)
print()


print("From 1st Position to 4rth Position")
a = x[1:5]
print(a)
print()


print("From 0th Position to last Position")
b = x[0:]
print(a)
print()


print("From 0th Position to 4rth Position")
c = x[:5]
print(c)
print()


print("Last 4 Tuples")
d = x[-4:]
print(d)
print()


print("From 0th Position to 6th Position Stepsize 2")
e = x[:7:2]
print(e)
print()


print("Last 5 Tuples with [-5-(-3)] = 2 Tuple toward right")
f = x[-5:-3]
print(f)
print()


print("*****************************************************************")
print("Slice Nested 2nd Positon, 0th Position")
g = x[2:3]
print(g)
m = x[2:3][0]
print(m)
print()


print("Slice 2nd Tuple then extract elements")
n = x[2:3][0][0]
print(n)
o = x[2:3][0]
for el in 0:
    print(el)
print()


print("Last Nested 4 Tuples then 1st Position then extract element")
v = x[-4:]
print(v)
b = x[-4:][1]
print(b)
print()


print("Last Nested 4 Tuples then 1st Position then extract element")
k = x[-4:][1][0]
print(k)
l = x[-4:][1]
for el in l:
    print(el)
print()






