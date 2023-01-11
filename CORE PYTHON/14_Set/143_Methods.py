# SET METHODS

a = {'Harsh', 'Yadav', 'Sangam', 'Utkarsh', 'Python'}
b = {'Mohan', 'Sonam', 'Yadav', 'Python', 'Java'}

print("A : ", a)
print("B : ", b)
print()


ism = a.intersection(b)
print(ism)
print()


itf = a.union(b)
print(itf)
print()


diff_a = a.difference(b)
print(diff_a)
diff_b = b.difference(a)
print(diff_b)
print()


l = a.issubset(b)
print(l)
print()


h = a.issuperset(b)
print(h)
print()









