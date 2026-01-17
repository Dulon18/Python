# Day 11: Functions - Advanced

## Overview
Today we'll explore advanced function concepts: `*args`, `**kwargs`, lambda functions, decorators, higher-order functions, and more. These features make Python functions incredibly powerful and flexible!

---

## 1. Variable-Length Arguments (*args)

Accept any number of positional arguments.

### Basic *args

```python
def sum_all(*args):
    """Sum any number of arguments."""
    total = 0
    for num in args:
        total += num
    return total

print(sum_all(1, 2, 3))           # 6
print(sum_all(10, 20, 30, 40))    # 100
print(sum_all(5))                  # 5
```

### How *args Works

```python
def print_info(*args):
    """Print all arguments."""
    print(f"Type: {type(args)}")  # <class 'tuple'>
    print(f"Arguments: {args}")
    
    for i, arg in enumerate(args):
        print(f"  Argument {i}: {arg}")

print_info("Python", 3.11, True, [1, 2, 3])
```

### Mixing Regular Parameters with *args

```python
def greet(greeting, *names):
    """Greet multiple people."""
    for name in names:
        print(f"{greeting}, {name}!")

greet("Hello", "Alice", "Bob", "Charlie")
# Output:
# Hello, Alice!
# Hello, Bob!
# Hello, Charlie!
```

### Important Rules

```python
# ✅ Correct - *args after regular parameters
def func(a, b, *args):
    pass

# ✅ Correct - *args before keyword-only parameters
def func(*args, c):
    pass

# ❌ Wrong - regular parameter after *args
def func(*args, b):  # b becomes keyword-only
    pass
```

---

## 2. Keyword Arguments (**kwargs)

Accept any number of keyword arguments.

### Basic **kwargs

```python
def print_info(**kwargs):
    """Print all keyword arguments."""
    print(f"Type: {type(kwargs)}")  # <class 'dict'>
    
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_info(name="Alice", age=25, city="NYC")
# Output:
# name: Alice
# age: 25
# city: NYC
```

### Practical Example

```python
def create_profile(**kwargs):
    """Create user profile with flexible fields."""
    profile = {
        "username": kwargs.get("username", "unknown"),
        "age": kwargs.get("age", 0),
        "email": kwargs.get("email", "not provided")
    }
    
    # Add any additional fields
    for key, value in kwargs.items():
        if key not in profile:
            profile[key] = value
    
    return profile

user1 = create_profile(username="alice", age=25, email="alice@email.com")
user2 = create_profile(username="bob", hobby="coding", location="NYC")

print(user1)
print(user2)
```

### Mixing Parameters, *args, and **kwargs

```python
def complex_function(a, b, *args, c=10, **kwargs):
    """
    Demonstrate all parameter types.
    
    a, b: required positional
    *args: additional positional
    c: keyword with default
    **kwargs: additional keyword
    """
    print(f"a: {a}")
    print(f"b: {b}")
    print(f"args: {args}")
    print(f"c: {c}")
    print(f"kwargs: {kwargs}")

complex_function(1, 2, 3, 4, c=20, x=100, y=200)
```

### Order Matters!

```python
# Correct order:
# 1. Regular parameters
# 2. *args
# 3. Keyword parameters (with defaults)
# 4. **kwargs

def proper_order(a, b, *args, c=10, d=20, **kwargs):
    pass

# ❌ This will cause errors
def wrong_order(**kwargs, *args):  # Wrong!
    pass
```

---

## 3. Lambda Functions

Anonymous, one-line functions.

### Basic Lambda

```python
# Regular function
def square(x):
    return x ** 2

# Lambda equivalent
square = lambda x: x ** 2

print(square(5))  # 25
```

### Lambda with Multiple Parameters

```python
# Addition
add = lambda a, b: a + b
print(add(5, 3))  # 8

# Maximum of three numbers
max_three = lambda a, b, c: max(a, max(b, c))
print(max_three(10, 25, 15))  # 25
```

