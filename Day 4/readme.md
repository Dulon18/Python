# Day 4: Lists & Tuples

## Overview
Today we'll learn about Lists and Tuples - two essential data structures in Python for storing collections of items. Lists are mutable (changeable), while tuples are immutable (unchangeable).

---

## 1. Lists

Lists are ordered, mutable collections that can store items of different types.

### Creating Lists

```python
# Empty list
empty_list = []

# List with items
numbers = [1, 2, 3, 4, 5]
fruits = ["apple", "banana", "orange"]
mixed = [1, "hello", 3.14, True]

# Using list() constructor
letters = list("abc")  # ['a', 'b', 'c']

# Nested lists (2D list)
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
```

### Accessing List Items

```python
fruits = ["apple", "banana", "orange", "mango"]

# Indexing (starts at 0)
print(fruits[0])    # 'apple'
print(fruits[2])    # 'orange'
print(fruits[-1])   # 'mango' (last item)
print(fruits[-2])   # 'orange' (second from end)

# Slicing
print(fruits[1:3])   # ['banana', 'orange']
print(fruits[:2])    # ['apple', 'banana']
print(fruits[2:])    # ['orange', 'mango']
print(fruits[::2])   # ['apple', 'orange'] (every 2nd)
print(fruits[::-1])  # ['mango', 'orange', 'banana', 'apple'] (reverse)
```

---

## 2. List Methods

### Adding Items

```python
fruits = ["apple", "banana"]

# append() - Add single item to end
fruits.append("orange")
print(fruits)  # ['apple', 'banana', 'orange']

# insert() - Add item at specific position
fruits.insert(1, "mango")
print(fruits)  # ['apple', 'mango', 'banana', 'orange']

# extend() - Add multiple items
fruits.extend(["grape", "kiwi"])
print(fruits)  # ['apple', 'mango', 'banana', 'orange', 'grape', 'kiwi']

# Using + operator
more_fruits = fruits + ["peach", "pear"]
```

### Removing Items

```python
fruits = ["apple", "banana", "orange", "banana", "mango"]

# remove() - Remove first occurrence
fruits.remove("banana")
print(fruits)  # ['apple', 'orange', 'banana', 'mango']

# pop() - Remove and return item at index (default: last)
last_fruit = fruits.pop()
print(last_fruit)  # 'mango'
print(fruits)      # ['apple', 'orange', 'banana']

second_fruit = fruits.pop(1)
print(second_fruit)  # 'orange'

# del - Delete by index or slice
del fruits[0]
print(fruits)  # ['banana']

# clear() - Remove all items
fruits.clear()
print(fruits)  # []
```

### Searching and Counting

```python
numbers = [1, 2, 3, 2, 4, 2, 5]

# count() - Count occurrences
print(numbers.count(2))  # 3

# index() - Find first index of value
print(numbers.index(3))  # 2
print(numbers.index(2))  # 1 (first occurrence)

# Check if item exists
print(3 in numbers)      # True
print(10 in numbers)     # False
```

### Sorting and Reversing

```python
numbers = [3, 1, 4, 1, 5, 9, 2]

# sort() - Sort in place (modifies original)
numbers.sort()
print(numbers)  # [1, 1, 2, 3, 4, 5, 9]

# sort() with reverse
numbers.sort(reverse=True)
print(numbers)  # [9, 5, 4, 3, 2, 1, 1]

# sorted() - Return new sorted list (doesn't modify original)
original = [3, 1, 4, 1, 5]
new_list = sorted(original)
print(original)  # [3, 1, 4, 1, 5] (unchanged)
print(new_list)  # [1, 1, 3, 4, 5]

# reverse() - Reverse in place
numbers = [1, 2, 3, 4, 5]
numbers.reverse()
print(numbers)  # [5, 4, 3, 2, 1]

# reversed() - Return reversed iterator
numbers = [1, 2, 3, 4, 5]
rev = list(reversed(numbers))
print(rev)  # [5, 4, 3, 2, 1]
```

### Other Useful Methods

```python
numbers = [1, 2, 3, 4, 5]

# len() - Get length
print(len(numbers))  # 5

# min() and max()
print(min(numbers))  # 1
print(max(numbers))  # 5

# sum()
print(sum(numbers))  # 15

# copy() - Create shallow copy
new_list = numbers.copy()
```

---

## 3. List Operations

### Concatenation and Repetition

```python
# Concatenation with +
list1 = [1, 2, 3]
list2 = [4, 5, 6]
combined = list1 + list2
print(combined)  # [1, 2, 3, 4, 5, 6]

# Repetition with *
repeated = [1, 2] * 3
print(repeated)  # [1, 2, 1, 2, 1, 2]
```

### Modifying Lists

```python
numbers = [1, 2, 3, 4, 5]

# Change single item
numbers[0] = 10
print(numbers)  # [10, 2, 3, 4, 5]

# Change multiple items with slicing
numbers[1:3] = [20, 30]
print(numbers)  # [10, 20, 30, 4, 5]

# Replace with different number of items
numbers[1:3] = [100, 200, 300]
print(numbers)  # [10, 100, 200, 300, 4, 5]
```

### List Comprehension (Preview)

A concise way to create lists:

```python
# Traditional way
squares = []
for i in range(5):
    squares.append(i ** 2)
print(squares)  # [0, 1, 4, 9, 16]

# List comprehension (we'll learn more later)
squares = [i ** 2 for i in range(5)]
print(squares)  # [0, 1, 4, 9, 16]
```

---

## 4. Tuples

Tuples are ordered, immutable collections. Once created, they cannot be modified.

### Creating Tuples

