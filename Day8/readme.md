# Day 8: Loops - Part 1 (for loops)

## Overview
Welcome to Week 2! Today we'll learn about `for` loops - one of the most powerful tools in programming. Loops allow you to repeat code multiple times without writing it over and over again.

---

## 1. Introduction to Loops

### Why Do We Need Loops?

**Without loops:**
```python
print("Hello 1")
print("Hello 2")
print("Hello 3")
print("Hello 4")
print("Hello 5")
```

**With loops:**
```python
for i in range(1, 6):
    print(f"Hello {i}")
```

Loops save time, reduce errors, and make code more maintainable!

---

## 2. The for Loop

A `for` loop iterates over a sequence (list, string, range, etc.).

### Basic Syntax

```python
for variable in sequence:
    # code to execute for each item
```

### Simple Examples

```python
# Loop through a list
fruits = ["apple", "banana", "orange"]
for fruit in fruits:
    print(fruit)

# Output:
# apple
# banana
# orange

# Loop through a string
for letter in "Python":
    print(letter)

# Output:
# P
# y
# t
# h
# o
# n
```

---

## 3. The range() Function

`range()` generates a sequence of numbers - perfect for loops!

### range() with One Argument

```python
# range(stop) - generates 0 to stop-1
for i in range(5):
    print(i)

# Output: 0 1 2 3 4
```

### range() with Two Arguments

```python
# range(start, stop) - generates start to stop-1
for i in range(3, 8):
    print(i)

# Output: 3 4 5 6 7
```

### range() with Three Arguments

```python
# range(start, stop, step) - generates with custom step
for i in range(0, 10, 2):
    print(i)

# Output: 0 2 4 6 8

# Counting backwards
for i in range(10, 0, -1):
    print(i)

# Output: 10 9 8 7 6 5 4 3 2 1
```

### range() Examples

```python
# Print numbers 1 to 10
for num in range(1, 11):
    print(num)

# Print even numbers from 0 to 20
for num in range(0, 21, 2):
    print(num)

# Countdown from 10 to 1
for num in range(10, 0, -1):
    print(num)
print("Blast off!")
```

---

## 4. Looping Through Collections

### Looping Through Lists

```python
numbers = [10, 20, 30, 40, 50]

# Method 1: Direct iteration
for num in numbers:
    print(num)

# Method 2: Using index
for i in range(len(numbers)):
    print(f"Index {i}: {numbers[i]}")

# Method 3: Using enumerate (best practice)
for index, value in enumerate(numbers):
    print(f"Index {index}: {value}")

# Starting enumerate from 1
for index, value in enumerate(numbers, start=1):
    print(f"Position {index}: {value}")
```

### Looping Through Dictionaries

```python
student = {
    "name": "John",
    "age": 20,
    "grade": "A"
}

# Loop through keys
for key in student:
    print(key)

# Loop through keys explicitly
for key in student.keys():
    print(key)

# Loop through values
for value in student.values():
    print(value)

# Loop through key-value pairs (most common)
for key, value in student.items():
    print(f"{key}: {value}")
```

### Looping Through Strings

```python
text = "Python"

# Loop through characters
for char in text:
    print(char)

# With index
for index, char in enumerate(text):
    print(f"Character at {index}: {char}")
```

### Looping Through Tuples

```python
coordinates = [(0, 0), (1, 2), (3, 4), (5, 6)]

# Method 1: As single items
for coord in coordinates:
    print(coord)

# Method 2: Unpacking
for x, y in coordinates:
    print(f"X: {x}, Y: {y}")
```

---

## 5. Nested Loops

Loops inside loops - useful for 2D data, patterns, and combinations.

### Basic Nested Loop

```python
# Multiplication table
for i in range(1, 4):
    for j in range(1, 4):
        print(f"{i} x {j} = {i * j}")
    print()  # Empty line after each outer loop
```

### Pattern Printing

