# NAMESPACES 

# Represent a memory block where names are mapped to objects.

# 1. Class Namespace
# 2. Instance Namespace

class Mobile:
    fp = 'Yes'              # Class Variable

    @classmethod
    def is_fp(cls):
        print("Pringer Print: ", cls.fp)       # Accessing Class Variable

realme = Mobile()
redmi = Mobile()
geek = Mobile()

print("Class FP: ", Mobile.fp)
print("Redmi: ", redmi.fp)
print("Geek: ", geek.fp)
print("Realme: ", realme.fp)
print()

Mobile.fp = 'No'
print("Class FP: ", Mobile.fp)
print("Redmi: ", redmi.fp)
print("Geek: ", geek.fp)
print("Realme: ", realme.fp)
print()

realme.fp = 'Not Working'
print("Class FP: ", Mobile.fp)
print("Redmi: ", redmi.fp)
print("Geek: ", geek.fp)
print("Realme: ", realme.fp)
print()












