class MinHeap:
  # Initializes an empty list to store heap elements
  def __init__(self):
    self.heap = []

  # Returns the parent index of the element at index i
  def parent(self, i):
    return (i - 1) // 2

  # Returns the left child index of the element at index i
  def left_child(self, i):
    return 2 * i + 1

  # Returns the right child index of the element at index i
  def right_child(self, i):
    return 2 * i + 2

  # Swap elements at indices i and j
  def swap(self, i, j):
    self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

  # Maintains the min heap property by ensuring the subtree rooted at index i is a valid heap
  def heapify(self, i):


  # Insert a new key to the heap
  def insert(self, key):


  # Remove and return the minimum (root) element from the heap
  def extract_min(self):


  # Return the minimum (root) element without removing it
  def get_min(self):


  # Delete element at index i
  def delete(self, i):


  # Build a min-heap from an unsorted list
  def build_heap(self, arr):


  # Sort the elements in the heap in ascending order
  def heap_sort(self):


  # Check if the heap is empty
  def is_empty(self):
    return len(self.heap) == 0

  # Return the size of the heap
  def size(self):
    return len(self.heap)

def test():


if __name__ == "__main__":
  test()
