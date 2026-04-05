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

Queues usually don't need this level of implementation, and it is heavier on the storage side of the data due to the fact that you are storing so much more node connections due to .prev, however if accessing certain nodes in the middle of the queue benefit from being optimised, then it is useful.

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
        pass

    # check if the queue is empty 
    def isEmpty(self):
        return self.head is None

    # enqueue 
    def enqueue(self):
        # check if the node is empty
        # (if empty, the head and tail become new_node)
        # if self.isEmpty():
        # self.head = self.tail = new_node
        # self.size+=1 (increment the zero-size by one)
        # return

        # else

        # old_tail = self.tail
        # old_tail.next = new_node
        # new_node.prev = old_tail
        # self.tail = new_node
        # self.size+=1
        # return
        pass

    # dequeue 
    def dequeue(self):
        # check if the queue is empty:
        # if self.isEmpty():
        # raise IndexError("Queue is Empty!")
        # else
        # old_head = self.head
        # removed_value = old_head.value
        # self.head = self.head.next
        # self.head.prev = None
        # self.size-=1
        # if self.head is None:
        # self.tail = None
        # return removed_value
        pass

    # peek
    def peek(self):
        pass

    # return queue 
    def returnQ(self):
        pass