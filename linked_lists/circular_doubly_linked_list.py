class Node:
  def __init__(self, data):
    self.data = data
    self.next = None
    self.prev = None

class CircularDoublyLinkedList:
  def __init__(self):
    self.head = None
    self.tail = None
    self.length = 0

  def isEmpty(self):  # O(1)
    return self.length == 0

  def size(self):  # O(1)
    return self.length

  def get(self, index):  # O(n) in the worst case
    if index < 0 or index >= self.length:
      return None

    temp = self.head
    for _ in range(index):  # Linear traversal
      temp = temp.next
    return temp.data

  def set(self, index, data):  # O(n) in the worst case
    if index < 0 or index >= self.length:
      return False

    temp = self.head
    for _ in range(index):  # Linear traversal
      temp = temp.next

    temp.data = data
    return True

  def append(self, data):  # O(1)
    # Appending at the tail is a constant-time operation
    new_node = Node(data)
    if self.isEmpty():
      self.head = self.tail = new_node
      new_node.next = new_node.prev = new_node
    else:
      new_node.prev = self.tail
      new_node.next = self.head
      self.tail.next = new_node
      self.head.prev = new_node
      self.tail = new_node
    self.length += 1

  def prepend(self, data):  # O(1)
    # Prepending at the head is a constant-time operation
    new_node = Node(data)
    if self.isEmpty():
      self.head = self.tail = new_node
      new_node.next = new_node.prev = new_node
    else:
      new_node.next = self.head
      new_node.prev = self.tail
      self.head.prev = new_node
      self.tail.next = new_node
      self.head = new_node
    self.length += 1

  def delete(self, data):  # O(n) in the worst case
    if self.isEmpty():
      return False

    temp = self.head
    for _ in range(self.length):  # Traverses at most O(n) elements
      if temp.data == data:
        if self.length == 1:
          self.head = self.tail = None
        else:
          temp.prev.next = temp.next
          temp.next.prev = temp.prev
          if temp == self.head:
            self.head = temp.next
          if temp == self.tail:
            self.tail = temp.prev
        self.length -= 1
        return True
      temp = temp.next
    return False

  def find(self, data):  # O(n)
    if self.isEmpty():
      return False

    temp = self.head
    for i in range(self.length):  # Linear search
      if temp.data == data:
        return i
      temp = temp.next
    return False

  def display(self):  # O(n)
    if self.isEmpty():
      print("List is empty")
      return
    temp = self.head
    for _ in range(self.length):  # Traverses O(n) elements
      print(temp.data, end=" <-> ")
      temp = temp.next
    print("(back to head)")

  def reverse(self):  # O(n)
    if self.isEmpty():
      return

    temp = self.head
    for _ in range(self.length):  # Reversing links in O(n)
      temp.next, temp.prev = temp.prev, temp.next
      temp = temp.prev

    self.head, self.tail = self.tail, self.head

  def removeDuplicates(self):  # O(n)
    if self.isEmpty() or self.length == 1:
      return

    seen = set()
    temp = self.head
    for _ in range(self.length):  # Each node is visited once
      if temp.data in seen:
        temp.prev.next = temp.next
        temp.next.prev = temp.prev
        if temp == self.tail:
          self.tail = temp.prev
        self.length -= 1
      else:
        seen.add(temp.data)
      temp = temp.next

  def insert_after(self, data, new_data):  # O(n) in the worst case
    if self.isEmpty():
      return False

    temp = self.head
    for _ in range(self.length):  # Linear traversal to find the node
      if temp.data == data:
        new_node = Node(new_data)
        new_node.prev = temp
        new_node.next = temp.next

        temp.next.prev = new_node
        temp.next = new_node

        if temp == self.tail:
          self.tail = new_node

        self.length += 1
        return True
      temp = temp.next

    return False

  def insert_before(self, data, new_data):  # O(n) in the worst case
    if self.isEmpty():
      return False

    temp = self.head
    for _ in range(self.length):  # Linear traversal to find the node
      if temp.data == data:
        new_node = Node(new_data)
        new_node.next = temp
        new_node.prev = temp.prev
        temp.prev.next = new_node
        temp.prev = new_node

        if temp == self.head:
          self.head = new_node
        self.length += 1
        return True
      temp = temp.next
    return False

  def clear(self):  # O(1)
    self.head = None
    self.tail = None
    self.length = 0

def main():
  cdll = CircularDoublyLinkedList()

  # Test: Empty List
  assert cdll.isEmpty() == True
  assert cdll.size() == 0

  # Test: Append Elements
  cdll.append(10)
  cdll.append(20)
  cdll.append(30)
  assert cdll.size() == 3
  assert cdll.head.data == 10
  assert cdll.tail.data == 30

  # Test: Prepend Element
  cdll.prepend(5)
  assert cdll.head.data == 5
  assert cdll.size() == 4

  # Test: Get Element
  assert cdll.get(0) == 5
  assert cdll.get(2) == 20

  # Test: Set Element
  assert cdll.set(1, 15) == True
  assert cdll.get(1) == 15

  # Test: Insert After
  assert cdll.insert_after(20, 25) == True  # Insert after 20
  assert cdll.get(3) == 25  # New element at index 3
  assert cdll.tail.data == 30  # Tail should remain unchanged

  # Test: Insert Before
  assert cdll.insert_before(15, 8) == True  # Insert before 10
  assert cdll.get(1) == 8  # Check new value at index 1

  # Test: Delete Element
  assert cdll.delete(15) == True  # Delete element 15
  assert cdll.size() == 5  # Ensure size is reduced

  # Test: Find Element
  assert cdll.find(25) == 3  # Check if 25 exists

  # Test: Reverse List
  cdll.reverse()
  assert cdll.head.data == 30  # Head should now be old tail
  assert cdll.tail.data == 5  # Tail should now be old head

  # Test: Remove Duplicates
  cdll.append(10)
  cdll.append(10)
  cdll.removeDuplicates()
  assert cdll.size() == 6 # Ensure duplicates removed

  # Test: Clear List
  cdll.clear()
  assert cdll.isEmpty() == True  # Ensure list is empty

  print("All tests passed!")

if __name__ == "__main__":
  main()
