## Can you implement a stack using a singly linked list as well as a doubly linked list?

Yes.

## Why is it possible to implement a stack with both version of a linked list?

- A stack only needs operations at one end of its structure:
  - `push(x)` adds to the top of the stack
  - `pop()` removes from the top of the stack as it is `LIFO`
    - LIFO: Last In, First Out
    - The lastest item pushed to the stack is the first to be popped off
  - `peek()` looks at the top of the stack
- If you make the top of the stack equal the head of the linked list, then:
  - `push(x)` at head is O(1) (because we can access the head due to storing its data point at its location)
  - `pop()` from head is O(1)
  - `peek()` at head is O(1)
- This means you do not need to store `tail` and you do not need `prev` (which is technically or intuitively the front of the stack - nearest to the earliest items pushed)

## Comparison of linked lists and stacks
