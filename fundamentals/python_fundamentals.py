# extensive_python_fundamentals_detailed.py

import math
import collections
import itertools
import os
import datetime

# 1. Data Types and List Comprehensions/Generators
def data_types_demo():
    """Demonstrates Python's core data types with details and edge cases."""

    # Lists (mutable, ordered)
    my_list = [1, 2, 3, "apple", "banana", [4, 5]]
    print(f"List: {my_list}")   # List: [1, 2, 3, 'apple', 'banana', [4, 5]]

    # Edge cases: empty list, mixed types, nested lists
    empty_list = []
    print(f"Empty list: {empty_list}")  # Empty list: []

    my_list.append(6)
    my_list.insert(0, 0)
    print(f"List after append & insert: {my_list}")  # List after append & insert: [0, 1, 2, 3, 'apple', 'banana', [4, 5], 6]

    # Slicing: start, stop, step
    print(f"List slicing (1:4): {my_list[1:4]}")
    # List slicing (1:4): [1, 2, 3]
    print(f"List slicing (::2): {my_list[::2]}")  # Every other element
    # List slicing (::2): [0, 2, 'apple', [4, 5]]

    my_list.pop()
    print(f"List after pop: {my_list}") # List after pop: [0, 1, 2, 3, 'apple', 'banana', [4, 5]]

    my_list.remove("apple")  # Removes the first occurrence
    print(f"List after remove: {my_list}")  # List after remove: [0, 1, 2, 3, 'banana', [4, 5]]

    # Edge cases: index out of range, element not found (index(), remove())
    try:
        print(f"Index of 99: {my_list.index(99)}") # will error 
    except ValueError as e:
        print(f"ValueError: {e}")  # ValueError: 99 is not in list

    print(f"Count of 3: {my_list.count(3)}")  # Count of 3: 1

    # Sorting: handles mixed types with a key function
    my_list.sort(key=lambda x: str(x))
    print(f"Sorted list: {my_list}")  # Sorted list: [0, 1, 2, 3, [4, 5], 'banana']

    # Tuples (immutable, ordered)
    my_tuple = (1, 2, 3, "hello", (4, 5))
    print(f"Tuple: {my_tuple}")  # Tuple: (1, 2, 3, 'hello', (4, 5))

    # Edge cases: empty tuple, single-element tuple (comma required)
    empty_tuple = ()
    single_tuple = (1,)
    print(f"Empty tuple: {empty_tuple}, Single tuple: {single_tuple}")  
    # Empty tuple: (), Single tuple: (1,)

    print(f"Tuple index of 2: {my_tuple.index(2)}")  # Tuple index of 2: 1
    print(f"Tuple count of 1: {my_tuple.count(1)}")  # Tuple count of 1: 1
    print(f"Tuple slicing: {my_tuple[1:3]}")  # Tuple slicing: (2, 3)

    # Dictionaries (mutable, unordered key-value pairs)
    my_dict = {"name": "Alice", "age": 30, "city": "New York", "hobbies": ["reading", "coding"]}
    print(f"Dictionary: {my_dict}")  # Dictionary: {'name': 'Alice', 'age': 30, 'city': 'New York', 'hobbies': ['reading', 'coding']}

    # Edge cases: accessing non-existent keys (get(), []), updating with existing keys
    print(f"Age (get): {my_dict.get('age')}")
    print(f"Job(get): {my_dict.get('job')}") # Returns None
    # Age (get): 30
    # Job(get): None

    try:
        print(f"Job: {my_dict['job']}") # will error
    except KeyError as e:
        print(f"KeyError: {e}") # KeyError: 'job'

    my_dict["job"] = "Engineer"
    del my_dict["city"]
    print(f"Updated dictionary: {my_dict}")
    # Updated dictionary: {'name': 'Alice', 'age': 30, 'hobbies': ['reading', 'coding'], 'job': 'Engineer'}

    # Sets (mutable, unordered, unique elements)
    my_set = {1, 2, 3, 4, 4, 5}
    print(f"Set: {my_set}")  # Set: {1, 2, 3, 4, 5}

    # Edge cases: empty set, adding/removing existing/non-existent elements
    empty_set = set()
    print(f"Empty set: {empty_set}")  # Empty set: set()

    my_set.add(6)
    my_set.remove(3)
    print(f"Set after add & remove: {my_set}")  # Set after add & remove: {1, 2, 4, 5, 6}

    try:
        my_set.remove(99) # will error
    except KeyError as e:
        print(f"KeyError: {e}")  # KeyError: 99

    my_set.discard(99) # Does not error.

    another_set = {4, 5, 6, 7}
    print(f"Union: {my_set.union(another_set)}")  # Union: {1, 2, 4, 5, 6, 7}
    print(f"Intersection: {my_set.intersection(another_set)}")  # Intersection: {4, 5, 6}
    print(f"Difference: {my_set.difference(another_set)}")  # Difference: {1, 2}

    # Strings (immutable, ordered sequence of characters)
    my_string = "Hello, world! Python is fun."
    print(f"String: {my_string}")  # String: Hello, world! Python is fun.

    # Edge cases: empty string, string formatting, escape sequences
    empty_string = ""
    formatted_string = f"Name: {my_dict['name']}, Age: {my_dict['age']}"
    escape_string = "Line 1\nLine 2\tTabbed"
    print(f"Empty string: {empty_string}, Formatted: {formatted_string}, Escape: {escape_string}")
    # Empty string: , Formatted: Name: Alice, Age: 30, Escape: Line 1
    # Line 2  Tabbed

    print(f"Uppercase: {my_string.upper()}")  # Uppercase: HELLO, WORLD! PYTHON IS FUN.
    print(f"Lowercase: {my_string.lower()}")  # Lowercase: hello, world! python is fun.
    print(f"Split: {my_string.split(' ')}")   # Split: ['Hello,', 'world!', 'Python', 'is', 'fun.']
    print(f"Find 'world': {my_string.find('world')}")  # Find 'world': 7
    print(f"Replace 'world' with 'Python': {my_string.replace('world', 'Python')}")  # Replace 'world' with 'Python': Hello, Python! Python is fun.
    print(f"String slicing: {my_string[0:5]}")  # String slicing: Hello

    # List Comprehensions
    squared_numbers = [x**2 for x in range(10) if x % 2 == 0]
    print(f"Squared even numbers: {squared_numbers}")  
    # Squared even numbers: [0, 4, 16, 36, 64]

    # Generator Expressions
    squared_generator = (x**2 for x in range(10))
    print(f"Squared generator (first 5): {list(itertools.islice(squared_generator, 5))}")  
    # Squared generator (first 5): [0, 1, 4, 9, 16]

