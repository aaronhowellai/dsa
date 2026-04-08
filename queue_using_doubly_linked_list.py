"""
Implement a python-based FIFO queue using a doubly linked-list data structure, with enqueue and dequeue in O(1).

A doubly-linked node should have three things: value, next, prev: 

None ← [A] ⇄ [B] ⇄ [C] → None

Where:

- A.prev = None
- A.next = B
- B.prev = A
- B.next = C
- C.prev = B
- C.next = None

The queue will store:

- head 
- tail

-------------------------------------------------------------------------

Q: Do doubly linked lists improve in time complexity in comparison to singly linked lists? Explain the benefits of choosing to implement it.

A: Because the singly linked list already had enqueue and dequeue operations at O(1), the time complexity does not improve for those operations, however, the extra pointer helps with:

- easier deletions in the middle of the queue 
- reverse traversal (as the singly linked list previously only allowed for forward traversal)

Queues usually don't need this level of implementation, and it is heavier on the storage side of the data due to the fact that you are storing so much more node connections due to .prev, however it is useful when reverse traversal matters, or when deleting an already-referenced node is easier because both next and prev links are available.

"""

# build a class for the node
class Node:

    # next/prev/value initialisation
    def __init__(self,value):
        self.value = value
        self.next = self.prev = None

# build a class for the doubly linked list
class QueueDLL:

    # head/tail + size initialisation
    def __init__(self):
        self.head = self.tail = None
        self.size = 0

    # check if the queue is empty 
    def isEmpty(self):
        return self.head is None

    # enqueue 
    def enqueue(self, value):
        # create a new node:
        new_node = Node(value)

        # check if the queue is empty

        # (if empty, the head and tail become new_node)
        if self.isEmpty():
            self.head = self.tail = new_node
            self.size+=1 # (increment the zero-size by one)
            return

        old_tail = self.tail
        old_tail.next = new_node
        new_node.prev = old_tail
        self.tail = new_node
        self.size+=1
        return

    # dequeue 
    def dequeue(self):
        # check if the queue is empty:
        if self.isEmpty():
            raise IndexError("Queue is empty!")
        # this is because you cannot dequeue from an empty list 
        
        # because the queue is FIFO, we remove from the head (we need to assign the old head before we move on to keep track of its next and prev)

        old_head = self.head 
        removed_value = old_head.value # (we need to store the remove the value)
        self.head = self.head.next # (this is the assignment of the new head)

        if self.head is not None:
            self.head.prev = None # (remove the prev connection)
            
        else:
            self.tail = None
            
        self.size-=1 # (decrease the size by one)
        return removed_value

    # peek() → show the next value that would be dequeued 
    def peek(self):

        # if the queue is empty, then there will be nothing to show, so it needs to be an exception raised
        if self.isEmpty():
            raise IndexError("Queue is empty!")
        
        # if non-empty, return self.head.value
        return self.head.value 

    # return queue 
    def returnQ(self):

        # create an empty list
        result = []
        current = self.head

        while current is not None:
            result.append(current.value)
            current = current.next

        return result
        

# for running script 
q = QueueDLL()
q.enqueue(1)
q.enqueue(67)
q.enqueue('hello')
q.enqueue(36)

print(f"\n{q.returnQ()}", f"\n\nSize: {q.size}\n")

q.dequeue()
q.peek()

print(f"\n{q.returnQ()}", f"\n\nSize: {q.size}\n")

q.dequeue()
q.dequeue()

print(f"\n{q.returnQ()}", f"\n\nSize: {q.size}\n")