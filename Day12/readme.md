# Day 12: Scope & Recursion

## Overview
Today we'll master two important concepts: **Scope** (understanding where variables are accessible) and **Recursion** (functions that call themselves). These concepts are crucial for writing clean, efficient code.

---

## Part 1: Variable Scope

## 1. Understanding Scope

Scope determines where variables can be accessed in your code.

### The LEGB Rule

Python searches for variables in this order:
1. **L**ocal - Inside current function
2. **E**nclosing - Inside enclosing functions
3. **G**lobal - At module level
4. **B**uilt-in - Python's built-in names

```python
x = "global"  # Global scope

def outer():
    x = "enclosing"  # Enclosing scope
    
    def inner():
        x = "local"  # Local scope
        print(x)
    
    inner()
    print(x)

outer()
print(x)

# Output:
# local
# enclosing
# global
```

---

## 2. Local Scope

Variables created inside a function.

### Basic Local Scope

```python
def my_function():
    x = 10  # Local variable
    print(x)

my_function()  # 10
# print(x)     # Error! x doesn't exist outside function
```

### Multiple Functions, Multiple Local Scopes

```python
def function_a():
    x = 5
    print(f"Function A: {x}")

def function_b():
    x = 10
    print(f"Function B: {x}")

function_a()  # Function A: 5
function_b()  # Function B: 10

# Each function has its own x
```

---

## 3. Global Scope

Variables created at the module level (outside all functions).

### Reading Global Variables

```python
count = 0  # Global variable

def show_count():
    print(count)  # Can read global variable

show_count()  # 0
```

### Modifying Global Variables

```python
count = 0

def increment():
    global count  # Declare we want to modify global count
    count += 1

increment()
print(count)  # 1

increment()
print(count)  # 2
```

### Local vs Global - Same Name

```python
x = 10  # Global x

def my_function():
    x = 5  # Local x (different from global)
    print(f"Inside: {x}")

my_function()        # Inside: 5
print(f"Outside: {x}")  # Outside: 10
```

### Best Practice: Avoid global

```python
# ❌ Bad - Using global
count = 0

def increment():
    global count
    count += 1

# ✅ Better - Return values
def increment(count):
    return count + 1

count = 0
count = increment(count)
```

---

## 4. Enclosing Scope

Variables in outer (enclosing) functions.

### Basic Enclosing Scope

```python
def outer():
    x = "outer"
    
    def inner():
        print(x)  # Accesses x from outer function
    
    inner()

outer()  # outer
```

### nonlocal Keyword

Modify variables in enclosing scope.

```python
def outer():
    count = 0
    
    def inner():
        nonlocal count  # Modify enclosing variable
        count += 1
        print(f"Count: {count}")
    
    inner()  # Count: 1
    inner()  # Count: 2
    print(f"Final count: {count}")  # Final count: 2

outer()
```

### Nested Functions Example

```python
def make_counter():
    count = 0
    
    def increment():
        nonlocal count
        count += 1
        return count
    
    def decrement():
        nonlocal count
        count -= 1
        return count
    
    def get_count():
        return count
    
    return increment, decrement, get_count

inc, dec, get = make_counter()

print(inc())  # 1
print(inc())  # 2
print(dec())  # 1
print(get())  # 1
```

---

## 5. Built-in Scope

Python's built-in functions and names.

```python
# Built-in functions
print(len([1, 2, 3]))  # len is built-in
print(max([1, 2, 3]))  # max is built-in

# Don't override built-ins!
# ❌ Bad
def len(x):
    return 0

# Now you've broken the built-in len()!
```

---

## 6. Scope Best Practices

### 1. Prefer Local Variables

```python
# ✅ Good
def calculate_total(items):
    total = 0
    for item in items:
        total += item
    return total

# ❌ Avoid
total = 0
def calculate_total(items):
    global total
    for item in items:
        total += item
```

### 2. Pass Parameters, Return Values

```python
# ✅ Good
def process_data(data):
    result = data * 2
    return result

# ❌ Avoid
data = None
def process_data():
    global data
    data = data * 2
```

