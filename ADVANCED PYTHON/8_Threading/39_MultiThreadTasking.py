# MULTITASKING USING MULTIPLE THREAD


from threading import *

class Hotel:
    def __init__(self, t):
        self.t = t
    
    def food(self):
        for i in range(1, 6):
            print(self.t, i)

h1 = Hotel('Take order from Table ')
h2 = Hotel('Serve order to Table ')

t1 = Thread(target=h1.food)
t2 = Thread(target=h2.food)

t1.start()
t2.start()



class Hotel:
    def __init__(self, t):
        self.t = t
    
    def food(self):
        for i in range(1, 6):
            print(self.t, i)

h1 = Hotel('Take order from Table ')
h2 = Hotel('Serve order to Table ')

t1 = Thread(target=h1.food)
t2 = Thread(target=h2.food)

t1.start()
t2.start()


