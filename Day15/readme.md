# Day 15: List Comprehensions

## Overview
Welcome to Week 3! Today we'll master comprehensions - a powerful Python feature that lets you create lists, dictionaries, and sets in a single, elegant line. This is one of Python's most loved features!

---

## 1. Introduction to Comprehensions

### Why Use Comprehensions?

**Traditional approach:**
```python
# Create list of squares
squares = []
for i in range(10):
    squares.append(i ** 2)
print(squares)  # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
```

**With list comprehension:**
```python
# Same result, one line!
squares = [i ** 2 for i in range(10)]
print(squares)  # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
```

### Benefits:
✅ **Concise** - Less code to write  
✅ **Readable** - Clear intent  
✅ **Faster** - Optimized by Python  
✅ **Pythonic** - Idiomatic Python style  

---

## 2. List Comprehensions

### Basic Syntax

```python
[expression for item in iterable]
```

### Simple Examples

```python
# Numbers 0-9
numbers = [x for x in range(10)]
print(numbers)  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# Squares
squares = [x**2 for x in range(10)]
print(squares)  # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

# Double each number
nums = [1, 2, 3, 4, 5]
doubled = [x * 2 for x in nums]
print(doubled)  # [2, 4, 6, 8, 10]

# Uppercase strings
words = ["hello", "world", "python"]
upper = [word.upper() for word in words]
print(upper)  # ['HELLO', 'WORLD', 'PYTHON']
```

### With Strings

```python
# Get each character
text = "Python"
chars = [char for char in text]
print(chars)  # ['P', 'y', 't', 'h', 'o', 'n']

# Uppercase each character
upper_chars = [char.upper() for char in text]
print(upper_chars)  # ['P', 'Y', 'T', 'H', 'O', 'N']
```

---

## 3. List Comprehensions with Conditions

### Basic Filtering (if)

```python
[expression for item in iterable if condition]
```

### Examples

```python
# Even numbers only
evens = [x for x in range(20) if x % 2 == 0]
print(evens)  # [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]

# Odd numbers only
odds = [x for x in range(20) if x % 2 != 0]
print(odds)  # [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]

# Numbers greater than 5
nums = [1, 3, 5, 7, 9, 11, 13]
greater = [x for x in nums if x > 5]
print(greater)  # [7, 9, 11, 13]

# Positive numbers
numbers = [-5, -2, 0, 3, 7, -1, 10]
positive = [x for x in numbers if x > 0]
print(positive)  # [3, 7, 10]

# Filter words by length
words = ["cat", "elephant", "dog", "butterfly"]
long_words = [word for word in words if len(word) > 5]
print(long_words)  # ['elephant', 'butterfly']
```

### Conditional Expression (if-else)

```python
[true_expression if condition else false_expression for item in iterable]
```

```python
# Even or odd labels
labels = ["even" if x % 2 == 0 else "odd" for x in range(10)]
print(labels)  # ['even', 'odd', 'even', 'odd', ...]

# Absolute values
numbers = [-5, 3, -2, 7, -9]
absolute = [x if x >= 0 else -x for x in numbers]
print(absolute)  # [5, 3, 2, 7, 9]

# Cap at maximum
values = [15, 25, 35, 45, 55]
capped = [x if x <= 30 else 30 for x in values]
print(capped)  # [15, 25, 30, 30, 30]
```

---

## 4. Nested List Comprehensions

### Flattening Lists

```python
# 2D list
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# Flatten to 1D
flat = [num for row in matrix for num in row]
print(flat)  # [1, 2, 3, 4, 5, 6, 7, 8, 9]
```

### Creating 2D Lists

```python
# Create 3x3 matrix
matrix = [[i * 3 + j for j in range(3)] for i in range(3)]
print(matrix)  # [[0, 1, 2], [3, 4, 5], [6, 7, 8]]

# Create multiplication table
table = [[i * j for j in range(1, 11)] for i in range(1, 11)]
```

### Nested with Conditions

```python
# Flatten and filter
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
evens = [num for row in matrix for num in row if num % 2 == 0]
print(evens)  # [2, 4, 6, 8]
```

---

## 5. Dictionary Comprehensions

### Basic Syntax

```python
{key_expression: value_expression for item in iterable}
```

### Simple Examples

```python
# Squares dictionary
squares = {x: x**2 for x in range(6)}
print(squares)  # {0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

# String lengths
words = ["cat", "elephant", "dog"]
lengths = {word: len(word) for word in words}
print(lengths)  # {'cat': 3, 'elephant': 8, 'dog': 3}

# Character indices
text = "Python"
indices = {char: idx for idx, char in enumerate(text)}
print(indices)  # {'P': 0, 'y': 1, 't': 2, 'h': 3, 'o': 4, 'n': 5}
```

### With Conditions

```python
# Only even numbers
evens = {x: x**2 for x in range(10) if x % 2 == 0}
print(evens)  # {0: 0, 2: 4, 4: 16, 6: 36, 8: 64}

# Filter by value length
words = ["cat", "elephant", "dog", "butterfly", "ant"]
long_words = {word: len(word) for word in words if len(word) > 3}
print(long_words)  # {'elephant': 8, 'butterfly': 9}
```