### 3. Use Descriptive Names

```python
# ✅ Good
def calculate_average(numbers):
    total = sum(numbers)
    count = len(numbers)
    return total / count

# ❌ Avoid
def calc(x):
    t = sum(x)
    c = len(x)
    return t / c
```

---

## Part 2: Recursion

## 7. What is Recursion?

A function that calls itself to solve a problem by breaking it into smaller, similar subproblems.

### Anatomy of Recursion

Every recursive function needs:
1. **Base case** - When to stop
2. **Recursive case** - Call itself with simpler input

```python
def countdown(n):
    # Base case
    if n <= 0:
        print("Blast off!")
        return
    
    # Recursive case
    print(n)
    countdown(n - 1)  # Call itself with smaller input

countdown(5)
# Output: 5 4 3 2 1 Blast off!
```

---

## 8. Basic Recursion Examples

### Example 1: Factorial

```python
def factorial(n):
    """
    Calculate n! (n factorial)
    5! = 5 × 4 × 3 × 2 × 1 = 120
    """
    # Base case
    if n == 0 or n == 1:
        return 1
    
    # Recursive case
    return n * factorial(n - 1)

print(factorial(5))  # 120
print(factorial(0))  # 1

# How it works:
# factorial(5) = 5 * factorial(4)
# factorial(4) = 4 * factorial(3)
# factorial(3) = 3 * factorial(2)
# factorial(2) = 2 * factorial(1)
# factorial(1) = 1 (base case)
# Then multiply back: 1 * 2 * 3 * 4 * 5 = 120
```

### Example 2: Sum of List

```python
def sum_list(numbers):
    """Sum all numbers in a list recursively."""
    # Base case: empty list
    if not numbers:
        return 0
    
    # Recursive case: first element + sum of rest
    return numbers[0] + sum_list(numbers[1:])

print(sum_list([1, 2, 3, 4, 5]))  # 15

# How it works:
# sum_list([1,2,3,4,5]) = 1 + sum_list([2,3,4,5])
# sum_list([2,3,4,5])   = 2 + sum_list([3,4,5])
# sum_list([3,4,5])     = 3 + sum_list([4,5])
# sum_list([4,5])       = 4 + sum_list([5])
# sum_list([5])         = 5 + sum_list([])
# sum_list([])          = 0 (base case)
# Then add back: 0 + 5 + 4 + 3 + 2 + 1 = 15
```

### Example 3: Power Function

```python
def power(base, exponent):
    """
    Calculate base^exponent recursively.
    2^3 = 2 × 2 × 2 = 8
    """
    # Base case
    if exponent == 0:
        return 1
    
    # Recursive case
    return base * power(base, exponent - 1)

print(power(2, 3))  # 8
print(power(5, 2))  # 25
```

---

## 9. Classic Recursion Problems

### Fibonacci Sequence

```python
def fibonacci(n):
    """
    Return nth Fibonacci number.
    Sequence: 0, 1, 1, 2, 3, 5, 8, 13, ...
    """
    # Base cases
    if n <= 0:
        return 0
    if n == 1:
        return 1
    
    # Recursive case
    return fibonacci(n - 1) + fibonacci(n - 2)

# Print first 10 Fibonacci numbers
for i in range(10):
    print(fibonacci(i), end=" ")
# Output: 0 1 1 2 3 5 8 13 21 34
```

### String Reversal

```python
def reverse_string(s):
    """Reverse a string recursively."""
    # Base case
    if len(s) <= 1:
        return s
    
    # Recursive case: last char + reverse of rest
    return s[-1] + reverse_string(s[:-1])

print(reverse_string("hello"))  # olleh
print(reverse_string("Python"))  # nohtyP
```

### Palindrome Checker

```python
def is_palindrome(s):
    """Check if string is palindrome recursively."""
    # Remove spaces and convert to lowercase
    s = s.replace(" ", "").lower()
    
    # Base cases
    if len(s) <= 1:
        return True
    
    # Check first and last characters
    if s[0] != s[-1]:
        return False
    
    # Recursive case: check middle part
    return is_palindrome(s[1:-1])

print(is_palindrome("radar"))      # True
print(is_palindrome("hello"))      # False
print(is_palindrome("A man a plan a canal Panama"))  # True
```

