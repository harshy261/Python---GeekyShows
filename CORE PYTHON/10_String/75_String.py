# STRING - group of Characters

str = 'HarshYadav'
print(str)

str = "HarshYadav"
print(str)

str = '''Hello guys
Subscribe
My Channel'''
print(str)

str = "My name is 'Harsh' "
print(str)

str = "My name is \tHarsh "
print(str)

str = r"My name is \tHarsh "
print(str)


str1 = "HarshYadav"
str2 = "Harsh"
str3 = "Hahaha"
str4 = str3
print("str1 = ", id(str1))
print("str2 = ", id(str2))
print("str3 = ", id(str3))
print("str4 = ", id(str4))


# Indexing

print(str2[0])
print(str2[4])
print(str2[-1])
print(str2[-5])




# STRING LENGTH

str = "HarshYadav"
n = len(str)
print(n)


# Accesing using For Loop
str1 = "HarshYadav"

for c in str1:
    print(c)
print()

for i in range(len(str1)):
    print(str1[i])
print()

n = len(str1)
i = 0 
while(i<len(str1)):
    print([str1[i]])
    i+=1