### Transforming Dictionaries

```python
# Original dictionary
prices = {"apple": 0.50, "banana": 0.30, "orange": 0.60}

# Increase all prices by 10%
new_prices = {item: price * 1.1 for item, price in prices.items()}
print(new_prices)  # {'apple': 0.55, 'banana': 0.33, 'orange': 0.66}

# Swap keys and values
swapped = {value: key for key, value in prices.items()}
print(swapped)  # {0.5: 'apple', 0.3: 'banana', 0.6: 'orange'}

# Filter dictionary
cheap = {item: price for item, price in prices.items() if price < 0.55}
print(cheap)  # {'apple': 0.5, 'banana': 0.3}
```

---

## 6. Set Comprehensions

### Basic Syntax

```python
{expression for item in iterable}
```

### Examples

```python
# Unique squares
squares = {x**2 for x in range(10)}
print(squares)  # {0, 1, 4, 9, 16, 25, 36, 49, 64, 81}

# Unique characters
text = "hello world"
unique_chars = {char for char in text if char != ' '}
print(unique_chars)  # {'h', 'e', 'l', 'o', 'w', 'r', 'd'}

# Remove duplicates while transforming
numbers = [1, 2, 2, 3, 3, 3, 4, 4, 5]
unique_doubled = {x * 2 for x in numbers}
print(unique_doubled)  # {2, 4, 6, 8, 10}
```

### With Conditions

```python
# Unique even numbers
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 2, 4, 6]
unique_evens = {x for x in numbers if x % 2 == 0}
print(unique_evens)  # {2, 4, 6, 8}

# First letters of long words
words = ["cat", "elephant", "dog", "butterfly", "eagle"]
first_letters = {word[0] for word in words if len(word) > 3}
print(first_letters)  # {'e', 'b'}
```

---

## 7. Practical Examples

### Example 1: Data Processing

```python
# Extract specific data
students = [
    {"name": "Alice", "age": 20, "grade": 85},
    {"name": "Bob", "age": 22, "grade": 92},
    {"name": "Charlie", "age": 21, "grade": 78}
]

# Get all names
names = [student["name"] for student in students]
print(names)  # ['Alice', 'Bob', 'Charlie']

# Get high achievers (grade >= 80)
high_achievers = [s["name"] for s in students if s["grade"] >= 80]
print(high_achievers)  # ['Alice', 'Bob']

# Create name-grade mapping
grade_map = {s["name"]: s["grade"] for s in students}
print(grade_map)  # {'Alice': 85, 'Bob': 92, 'Charlie': 78}
```

### Example 2: String Manipulation

```python
# Convert to uppercase and filter
words = ["hello", "world", "python", "is", "awesome"]
upper_long = [w.upper() for w in words if len(w) > 4]
print(upper_long)  # ['HELLO', 'WORLD', 'PYTHON', 'AWESOME']

# Count vowels in each word
vowel_counts = {word: sum(1 for char in word if char in 'aeiou') 
                for word in words}
print(vowel_counts)  # {'hello': 2, 'world': 1, 'python': 1, ...}
```

### Example 3: Number Operations

```python
# Factorial using range
import math
factorials = {n: math.factorial(n) for n in range(1, 6)}
print(factorials)  # {1: 1, 2: 2, 3: 6, 4: 24, 5: 120}

# Celsius to Fahrenheit
celsius = [0, 10, 20, 30, 40]
fahrenheit = [c * 9/5 + 32 for c in celsius]
print(fahrenheit)  # [32.0, 50.0, 68.0, 86.0, 104.0]
```

### Example 4: Matrix Operations

```python
# Transpose matrix
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
transposed = [[row[i] for row in matrix] for i in range(len(matrix[0]))]
print(transposed)  # [[1, 4, 7], [2, 5, 8], [3, 6, 9]]

# Diagonal elements
diagonal = [matrix[i][i] for i in range(len(matrix))]
print(diagonal)  # [1, 5, 9]
```

### Example 5: File Processing Simulation

```python
# Parse CSV-like data
data = ["name,age,city", "Alice,25,NYC", "Bob,30,LA", "Charlie,35,Chicago"]

# Skip header and parse
parsed = [line.split(',') for line in data[1:]]
print(parsed)  # [['Alice', '25', 'NYC'], ['Bob', '30', 'LA'], ...]

# Create dictionaries
headers = data[0].split(',')
records = [{headers[i]: values[i] for i in range(len(headers))} 
           for values in parsed]
print(records)  # [{'name': 'Alice', 'age': '25', 'city': 'NYC'}, ...]
```

---

## 8. When NOT to Use Comprehensions

### Don't Use for Complex Logic

