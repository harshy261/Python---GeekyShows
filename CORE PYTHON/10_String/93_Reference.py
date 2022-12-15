# PASS BY VALUE / CALL BY REFERENCE ------- JAVA / C++

# PASS BY OBJECT REFERENCE 


# INTEGERS ARE IMMUTABLE and cannot be modified

def val(x):
    print(x, id(x))
    x = 15
    print(x, id(x))

x = 10
val(x)
print(x, id(x))




# LIST ARE MUTABLE and Can be Modified

def val(lst):
    print("IIBA:", lst, id(lst))
    lst.append(4)
    print("IIFA:", lst, id(lst))

lst = [1, 2, 3]
print("BCF: ", lst, id(lst))
val(lst)
print("ACF: ", lst, id(lst))


# If object is immutable then the modified value is not available outside the function.

# If object is mutable then the modified value is available outside the function.

# IMMUTABLE OBJECT ---- Integer, Float, String and Tuple
# MUTABLE OBJECT ---- LIST and Dictionary