### Lambda in Sorting

```python
# Sort by second element
pairs = [(1, 5), (3, 2), (2, 8), (4, 1)]
pairs.sort(key=lambda x: x[1])
print(pairs)  # [(4, 1), (3, 2), (1, 5), (2, 8)]

# Sort strings by length
words = ["python", "is", "awesome", "fun"]
words.sort(key=lambda x: len(x))
print(words)  # ['is', 'fun', 'python', 'awesome']

# Sort dictionaries
students = [
    {"name": "Alice", "age": 25},
    {"name": "Bob", "age": 20},
    {"name": "Charlie", "age": 23}
]
students.sort(key=lambda x: x["age"])
print(students)
```

### Lambda with map(), filter(), reduce()

```python
# map() - Apply function to each element
numbers = [1, 2, 3, 4, 5]
squares = list(map(lambda x: x**2, numbers))
print(squares)  # [1, 4, 9, 16, 25]

# filter() - Keep elements that match condition
evens = list(filter(lambda x: x % 2 == 0, numbers))
print(evens)  # [2, 4]

# reduce() - Reduce to single value
from functools import reduce
product = reduce(lambda x, y: x * y, numbers)
print(product)  # 120
```

### When to Use Lambda

✅ **Use lambda for:**
- Short, simple operations
- One-time use functions
- Sorting keys
- map/filter operations

❌ **Avoid lambda for:**
- Complex logic
- Multiple statements
- Functions you'll reuse
- Functions needing documentation

```python
# ✅ Good use of lambda
nums.sort(key=lambda x: abs(x))

# ❌ Bad - too complex
process = lambda x: x * 2 if x > 0 else x / 2 if x < 0 else 0

# ✅ Better - use regular function
def process(x):
    if x > 0:
        return x * 2
    elif x < 0:
        return x / 2
    else:
        return 0
```

---

## 4. Higher-Order Functions

Functions that take functions as arguments or return functions.

### Functions as Arguments

```python
def apply_operation(numbers, operation):
    """Apply operation to all numbers."""
    result = []
    for num in numbers:
        result.append(operation(num))
    return result

# Different operations
numbers = [1, 2, 3, 4, 5]

doubled = apply_operation(numbers, lambda x: x * 2)
squared = apply_operation(numbers, lambda x: x ** 2)

print(doubled)  # [2, 4, 6, 8, 10]
print(squared)  # [1, 4, 9, 16, 25]
```

### Functions Returning Functions

```python
def make_multiplier(n):
    """Return a function that multiplies by n."""
    def multiplier(x):
        return x * n
    return multiplier

times_2 = make_multiplier(2)
times_5 = make_multiplier(5)

print(times_2(10))  # 20
print(times_5(10))  # 50
```

### Practical Example: Validator Factory

```python
def make_validator(min_val, max_val):
    """Create a validator function."""
    def validate(value):
        return min_val <= value <= max_val
    return validate

age_validator = make_validator(0, 120)
percentage_validator = make_validator(0, 100)

print(age_validator(25))   # True
print(age_validator(150))  # False
print(percentage_validator(85))  # True
```

---

## 5. Decorators (Introduction)

Functions that modify other functions.

### Basic Decorator

```python
def uppercase_decorator(func):
    """Decorator to convert result to uppercase."""
    def wrapper():
        result = func()
        return result.upper()
    return wrapper

@uppercase_decorator
def greet():
    return "hello, world"

print(greet())  # HELLO, WORLD
```

### How Decorators Work

```python
# Using @ syntax
@uppercase_decorator
def greet():
    return "hello"

# Is equivalent to:
def greet():
    return "hello"
greet = uppercase_decorator(greet)
```

### Decorator with Arguments

