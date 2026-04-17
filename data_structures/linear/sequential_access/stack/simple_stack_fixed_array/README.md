# Undo/Redo Program 💻

## Dual-stack data structures implemented using fixed arrays and OOP

OOP Implementation of one stack using a fixed array with push/pop operations and another stack enabling undo/redo actions, both in O(1) time on integer, floating point and string data types.

### Stack Details

- **stack_one:** `data_stack` → current state

  - where the current working data is stored.
- **stack_two:** `history_stack` → mod states

  - where the history that you can undo from stack_one to stack_two is stored as well as redo from stack_two to stack_one.

### How the program should behave

**Start**

* `data_stack` = [ ]
* `history_stack` = [ ]

**Push Operations**

* `push`(X)
* `push`(Y)
* `push`(Z)

`data_stack` = [X, Y, Z]

`history_stack` = [ ]

**Undo Operations**

* `undo`()
* `data_stack` = [X, Y]
* `history stack` = [Z]
* `undo`()
* `data_stack` = [X]
* `history stack` = [Z, Y]
* `undo`()
* `data_stack` = [ ]
* `history stack` = [Z, Y, X]

**Redo Operations**

* `redo`()
* `data_stack` = [X]
* `history_stack` = [Z, Y]
* `redo`()
* `data_stack` = [X, Y]
* `history_stack` = [Z]
* `redo`()
* `data_stack` = [X, Y, Z]
* `history_stack` = [ ]

#### Important design rule

- Whenever a new push(x) is executed, the history_stack must be cleared

  - This is because the previously built history becomes invalid as it is joined to only sequential chains of events
  - `push` A → `push` B → `undo` → `push` X

    - The right way to think of it is a timeline
      - `data_stack` (now): [A, X]
      - the command undo would now remove X, and redo is an invalid move because its history in the sequence was overwritten before redoing it before the next push

### `Layer 1`: One fixed array stack

**This stack should manage:**

- underlying array
- capacity
- top index
- Methods:

  - `isEmpty`()
  - `isFull`()
  - `push`(value)
  - `pop`()
  - `peek`()
  - `returnStack`()

  ### Peek -> Mental model


  * `self.stack` → the container
  * `self.top` → the position
  * `self.stack[self.top]` → the value of the stack at that position

#### 🧊 `class` FixedArrayStack, Attribute Access Design

┣🧊 `__init__(self, capacity)`
┣ `self.stack`
┣ `self.capacity`
┗ `self.top`

┣🧊 `isEmpty(self) `
┗ `self.top`

┣🧊 `isFull(self) `
┣ `self.top`
┗ `self.capacity`

┣🧊 `peek(self)`
┣ `self.isEmpty()`
┗ `self.stack[self.top]`

┣🧊 `push(self,value)`
┣ `self.isFull()`
┣ `self.stack[self.top]`
┗ `self.top`

┣🧊 `pop(self)`
┣ `self.isEmpty()`
┣ `self.top`
┗ `self.stack`

┣🧊 `returnStack(self)`
┣ `self.top`
┗ `self.stack`

### `Layer 2`: undo/redo program

#### Class to contain

* `data_stack`
* `history_stack`

#### Methods

- `push`(value)
- `undo`()
- `redo`()

#### 🧊 `class` UndoRedoManager, Attribute Access Design

┣🧊 `__init__(self, capacity)`
┣ `self.history_stack`
┗ `self.data_stack`

┣🧊 `push(self,value)`
┣ `self.data_stack.push(value)`
┗ `self.history_stack`
      ┗ `self.history_stack.top`
      ┗ `self.history_stack.stack`
      ┗ `self.history_stack.capacity`

┣🧊 `undo(self)`
┣ `self.data_stack`
      ┗ `self.data_stack.isEmpty()`
      ┗ `self.data_stack.pop()`
┗ `self.history_stack.push(popped)`

┣🧊 `redo(self)`
┣ `self.history_stack`
      ┗ `self.history_stack.isEmpty()`
      ┗ `self.history_stack.pop()`
┗ `self.data_stack.push(popped)`

┣🧊 `returnHistory(self)`
┗ `self.history_stack.returnStack()`

## Empty protocol

- When empty, `stack.top.index` == -1

  - This is because top represents an array index and when capacity is fully open, the first position is 0
  - Upon the push() operation, `stack.top.index` += 1

## Full stack protocol

- The condition to mark the stack as full is `stack.top` == `stack.size` - 1

  - This is because with zero-indexing, the array will start at `n-1`, which is zero.

## Summary

### Push:

* check if full
* move top up

* place value

### Pop:

* check if empty

* read value at top
* move top down
