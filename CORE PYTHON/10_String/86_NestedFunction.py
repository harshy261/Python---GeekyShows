# NESTED FUNCTION -- define one function inside another function

def disp():
    def show():
        print("SHow Function")
    print("Disp Function")
    show()

disp()




def disp():
    def show():
        return "SHow Function"
    result = show() + " Disp Function"
    return result

a = disp()
print(a)





def disp(str):
    def show():
        return "SHow Function"
    result = show() + str + " Disp Function"
    return result

print(disp("Harsh Yadav"))








