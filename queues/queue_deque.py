from collections import deque

class QueueUsingDeque:
  def __init__(self):
    self.queue = deque()

  # Allows using len(queue) to get the queue size.
  def __len__(self):
    return self.size()

  # Returns a string representation of the queue for easy debugging.
  def __str__(self):
    return "Queue(" + " -> ".join(map(str, self.queue)) + ")"

  # Adds an element to the rear of the queue.
  def enqueue(self, value):
    self.queue.append(value)

  # Removes and returns the front element.
  def dequeue(self):
    if self.is_empty():
      return None
    return self.queue.popleft()

  # Returns the front element without removing it.
  def peek(self):
    if self.is_empty():
      raise IndexError("peek from an empty queue")
    return self.queue[0]

  # Checks if the queue is empty.
  def is_empty(self):
    return self.size() == 0

  # Returns the number of elements in the queue.
  def size(self):
    return len(self.queue)

  # Removes all elements from the queue.
  def clear(self):
    self.queue.clear()

  # Checks if a specific value is in the queue.
  def contains(self, value):
    return value in self.queue

  # Returns a list representation of the queue.
  def to_list(self):
    return list(self.queue)

  # Reverses the order of elements in the queue.
  def reverse(self):
    return self.queue.reverse()

  # Adds multiple elements to the queue from an iterable.
  def extend(self, iterable):
    return self.queue.extend(iterable)

  # Returns a shallow copy of the queue.
  def copy(self):
    new_queue = QueueUsingDeque()
    new_queue.queue = self.queue.copy()
    return new_queue

def test():
  q = QueueUsingDeque()

  # Test 1: Create an empty queue
  assert q.is_empty() == True, "Queue should be empty initially"
  assert len(q) == 0, "Queue size should be 0 initially"
  assert str(q) == "Queue()", "String representation of the queue should be empty"

  # Test 2: Enqueue elements into the queue
  q.enqueue(1)
  q.enqueue(2)
  q.enqueue(3)
  assert q.is_empty() == False, "Queue should not be empty after enqueueing"
  assert len(q) == 3, "Queue size should be 3 after enqueueing three elements"
  assert str(q) == "Queue(1 -> 2 -> 3)", "String representation of the queue should reflect the elements"

  # Test 3: Dequeue an element from the queue
  dequeued = q.dequeue()
  assert dequeued == 1, f"Expected dequeued value 1, but got {dequeued}"
  assert len(q) == 2, "Queue size should be 2 after dequeuing one element"
  assert str(q) == "Queue(2 -> 3)", "String representation should reflect remaining elements"

  # Test 4: Peek the front element
  q.enqueue(4)
  front = q.peek()
  assert front == 2, f"Expected front value 2, but got {front}"
  assert len(q) == 3, "Queue size should not change after peek"

  # Test 5: Peek on an empty queue should raise an exception
  q.dequeue()  # Remove 2
  q.dequeue()  # Remove 3
  q.dequeue()  # Remove 4
  try:
    q.peek()
  except IndexError as e:
    assert str(e) == "peek from an empty queue", f"Expected 'peek from an empty queue' error, but got {str(e)}"

  # Test 6: Dequeue from an empty queue
  q.enqueue(5)
  q.dequeue()  # Should dequeue 5
  assert q.dequeue() is None, "Dequeueing from an empty queue should return None"

  # Test 7: Clear the queue
  q.enqueue(6)
  q.enqueue(7)
  q.clear()
  assert q.is_empty() == True, "Queue should be empty after clearing"
  assert len(q) == 0, "Queue size should be 0 after clearing"

  # Test 8: Contains method
  q.enqueue(8)
  q.enqueue(9)
  assert q.contains(8) == True, "Queue should contain the element 8"
  assert q.contains(9) == True, "Queue should contain the element 9"
  assert q.contains(10) == False, "Queue should not contain the element 10"

  # Test 9: Convert queue to list
  q_list = q.to_list()
  assert q_list == [8, 9], f"Expected [8, 9], but got {q_list}"

  # Test 10: Reverse the queue
  q.reverse()
  assert str(q) == "Queue(9 -> 8)", "Queue should be reversed"

  # Test 11: Extend queue with an iterable
  q.extend([10, 11])
  assert str(q) == "Queue(9 -> 8 -> 10 -> 11)", "Queue should be extended with [10, 11]"

  # Test 12: Copy the queue
  q_copy = q.copy()
  assert str(q_copy) == "Queue(9 -> 8 -> 10 -> 11)", "Copied queue should have the same elements"
  q_copy.enqueue(12)
  assert str(q_copy) == "Queue(9 -> 8 -> 10 -> 11 -> 12)", "Copied queue should reflect changes"
  assert str(q) == "Queue(9 -> 8 -> 10 -> 11)", "Original queue should remain unchanged"

  # Test 13: Edge case of enqueueing and dequeuing the same element
  q.clear()
  q.enqueue(13)
  q.enqueue(13)
  assert q.size() == 2, "Queue size should be 2 after enqueueing two identical elements"
  assert q.dequeue() == 13, "First dequeue should return 13"
  assert q.dequeue() == 13, "Second dequeue should return 13"

  # Test 14: Edge case with large number of elements
  q.clear()
  for i in range(1000):
    q.enqueue(i)
  assert len(q) == 1000, "Queue size should be 1000 after enqueueing 1000 elements"
  assert q.dequeue() == 0, "First dequeue should return the first element"
  assert q.size() == 999, "Queue size should be 999 after one dequeue"

  # Test 15: Edge case with very large value
  q.clear()
  q.enqueue(10**6)
  assert q.peek() == 10**6, "Peek should return the correct large number"
  assert q.size() == 1, "Queue size should be 1 after enqueueing a large number"

  # Test 16: Dequeuing until empty
  while not q.is_empty():
    q.dequeue()
  assert q.is_empty() == True, "Queue should be empty after dequeuing all elements"
  assert len(q) == 0, "Queue size should be 0 after dequeuing all elements"

  print("All test cases passed.")

if __name__ == "__main__":
  test()
