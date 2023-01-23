# METHOD OVERLOADING

# When more than one method with the same name is defined in the same class, it is known as method overloading.

# If a method is written such that it can perform more than one task.


# # 1 >>>>>
# class Myclass:
#     def sum(self, a, b, c):
#         s = a+b+c
#         return s
    
# obj = Myclass()
# print(obj.sum(10, 20, 30))



# # 2 >>>>>
# class Myclass:
#     def sum(self, a, b, c):
#         s = a+b+c
#         return s
    
# obj = Myclass()
# print(obj.sum(10))




# 3 >>>>>
class Myclass:
    def sum(self, a=None, b=None, c=None):
        if a!=None and b!=None and c!=None:
            s = a+b+c
        elif a!=None and b!=None:
            s = a+b
        else:
            s = "Print atleast 2 numbers"
        return s
    
obj = Myclass()
print(obj.sum(10, 20, 30))
print(obj.sum(10, 20))
print(obj.sum(10))
print(obj.sum())



