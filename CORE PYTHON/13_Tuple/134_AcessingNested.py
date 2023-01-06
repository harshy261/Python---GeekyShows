# ACCESSING NESTED TUPLE 


a = ( (1, 2, 3), (4, 5, 6) )
n = len(a)

for i in range(n):
    if type (a[i]) is tuple:
        if len(a[i])>1:
            m = len(a[i])
            for j in range(m):
                print(i, j, a[i][j])
    else:
        print(i, a[i])



# Without Index
for r in a:
    for c in r:
        print(c)
    print()



# With Index

a = ( (1, 2, 3), (4, 5, 6) )

n = len(a)

for i in range(n):
    if type (a[i]) is tuple:
        if len(a[i])>1:
            m = len(a[i])
            for j in range(m):
                print(i, j, a[i][j])
    else:
        print(i, a[i])


