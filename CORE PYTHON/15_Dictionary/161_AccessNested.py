# ACCESS NESTED DICTIONARY USING FOR LOOP

a = { 1:{'course':'JavaScript', 'fees':15000}, 2:{'course':'ReactJs', 'fees':45000}, 3:{'course':'Mern', 'fees':95000}, 'course':'Pyhton', 'fees':12000 }


for i in a:
    print(i)

print()

for i in a:
    if(type(a[i]) is dict):
        for k in a[i]:
            print(k, '=', a[i][k])
    else:
        print(i, '=', a[i])



