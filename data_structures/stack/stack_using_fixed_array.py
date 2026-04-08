"""

Implementation of a stack using a fixed array with push/pop operations on integers and strings in O(1) time, to simulate the function of undo/redo.

This will use parallel stacks:
- stack_one: data_stack 
- stack_two: history_stack
- data_stack: where the current working data is stored.
- history_stack: where the history that you can undo from stack_one to stack_two is stored as well as redo from stack_two to stack_one.

"""

class fixedArraryStack():

    def __init__(self,stack_one,stack_two,size):
        pass

    def Pop():
        pass

    def Push(self,value):
        self.value = value
        pass

    def undo():
        # if the data stack is empty, you cannot undo any further

        # if self.stack1.size is None:
            # raise IndexError("There is no data in the data_stack to undo. Please add data using <self>.Push()!")
        pass

    def redo():
        # you cannot undo if the history stack size is None
        
        # if self.stack2.size is None:
            # raise IndexError("There is no data in the history_stack to redo. Please use undo first!")
        pass

    def returnStack():
        pass

