#  Day 23: Decorators & Generators in Python

> **Week 4 — Advanced Topics** | 30-Day Python Learning Plan

Two powerful Python features that make your code cleaner, smarter, and more memory-efficient.

---

## 📌 Part A — Decorators

A decorator is a function that **wraps another function** to add extra behavior — without changing the original function's code.

Think of it like a gift wrapper 🎁 — the gift (function) stays the same, but the wrapper adds something extra around it.

---

### 1. Basic Decorator Structure

```python
def my_decorator(func):
    def wrapper(*args, **kwargs):
        print("Before the function runs")
        result = func(*args, **kwargs)
        print("After the function runs")
        return result
    return wrapper

@my_decorator
def say_hello():
    print("Hello!")

say_hello()
# Output:
# Before the function runs
# Hello!
# After the function runs
```

> **`@my_decorator`** is shorthand for `say_hello = my_decorator(say_hello)`

---

### 2. How Decorators Work — Step by Step

```python
# Step 1: Without @ syntax (manual way)
def greet():
    print("Good morning!")

greet = my_decorator(greet)  # wrapping manually
greet()

# Step 2: With @ syntax (clean way)
@my_decorator
def greet():
    print("Good morning!")

greet()  # same result, cleaner code
```

---

### 3. Practical Decorators

#### ⏱️ Timer Decorator — measure how long a function takes

```python
import time

def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} took {end - start:.4f} seconds")
        return result
    return wrapper

@timer
def slow_function():
    time.sleep(1)
    print("Done!")

slow_function()
# Done!
# slow_function took 1.0012 seconds
```

---

#### 📋 Logger Decorator — log every function call

```python
def logger(func):
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__} with args={args}, kwargs={kwargs}")
        result = func(*args, **kwargs)
        print(f"{func.__name__} returned {result}")
        return result
    return wrapper

@logger
def add(a, b):
    return a + b

add(3, 5)
# Calling add with args=(3, 5), kwargs={}
# add returned 8
```

---

#### 🔐 Login Required Decorator — protect functions

```python
is_logged_in = True

def login_required(func):
    def wrapper(*args, **kwargs):
        if not is_logged_in:
            print("Please login first!")
            return
        return func(*args, **kwargs)
    return wrapper

@login_required
def view_dashboard():
    print("Welcome to your dashboard!")

view_dashboard()
# Welcome to your dashboard!
```

---

#### 🔁 Retry Decorator — retry on failure

```python
import time

def retry(times=3):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for attempt in range(1, times + 1):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    print(f"Attempt {attempt} failed: {e}")
                    time.sleep(1)
            print("All attempts failed.")
        return wrapper
    return decorator

@retry(times=3)
def connect_to_server():
    raise ConnectionError("Server not responding")

connect_to_server()
# Attempt 1 failed: Server not responding
# Attempt 2 failed: Server not responding
# Attempt 3 failed: Server not responding
# All attempts failed.
```

---

### 4. Stacking Multiple Decorators

You can apply more than one decorator to a single function. They run from **bottom to top**.

```python
@logger
@timer
def multiply(a, b):
    return a * b

multiply(4, 5)
# timer runs first (bottom), then logger (top)
```

---

### 5. Preserving Function Metadata with `functools.wraps`

Without `functools.wraps`, the wrapped function loses its name and docstring.

```python
from functools import wraps

def my_decorator(func):
    @wraps(func)  # preserves original function's name and docs
    def wrapper(*args, **kwargs):
        print("Decorated!")
        return func(*args, **kwargs)
    return wrapper

@my_decorator
def greet():
    """Says hello"""
    print("Hello!")

print(greet.__name__)  # greet (not wrapper)
print(greet.__doc__)   # Says hello
```

> ✅ Always use `@wraps(func)` inside your decorators — it's best practice.

---

## 📌 Part B — Generators

A generator is a function that **produces values one at a time** using `yield` instead of returning everything at once. This saves memory, especially for large datasets.

---

### 1. `yield` vs `return`

```python
# Normal function — loads ALL data into memory at once
def normal_squares(n):
    result = []
    for i in range(n):
        result.append(i * i)
    return result  # returns full list

# Generator — produces ONE value at a time
def gen_squares(n):
    for i in range(n):
        yield i * i  # pauses here, sends value, then resumes
```

