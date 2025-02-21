class Node:
  def __init__(self, data):
    self.data = data  # Stores the data
    self.next = None  # Pointer to the next node

class SinglyLinkedList:
  def __init__(self):
    self.head = None  # Head of the linked list
    self.length = 0   # Track the number of nodes

  # Time Complexity: O(n) (Traverses up to index)
  def get(self, index):
    """Retrieve node at a specific index (0-based)."""
    if index < 0 or index >= self.length:
      return None  # Index out of bounds

    current = self.head
    for _ in range(index):
      current = current.next

    return current  # Returns the node (not just data)

  # Time Complexity: O(1) (Constant time insertion at head)
  def prepend(self, data):
    """Insert a new node at the beginning."""
    new_node = Node(data)
    new_node.next = self.head  # Point new node to current head
    self.head = new_node  # Update head to the new node
    self.length += 1

  # Time Complexity: O(n) (Traverses entire list to insert at end)
  def append(self, data):
    """Insert a new node at the end."""
    new_node = Node(data)
    if self.head is None:  # If list is empty, make new node the head
      self.head = new_node
    else:
      current = self.head
      while current.next:  # Traverse to the last node
        current = current.next
      current.next = new_node
    self.length += 1

  # Time Complexity: O(n) (Traverses to index before inserting)
  def insert(self, index, data):
    """Insert a new node at a given index."""
    if index == 0:
      return self.prepend(data)
    if index == self.length:
      return self.append(data)
    if index < 0 or index > self.length:
      return None  # Index out of bounds

    new_node = Node(data)
    previous = self.get(index - 1)  # Get node before the insertion point
    new_node.next = previous.next
    previous.next = new_node
    self.length += 1
    return True

  # Time Complexity: O(n) (Traverses the entire list)
  def printSLL(self):
    """Prints all elements in the linked list."""
    current = self.head
    while current:
      print(current.data, end=" -> ")
      current = current.next
    print("None")

  # Time Complexity: O(n) (Finds the node before updating)
  def set(self, index, data):
    """Update the value at a given index."""
    current = self.get(index)
    if current:
      current.data = data
      return True
    return False  # Index out of bounds

  # Time Complexity: O(1) (Removes first element directly)
  def popFront(self):
    """Remove and return the first node."""
    if self.head is None:
      return None  # Empty list

    current = self.head
    self.head = self.head.next  # Move head to the next node
    current.next = None  # Remove reference
    self.length -= 1
    return current.data

  # Time Complexity: O(n) (Traverses to last node before deleting)
  def popBack(self):
    """Remove and return the last node."""
    if self.head is None:
      return None  # Empty list

    current = self.head
    previous = None
    while current.next:
      previous = current
      current = current.next

    if previous:
      previous.next = None  # Remove last node
    else:
      self.head = None  # If only one node was present

    self.length -= 1
    return current.data

  # Time Complexity: O(n) (Traverses to index before deleting)
  def popAt(self, index):
    """Remove and return the node at a specific index."""
    if self.head is None or index < 0 or index >= self.length:
      return None  # Invalid index or empty list

    if index == 0:
      return self.popFront()
    if index == self.length - 1:
      return self.popBack()

    previous = self.get(index - 1)  # Get node before target
    current = previous.next
    previous.next = current.next  # Skip the target node
    self.length -= 1
    return current.data

def main():
    sll = SinglyLinkedList()

    print("\n=== TESTING SINGLY LINKED LIST ===\n")

    print("Appending elements: 1 to 10")
    for i in range(1, 11):
        sll.append(i)
    sll.printSLL()

    print("Prepending element: 0")
    sll.prepend(0)
    sll.printSLL()

    print("Inserting 33 at index 3")
    sll.insert(3, 33)
    sll.printSLL()

    print("Get element at index 2:", sll.get(2).data)

    print("Updating index 2 to 100")
    sll.set(2, 100)
    sll.printSLL()

    print("Popping from front:", sll.popFront())
    sll.printSLL()

    print("Popping from back:", sll.popBack())
    sll.printSLL()

    print("Popping element at index 4:", sll.popAt(4))
    sll.printSLL()

    print("Popping all elements...")
    while sll.length > 0:
        print(f"Removed: {sll.popFront()}")
        sll.printSLL()

    print("\nTrying to pop from an empty list:")
    print(f"PopFront: {sll.popFront()}")
    print(f"PopBack: {sll.popBack()}")
    print(f"PopAt(0): {sll.popAt(0)}")

if __name__ == "__main__":
    main()
