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
        # if the stack is full (use a method), then raise an exception
        # if isFull():
            # raise IndexError("The stack is already full. Please pop off more elements to push!")
        
        # read value at top (use method)
        # call peek()

        # move top up
        # self.top += 1

        # place value at top
        # self.top.value = value
        pass

    # # removal mutation method
    def pop(self):
        # check if the stack is empty 
        # is the stack is empty (use a method), then raise an exception
        # if isEmpty():
            # raise IndexError("The stack is empty. Please push elements first to execute pop!")

        # read value at top (use method)
        # call peek()

        # move top down
        # self.top -= 1
        pass

    # output helper
    def returnStack(self):
        # result = []
        # for every value in the array that is present, append it to the result python list
        # for value in 'the values in the stack':
            # result.append(value)

        # return result
        pass

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