```python
# Empty tuple
empty_tuple = ()

# Tuple with items
numbers = (1, 2, 3, 4, 5)
fruits = ("apple", "banana", "orange")
mixed = (1, "hello", 3.14, True)

# Single item tuple (need comma!)
single = (5,)     # This is a tuple
not_tuple = (5)   # This is just an integer

# Without parentheses (tuple packing)
coordinates = 10, 20
print(coordinates)  # (10, 20)

# Using tuple() constructor
letters = tuple("abc")  # ('a', 'b', 'c')
```

### Accessing Tuple Items

```python
fruits = ("apple", "banana", "orange", "mango")

# Indexing (same as lists)
print(fruits[0])    # 'apple'
print(fruits[-1])   # 'mango'

# Slicing (same as lists)
print(fruits[1:3])  # ('banana', 'orange')
```

### Tuple Methods

Tuples have only 2 methods (because they're immutable):

```python
numbers = (1, 2, 3, 2, 4, 2, 5)

# count() - Count occurrences
print(numbers.count(2))  # 3

# index() - Find first index
print(numbers.index(3))  # 2
```

### Tuple Operations

```python
# Concatenation
tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)
combined = tuple1 + tuple2
print(combined)  # (1, 2, 3, 4, 5, 6)

# Repetition
repeated = (1, 2) * 3
print(repeated)  # (1, 2, 1, 2, 1, 2)

# Membership
print(2 in tuple1)  # True

# Length
print(len(tuple1))  # 3
```

### Tuple Unpacking

```python
# Basic unpacking
coordinates = (10, 20)
x, y = coordinates
print(x)  # 10
print(y)  # 20

# Multiple assignment
name, age, city = ("John", 25, "New York")

# Swapping variables
a = 5
b = 10
a, b = b, a
print(a, b)  # 10 5

# Unpacking with * (extended unpacking)
numbers = (1, 2, 3, 4, 5)
first, *middle, last = numbers
print(first)   # 1
print(middle)  # [2, 3, 4]
print(last)    # 5
```

---

## 5. Lists vs Tuples

| Feature | List | Tuple |
|---------|------|-------|
| Syntax | `[1, 2, 3]` | `(1, 2, 3)` |
| Mutable | ✅ Yes | ❌ No |
| Speed | Slower | Faster |
| Methods | Many | Only 2 (count, index) |
| Use Case | Dynamic data | Fixed data |
| Memory | More | Less |

### When to Use Lists
- When you need to modify the collection
- When order matters and data changes
- For dynamic collections

### When to Use Tuples
- When data shouldn't change
- For fixed collections (coordinates, RGB colors)
- As dictionary keys (lists can't be keys)
- Better performance for large collections

---
## Additional Exercises

### Exercise 1: List Statistics
Create a program that takes a list of numbers and calculates:
- Sum, average, min, max
- Count of even and odd numbers
- Second largest number

### Exercise 2: List Manipulation
Given a list `[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]`:
- Extract all even numbers
- Extract all odd numbers
- Create list of squares of all numbers
- Reverse every 2 elements

### Exercise 3: Tuple Practice
Create tuples for:
- Student information (name, age, grade)
- Geographic coordinates (latitude, longitude)
- RGB color values (red, green, blue)

### Exercise 4: Shopping Cart
Build a shopping cart using lists where each item is a tuple:
```python
cart = [("Apple", 0.5, 5), ("Banana", 0.3, 10), ("Orange", 0.6, 8)]
# Format: (item_name, price, quantity)
# Calculate total cost
```

---

## Quick Reference

### List Methods Cheatsheet

```python
list.append(x)        # Add x to end
list.extend(iterable) # Add all items from iterable
list.insert(i, x)     # Insert x at position i
list.remove(x)        # Remove first occurrence of x
list.pop([i])         # Remove and return item at i (default: last)
list.clear()          # Remove all items
list.index(x)         # Return index of first x
list.count(x)         # Count occurrences of x
list.sort()           # Sort in place
list.reverse()        # Reverse in place
list.copy()           # Return shallow copy
```

### Common List Patterns

```python
# Create list of numbers
numbers = list(range(10))          # [0, 1, 2, ..., 9]

# Create list with same value
zeros = [0] * 5                     # [0, 0, 0, 0, 0]

# Filter list
evens = [x for x in numbers if x % 2 == 0]

# Get unique items
unique = list(set(numbers))

# Flatten 2D list
flat = [item for sublist in matrix for item in sublist]
```

---

## Key Takeaways

✅ **Lists** are mutable and use `[]`  
✅ **Tuples** are immutable and use `()`  
✅ Both support indexing and slicing  
✅ Lists have many methods, tuples have only 2  
✅ Use lists for dynamic data, tuples for fixed data  
✅ Tuples are faster and use less memory  
✅ List methods like `.sort()` modify in place  
✅ Functions like `sorted()` return new objects  

---

## Common Mistakes to Avoid

❌ **Trying to modify tuples**
```python
t = (1, 2, 3)
t[0] = 10  # ERROR!
```

❌ **Forgetting comma for single-item tuple**
```python
t = (5)    # This is int, not tuple
t = (5,)   # Correct way
```

❌ **Using mutable default arguments**
```python
def add_item(item, my_list=[]):  # BAD!
    my_list.append(item)
    return my_list
```

---

## Next Steps

Tomorrow (Day 5), we'll explore **Dictionaries and Sets** - powerful data structures for storing unique values and key-value pairs!

---

## Resources

- [Python Lists Documentation](https://docs.python.org/3/tutorial/datastructures.html#more-on-lists)
- [Python Tuples Documentation](https://docs.python.org/3/tutorial/datastructures.html#tuples-and-sequences)

---

**Keep Building! 🐍**