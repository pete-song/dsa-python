# https://www.geeksforgeeks.org/binary-search/

# It returns location of x in given array arr
def binarySearch(arr, low, high, x):

  while low <= high:

    mid = low + (high - low) // 2

    # Check if x is present at mid
    if arr[mid] == x:
      return mid

    # If x is greater, ignore left half
    elif arr[mid] < x:
      low = mid + 1

    # If x is smaller, ignore right half
    else:
      high = mid - 1

  # If we reach here, then the element
  # was not present
  return -1

def test():
  # Test Case 1: Search for an element in a sorted array
  arr1 = [1, 2, 3, 4, 5]
  index1 = binarySearch(arr1, 0, len(arr1) - 1, 3)
  assert index1 == 2, f"Test failed for searching 3: expected index 2, got {index1}"

  # Test Case 2: Search for an element that doesn't exist
  arr2 = [1, 2, 3, 4, 5]
  index2 = binarySearch(arr2, 0, len(arr2) - 1, 6)
  assert index2 == -1, f"Test failed for searching 6: expected index -1, got {index2}"

  # Test Case 3: Search for the first element in the array
  arr3 = [1, 2, 3, 4, 5]
  index3 = binarySearch(arr3, 0, len(arr3) - 1, 1)
  assert index3 == 0, f"Test failed for searching 1: expected index 0, got {index3}"

  # Test Case 4: Search for the last element in the array
  arr4 = [1, 2, 3, 4, 5]
  index4 = binarySearch(arr4, 0, len(arr4) - 1, 5)
  assert index4 == 4, f"Test failed for searching 5: expected index 4, got {index4}"

  # Test Case 5: Empty array (edge case)
  arr5 = []
  index5 = binarySearch(arr5, 0, len(arr5) - 1, 3)
  assert index5 == -1, f"Test failed for empty array searching 3: expected index -1, got {index5}"

  # Test Case 6: Array with one element, element present
  arr6 = [5]
  index6 = binarySearch(arr6, 0, len(arr6) - 1, 5)
  assert index6 == 0, f"Test failed for single element array searching 5: expected index 0, got {index6}"

  # Test Case 7: Array with one element, element absent
  arr7 = [5]
  index7 = binarySearch(arr7, 0, len(arr7) - 1, 3)
  assert index7 == -1, f"Test failed for single element array searching 3: expected index -1, got {index7}"

  # Test Case 8: Array with negative numbers
  arr8 = [-5, -4, -3, -2, -1]
  index8 = binarySearch(arr8, 0, len(arr8) - 1, -3)
  assert index8 == 2, f"Test failed for searching -3: expected index 2, got {index8}"

  # Test Case 9: Array with both positive and negative numbers
  arr9 = [-5, -3, 0, 2, 4, 6]
  index9 = binarySearch(arr9, 0, len(arr9) - 1, 2)
  assert index9 == 3, f"Test failed for searching 2: expected index 3, got {index9}"

  print("All test cases passed!")

if __name__ == "__main__":
  test()