```python
def log_function(func):
    """Log when function is called."""
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__}...")
        result = func(*args, **kwargs)
        print(f"{func.__name__} returned: {result}")
        return result
    return wrapper

@log_function
def add(a, b):
    return a + b

result = add(5, 3)
# Output:
# Calling add...
# add returned: 8
```

### Multiple Decorators

```python
def bold(func):
    def wrapper():
        return f"<b>{func()}</b>"
    return wrapper

def italic(func):
    def wrapper():
        return f"<i>{func()}</i>"
    return wrapper

@bold
@italic
def greet():
    return "Hello"

print(greet())  # <b><i>Hello</i></b>
```

### Practical Decorator: Timer

```python
import time

def timer(func):
    """Measure function execution time."""
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
    return "Done"

slow_function()
```

---

## 6. Closures

Functions that remember values from their enclosing scope.

### Basic Closure

```python
def outer(x):
    """Outer function."""
    def inner(y):
        """Inner function that remembers x."""
        return x + y
    return inner

add_5 = outer(5)
add_10 = outer(10)

print(add_5(3))   # 8  (5 + 3)
print(add_10(3))  # 13 (10 + 3)
```

### Practical Example: Counter

```python
def make_counter():
    """Create a counter function."""
    count = 0
    
    def counter():
        nonlocal count
        count += 1
        return count
    
    return counter

counter1 = make_counter()
counter2 = make_counter()

print(counter1())  # 1
print(counter1())  # 2
print(counter1())  # 3

print(counter2())  # 1
print(counter2())  # 2
```

### Why Use Closures?

✅ Data encapsulation  
✅ Function factories  
✅ Decorators  
✅ Callbacks with state  

---

## 7. Recursion (Preview)

Functions that call themselves.

### Basic Recursion

```python
def factorial(n):
    """Calculate factorial recursively."""
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

print(factorial(5))  # 120
```

### Fibonacci

```python
def fibonacci(n):
    """Generate nth Fibonacci number."""
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

print(fibonacci(7))  # 13
```

**Note:** We'll cover recursion in detail on Day 12!

---

## 8. Function Annotations (Type Hints)

Document expected types.

### Basic Type Hints

```python
def greet(name: str) -> str:
    """Greet a person."""
    return f"Hello, {name}!"

def add(a: int, b: int) -> int:
    """Add two integers."""
    return a + b
```

### Complex Type Hints

```python
from typing import List, Dict, Tuple, Optional

def process_numbers(numbers: List[int]) -> Tuple[int, float]:
    """Process a list of numbers."""
    total = sum(numbers)
    average = total / len(numbers)
    return total, average

def get_user(user_id: int) -> Optional[Dict[str, str]]:
    """Get user by ID, return None if not found."""
    # Implementation
    pass
```

**Note:** Type hints are optional and not enforced at runtime!

---

## 9. Practical Examples

### Example 1: Flexible Logger

```python
def log_message(message, *tags, level="INFO", **metadata):
    """
    Log a message with tags and metadata.
    
    Args:
        message: Log message
        *tags: Variable tags
        level: Log level
        **metadata: Additional info
    """
    tag_str = ", ".join(tags) if tags else "None"
    
    print(f"[{level}] {message}")
    print(f"  Tags: {tag_str}")
    
    if metadata:
        print("  Metadata:")
        for key, value in metadata.items():
            print(f"    {key}: {value}")

log_message(
    "User logged in",
    "auth", "security",
    level="INFO",
    user_id=123,
    ip="192.168.1.1"
)
```

### Example 2: Retry Decorator

```python
def retry(max_attempts=3):
    """Retry function on failure."""
    def decorator(func):
        def wrapper(*args, **kwargs):
            for attempt in range(max_attempts):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    if attempt == max_attempts - 1:
                        raise
                    print(f"Attempt {attempt + 1} failed: {e}")
            return None
        return wrapper
    return decorator

@retry(max_attempts=3)
def unstable_function():
    import random
    if random.random() < 0.7:
        raise Exception("Random failure")
    return "Success!"
```

