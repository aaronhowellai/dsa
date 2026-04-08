"""
Implement a python-based FIFO queue using a singly linked-list data structure, with enqueue and dequeue in O(1).
"""

# create new_node (new_node = Node(x)), value = x, next = None to allow for enqueue operations  
class Node:

# value/next initialisation
    def __init__(self, value):

        self.value = value
        self.next = None

# create a class to initialise a queue instance using a singly linked-list 
class QueueLL:

    # head/tail initialisation
    def __init__(self):
        self.head = self.tail = None
        self.size = 0

    # check if the queue is empty
    def isEmpty(self):
        return self.head is None
        
    # for self.enQueue(x):
    def enqueue(self, value):

        # create a new node instance from the node class
        new_node = Node(value)
        
        # check if the queue is empty - because if it is, the head and tail become new node
        if self.isEmpty():
            self.head = self.tail = new_node
            self.size+=1 # increase the size by one
            return
        
        else:
           self.tail.next = new_node
           self.tail = new_node
           self.size+=1 # increase the size by one

    # for self.deQueue(x):
    def dequeue(self):
        
        # aim: remove from the front (head) as it is FIFO
        if self.isEmpty():
          raise IndexError("Queue is empty!")

        else: 
          old_head = self.head
          removed_value = old_head.value
          self.head = self.head.next
          self.size-=1 # decrease the size by one 

        if self.head is None:
          self.tail = None 

        return removed_value
    
    # function to return queue
    def returnQueue(self):
       
       # create an empty list
       result = []
       current = self.head 

       while current is not None:
          result.append(current.value)
          current = current.next

       return result
    
    # peek() → show the next value that would be dequeued
    def peek(self):
       
      # if empty, raise an exception error
      if self.isEmpty():
        raise IndexError("Queue is empty!")

      # if non-empty return self.head.value
      return self.head.value

# for running script
q = QueueLL()
q.enqueue(1)
q.enqueue(4)
q.enqueue(6)
q.enqueue(8)

print(f"\n{q.returnQueue()}", f"\n\nSize: {q.size}\n")

q.dequeue()
q.dequeue()

print(f"\n{q.returnQueue()}", f"\n\nSize: {q.size}\n")

q.enqueue(198)

print(f"\n{q.returnQueue()}", f"\n\nSize: {q.size}\n")

# ----------------------------------------------------

# FIFO (first in, first out)

# enqueue(x) adds to the rear
# dequeue() removes from the front
# self.isEmpty() checks if the queue is empty

# ----------------------------------------------------

# Linked-list structure

# made of nodes
# nodes:
# 1. value (data)
# 2. next (pointer - reference to the next node)

# why is it O(1)?
# the list is never traversed 
# the elements are never shifted 
# only a constant number of pointers is updated:
#   at most 2 for enqueue
#   at most 2 for dequeue
# If we did not know where the tail was (and didn't store it), traversing the list would make it O(n)

# ----------------------------------------------------

# Queue structure

# these allows for O(1) enqueue/dequeue operations:
# 1. head = front of the queue (FIFO dequeues from front)
# 2. tail = rear of the queue

# ----------------------------------------------------

# mental model:
# __init__ = constructor to set up initial values, create attributes, prepare the object to be used
# self = the Queue object 
# self.head = reference to the first node object inside the queue 
# self.tail = reference to the last node object inside the queue 
# new_node = a separate node instance created inside enqueue

# ----------------------------------------------------

# Why we store head
# ------------------
# We store the head to locate where the front of the queue is to enable dequeue operations in O(1) time, as queue's are FIFO.

# Why we store tail
# ------------------
# We store the tail to locate where the end of the queue is to enable enqueue operations in O(1) time.

# Why we don't need prev in this queue
# ------------------------------------
# We don't need prev in this queue because singly linked lists can enqueue and dequeue already in O(1) time without the extra complication of managing twice the number of pointers. Head for example having prev would point to None, and we only need to reference next.

# ----------------------------------------------------

# Interview question 

# “Why does a linked-list queue require storing both head and tail to achieve O(1) enqueue and dequeue?”

# A linked-list queue stores both head and tail to enable removal from the front and insert at the back in constant time without traversing the list. 

# Without the tail pointer, enqueue would require the walking of the entire queue, making it O(n).

# Storing both ensures enqueue and dequeue are performed in O(1).
