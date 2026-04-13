"""
Implementation of one stack using a fixed array with push/pop operations and another stack enabling undo/redo actions, both in O(1) time on integer, floating point and string data types.
"""

# manage one fixed-capacity stack
class FixedArrayStack:

    # constructor 
    def __init__(self,capacity):

        # initialise the array 
        self.stack = [None] * capacity

        # store the fixed maximum capacity of the stack for boundary checks (e.g. isFull)
        # capacity represents the maximum number of elements the stack can hold (fixed size constraint) 
        # storing it explicitly so that it can be checked without relying on the 'len(self.stack)' method
        self.capacity = capacity
        
        # top always points to the index of the current element 
        # when the stack is empty, there is no valid index, so top = -1
        self.top = -1

    # stack state check
    def isEmpty(self):

        # return True if the stack is empty (top has no valid index)
        return self.top == -1

    # stack state check
    def isFull(self):

        # return True if the stack is full (top index matches the maximum capacity - 1 due to zero indexing)
        return self.top == self.capacity - 1

    # read-only accessor
    def peek(self):
        # if the stack is empty (there is no value to peek at), raise an error 
        if self.isEmpty():
            raise IndexError("Stack is empty. Cannot peek.")

        # read the value at the top of the stack (use the index of the top element to access the value of the array, with respect to how python accesses list elements)
        return self.stack[self.top]

    # append mutation method 
    def push(self,value):
        # check if the stack is full
        if self.isFull():
            raise IndexError("Stack is full, Cannot push.")
        
        # increment index to prepare for new value assignment at new top
        self.top += 1

        # assign value at new top index
        self.stack[self.top] = value

    # # removal mutation method
    def pop(self):
        # check if the stack is empty 
        if self.isEmpty():
            raise IndexError("Stack is empty. Cannot pop.")
        
        # read the value at the top
        popped = self.stack[self.top]

        # clear the top value to prevent data overwrites (cleaner design)
        self.stack[self.top] = None

        # decrement index by 1 after removing the current value
        self.top -= 1

        # return the popped value
        return popped

    # output helper
    def returnStack(self):
        # init an empty array to append to 
        result = []

        # inclusive top for range
        inclusive_top = self.top + 1

        # create a loop to append the range of indices
        for i in range(0, inclusive_top):
            # return the stack value at the current index
            result.append(self.stack[i])

        # return the resulting array
        return result

# can use two instances of the previous stack to implement undo/redo
class UndoRedoManager:

    def __init__(self,data_stack, history_stack):
        pass

    def undo():
        pass

    def redo():
        pass

    def push(value):
        pass




