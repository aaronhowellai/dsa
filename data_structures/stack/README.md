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

### Singly Linked list stack

**Node stores:**

- `value`
- `next`

**Stack stores:**

- `head` or `top`
  - Usually the best choice for a stack because it is simpler and lighter

### Doubly Linked list stack

**Node stores:**

* `value`
* `next`
* `prev
  `
  * While this also works, it is usually unnecessary for a standard stack because stacks do not need backward traversal.

## Interview Answer

Yes, a stack can be implemented with both a singly or doubly linked list, but a singly linked list is usually preferred because stack operations only need one end of the strusture, so the extra `prev` pointer adds overhead without improving the core O(1) push and pop operations.

### If the stack uses a singly linked list, would you want the top to be assigned as the `head` or `tail`? 

*(Design Question)*

Given that it has been established already that we don't store the tail of the stack (which would correspond to the bottom where the earliest pushed items are stored), you would want to assign the top as the head, where we can execute both push and pop operations in constant or O(1) time.
