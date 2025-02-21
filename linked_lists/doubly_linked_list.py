class Node:
  def __init__(self, data):
    self.data = data  # Store data
    self.next = None  # Pointer to next node
    self.prev = None  # Pointer to previous node

class DoublyLinkedList:
  def __init__(self):
    self.head = None  # First node
    self.tail = None  # Last node
    self.length = 0   # Number of elements

  def printFirst(self):
    print(self.head.data if self.head else "List is empty")

  def printLast(self):
    print(self.tail.data if self.tail else "List is empty")

  def printDLL(self):
    temp = self.head
    while temp:
      print(temp.data, end=" <-> ")
      temp = temp.next
    print("None")

  def get(self, index):
    if index < 0 or index >= self.length:
      return None  # Out of bounds

    temp = self.head
    for _ in range(index):
      temp = temp.next
    return temp  # Returns the node at index

  def set(self, index, data):
    temp = self.get(index)
    if temp:
      temp.data = data
      return True
    return False  # Index out of range

  def prepend(self, data):
    new_node = Node(data)
    new_node.next = self.head  # New node points to old head

    if self.head:  # If list is not empty
      self.head.prev = new_node
    else:  # If list is empty, set tail too
      self.tail = new_node

    self.head = new_node  # Update head
    self.length += 1

  def append(self, data):
    new_node = Node(data)
    new_node.prev = self.tail  # New node points to old tail

    if self.tail:  # If list is not empty
      self.tail.next = new_node
    else:  # If list is empty, set head too
      self.head = new_node

    self.tail = new_node  # Update tail
    self.length += 1

  def insert(self, index, data):
    if index < 0 or index > self.length:
      return False  # Invalid index

    if index == 0:
      self.prepend(data)
      return True

    if index == self.length:
      self.append(data)
      return True

    new_node = Node(data)
    temp = self.get(index - 1)  # Get previous node

    new_node.next = temp.next  # New node points to node at index
    new_node.prev = temp  # New node points back to previous node
    temp.next.prev = new_node  # Adjust next node's previous pointer
    temp.next = new_node  # Previous node's next points to new node

    self.length += 1
    return True

  def popFront(self):
    if not self.head:  # Empty list
      return None

    removed_data = self.head.data

    if self.head == self.tail:  # Only one element
      self.head = None
      self.tail = None
    else:
      self.head = self.head.next  # Move head forward
      self.head.prev = None  # Remove old head reference

    self.length -= 1
    return removed_data

  def popBack(self):
    if not self.tail:  # Empty list
      return None

    removed_data = self.tail.data

    if self.head == self.tail:  # Only one element
      self.head = None
      self.tail = None
    else:
      self.tail = self.tail.prev  # Move tail backward
      self.tail.next = None  # Remove old tail reference

    self.length -= 1
    return removed_data

  def popAt(self, index):
    if index < 0 or index >= self.length:  # Check valid index
      return None

    if index == 0:
      return self.popFront()

    if index == self.length - 1:
      return self.popBack()

    temp = self.get(index)  # Get node to remove
    removed_data = temp.data

    temp.prev.next = temp.next  # Adjust previous node's next pointer
    temp.next.prev = temp.prev  # Adjust next node's prev pointer

    self.length -= 1
    return removed_data  # Return deleted value

# Time Complexity:
# - get(index) -> O(n) (traverse list to find index)
# - set(index, data) -> O(n) (find node + update data)
# - prepend(data) -> O(1) (insert at head)
# - append(data) -> O(1) (insert at tail)
# - insert(index, data) -> O(n) (traverse + insert)
# - popFront() -> O(1) (remove head)
# - popBack() -> O(1) (remove tail)
# - popAt(index) -> O(n) (find + remove)
#
# Space Complexity:
# - O(n) for storing n nodes

def main():
  dll = DoublyLinkedList()

  print("=== TESTING DOUBLY LINKED LIST ===\n")

  # Test: Append Elements
  print("Appending elements: 10, 20, 30")
  dll.append(10)
  dll.append(20)
  dll.append(30)
  dll.printDLL()  # Expected: 10 <-> 20 <-> 30 <-> None
  print()

  # Test: Prepend Elements
  print("Prepending elements: 5, 0")
  dll.prepend(5)
  dll.prepend(0)
  dll.printDLL()  # Expected: 0 <-> 5 <-> 10 <-> 20 <-> 30 <-> None
  print()

  # Test: Insert Elements
  print("Inserting 15 at index 3")
  dll.insert(3, 15)
  dll.printDLL()  # Expected: 0 <-> 5 <-> 10 <-> 15 <-> 20 <-> 30 <-> None
  print()

  # Test: Get Elements
  print(f"Get element at index 2: {dll.get(2).data}")  # Expected: 10
  print(f"Get element at index 4: {dll.get(4).data}")  # Expected: 20
  print()

  # Test: Set Elements
  print("Updating index 2 to 12")
  dll.set(2, 12)
  dll.printDLL()  # Expected: 0 <-> 5 <-> 12 <-> 15 <-> 20 <-> 30 <-> None
  print()

  # Test: Pop Front
  print("Popping from front")
  print(f"Removed: {dll.popFront()}")  # Expected: 0
  dll.printDLL()  # Expected: 5 <-> 12 <-> 15 <-> 20 <-> 30 <-> None
  print()

  # Test: Pop Back
  print("Popping from back")
  print(f"Removed: {dll.popBack()}")  # Expected: 30
  dll.printDLL()  # Expected: 5 <-> 12 <-> 15 <-> 20 <-> None
  print()

  # Test: Pop At Index
  print("Popping element at index 1")
  print(f"Removed: {dll.popAt(1)}")  # Expected: 12
  dll.printDLL()  # Expected: 5 <-> 15 <-> 20 <-> None
  print()

  # Edge Case: Pop from empty list
  print("Popping all elements...")
  while dll.length > 0:
    print(f"Removed: {dll.popFront()}")
    dll.printDLL()

  print("\nTrying to pop from an empty list:")
  print(f"PopFront: {dll.popFront()}")  # Expected: None
  print(f"PopBack: {dll.popBack()}")    # Expected: None
  print(f"PopAt(0): {dll.popAt(0)}")    # Expected: Invalid index

if __name__ == "__main__":
  main()


'''
=== TESTING DOUBLY LINKED LIST ===

Appending elements: 10, 20, 30
10 <-> 20 <-> 30 <-> None

Prepending elements: 5, 0
0 <-> 5 <-> 10 <-> 20 <-> 30 <-> None

Inserting 15 at index 3
0 <-> 5 <-> 10 <-> 15 <-> 20 <-> 30 <-> None

Get element at index 2: 10
Get element at index 4: 20

Updating index 2 to 12
0 <-> 5 <-> 12 <-> 15 <-> 20 <-> 30 <-> None

Popping from front
Removed: 0
5 <-> 12 <-> 15 <-> 20 <-> 30 <-> None

Popping from back
Removed: 30
5 <-> 12 <-> 15 <-> 20 <-> None

Popping element at index 1
Removed: 12
5 <-> 15 <-> 20 <-> None

Popping all elements...
Removed: 5
15 <-> 20 <-> None
Removed: 15
20 <-> None
Removed: 20
None

Trying to pop from an empty list:
PopFront: None
PopBack: None
Invalid index
PopAt(0): None
'''
