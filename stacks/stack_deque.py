from collections import deque

class Stack:
  def __init__(self):
    self.stack = deque()

  def push(self, data):  # O(1)
    self.stack.append(data)

  def pop(self):  # O(1)
    return None if self.isEmpty() else self.stack.pop()

  def top(self):  # O(1)
    return None if self.isEmpty() else self.stack[-1]

  def isEmpty(self):  # O(1)
    return len(self.stack) == 0

  def size(self):  # O(1)
    return len(self.stack)

  def clear(self):  # O(1)
    self.stack.clear()

  def contains(self, item):  # O(n)
    return item in self.stack

  def reverse(self):  # O(n)
    self.stack = deque(reversed(self.stack))

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
