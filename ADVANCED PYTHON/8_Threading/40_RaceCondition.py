# RACE CONDITION IS A SITUATION THAT OCCURS WHEN A THREADS ARE ACTING IN AN UNEXPECTED SEQUENCE THUS LEADING TO AN UNRELIABLE OUTPUT.
# THIS CAN BE ELIMINATED USING THREAD SYNCHRONIZATION.

from threading import Thread, current_thread
class Flight:
    def __init__(self, available_seat):
        self.available_seat = available_seat

    def reserve(self, need_seat):
        print('Available Seat: ', self.available_seat)
        if(self.available_seat >= need_seat):
            name = current_thread().name
            print(f'{need_seat} seat is alloted for {name}')
            self.available_seat -= need_seat

        else:
            print('Sorry!! All Seats are alloted ')

f = Flight(1)
t1 = Thread(target= f.reserve, args=(1,), name='Rahul')
t2 = Thread(target= f.reserve, args=(1,), name='Sonam')
t1.start()
t2.start()