### Greatest Common Divisor (GCD)

```python
def gcd(a, b):
    """
    Find GCD using Euclidean algorithm (recursive).
    """
    # Base case
    if b == 0:
        return a
    
    # Recursive case
    return gcd(b, a % b)

print(gcd(48, 18))  # 6
print(gcd(100, 35))  # 5
```

---

## 10. Tree Recursion

Problems that branch into multiple recursive calls.

### Binary Tree Sum

```python
def sum_digits(n):
    """Sum all digits of a number recursively."""
    # Base case
    if n < 10:
        return n
    
    # Recursive case: last digit + sum of remaining
    return (n % 10) + sum_digits(n // 10)

print(sum_digits(12345))  # 15 (1+2+3+4+5)
print(sum_digits(999))    # 27 (9+9+9)
```

### Tower of Hanoi

```python
def hanoi(n, source, target, auxiliary):
    """
    Solve Tower of Hanoi puzzle.
    Move n disks from source to target using auxiliary.
    """
    # Base case: only one disk
    if n == 1:
        print(f"Move disk 1 from {source} to {target}")
        return
    
    # Recursive case:
    # 1. Move n-1 disks from source to auxiliary
    hanoi(n - 1, source, auxiliary, target)
    
    # 2. Move largest disk from source to target
    print(f"Move disk {n} from {source} to {target}")
    
    # 3. Move n-1 disks from auxiliary to target
    hanoi(n - 1, auxiliary, target, source)

hanoi(3, 'A', 'C', 'B')
```

---

## 11. Recursion vs Iteration

### When to Use Recursion

✅ **Use recursion when:**
- Problem has recursive structure (trees, graphs)
- Solution is naturally recursive (Fibonacci, factorial)
- Code is clearer with recursion

### When to Use Iteration

✅ **Use iteration when:**
- Simple counting/looping
- Performance is critical
- Risk of stack overflow

### Same Problem - Both Ways

```python
# Factorial - Recursive
def factorial_recursive(n):
    if n <= 1:
        return 1
    return n * factorial_recursive(n - 1)

# Factorial - Iterative
def factorial_iterative(n):
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

# Both produce same result
print(factorial_recursive(5))  # 120
print(factorial_iterative(5))  # 120
```

---

## 12. Recursion Pitfalls

### Stack Overflow

```python
#  Infinite recursion - no base case!
def bad_recursion(n):
    return bad_recursion(n - 1)

# This will crash with RecursionError
# bad_recursion(5)
```

### Too Many Recursive Calls

```python
#  Inefficient - recalculates same values
def fibonacci_slow(n):
    if n <= 1:
        return n
    return fibonacci_slow(n - 1) + fibonacci_slow(n - 2)

# ✅ Better - with memoization
def fibonacci_fast(n, memo={}):
    if n in memo:
        return memo[n]
    if n <= 1:
        return n
    
    memo[n] = fibonacci_fast(n - 1, memo) + fibonacci_fast(n - 2, memo)
    return memo[n]

# Much faster!
print(fibonacci_fast(100))
```

---

## 13. Tail Recursion (Advanced)

Recursion where recursive call is the last operation.

```python
# Regular recursion (not tail recursive)
def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n - 1)  # Multiplication after recursive call

# Tail recursive version
def factorial_tail(n, accumulator=1):
    if n <= 1:
        return accumulator
    return factorial_tail(n - 1, n * accumulator)  # Recursive call is last

print(factorial_tail(5))  # 120
```

**Note:** Python doesn't optimize tail recursion, but it's good to know!

---

## 14. Practical Recursion Examples

### Directory Traversal (Simulated)