# 2. Control Flow (detailed explanations)
def control_flow_demo():
    """Demonstrates control flow statements with detailed explanations."""
    x = 10
    if x > 5:
        print("x is greater than 5")
    elif x == 5:
        print("x is equal to 5")
    else:
        print("x is less than 5")
    # x is greater than 5

    for i in range(3):
        print(f"Loop iteration: {i}")
    else:  # Executes if loop completes normally (no break)
        print("Loop finished normally")
    # Loop iteration: 0
    # Loop iteration: 1
    # Loop iteration: 2
    # Loop finished normally    
    
    i = 0
    while i < 3:
        print(f"While loop iteration: {i}")
        i += 1
    else:  # Executes if loop completes normally
        print("While loop finished normally")
    # While loop iteration: 0
    # While loop iteration: 1
    # While loop iteration: 2
    # While loop finished normally

    for j in range(5):
        if j == 3:
            break  # Exits the loop immediately
        print(f"Break loop: {j}")
    # Break loop: 0
    # Break loop: 1
    # Break loop: 2

    for k in range(5):
        if k == 2:
            continue  # Skips the rest of the current iteration
        print(f"Continue loop: {k}")
    # Continue loop: 0
    # Continue loop: 1
    # Continue loop: 3
    # Continue loop: 4

    for l in range(3):
        pass  # Placeholder, does nothing
    print("Pass example finished")
    # Pass example finished