```python
# Right triangle pattern
for i in range(1, 6):
    for j in range(i):
        print("*", end="")
    print()

# Output:
# *
# **
# ***
# ****
# *****

# Number pyramid
for i in range(1, 6):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()

# Output:
# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5
```

### Looping Through 2D Lists

```python
# Matrix (2D list)
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Access each element
for row in matrix:
    for element in row:
        print(element, end=" ")
    print()

# With indices
for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        print(f"[{i}][{j}] = {matrix[i][j]}")
```

---

## 6. Loop Control Statements

### break Statement

Exits the loop immediately.

```python
# Stop when finding target
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for num in numbers:
    if num == 5:
        print(f"Found {num}!")
        break
    print(num)

# Output: 1 2 3 4 Found 5!

# Search in list
fruits = ["apple", "banana", "orange", "mango"]
search = "orange"

for fruit in fruits:
    if fruit == search:
        print(f"✓ Found {search}!")
        break
else:
    print(f"✗ {search} not found!")
```

### continue Statement

Skips the rest of the current iteration and moves to the next.

```python
# Skip even numbers
for num in range(1, 11):
    if num % 2 == 0:
        continue
    print(num)

# Output: 1 3 5 7 9

# Skip specific values
for num in range(1, 11):
    if num == 5:
        continue
    print(num)

# Output: 1 2 3 4 6 7 8 9 10
```

### pass Statement

Does nothing - placeholder for future code.

```python
# Placeholder for future implementation
for i in range(5):
    if i == 3:
        pass  # TODO: Add logic here
    else:
        print(i)
```

### else Clause with for Loop

Executes when loop completes normally (not broken by `break`).

```python
# Search with else
numbers = [1, 2, 3, 4, 5]
search = 10

for num in numbers:
    if num == search:
        print(f"Found {search}!")
        break
else:
    print(f"{search} not found in list")

# Output: 10 not found in list
```

---

## 7. Common Loop Patterns

### Accumulator Pattern

```python
# Sum of numbers
total = 0
for num in range(1, 101):
    total += num
print(f"Sum: {total}")  # 5050

# Product of numbers
product = 1
for num in range(1, 6):
    product *= num
print(f"Product: {product}")  # 120 (factorial of 5)
```

### Counter Pattern

```python
# Count even numbers
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
count = 0

for num in numbers:
    if num % 2 == 0:
        count += 1

print(f"Even numbers: {count}")  # 5
```

### Filter Pattern

```python
# Get all even numbers
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
evens = []

for num in numbers:
    if num % 2 == 0:
        evens.append(num)

print(evens)  # [2, 4, 6, 8, 10]
```

### Transform Pattern

```python
# Square each number
numbers = [1, 2, 3, 4, 5]
squares = []

for num in numbers:
    squares.append(num ** 2)

print(squares)  # [1, 4, 9, 16, 25]
```

### Search Pattern

```python
# Find maximum
numbers = [45, 23, 67, 89, 12, 34]
maximum = numbers[0]

for num in numbers:
    if num > maximum:
        maximum = num

print(f"Maximum: {maximum}")  # 89
```

---

## 8. List Comprehensions (Preview)

A concise way to create lists using loops.

### Basic Syntax

```python
# Traditional way
squares = []
for i in range(10):
    squares.append(i ** 2)

# List comprehension (one line!)
squares = [i ** 2 for i in range(10)]
print(squares)  # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
```

### With Conditions

```python
# Get even numbers
evens = [num for num in range(20) if num % 2 == 0]
print(evens)  # [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]

# Transform strings
words = ["hello", "world", "python"]
uppercase = [word.upper() for word in words]
print(uppercase)  # ['HELLO', 'WORLD', 'PYTHON']
```

---

## 9. Practical Examples

### Example 1: Calculate Average

```python
numbers = [85, 90, 78, 92, 88]
total = 0

for num in numbers:
    total += num

average = total / len(numbers)
print(f"Average: {average:.2f}")
```

### Example 2: Find All Factors

