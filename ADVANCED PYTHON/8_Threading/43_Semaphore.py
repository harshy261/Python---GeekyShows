# This is one of the oldest synchronization primitives in the history of computer science, invented by the early Dutch computer scientist Edger W. Djiktra

# A semaphore manages an internal counter which is decremented by each acqiure() call and incremented by each release call.

# The counter can never go below zero; when acquire() finds that it is zero, it blocks, waiting until some other thread calls release().

# It's usually better to use the BoundedSemaphore class, which considers it to be an error to call release more often than you've called acquire.





from threading import * 
import time
class Flight:
    def __init__(self, available_seat):
        self.available_seat = available_seat
        self.l = Semaphore(2)
        # print(self.l)

    def reserve(self, need_seat):
        self.l.acquire(blocking=True, timeout=-1)
        print(self.l._value)
        print('Available Seat: ', self.available_seat)
        if(self.available_seat >= need_seat):
            name = current_thread().name
            print(f'{need_seat} seat is alloted for {name}')
            self.available_seat -= need_seat
            # time.sleep(4)
        else:
            print('Sorry!! All Seats are alloted ')
        self.l.release()
        self.l.release()

f = Flight(3)
t1 = Thread(target= f.reserve, args=(1,), name='Rahul')
t2 = Thread(target= f.reserve, args=(1,), name='Sonam')
t3 = Thread(target= f.reserve, args=(1,), name='Sangam')
t1.start()
t2.start()
t3.start()
t1.join()
t2.join()
t3.join()
print("Main Thread")



