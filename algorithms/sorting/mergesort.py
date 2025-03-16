# https://www.geeksforgeeks.org/python-program-for-merge-sort/

def merge(arr, l, m, r):
  n1 = m - l + 1
  n2 = r - m

  # create temp arrays
  L = [0] * (n1)
  R = [0] * (n2)

  # Copy data to temp arrays L[] and R[]
  for i in range(0, n1):
    L[i] = arr[l + i]

  for j in range(0, n2):
    R[j] = arr[m + 1 + j]

  # Merge the temp arrays back into arr[l..r]
  i = 0     # Initial index of first subarray
  j = 0     # Initial index of second subarray
  k = l     # Initial index of merged subarray

  while i < n1 and j < n2:
    if L[i] <= R[j]:
      arr[k] = L[i]
      i += 1
    else:
      arr[k] = R[j]
      j += 1
    k += 1

  # Copy the remaining elements of L[], if there
  # are any
  while i < n1:
    arr[k] = L[i]
    i += 1
    k += 1

  # Copy the remaining elements of R[], if there
  # are any
  while j < n2:
    arr[k] = R[j]
    j += 1
    k += 1

# l is for left index and r is right index of the
# sub-array of arr to be sorted


def mergeSort(arr, l, r):
  if l < r:

    # Same as (l+r)//2, but avoids overflow for
    # large l and h
    m = l+(r-l)//2

    # Sort first and second halves
    mergeSort(arr, l, m)
    mergeSort(arr, m+1, r)
    merge(arr, l, m, r)


def test():
    # Test Case 1: Already sorted array
    arr1 = [1, 2, 3, 4, 5]
    mergeSort(arr1, 0, len(arr1) - 1)
    assert arr1 == [1, 2, 3, 4, 5], f"Test failed for sorted array: {arr1}"

    # Test Case 2: Reverse sorted array
    arr2 = [5, 4, 3, 2, 1]
    mergeSort(arr2, 0, len(arr2) - 1)
    assert arr2 == [1, 2, 3, 4, 5], f"Test failed for reverse sorted array: {arr2}"

    # Test Case 3: Array with duplicate elements
    arr3 = [4, 3, 4, 1, 2, 2, 3]
    mergeSort(arr3, 0, len(arr3) - 1)
    assert arr3 == [1, 2, 2, 3, 3, 4, 4], f"Test failed for array with duplicates: {arr3}"

    # Test Case 4: Single element array (edge case)
    arr4 = [5]
    mergeSort(arr4, 0, len(arr4) - 1)
    assert arr4 == [5], f"Test failed for single element array: {arr4}"

    # Test Case 5: Empty array (edge case)
    arr5 = []
    mergeSort(arr5, 0, len(arr5) - 1)
    assert arr5 == [], f"Test failed for empty array: {arr5}"

    # Test Case 6: Array with negative numbers
    arr6 = [-3, -1, -2, -5, -4]
    mergeSort(arr6, 0, len(arr6) - 1)
    assert arr6 == [-5, -4, -3, -2, -1], f"Test failed for array with negative numbers: {arr6}"

    # Test Case 7: Array with mixed positive and negative numbers
    arr7 = [3, -1, 4, -5, 2]
    mergeSort(arr7, 0, len(arr7) - 1)
    assert arr7 == [-5, -1, 2, 3, 4], f"Test failed for mixed positive and negative numbers: {arr7}"

    # Test Case 8: Array with all equal elements
    arr8 = [7, 7, 7, 7, 7]
    mergeSort(arr8, 0, len(arr8) - 1)
    assert arr8 == [7, 7, 7, 7, 7], f"Test failed for array with all equal elements: {arr8}"

    print("All test cases passed!")

if __name__ == "__main__":
  test()
