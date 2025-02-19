# Basic Array Operations with Time Complexities


'''Time Complexity Notation:
- n: number of elements in the list
- O(1): Constant time
- O(n): Linear time
- O(log n): Logarithmic time'''


# Creating an array (list in Python) -> O(1)
arr = [1, 2, 3, 4, 5]

# Accessing elements by index -> O(1)
first_element = arr[0]  # 1
last_element = arr[-1]  # 5

# Updating an element -> O(1)
arr[2] = 10  # arr becomes [1, 2, 10, 4, 5]

# Appending an element to the end -> O(1) (amortized)
arr.append(6)  # arr becomes [1, 2, 10, 4, 5, 6]

# Inserting an element at a specific index -> O(n)
arr.insert(2, 99)  # arr becomes [1, 2, 99, 10, 4, 5, 6]

# Deleting an element by index -> O(n)
del arr[2]  # arr becomes [1, 2, 10, 4, 5, 6]

# Removing an element by value -> O(n)
arr.remove(4)  # arr becomes [1, 2, 10, 5, 6]

# Popping the last element -> O(1)
last_item = arr.pop()  # arr becomes [1, 2, 10, 5]

# Popping an element at a specific index -> O(n)
second_item = arr.pop(1)  # arr becomes [1, 10, 5]

# Searching for an element (Linear Search) -> O(n)
def search_element(arr, target):
    for i, num in enumerate(arr):
        if num == target:
            return i
    return -1  # Not found

index = search_element(arr, 10)  # Returns 1

# Sorting the array (TimSort) -> O(n log n)
arr.sort()  # In-place sorting
sorted_arr = sorted(arr)  # Returns a new sorted list

# Reversing an array -> O(n)
arr.reverse()
reversed_arr = arr[::-1]  # better for memory efficiency

# Copying an array -> O(n)
copy_arr = arr.copy()

# Finding the minimum and maximum -> O(n)
min_val = min(arr)
max_val = max(arr)

# Sum of all elements -> O(n)
total = sum(arr)

# List comprehension (efficient transformations) -> O(n)
squared = [x**2 for x in arr]

# Merging two arrays -> O(n + m)
arr2 = [7, 8, 9]
merged_arr = arr + arr2  # Concatenation

# Checking membership -> O(n) (O(1) for sets)
is_present = 5 in arr

# Slicing an array -> O(k), where k is the slice size
slice1 = arr[:3]  # First 3 elements
slice2 = arr[2:5]  # Elements from index 2 to 4
slice3 = arr[::-1]  # Reversed array

# Two-dimensional (2D) array operations
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Accessing an element in a 2D array -> O(1)
element = matrix[1][2]  # 6

# Transposing a matrix -> O(n^2)
transposed = [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]

# Printing all operations' results
if __name__ == "__main__":
    print("Updated Array:", arr)
    print("Index of 10:", index)
    print("Sorted Array:", sorted_arr)
    print("Reversed Array:", reversed_arr)
    print("Minimum Value:", min_val)
    print("Maximum Value:", max_val)
    print("Sum of Elements:", total)
    print("Squared Values:", squared)
    print("Merged Array:", merged_arr)
    print("Is 5 in Array:", is_present)
    print("First 3 Elements:", slice1)
    print("Reversed Slice:", slice3)
    print("Transposed Matrix:", transposed)
