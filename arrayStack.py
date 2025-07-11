class ArrayStack:
  def __init__(self, capacity):
    self.stack = [None] * capacity
    self.capacity = capacity
    self.n = -1
  def is_empty(self):
    return self.n == -1
  
  def is_full(self):
    return self.n == self.capacity - 1
  
  def push(self, data):
    if self.is_full():
      print("Stack is full. Cannot push.")
      return
    self.n += 1
    self.stack[self.n] = data
  def pop(self):
    if self.is_empty():
      return None
    value = self.stack[self.n]
    self.n -= 1 
    return value
  def peek(self):
    if self.is_empty():
      return None
    return self.stack[self.n]
  
  def doubleTheSize (self):
    new_stack = [None] * (self.capacity * 2)
    for i in range(self.n + 1):
        new_stack[i] = self.stack[i]
    self.stack = new_stack
    self.capacity *= 2
    
  def doubleTheSizeInPlace(self):
    self.stack.extend([None] * self.capacity)
    self.capacity *= 2
    