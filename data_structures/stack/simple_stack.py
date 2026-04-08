"""
Create a stack a simple stack in python with pop/push operations on strings in O(1) time.
"""

# create a stack with a size of zero
def createStack():
    stack = []
    return stack

# check if the stack is empty
def isEmpty(stack):
    # equivalence test 
    return len(stack) == 0

# adds item to stack
def push(stack, item):
    stack.append(item)
    return print(f"\n{item} pushed to stack!")

# LIFO: removes top item from the stack 
def pop(stack):
    # 1st check if the stack is empty to avoid errors
    if (isEmpty(stack)):
        raise IndexError("Stack is empty! Please add data in order to call pop() properly!")
    
    return stack.pop()

stack = createStack()
push(stack, str(26))
push(stack, str(14))
push(stack, str(9))
push(stack, str(88))

print(f"\nstack: {stack}\n")

print(f"popped {pop(stack)} from stack!\n\nstack is now: {stack}\n")