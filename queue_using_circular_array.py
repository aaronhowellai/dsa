"""
Implement a python-based queue using a circular array structure in constant time.
"""

# create a circular array class 
class Queue:

    # create __init__ function 
    def __init__(self, capacity):
        
        # set the size and the front equal to zero
        self.front = self.size = 0 
        
        # set the tail equal to the capacity -1; because of zero indexing 
        self.rear = capacity - 1

        # set the queue capacity equal to the capacity input
        self.Q = [None]*capacity
        self.capacity = capacity 

    # define a function to check q size against capacity: is it full?
    def isFull(self):
        return self.size == self.capacity

    # define a function to explicitly call the queue array 
    def returnQueue(self): 
        return self.Q
    
    # perform an enqueue on the queue if not null 
    def enQueue(self, item):

        # code to check whether the queue is full
        if self.isFull():
            print("full")
            return 
        
        # the rear gets set to an index based off of the result of a modulo 
        # """
        # >> ex. 1%5 = 1 (if the rear is 0 and +1 makes it 1, with an array the capacity of 5) because the quotient (the result of the division of one number by another) is in this case 0. 1 = 5 * 0 + 1 
        # >> in the first instance, this is the 0th index -> if the rear is initialised to n-1, and if the capacity was 5, then it would be the equivalent of saying 5%5 which equals zero
        # """
        self.rear = (self.rear + 1) % (self.capacity) 

        # the rear is now set to the value of the item 
        self.Q[self.rear] = item 
        
        # the size grows by an increment of 1
        self.size+=1

        # print the result of the operation 
        print(f"\n{str(item)} enqueued to queue.")
        print("The Queue values are: ",self.Q,"\n\n")
        print(f"\ncapacity: {self.capacity}")
        print(f"size: {self.size}\n\n--------\n")

# initialise a 5-capacity queue
queue_one = Queue(5)
print(f"\ncapacity: {queue_one.capacity}")
print(f"size: {queue_one.size}\n\n--------\n")

queue_one.enQueue(16)

queue_one.enQueue(22)

queue_one.enQueue("hello")

queue_one.enQueue(4)

queue_one.enQueue(1)

queue_one.enQueue(0)

print("\n")

print("queue_one:",queue_one.returnQueue(),"\n")