```python
# ❌ Too complex - hard to read
result = [x * 2 if x > 0 else x / 2 if x < 0 else 0 for x in numbers 
          if x != 5 and x != 10]

# ✅ Better - use regular loop
result = []
for x in numbers:
    if x == 5 or x == 10:
        continue
    if x > 0:
        result.append(x * 2)
    elif x < 0:
        result.append(x / 2)
    else:
        result.append(0)
```

### Don't Sacrifice Readability

```python
# ❌ Too nested - confusing
result = [[y * 2 for y in row if y > 0] for row in matrix 
          if sum(row) > 10]

# ✅ Better - break it down
result = []
for row in matrix:
    if sum(row) > 10:
        filtered = [y * 2 for y in row if y > 0]
        result.append(filtered)
```

---

## 9. Performance Comparison

### List Comprehension vs Loop

```python
import time

# Traditional loop
start = time.time()
squares1 = []
for i in range(1000000):
    squares1.append(i**2)
time1 = time.time() - start

# List comprehension
start = time.time()
squares2 = [i**2 for i in range(1000000)]
time2 = time.time() - start

print(f"Loop: {time1:.4f}s")
print(f"Comprehension: {time2:.4f}s")
print(f"Speedup: {time1/time2:.2f}x")
# Comprehension is typically 20-30% faster
```

---

## 10. Advanced Patterns

### Multiple Conditions

```python
# AND condition
result = [x for x in range(100) if x % 2 == 0 if x % 3 == 0]
# Same as: if x % 2 == 0 and x % 3 == 0

# OR condition - use single if with or
result = [x for x in range(20) if x % 2 == 0 or x % 3 == 0]
```

### Nested Iteration

```python
# Cartesian product
colors = ["red", "blue"]
sizes = ["S", "M", "L"]
products = [f"{color}-{size}" for color in colors for size in sizes]
print(products)  # ['red-S', 'red-M', 'red-L', 'blue-S', 'blue-M', 'blue-L']
```

### Function Calls in Comprehension

```python
def process(x):
    return x ** 2 + 1

results = [process(x) for x in range(5)]
print(results)  # [1, 2, 5, 10, 17]
```

---

## Practice Exercises

### Exercise 1: Basic Filtering
Create list comprehensions for:
- Multiples of 3 between 1-50
- Words starting with vowels
- Numbers divisible by both 2 and 3

### Exercise 2: Dictionary Operations
Given a dictionary of student grades:
- Create dict with only passing grades (>=60)
- Swap names and grades
- Add 5 points to all grades

### Exercise 3: Matrix Operations
- Create 5x5 identity matrix
- Sum each row in a matrix
- Find all prime numbers in matrix

### Exercise 4: String Processing
- Extract all digits from string
- Count frequency of each character
- Remove vowels from list of words

### Exercise 5: Data Transformation
Convert list of tuples to dictionary:
```python
data = [("apple", 5), ("banana", 3), ("orange", 7)]
# Result: {'apple': 5, 'banana': 3, 'orange': 7}
```

---

## Practice Project

**See:** `day15_comprehension_toolkit.py` for the complete Comprehension Toolkit project.

The project includes:
- 20+ comprehension examples
- Data processing utilities
- Matrix operations
- String manipulation
- Interactive demonstrations

---

## Quick Reference

### List Comprehension
```python
# Basic
[expression for item in iterable]

# With condition
[expression for item in iterable if condition]

# With if-else
[expr1 if condition else expr2 for item in iterable]

# Nested
[expression for item1 in iter1 for item2 in iter2]
```

### Dictionary Comprehension
```python
{key: value for item in iterable}
{key: value for item in iterable if condition}
```

### Set Comprehension
```python
{expression for item in iterable}
{expression for item in iterable if condition}
```

---

## Key Takeaways

✅ Comprehensions are concise and fast  
✅ Use for simple transformations and filtering  
✅ List: `[...]`, Dict: `{k:v...}`, Set: `{...}`  
✅ Can include conditions with `if`  
✅ Can nest, but keep it readable  
✅ Don't sacrifice clarity for brevity  
✅ Faster than equivalent loops  
✅ More Pythonic than loops for simple operations  

---

## Common Mistakes to Avoid

❌ **Making comprehensions too complex**
```python
# Too complex!
result = [x*2 if x>0 else x/2 if x<0 else 0 for x in nums if x!=5]
```

❌ **Forgetting parentheses for tuple**
```python
# Wrong
result = [x, x**2 for x in range(5)]  # Syntax error

# Correct
result = [(x, x**2) for x in range(5)]
```

❌ **Using comprehension with side effects**
```python
# Bad - side effect in comprehension
[print(x) for x in numbers]  # Don't do this!

# Good - use regular loop
for x in numbers:
    print(x)
```

---

## Next Steps

Tomorrow (Day 16), we'll learn about **Modules & Packages** - how to organize and reuse code across files!

---

## Resources

- [Python Comprehensions Documentation](https://docs.python.org/3/tutorial/datastructures.html#list-comprehensions)
- [PEP 202 - List Comprehensions](https://www.python.org/dev/peps/pep-0202/)

---

**Write Elegant Python! 🐍**