```python
number = 24
factors = []

for i in range(1, number + 1):
    if number % i == 0:
        factors.append(i)

print(f"Factors of {number}: {factors}")
# Output: [1, 2, 3, 4, 6, 8, 12, 24]
```

### Example 3: Count Vowels

```python
text = "Hello World"
vowels = "aeiouAEIOU"
count = 0

for char in text:
    if char in vowels:
        count += 1

print(f"Vowels: {count}")  # 3
```

### Example 4: Reverse a String

```python
text = "Python"
reversed_text = ""

for char in text:
    reversed_text = char + reversed_text

print(reversed_text)  # "nohtyP"
```

### Example 5: FizzBuzz

```python
# Print numbers 1-20, but:
# - "Fizz" for multiples of 3
# - "Buzz" for multiples of 5
# - "FizzBuzz" for multiples of both

for num in range(1, 21):
    if num % 3 == 0 and num % 5 == 0:
        print("FizzBuzz")
    elif num % 3 == 0:
        print("Fizz")
    elif num % 5 == 0:
        print("Buzz")
    else:
        print(num)
```

---

## Practice Exercises

### Exercise 1: Sum and Average
Write a program that:
- Takes 5 numbers from user
- Calculates sum and average
- Displays results

### Exercise 2: Multiplication Table
Create a multiplication table from 1 to 10 for a given number.

### Exercise 3: Prime Number Checker
Check if a number is prime using a loop.

### Exercise 4: Pattern Printer
Print these patterns:
```
*
**
***
****
*****
```

```
    *
   ***
  *****
 *******
*********
```

### Exercise 5: List Operations
Given a list: `[12, 45, 23, 67, 34, 89, 56, 78, 90, 11]`
- Find sum and average
- Count numbers > 50
- Find second largest
- Get all even numbers

---

## Practice Project

**See:** `day08_pattern_generator.py` for the complete Pattern Generator project.

The project includes:
- 8+ different pattern types
- Customizable size and characters
- Nested loops practice
- User input handling
- Pattern gallery

---

## Quick Reference

### for Loop Syntax

```python
# Basic for loop
for item in sequence:
    # code

# With range
for i in range(start, stop, step):
    # code

# With enumerate
for index, value in enumerate(sequence):
    # code

# Dictionary items
for key, value in dict.items():
    # code
```

### Loop Control

```python
break      # Exit loop immediately
continue   # Skip to next iteration
pass       # Do nothing (placeholder)
else:      # Execute if loop completes normally
```

### Common Patterns

```python
# Sum
total = sum(numbers)

# Count
count = len([x for x in items if condition])

# Filter
filtered = [x for x in items if condition]

# Transform
transformed = [func(x) for x in items]
```

---

## Key Takeaways

✅ `for` loops iterate over sequences  
✅ `range()` generates number sequences  
✅ Use `enumerate()` when you need both index and value  
✅ `break` exits loop, `continue` skips iteration  
✅ Nested loops for 2D data and patterns  
✅ List comprehensions for concise code  
✅ `else` clause runs if loop completes normally  
✅ Common patterns: accumulator, counter, filter, transform  

---

## Common Mistakes to Avoid

❌ **Modifying list while iterating**
```python
# Bad
numbers = [1, 2, 3, 4, 5]
for num in numbers:
    numbers.remove(num)  # Don't do this!

# Good
numbers = [1, 2, 3, 4, 5]
numbers_to_remove = []
for num in numbers:
    if condition:
        numbers_to_remove.append(num)
for num in numbers_to_remove:
    numbers.remove(num)
```


---

## Next Steps

Tomorrow (Day 9), we'll learn about **while loops** - loops that continue until a condition becomes False!

---

## Resources

- [Python for Loops Documentation](https://docs.python.org/3/tutorial/controlflow.html#for-statements)
- [Python range() Function](https://docs.python.org/3/library/stdtypes.html#range)

---

**Loop It Up! **
