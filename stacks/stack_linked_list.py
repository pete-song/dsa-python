class Node:
  def __init__(self, data):
    self.data = data
    self.next = None

class Stack:
  def __init__(self):
    self.head = None
    self.length = 0

  def push(self, data):  # O(1)
    new_node = Node(data)
    new_node.next = self.head
    self.head = new_node
    self.length += 1

  def pop(self):  # O(1)
    if self.isEmpty():
        return None
    data = self.head.data
    self.head = self.head.next
    self.length -= 1
    return data

  def top(self):  # O(1)
    return None if self.isEmpty() else self.head.data

  def isEmpty(self):  # O(1)
    return self.head is None

  def size(self):  # O(1)
    return self.length

  def clear(self):  # O(1)
    self.head = None
    self.length = 0

  def contains(self, item):  # O(n)
    temp = self.head
    while temp:
      if temp.data == item:
        return True
      temp = temp.next
    return False

  def reverse(self):  # O(n)
    prev = None
    curr = self.head
    while curr:
      next_node = curr.next
      curr.next = prev
      prev = curr
      curr = next_node
    self.head = prev

def main():
  s = Stack()

  # Test isEmpty() on an empty stack
  assert s.isEmpty() == True, "Test Failed: Stack should be empty initially."

  # Test size() on an empty stack
  assert s.size() == 0, "Test Failed: Stack size should be 0 initially."

  # Test pop() on an empty stack
  assert s.pop() is None, "Test Failed: Popping an empty stack should return None."

  # Test top() on an empty stack
  assert s.top() is None, "Test Failed: Top of an empty stack should return None."

  # Test push() and size()
  s.push(10)
  s.push(20)
  s.push(30)
  assert s.size() == 3, "Test Failed: Stack size should be 3 after pushing three elements."

  # Test top()
  assert s.top() == 30, "Test Failed: Top element should be 30."

  # Test contains()
  assert s.contains(20) == True, "Test Failed: Stack should contain 20."
  assert s.contains(40) == False, "Test Failed: Stack should not contain 40."

  # Test pop()
  assert s.pop() == 30, "Test Failed: Popped element should be 30."
  assert s.size() == 2, "Test Failed: Stack size should be 2 after popping."

  # Test reverse()
  s.reverse()
  assert s.pop() == 10, "Test Failed: After reversing, first pop should return 10."

  # Test clear()
  s.clear()
  assert s.isEmpty() == True, "Test Failed: Stack should be empty after clear()."
  assert s.size() == 0, "Test Failed: Stack size should be 0 after clear()."

  print("All tests passed!")

if __name__ == "__main__":
  main()
