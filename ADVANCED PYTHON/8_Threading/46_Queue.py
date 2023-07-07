# The Queue class of queue module is useful to create a queue that holds the data produced by the producer. 
# The data can be taken from the queue and utilized by the consumer. 
# We need not use locks since queries are thread safe. 

# Create Queue Object --- 
# from queue import Queue
# q = Queue()

# QUEUE METHODS --- 

# 1. put()
# This method is used by the producer to insert items into the queue.

# 2. get()
# This method is used by the consumer to retrieve items from the queue.

# 3. empty()
# This method returns True if queue is Empty else return False

# 4. full()
# This method return True if queue is Full else returns False. 



from threading import Thread
from queue import Queue
from time import sleep

class Producer:
    def __init__(self):
        self.q = Queue()
    
    def produce(self):
        for i in range(1, 6):
            print('Item Produced ', i)
            self.q.put(i)
            sleep(1)

class Consumer:
    def __init__(self, prod):
        self.prod = prod

    def consumer(self):
        for i in range(1, 6):
            print('Item Received ', self.prod.q.get(i) )

p = Producer()
c = Consumer(p)

t1 = Thread(target=p.produce)
t2 = Thread(target=c.consume)

t1.start()
t2.start()



