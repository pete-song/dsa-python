class Stack:
  def __init__(self):
    self.stack = []
    self.length = 0

  def display(self):
    print(self.stack)

  def push(self, data): # Adds an item to the top of the stack. O(1)
    self.stack.append(data)
    self.length += 1

  def pop(self): # Removes and returns the top item. O(1)
    if self.isEmpty():
      return None
    popped = self.stack.pop()
    self.length -= 1
    return popped # pop can be done with linked list

  def top(self): # Returns the top item without removing it. O(1)
    if self.isEmpty():
      return None
    return self.stack[-1]

  def isEmpty(self): # Checks if the stack is empty. O(1)
    return len(self.stack) == 0

  def size(self): # Returns the number of elements in the stack. O(1)
    return len(self.stack)

  def clear(self): # Removes all elements from the stack. O(1)
    self.stack = []
    self.length = 0

  def contains(self, item): # Checks if an item exists in the stack. O(n)
    return item in self.stack

  def reverse(self): # Reverses the stack. O(n)
    temp_stack = Stack()
    while not self.isEmpty():  # O(n) time complexity to pop all elements
      temp_stack.push(self.pop())
    self.stack = temp_stack.stack
    # We could use self.stack.reverse() instead

def main():
    s = Stack()

    # Test isEmpty on new stack
    assert s.isEmpty() == True, "Test Failed: Stack should be empty"

    # Test size on empty stack
    assert s.size() == 0, "Test Failed: Stack size should be 0"

    # Test push
    s.push(10)
    assert s.isEmpty() == False, "Test Failed: Stack should not be empty after push"
    assert s.size() == 1, "Test Failed: Stack size should be 1"
    assert s.top() == 10, "Test Failed: Top element should be 10"

    # Test push multiple elements
    s.push(20)
    s.push(30)
    assert s.size() == 3, "Test Failed: Stack size should be 3"
    assert s.top() == 30, "Test Failed: Top element should be 30"

    # Test pop
    assert s.pop() == 30, "Test Failed: Popped element should be 30"
    assert s.size() == 2, "Test Failed: Stack size should be 2"
    assert s.top() == 20, "Test Failed: Top element should be 20"

    # Test contains
    assert s.contains(10) == True, "Test Failed: Stack should contain 10"
    assert s.contains(30) == False, "Test Failed: Stack should not contain 30"

    # Test reverse
    s.reverse()
    assert s.pop() == 10, "Test Failed: After reverse, top element should be 10"
    assert s.pop() == 20, "Test Failed: After reverse, top element should be 20"

    # Test pop on empty stack
    assert s.pop() == None, "Test Failed: Popping empty stack should return None"

    # Test clear
    s.push(5)
    s.push(15)
    s.clear()
    assert s.isEmpty() == True, "Test Failed: Stack should be empty after clear"
    assert s.size() == 0, "Test Failed: Stack size should be 0 after clear"

    print("All tests passed!")

if __name__ == "__main__":
  main()
