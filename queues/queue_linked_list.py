class Node:
  def __init__(self, data):
    # Initializes a node with data and sets next to None
    self.data = data
    self.next = None

class QueueUsingLinkedList:
  def __init__(self):
    # Initializes the queue with an empty head, tail, and length of 0
    self.head = None
    self.tail = None
    self.length = 0

  # O(1) - Adds a value to the tail of the queue
  def enqueue(self, value):
    new_node = Node(value)
    if self.is_empty():
      # If queue is empty, both head and tail point to the new node
      self.head = self.tail = new_node
    else:
      # Otherwise, add the new node to the tail and update the tail
      self.tail.next = new_node
      self.tail = new_node
    self.length += 1

  # O(1) - Removes the value from the head of the queue and returns it
  def dequeue(self):
    if self.is_empty():
      return None  # Queue is empty
    temp = self.head
    self.head = self.head.next
    if self.head == None:
      self.tail = None  # If the queue becomes empty, set tail to None
    self.length -= 1
    return temp

  # O(1) - Checks if the queue is empty
  def is_empty(self):
    return self.length == 0

  # O(1) - Returns the number of elements in the queue
  def size(self):
    return self.length

  # O(1) - Returns the value at the front of the queue without removing it
  def peek(self):
    if self.is_empty():
      return None
    return self.head.data

  # O(1) - Clears the entire queue (sets head, tail, and length to zero)
  def clear(self):
    self.head = self.tail = None
    self.length = 0

  # O(n) - Checks if the queue contains the specified value
  def contains(self, value):
    curr = self.head
    while curr:
      if curr.data == value:
        return True  # Value found in the queue
      curr = curr.next
    return False  # Value not found

  # O(n) - Converts the queue to a list of values
  def to_list(self):
    elements = []
    curr = self.head
    while curr:
      elements.append(curr.data)
      curr = curr.next
    return elements

  # O(n) - Reverses the queue by changing the direction of links
  def reverse(self):
    prev = None
    curr = self.head
    while curr:
      next_node = curr.next  # Store the next node
      curr.next = prev       # Reverse the current node's link
      prev = curr            # Move prev and current one step forward
      curr = next_node
    self.head, self.tail = self.tail, self.head  # Swap head and tail

  # O(m) - Adds all elements from an iterable to the queue
  def extend(self, iterable):
    for item in iterable:
      self.enqueue(item)

  # O(n) - Creates a shallow copy of the queue
  def copy(self):
    new_queue = QueueUsingLinkedList()
    curr = self.head
    while curr:
      new_queue.enqueue(curr.data)
      curr = curr.next
    return new_queue

def test():
  # Test case 1: Initialize the queue and check if it's empty
  queue = QueueUsingLinkedList()
  assert queue.is_empty() == True, "Queue should be empty initially"
  assert queue.size() == 0, "Queue size should be 0 initially"

  # Test case 2: Enqueue elements and check if the size increases
  queue.enqueue(1)
  queue.enqueue(2)
  queue.enqueue(3)
  assert queue.is_empty() == False, "Queue should not be empty after enqueuing elements"
  assert queue.size() == 3, "Queue size should be 3 after enqueuing 3 elements"

  # Test case 3: Peek at the front element
  assert queue.peek() == 1, "Peek should return the front element (1)"

  # Test case 4: Dequeue elements and check if the size decreases
  dequeued = queue.dequeue()
  assert dequeued.data == 1, "Dequeue should return the front element (1)"
  assert queue.size() == 2, "Queue size should be 2 after dequeuing 1 element"

  # Test case 5: Check the front element after dequeuing
  assert queue.peek() == 2, "Peek should return the front element (2) after dequeuing"

  # Test case 6: Dequeue all elements
  queue.dequeue()  # Removes 2
  queue.dequeue()  # Removes 3
  assert queue.is_empty() == True, "Queue should be empty after dequeuing all elements"

  # Test case 7: Clear the queue
  queue.enqueue(4)
  queue.enqueue(5)
  queue.clear()
  assert queue.is_empty() == True, "Queue should be empty after clearing"
  assert queue.size() == 0, "Queue size should be 0 after clearing"

  # Test case 8: Check if contains method works
  queue.enqueue(6)
  queue.enqueue(7)
  assert queue.contains(6) == True, "Queue should contain 6"
  assert queue.contains(7) == True, "Queue should contain 7"
  assert queue.contains(8) == False, "Queue should not contain 8"

  # Test case 9: Convert queue to list and check the result
  queue_list = queue.to_list()
  assert queue_list == [6, 7], "Queue should be converted to list [6, 7]"

  # Test case 10: Reverse the queue and check the result
  queue.reverse()
  queue_list_reversed = queue.to_list()
  assert queue_list_reversed == [7, 6], "Queue should be reversed to [7, 6]"

  # Test case 11: Extend the queue with an iterable
  queue.extend([8, 9])
  queue_list_extended = queue.to_list()
  assert queue_list_extended == [7, 6, 8, 9], "Queue should be extended to [7, 6, 8, 9]"

  # Test case 12: Copy the queue and check if the elements are the same
  new_queue = queue.copy()
  assert new_queue.to_list() == [7, 6, 8, 9], "Copied queue should be [7, 6, 8, 9]"
  assert new_queue.is_empty() == False, "Copied queue should not be empty"

  # Test case 13: Check if the original and copied queues are separate instances
  new_queue.enqueue(10)
  assert new_queue.size() == 5, "Copied queue size should be 5 after adding 10"
  assert queue.size() == 4, "Original queue size should still be 4"

  print("All test cases passed!")

if __name__ == "__main__":
  test()
