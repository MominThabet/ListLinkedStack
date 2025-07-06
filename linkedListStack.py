
from node import Node
class LinkedListStack:
  def __init__(self):
    self.top = None
  
  def push(self ,data):
    new_Node = Node(data)
    new_Node.next = self.top
    self.top = new_Node

  def pop(self):
    if self.top is None :
      return "Stack is Empty"
    curr = self.top
    self.top = self.top.next
    return curr.data
  
  def isEmpty(self):
    return self.top is None

  def clear(self):
    self.top = None
  
  def peek(self):
    if self.top is None :
      return None
    return self.top.data
  