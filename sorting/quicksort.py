import random
# https://www.geeksforgeeks.org/quick-sort-algorithm/

# Partition function
def partition(arr, low, high):

  # Choose the pivot
  pivot = arr[high]

  # Index of smaller element and indicates
  # the right position of pivot found so far
  i = low - 1

  # Traverse arr[low..high] and move all smaller
  # elements to the left side. Elements from low to
  # i are smaller after every iteration
  for j in range(low, high):
    if arr[j] < pivot:
      i += 1
      swap(arr, i, j)

  # Move pivot after smaller elements and
  # return its position
  swap(arr, i + 1, high)
  return i + 1

# Swap function
def swap(arr, i, j):
  arr[i], arr[j] = arr[j], arr[i]

# The QuickSort function implementation
def quickSort(arr, low, high):
  if low < high:

    # pi is the partition return index of pivot
    pi = partition(arr, low, high)

    # Recursion calls for smaller elements
    # and greater or equals elements
    quickSort(arr, low, pi - 1)
    quickSort(arr, pi + 1, high)

def test():
  # Test Case 1: Already sorted array
  arr1 = [1, 2, 3, 4, 5]
  quickSort(arr1, 0, len(arr1) - 1)
  assert arr1 == [1, 2, 3, 4, 5], f"Test failed for sorted array: {arr1}"

  # Test Case 2: Reverse sorted array
  arr2 = [5, 4, 3, 2, 1]
  quickSort(arr2, 0, len(arr2) - 1)
  assert arr2 == [1, 2, 3, 4, 5], f"Test failed for reverse sorted array: {arr2}"

  # Test Case 3: Array with duplicate elements
  arr3 = [4, 3, 4, 1, 2, 2, 3]
  quickSort(arr3, 0, len(arr3) - 1)
  assert arr3 == [1, 2, 2, 3, 3, 4, 4], f"Test failed for array with duplicates: {arr3}"

  # Test Case 4: Single element array (edge case)
  arr4 = [5]
  quickSort(arr4, 0, len(arr4) - 1)
  assert arr4 == [5], f"Test failed for single element array: {arr4}"

  # Test Case 5: Empty array (edge case)
  arr5 = []
  quickSort(arr5, 0, len(arr5) - 1)
  assert arr5 == [], f"Test failed for empty array: {arr5}"

  # Test Case 6: Array with negative numbers
  arr6 = [-3, -1, -2, -5, -4]
  quickSort(arr6, 0, len(arr6) - 1)
  assert arr6 == [-5, -4, -3, -2, -1], f"Test failed for array with negative numbers: {arr6}"

  # Test Case 7: Array with mixed positive and negative numbers
  arr7 = [3, -1, 4, -5, 2]
  quickSort(arr7, 0, len(arr7) - 1)
  assert arr7 == [-5, -1, 2, 3, 4], f"Test failed for mixed positive and negative numbers: {arr7}"

  # Test Case 8: Array with all equal elements
  arr8 = [7, 7, 7, 7, 7]
  quickSort(arr8, 0, len(arr8) - 1)
  assert arr8 == [7, 7, 7, 7, 7], f"Test failed for array with all equal elements: {arr8}"

  # Test Case 9: Large array with random elements
  arr9 = [random.randint(1, 1000) for _ in range(1000)]  # Random array of 1000 elements
  quickSort(arr9, 0, len(arr9) - 1)
  assert arr9 == sorted(arr9), f"Test failed for large array: {arr9[:10]}..."  # Check if the result is sorted

  print("All test cases passed!")

if __name__ == "__main__":
  test()