| | `return` | `yield` |
|---|---|---|
| Returns | Once, then stops | Many times, pauses each time |
| Memory | Stores ALL results | Produces ONE at a time |
| Type | Regular value | Generator object |
| Use case | Small data | Large data, infinite sequences |

---

### 2. Using a Generator

```python
gen = gen_squares(5)

print(next(gen))  # 0
print(next(gen))  # 1
print(next(gen))  # 4

# Or loop through it
for val in gen_squares(5):
    print(val)
# 0
# 1
# 4
# 9
# 16
```

---

### 3. Real World Generator Examples

#### ♾️ Infinite Counter

```python
def counter(start=0):
    while True:
        yield start
        start += 1

c = counter(1)
print(next(c))  # 1
print(next(c))  # 2
print(next(c))  # 3
# runs forever, only computes when asked
```

---

#### 📂 Reading Large Files Line by Line

```python
# Without generator — loads entire file into memory (BAD for large files)
def read_all(filepath):
    with open(filepath, "r") as f:
        return f.readlines()  # all lines in memory at once

# With generator — reads one line at a time (GOOD)
def read_large_file(filepath):
    with open(filepath, "r") as f:
        for line in f:
            yield line.strip()

for line in read_large_file("big_file.txt"):
    print(line)
```

---

#### 🔢 Fibonacci Generator

```python
def fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

fib = fibonacci()
for _ in range(10):
    print(next(fib), end=" ")
# 0 1 1 2 3 5 8 13 21 34
```

---

#### 🔍 Filtering Data with a Generator

```python
def even_numbers(limit):
    for n in range(limit):
        if n % 2 == 0:
            yield n

for num in even_numbers(20):
    print(num, end=" ")
# 0 2 4 6 8 10 12 14 16 18
```

---

### 4. Generator Expressions (One-liners)

Just like list comprehensions but with `()` instead of `[]` — uses far less memory.

```python
# List comprehension — stores all values in memory
squares_list = [x * x for x in range(1000000)]

# Generator expression — computes one at a time
squares_gen = (x * x for x in range(1000000))

print(next(squares_gen))  # 0
print(next(squares_gen))  # 1
```

---

## 🛠️ Practice Project — Function Profiler using Decorators + Generator

This combines both concepts in one project.

```python
import time
from functools import wraps

# --- Decorator: Timer ---
def timer(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        elapsed = time.time() - start
        print(f"[TIMER] {func.__name__} completed in {elapsed:.6f} seconds")
        return result
    return wrapper

# --- Decorator: Logger ---
def logger(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"[LOG] Calling '{func.__name__}' | args={args}")
        result = func(*args, **kwargs)
        print(f"[LOG] '{func.__name__}' returned: {result}")
        return result
    return wrapper

# --- Generator: Large number sequence ---
def number_stream(limit):
    """Generates numbers one at a time up to limit"""
    n = 0
    while n < limit:
        yield n
        n += 1

# --- Function using both ---
@timer
@logger
def sum_stream(limit):
    """Sum all numbers in the stream using a generator"""
    total = sum(number_stream(limit))
    return total

# --- Run ---
result = sum_stream(1000000)
print(f"Sum: {result}")

# Output:
# [LOG] Calling 'sum_stream' | args=(1000000,)
# [LOG] 'sum_stream' returned: 499999500000
# [TIMER] sum_stream completed in 0.045123 seconds
# Sum: 499999500000
```

---

## 📝 Quick Summary

| Concept | Key Point |
|---|---|
| Decorator | Wraps a function to add behavior without modifying it |
| `@syntax` | Shorthand for `func = decorator(func)` |
| `*args, **kwargs` | Makes decorator work with any function signature |
| `@wraps(func)` | Preserves original function name and docstring |
| Generator | Produces values one at a time using `yield` |
| `yield` | Pauses function, sends value, resumes on next call |
| `next()` | Gets the next value from a generator |
| Generator expression | `(x for x in list)` — memory-efficient one-liner |

---

## 🔗 Resources

- [Python Decorators — Real Python](https://realpython.com/primer-on-python-decorators/)
- [Python Generators — Real Python](https://realpython.com/introduction-to-python-generators/)
- [Python `functools` Docs](https://docs.python.org/3/library/functools.html)

---

> 📅 Part of the **30-Day Python Learning Plan**
> Previous: [Day 22 - Regular Expressions](#) | Next: [Day 24 - Data Structures & Collections](#)
