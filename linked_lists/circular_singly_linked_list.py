class Node:
  def __init__(self, data):
    self.data = data
    self.next = None

class CircularSinglyLinkedList:
  def __init__(self):
    self.head = None
    self.length = 0

  # Checks if the list is empty - O(1)
  def isEmpty(self):
    return self.length == 0

  # Returns the size of the list - O(1)
  def size(self):
    return self.length

  # Retrieves the data at a given index - O(n)
  def get(self, index):
    if index < 0 or index >= self.length:
      return None

    current = self.head
    for _ in range(index):  # Traverse to index
      current = current.next
    return current.data

  # Sets the data at a given index - O(n)
  def set(self, index, data):
    if index < 0 or index >= self.length:
      return False

    current = self.head
    for _ in range(index):
      current = current.next
    current.data = data
    return True

  # Adds a new node at the end - O(n)
  def append(self, data):
    new_node = Node(data)
    if self.isEmpty():
      self.head = new_node
      self.head.next = self.head
    else:
      temp = self.head
      while temp.next != self.head:
        temp = temp.next
      temp.next = new_node
      new_node.next = self.head
    self.length += 1

  # Adds a new node at the beginning - O(n)
  def prepend(self, data):
    new_node = Node(data)
    if self.isEmpty():
      self.head = new_node
      self.head.next = self.head
    else:
      temp = self.head
      while temp.next != self.head:
        temp = temp.next
      temp.next = new_node
      new_node.next = self.head
      self.head = new_node
    self.length += 1

  # Deletes a node by value - O(n)
  def delete(self, data):
    if self.isEmpty(): return False

    if self.head.data == data:
      if self.head.next == self.head:  # Single node case
        self.head = None
      else:
        temp = self.head
        while temp.next != self.head:
          temp = temp.next
        temp.next = self.head.next
        self.head = self.head.next
      self.length -= 1
      return True

    prev = None
    temp = self.head
    while temp.next != self.head and temp.data != data:
      prev = temp
      temp = temp.next

    if temp.data == data:
      prev.next = temp.next
      self.length -= 1
      return True

    return False

  # Searches for a node by value - O(n)
  def find(self, data):
    if self.isEmpty():
      return None
    temp = self.head
    while temp.data != data and temp.next != self.head:
      temp = temp.next
    return temp if temp.data == data else None

  # Displays the list - O(n)
  def display(self):
    if self.isEmpty():
      print("List is empty")
      return
    temp = self.head
    while True:
      print(temp.data, end=" -> ")
      temp = temp.next
      if temp == self.head:
        break
    print("(back to head)")

  # Reverses the circular list - O(n)
  def reverse(self):
    if self.isEmpty():
      return

    prev = None
    curr = self.head
    next = None

    while curr.next != self.head:
      next = curr.next
      curr.next = prev
      prev = curr
      curr = next

    curr.next = prev
    self.head.next = curr
    self.head = curr

  # Removes duplicate values - O(n)
  def removeDuplicates(self):
    if self.isEmpty():
      return

    seen = set()
    prev = None
    curr = self.head

    while curr.next != self.head:
      prev = curr
      if curr.data in seen:
        prev.next = curr.next
        self.length -= 1
      else:
        seen.add(curr.data)
        prev = curr
      curr = curr.next

    if curr.data in seen:
      prev.next = curr.next
      self.length -= 1
    else:
      seen.add(curr.data)

  # Inserts a node after a given value - O(n)
  def insert_after(self, data, new_data):
    node = self.find(data)
    if node:
      new_node = Node(new_data)
      new_node.next = node.next
      node.next = new_node
      self.length += 1
      return True
    return False

  # Inserts a node before a given value - O(n)
  def insert_before(self, data, new_data):
    if self.isEmpty():
      return False

    if self.head.data == data:
      self.prepend(new_data)
      return True

    prev = None
    temp = self.head
    while temp.data != data and temp.next != self.head:
      prev = temp
      temp = temp.next

    if temp.data == data:
      new_node = Node(new_data)
      new_node.next = temp
      prev.next = new_node
      self.length += 1
      return True

    return False

  # Clears the list - O(1)
  def clear(self):
    self.head = None
    self.length = 0

def main():
  # Create a new circular linked list
  csll = CircularSinglyLinkedList()

  # Test isEmpty() on new list
  assert csll.isEmpty() == True, "Expected list to be empty"

  # Test append()
  csll.append(10)
  csll.append(20)
  csll.append(30)
  assert csll.size() == 3, "Expected size to be 3 after appending"

  # Test display()
  print("Displaying list after appends:")
  csll.display()  # Expected: 10 -> 20 -> 30 -> (back to head)

  # Test get() for valid index
  assert csll.get(0) == 10, "Expected 10 at index 0"
  assert csll.get(1) == 20, "Expected 20 at index 1"
  assert csll.get(2) == 30, "Expected 30 at index 2"

  # Test set() for valid index
  csll.set(1, 25)  # Set the value at index 1 to 25
  assert csll.get(1) == 25, "Expected 25 at index 1 after set"

  # Test prepend()
  csll.prepend(5)
  assert csll.get(0) == 5, "Expected 5 at index 0 after prepend"
  assert csll.size() == 4, "Expected size to be 4 after prepend"

  # Test find()
  node = csll.find(25)
  assert node is not None and node.data == 25, "Expected node with data 25"
  node = csll.find(100)  # Data that doesn't exist
  assert node is None, "Expected None for data not found"

  # Test delete()
  csll.display()
  assert csll.delete(25) == True, "Expected deletion to be successful"
  assert csll.size() == 3, "Expected size to be 3 after deletion"
  assert csll.find(25) is None, "Expected node with data 20 to be deleted"

  # Test delete non-existing element
  assert csll.delete(100) == False, "Expected deletion to fail for non-existing element"

  # Test reverse()
  csll.reverse()
  print("Displaying list after reverse:")
  csll.display()  # Expected: 30 -> 25 -> 5 -> (back to head)

  # Test removeDuplicates()
  csll.append(25)  # Add a duplicate value
  csll.append(5)    # Add a duplicate value
  csll.removeDuplicates()
  print("Displaying list after removing duplicates:")
  csll.display()  # Expected: 30 -> 25 -> 5 -> (back to head)

  # Test insert_after()
  assert csll.insert_after(25, 40) == True, "Expected successful insertion after 25"
  print("Displaying list after insert_after:")
  csll.display()  # Expected: 30 -> 25 -> 40 -> 5 -> (back to head)

  # Test insert_before()
  assert csll.insert_before(40, 35) == True, "Expected successful insertion before 40"
  print("Displaying list after insert_before:")
  csll.display()  # Expected: 30 -> 25 -> 35 -> 40 -> 5 -> (back to head)

  # Test clear()
  csll.clear()
  assert csll.isEmpty() == True, "Expected list to be empty after clear"

  print("All tests passed successfully!")

if __name__ == "__main__":
  main()