# 3. Functions (with docstrings and recursion)
def functions_demo():
    """Demonstrates function definitions, arguments, scope, closures, and recursion."""

    def greet(name, greeting="Hello"):
        """Greets a person.
        Args:
            name (str): The person's name.
            greeting (str, optional): The greeting message. Defaults to "Hello".
        """
        print(f"{greeting}, {name}!")

    greet("Bob")            # Hello, Bob!
    greet("Charlie", "Hi")  # Hi, Charlie!

    def variable_args(*args, **kwargs):
        """Demonstrates variable arguments (*args and **kwargs)."""
        print(f"Args: {args}")  # Args: (1, 2, 3)
        print(f"Kwargs: {kwargs}")  # Kwargs: {'name': 'Alice', 'age': 30}

    variable_args(1, 2, 3, name="Alice", age=30)

    def outer_function(x):
        """Demonstrates closures."""
        def inner_function(y):
            return x + y
        return inner_function

    closure_func = outer_function(10)
    print(f"Closure: {closure_func(5)}")  # Closure: 15

    lambda_func = lambda a, b: a * b
    print(f"Lambda: {lambda_func(2, 3)}")  # Lambda: 6

    def recursive_factorial(n):
        """Calculates factorial recursively."""
        if n == 0:
            return 1
        else:
            return n * recursive_factorial(n - 1)

    print(f"Factorial of 5: {recursive_factorial(5)}")  # Factorial of 5: 120

# 4. OOP (with inheritance and polymorphism)
def oop_demo():
    """Demonstrates object-oriented programming concepts."""

    class Animal:
        """Base class for animals."""
        def __init__(self, name, sound="Generic Animal Sound"):
            self.name = name
            self.sound = sound

        def speak(self):
            print(self.sound)

    class Dog(Animal):
        """Dog class, inheriting from Animal."""
        def __init__(self, name):
            super().__init__(name, "Woof!")

        def fetch(self, item):
            print(f"{self.name} fetches {item}")

    animal = Animal("Generic Animal")
    dog = Dog("Buddy")

    animal.speak()  # Generic Animal Sound
    dog.speak()  # Woof!
    dog.fetch("ball")  # Buddy fetches ball

# 5. Error Handling (detailed exception handling)
def error_handling_demo():
    """Demonstrates error handling with try, except, and finally blocks."""
    try:
        result = 10 / 0
    except ZeroDivisionError as e:
        print(f"Cannot divide by zero: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        print("This always executes")
    # Cannot divide by zero: division by zero
    # This always executes  

    try:
        int("hello")
    except ValueError as e:
        print(f"ValueError: {e}")
    # ValueError: invalid literal for int() with base 10: 'hello'

# 6. Modules and Libraries (detailed examples)
def modules_demo():
    """Demonstrates common built-in modules."""
    print(f"Square root of 16: {math.sqrt(16)}")  # Square root of 16: 4.0

    my_list = [1, 2, 2, 3, 3, 3]
    print(f"Counter: {collections.Counter(my_list)}")  # Counter: Counter({3: 3, 2: 2, 1: 1})

    my_dict = collections.defaultdict(int)
    for num in my_list:
        my_dict[num] += 1
    print(f"defaultdict: {my_dict}")  # defaultdict: defaultdict(<class 'int'>, {1: 1, 2: 2, 3: 3})

    for i in itertools.combinations([1, 2, 3], 2):
        print(f"combinations: {i}")
    # combinations: (1, 2)
    # combinations: (1, 3)
    # combinations: (2, 3)

    print(f"Current working directory: {os.getcwd()}")
    #

    now = datetime.datetime.now()
    print(f"Current time: {now}")
    # Current time: 2025-04-03 18:03:09.682803

# Main execution
if __name__ == "__main__":
    data_types_demo()
    print("\n--- Control Flow Demo ---")
    control_flow_demo()
    print("\n--- Functions Demo ---")
    functions_demo()
    print("\n--- OOP Demo ---")
    oop_demo()
    print("\n--- Error Handling Demo ---")
    error_handling_demo()
    print("\n--- Modules Demo ---")
    modules_demo()