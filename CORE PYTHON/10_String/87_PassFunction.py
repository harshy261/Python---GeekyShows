# PASS A FUNCTION AS PARAMETER

# def disp(sh):
#     print("Disp Function" + sh())

# def show():
#     return "Show Function"

# reasult = disp(show)
# print(reasult)




# FUNCTION RETURN ANOTHER FUNCTION

def disp():
    def show():
        return "Show Function"
    print("Disp Function")
    return show

r_sh = disp()
print(r_sh())


def disp(sh):
    print("Disp Function")
    return sh
def show():
    return "Show Function"

r_sh = disp(show)
print(r_sh())



