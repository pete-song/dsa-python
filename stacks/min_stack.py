class MinStack:
  def __init__(self):
    self.stack = []
    self.min_stack = []  # Maintains the minimum values

  def push(self, data):  # O(1)
    self.stack.append(data)
    if not self.min_stack or self.min_stack[-1] >= data:
      self.min_stack.append(data)

  def pop(self):  # O(1)
    if not self.stack:
      return None
    popped = self.stack.pop()
    if popped == self.min_stack[-1]:
      self.min_stack.pop()
    return popped

  def top(self):  # O(1)
    return None if not self.stack else self.stack[-1]

  def getMin(self):  # O(1)
    return None if not self.min_stack else self.min_stack[-1]

  def isEmpty(self):  # O(1)
    return len(self.stack) == 0

  def size(self):  # O(1)
    return len(self.stack)

  def clear(self):  # O(1)
    self.stack = []
    self.min_stack = []

def main():
  s = MinStack()

  # Test isEmpty() on a new stack
  assert s.isEmpty() == True, "Test Failed: Stack should be empty initially."

  # Test getMin() on an empty stack
  assert s.getMin() is None, "Test Failed: getMin() should return None for an empty stack."

  # Test push() and getMin()
  s.push(5)
  assert s.getMin() == 5, "Test Failed: Minimum should be 5."

  s.push(3)
  assert s.getMin() == 3, "Test Failed: Minimum should be 3."

  s.push(7)
  assert s.getMin() == 3, "Test Failed: Minimum should still be 3 after pushing 7."

  s.push(2)
  assert s.getMin() == 2, "Test Failed: Minimum should be 2."

  # Test pop() and getMin()
  assert s.pop() == 2, "Test Failed: Popped element should be 2."
  assert s.getMin() == 3, "Test Failed: Minimum should revert to 3."

  assert s.pop() == 7, "Test Failed: Popped element should be 7."
  assert s.getMin() == 3, "Test Failed: Minimum should still be 3."

  assert s.pop() == 3, "Test Failed: Popped element should be 3."
  assert s.getMin() == 5, "Test Failed: Minimum should revert to 5."

  assert s.pop() == 5, "Test Failed: Popped element should be 5."
  assert s.getMin() is None, "Test Failed: Minimum should be None after popping everything."

  # Test isEmpty() after popping all elements
  assert s.isEmpty() == True, "Test Failed: Stack should be empty."

  # Test size()
  assert s.size() == 0, "Test Failed: Stack size should be 0."

  # Test clear()
  s.push(10)
  s.push(20)
  s.clear()
  assert s.isEmpty() == True, "Test Failed: Stack should be empty after clear()."
  assert s.getMin() is None, "Test Failed: Minimum should be None after clear()."

  print("All tests passed!")

if __name__ == "__main__":
    main()
