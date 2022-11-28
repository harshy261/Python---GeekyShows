# FIND THE DATATYPE OF VARIABLE VALUE

# Sequence Type :::


#String
str1 = "Harsh"
print(type(str1))


#List
data = [10, 20, 3.45, -2, 'Harsh']
print(type(data))
data[1] = 25
print(data)


#Tuple - Read only , Similar to List but we cannot modify elements
TupleData = (10, 20, 3.45, -2, 'Harsh')
print(type(data))
# TupleData[1] = 25             # Cannot do this


#Range 
rg = range(5)
rg1 = range(10, 20, 2)
print(rg)
print(rg[0])
print(rg[1])
print(rg[4])
print(rg1)
print(rg1[1])
print(rg1[2])