```python
def count_files(directory):
    """
    Count files in directory recursively.
    (Simulated with nested lists)
    """
    count = 0
    
    for item in directory:
        if isinstance(item, list):
            # It's a subdirectory - recurse
            count += count_files(item)
        else:
            # It's a file
            count += 1
    
    return count

# Simulated directory structure
files = [
    "file1.txt",
    "file2.txt",
    ["subdir1", "file3.txt", "file4.txt"],
    ["subdir2", ["subdir3", "file5.txt"]]
]

print(f"Total files: {count_files(files)}")  # 5
```

### Binary Search (Recursive)

```python
def binary_search(arr, target, left=0, right=None):
    """
    Search for target in sorted array using recursion.
    """
    if right is None:
        right = len(arr) - 1
    
    # Base case: not found
    if left > right:
        return -1
    
    # Find middle
    mid = (left + right) // 2
    
    # Base case: found
    if arr[mid] == target:
        return mid
    
    # Recursive cases
    if arr[mid] > target:
        return binary_search(arr, target, left, mid - 1)
    else:
        return binary_search(arr, target, mid + 1, right)

numbers = [1, 3, 5, 7, 9, 11, 13, 15]
print(binary_search(numbers, 7))   # 3
print(binary_search(numbers, 10))  # -1
```

---

## Practice Exercises

### Exercise 1: List Length
Write a recursive function to find the length of a list without using `len()`.

### Exercise 2: Count Occurrences
Count how many times a value appears in a list recursively.

### Exercise 3: Flatten List
Flatten a nested list recursively.
```python
# Input: [1, [2, 3], [4, [5, 6]]]
# Output: [1, 2, 3, 4, 5, 6]
```

### Exercise 4: Tree Sum
Calculate the sum of all values in a binary tree (represented as nested lists).

### Exercise 5: Generate Permutations
Generate all permutations of a string recursively.

---

## Practice Project

**See:** `day12_recursion_visualizer.py` for the complete Recursion Visualizer project.

The project includes:
- Visual recursion demonstrations
- Step-by-step execution trace
- Classic recursive problems
- Performance comparisons
- Interactive exploration

---

## Quick Reference

### Scope Keywords

```python
# global - modify global variable
global variable_name

# nonlocal - modify enclosing variable
nonlocal variable_name
```

### Recursion Template

```python
def recursive_function(parameters):
    # Base case(s) - when to stop
    if base_condition:
        return base_value
    
    # Recursive case - call itself with simpler input
    return recursive_function(modified_parameters)
```

### Common Recursive Patterns

```python
# Countdown
def countdown(n):
    if n <= 0: return
    print(n)
    countdown(n - 1)

# Sum
def sum_list(lst):
    if not lst: return 0
    return lst[0] + sum_list(lst[1:])

# Tree recursion
def fibonacci(n):
    if n <= 1: return n
    return fibonacci(n-1) + fibonacci(n-2)
```

---

## Key Takeaways

✅ **LEGB Rule**: Local → Enclosing → Global → Built-in  
✅ Use `global` to modify global variables (avoid when possible)  
✅ Use `nonlocal` to modify enclosing variables  
✅ Prefer passing parameters and returning values  
✅ Recursion needs base case and recursive case  
✅ Every recursive call should move toward base case  
✅ Recursion can be elegant but may be slower  
✅ Watch out for infinite recursion and stack overflow  
✅ Consider memoization for repeated calculations  

---

## Common Mistakes to Avoid

 **Forgetting base case**
```python
def bad_recursion(n):
    return bad_recursion(n - 1)  # Never stops!
```

 **Not moving toward base case**
```python
def bad_countdown(n):
    if n == 0: return
    print(n)
    countdown(n)  # n never changes!
```

 **Overusing global variables**
```python
# Bad
result = 0
def calculate():
    global result
    result = 42

# Better
def calculate():
    return 42
result = calculate()
```

---

## Next Steps

Tomorrow (Day 13), we'll learn about **Error Handling** - how to gracefully handle errors using try-except blocks!

---

## Resources

- [Python Scope Documentation](https://docs.python.org/3/tutorial/classes.html#python-scopes-and-namespaces)
- [Recursion in Python](https://realpython.com/python-thinking-recursively/)

---

**Master Scope & Recursion! **
