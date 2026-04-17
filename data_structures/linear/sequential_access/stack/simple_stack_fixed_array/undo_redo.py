# import module from "stack_using_fixed_array.py"
from stack_using_fixed_array import UndoRedoManager

# run tests
def run_tests():

    # create undo-redo manager with capacity of 5
    print("\n// Creating UndoRedoManager with capacity of 5 //\n")
    manager = UndoRedoManager(5)

    # testing push-to-data-stack method
    print("\n=== Testing push ===")
    manager.push(1)
    manager.push(2)
    manager.push(3)
    print(f"\nData stack: {manager.data_stack.returnStack()}")

    # testing peek method to see top value of data stack
    print("\n=== Testing peek ===")
    print(f"\nTop value: {manager.data_stack.peek()}")

    # testing undo
    print("\n=== Testing undo ===\n")
    
    def undo_print():
        manager.undo()
        return str("Undo Executed!")
    
    print(undo_print(),"\n")
    
    print(f"Data stack: {manager.data_stack.returnStack()}\n")

    print(f"History stack: {manager.returnHistory()}\n")

    # testing redo
    print("=== Testing redo ===\n")

    def redo_print():
        manager.redo()
        return str("Redo Executed!")

    print(redo_print(),"\n")

    print(f"Data stack: {manager.data_stack.returnStack()}\n\n")

    # try to undo from empty data stack
    # print("=== Try to undo from empty data stack ===\n")
    # print(undo_print(),"\n")
    # print(undo_print(),"\n")
    # print(undo_print(),"\n")
    # print(undo_print(),"\n")

    # manager.push(103)
    # print(f"Reset Data stack: {manager.data_stack.returnStack()}")

    # try to redo from empty history stack
    # print("=== Try to redo from empty history stack ===\n")
    # print(redo_print(),"\n")

run_tests()