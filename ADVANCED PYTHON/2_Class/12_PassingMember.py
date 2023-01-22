# PASSING MEMBER OF ONE CLASS TO ANOTHER CLASS

class Student:
    # Constructor
    def __init__(self, n, r):
        self.name = n
        self.roll = r

    # Instance Method
    def disp(self):
        print("Student Name:", self.name)
        print("Student Roll:", self.roll)


class User:
    @staticmethod
    def show(s):
        print("User Name:", s.name)
        print("User Roll:", s.roll)

# Creating object of Student Class
stu = Student('Rahul', 101)
User.show(stu)


