# VALUES METHOD

stu = {100: 'Harsh', 101: 'Sangam', 103:'Yadav'}
print("Original Dict: ")
print(stu)
print()

all_value = stu.values()
print(all_value)
print(type(all_value))

value_lst = list(all_value)
print(value_lst)
print(type(value_lst))
print(value_lst[0])
print(value_lst[1])
print(value_lst[2])

for v in value_lst:
    print(v)

    
