class QueueUsingList:
  def __init__(self):  # O(1)
    self.queue = []

  # Adds an item to the end of the queue. O(1)
  def enqueue(self, data):
    self.queue.append(data)

  # Removes and returns the front item from the queue. O(n)
  def dequeue(self):
    if self.isEmpty():
      return None   # O(n) because all elements shift left
    return self.queue.pop(0)

  # Returns the front item without removing it. O(1)
  def front(self):
    return None if self.isEmpty() else self.queue[0]

  # Returns the last item without removing it. O(1)
  def rear(self):
    return None if self.isEmpty() else self.queue[-1]

  # Checks if the queue is empty. O(1)
  def isEmpty(self):
    return len(self.queue) == 0

  # Returns the number of elements in the queue. O(1)
  def size(self):
    return len(self.queue)

  # Removes all elements from the queue. O(1)
  def clear(self):
    self.queue = []

  # Checks if an item exists in the queue. O(n)
  def contains(self, item):
    return item in self.queue

  # Reverses the queue. O(n)
  def reverse(self):
    self.queue.reverse()

def main():
  q = QueueUsingList()

  # Test isEmpty() on a new queue
  assert q.isEmpty() == True, "Test Failed: Queue should be empty initially."

  # Test front() and rear() on an empty queue
  assert q.front() is None, "Test Failed: front() should return None for an empty queue."
  assert q.rear() is None, "Test Failed: rear() should return None for an empty queue."

  # Test enqueue() and size()
  q.enqueue(1)
  q.enqueue(2)
  q.enqueue(3)
  assert q.size() == 3, "Test Failed: Queue size should be 3."
  assert q.front() == 1, "Test Failed: Front should be 1."
  assert q.rear() == 3, "Test Failed: Rear should be 3."

  # Test dequeue()
  assert q.dequeue() == 1, "Test Failed: Dequeued element should be 1."
  assert q.size() == 2, "Test Failed: Queue size should be 2."
  assert q.front() == 2, "Test Failed: Front should now be 2."

  assert q.dequeue() == 2, "Test Failed: Dequeued element should be 2."
  assert q.dequeue() == 3, "Test Failed: Dequeued element should be 3."
  assert q.isEmpty() == True, "Test Failed: Queue should be empty after all dequeues."

  # Test dequeue() on an empty queue
  assert q.dequeue() is None, "Test Failed: Dequeue should return None for an empty queue."

  # Test clear()
  q.enqueue(10)
  q.enqueue(20)
  q.clear()
  assert q.isEmpty() == True, "Test Failed: Queue should be empty after clear()."
  assert q.size() == 0, "Test Failed: Queue size should be 0 after clear()."

  # Test contains()
  q.enqueue(5)
  q.enqueue(15)
  assert q.contains(5) == True, "Test Failed: Queue should contain 5."
  assert q.contains(10) == False, "Test Failed: Queue should not contain 10."

  # Test reverse()
  q.enqueue(25)
  q.reverse()
  assert q.front() == 25, "Test Failed: After reverse, front should be 25."
  assert q.rear() == 5, "Test Failed: After reverse, rear should be 5."

  print("All tests passed!")

if __name__ == "__main__":
  main()