### Example 3: Memoization (Caching)

```python
def memoize(func):
    """Cache function results."""
    cache = {}
    
    def wrapper(*args):
        if args in cache:
            print(f"Using cached result for {args}")
            return cache[args]
        
        result = func(*args)
        cache[args] = result
        return result
    
    return wrapper

@memoize
def fibonacci(n):
    """Calculate Fibonacci (expensive without cache)."""
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

print(fibonacci(10))  # Much faster with caching!
```

---

## Practice Exercises

### Exercise 1: Flexible Calculator
Create a function that:
- Accepts any number of numbers
- Accepts operation as keyword argument
- Supports: sum, product, average, max, min

### Exercise 2: Function Composer
Create a function that combines multiple functions:
```python
def compose(*functions):
    # Return a function that applies all functions in sequence
    pass

# Example usage
add_5 = lambda x: x + 5
multiply_2 = lambda x: x * 2
combined = compose(add_5, multiply_2)
print(combined(10))  # (10 + 5) * 2 = 30
```

### Exercise 3: Validation Decorator
Create a decorator that validates function arguments:
```python
@validate_positive
def divide(a, b):
    return a / b
```

### Exercise 4: Rate Limiter
Create a decorator that limits function calls per minute.

### Exercise 5: Argument Logger
Create a decorator that logs all arguments and return values.

---

## Practice Project

**See:** `day11_decorator_showcase.py` for the complete Decorator Showcase project.

The project includes:
- Multiple useful decorators
- Interactive testing interface
- Real-world applications
- Performance monitoring
- Error handling decorators

---

## Quick Reference

### *args and **kwargs

```python
def func(*args, **kwargs):
    # args is tuple of positional arguments
    # kwargs is dict of keyword arguments
    pass
```

### Lambda Functions

```python
# Basic
lambda x: x * 2

# Multiple parameters
lambda a, b: a + b

# With condition
lambda x: "even" if x % 2 == 0 else "odd"
```

### Decorators

```python
def my_decorator(func):
    def wrapper(*args, **kwargs):
        # Before function call
        result = func(*args, **kwargs)
        # After function call
        return result
    return wrapper

@my_decorator
def my_function():
    pass
```

---

## Key Takeaways

✅ `*args` accepts variable positional arguments (tuple)  
✅ `**kwargs` accepts variable keyword arguments (dict)  
✅ Lambda creates anonymous functions  
✅ Higher-order functions take/return functions  
✅ Decorators modify function behavior  
✅ Closures remember enclosing scope  
✅ Type hints document expected types  
✅ Order: regular, *args, defaults, **kwargs  

---

## Common Mistakes to Avoid

❌ **Wrong parameter order**
```python
# Wrong
def func(**kwargs, *args):  # Error!
    pass

# Correct
def func(*args, **kwargs):
    pass
```

❌ **Complex lambda functions**
```python
# Bad
calc = lambda x, y: x * 2 if x > y else y * 2 if y > x else 0

# Better
def calc(x, y):
    if x > y:
        return x * 2
    elif y > x:
        return y * 2
    return 0
```

❌ **Modifying mutable default arguments**
```python
# Dangerous!
def add_item(item, items=[]):
    items.append(item)
    return items

# Better
def add_item(item, items=None):
    if items is None:
        items = []
    items.append(item)
    return items
```

---

## Next Steps

Tomorrow (Day 12), we'll learn about **Scope & Recursion** - understanding variable scope and mastering recursive functions!

---

## Resources

- [Python *args and **kwargs](https://docs.python.org/3/tutorial/controlflow.html#arbitrary-argument-lists)
- [Python Decorators](https://docs.python.org/3/glossary.html#term-decorator)
- [Lambda Expressions](https://docs.python.org/3/tutorial/controlflow.html#lambda-expressions)

---

**Level Up Your Functions! 🐍**
