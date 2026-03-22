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

Do doubly linked lists improve in time complexity in comparison to singly linked lists? Explain the benefits of choosing to implement it.



"""


