# NESTED DICTIONARY

a = { 1:{'course':'JavaScript', 'fees':15000}, 2:{'course':'ReactJs', 'fees':45000}, 3:{'course':'Mern', 'fees':95000}, 'course':'Pyhton', 'fees':12000 }


print(a['course'])
print()
print(a['fees'])
print()
print(a[1]['course'])
print()
print(a[1]['fees'])
print()

a['course'] = 'Java'
a[1]['fees'] = 200000
print(a['course'])
print(a[1]['fees'])
print()



# Delete Items

del a[1]['course']
print(a)
print()




# Add Items

a['duration'] = '6 months'
a[1]['teacher'] = 'GeekyShows'


a[2] = {'course': 'Nodejs', 'fees': 30000}
a[1][2] = {'course': 'Angular', 'fees': 65000}

print(a)










