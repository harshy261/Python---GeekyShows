# THREAD CHILD CLASS WITH CONSTRUCTOR

from threading import *

class Mythread(Thread):
    def __init__(self, a):
        Thread.__init__(self)
        print("Child thread Constructor", a)
    
    def run(self):
        pass

t = Mythread(10)
t.start()
print("Main Thread")

