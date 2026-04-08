"""

Implementation of a stack using a fixed array with push/pop operations on integers and strings in O(1) time, to simulate the function of undo/redo.

// This implementation will use parallel stacks:

- stack_one: data_stack → current state
    - where the current working data is stored.

- stack_two: history_stack → mod states
    - where the history that you can undo from stack_one to stack_two is stored as well as redo from stack_two to stack_one.

// How the system should behave

Start: 

data_stack = []
history_stack = []

Push Operations:

push(X)
push(Y)
push(Z)

data_stack = [X, Y, Z]
history_stack = []

Undo Operations:

undo()

data_stack = [X, Y]
history stack = [Z]

undo()

data_stack = [X]
history stack = [Z, Y]

undo()

data_stack = []
history stack = [Z, Y, X]

Redo Operations:

redo()

data_stack = [X]
history_stack = [Z, Y]

redo()

data_stack = [X, Y]
history_stack = [Z]

redo()

data_stack = [X, Y, Z]
history_stack = []

// Important design rule

- Whenever a new push(x) is executed, the history_stack must be cleared
    - This is because the previously built history becomes invalid as it is joined to only sequential chains of events
    - push A → push B → undo → push X
        - The right way to think of it is a timeline 
        - data_stack (now): [A, X] 
        - the command undo would now remove X, and redo is an invalid move because its history in the sequence was overwritten before redoing it before the next push
    

"""

class fixedArraryStack():

    def __init__(self,stack_one,stack_two,size):
        pass

    def Pop(self):
        pass

    def Push(self,value):
        self.value = value
        pass

    def undo(self):
        # if the data stack is empty, you cannot undo any further

        # if self.stack1.size is None:
            # raise IndexError("There is no data in the data_stack to undo. Please add data using <self>.Push()!")
        pass

    def redo(self):
        # you cannot undo if the history stack size is None
        
        # if self.stack2.size is None:
            # raise IndexError("There is no data in the history_stack to redo. Please use undo first!")
        pass

    def returnStack():
        pass

