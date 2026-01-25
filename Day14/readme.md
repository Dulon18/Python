# Day 14: Week 2 Review & Banking System

## Overview
Congratulations on completing Week 2! 🎉 Today we'll review everything you've learned and build a comprehensive Banking System that integrates all Week 2 concepts.

---

## 📚 Week 2 Summary

### Day 8: Loops - Part 1 (for loops)
```python
# Basic for loop
for i in range(5):
    print(i)

# Loop through list
fruits = ["apple", "banana", "orange"]
for fruit in fruits:
    print(fruit)

# Loop with enumerate
for index, value in enumerate(fruits):
    print(f"{index}: {value}")

# Nested loops
for i in range(3):
    for j in range(3):
        print(f"({i}, {j})")

# Loop control
for i in range(10):
    if i == 5:
        break  # Exit loop
    if i % 2 == 0:
        continue  # Skip iteration
    print(i)
```

**Key Concepts:**
- `range()` generates sequences
- `enumerate()` provides index and value
- Nested loops for 2D operations
- `break`, `continue`, `pass` for control
- List comprehensions for concise code

---

### Day 9: Loops - Part 2 (while loops)
```python
# Basic while loop
count = 0
while count < 5:
    print(count)
    count += 1

# Input validation
while True:
    age = input("Enter age: ")
    if age.isdigit() and int(age) > 0:
        break
    print("Invalid input!")

# Menu-driven program
while True:
    print("1. Option 1")
    print("2. Exit")
    choice = input("Choice: ")
    
    if choice == '1':
        print("Processing...")
    elif choice == '2':
        break
```

**Key Concepts:**
- Condition-based iteration
- Input validation loops
- `while True` with `break` for menus
- Flag-based loops
- Infinite loops (intentional vs accidental)

---

### Day 10: Functions - Basics
```python
# Basic function
def greet(name):
    """Greet a person."""
    return f"Hello, {name}!"

# Multiple parameters
def add(a, b):
    return a + b

# Default parameters
def power(base, exponent=2):
    return base ** exponent

# Multiple return values
def get_stats(numbers):
    return min(numbers), max(numbers), sum(numbers)

# Docstrings
def calculate_area(length, width):
    """
    Calculate rectangle area.
    
    Args:
        length: Rectangle length
        width: Rectangle width
    
    Returns:
        Area of rectangle
    """
    return length * width
```

**Key Concepts:**
- Functions make code reusable
- Parameters pass data in
- `return` sends data back
- Default parameters provide fallbacks
- Docstrings document functions
- Scope: local vs global

---

### Day 11: Functions - Advanced
```python
# *args - variable positional arguments
def sum_all(*args):
    return sum(args)

# **kwargs - variable keyword arguments
def create_profile(**kwargs):
    return kwargs

# Lambda functions
square = lambda x: x ** 2
nums.sort(key=lambda x: abs(x))

# Decorators
def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        print(f"Time: {time.time() - start}")
        return result
    return wrapper

@timer
def slow_function():
    time.sleep(1)

# Closures
def make_counter():
    count = 0
    def counter():
        nonlocal count
        count += 1
        return count
    return counter
```

**Key Concepts:**
- `*args` accepts any number of arguments (tuple)
- `**kwargs` accepts keyword arguments (dict)
- Lambda creates anonymous functions
- Decorators modify function behavior
- Closures remember enclosing scope
- Higher-order functions

---

### Day 12: Scope & Recursion
```python
# Scope - LEGB Rule
x = "global"

def outer():
    x = "enclosing"
    
    def inner():
        x = "local"
        print(x)  # local
    
    inner()
    print(x)  # enclosing

outer()
print(x)  # global

# global keyword
count = 0
def increment():
    global count
    count += 1

# nonlocal keyword
def outer():
    count = 0
    def inner():
        nonlocal count
        count += 1
    inner()

# Recursion
def factorial(n):
    if n <= 1:  # Base case
        return 1
    return n * factorial(n - 1)  # Recursive case

def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)
```

**Key Concepts:**
- LEGB: Local, Enclosing, Global, Built-in
- Use `global` to modify global variables
- Use `nonlocal` for enclosing scope
- Recursion needs base case and recursive case
- Each call moves toward base case
- Consider iteration vs recursion

---

### Day 13: Error Handling
```python
# Basic try-except
try:
    number = int(input("Enter number: "))
    result = 10 / number
except ValueError:
    print("Invalid number!")
except ZeroDivisionError:
    print("Cannot divide by zero!")

# try-except-else-finally
try:
    file = open("data.txt")
except FileNotFoundError:
    print("File not found!")
else:
    content = file.read()
    print(content)
finally:
    if file:
        file.close()

# Raising exceptions
def check_age(age):
    if age < 0:
        raise ValueError("Age cannot be negative!")
    return age

# Custom exceptions
class InvalidEmailError(Exception):
    pass

def validate_email(email):
    if '@' not in email:
        raise InvalidEmailError("Invalid email format")

# with statement
with open("data.txt", "r") as file:
    content = file.read()
# File automatically closed
```

**Key Concepts:**
- `try-except` handles errors gracefully
- Catch specific exceptions
- `else` runs on success
- `finally` always runs (cleanup)
- `raise` creates exceptions
- Custom exceptions for domain errors
- `with` statement for resource management

---

## 🎯 Concept Integration Quiz

### Question 1: Loops + Functions
```python
# What does this print?
def process(n):
    total = 0
    for i in range(n):
        if i % 2 == 0:
            total += i
    return total

print(process(10))
```
**Answer:** 20 (sum of even numbers 0+2+4+6+8)

### Question 2: Decorators + Error Handling
```python
# What happens here?
def safe_divide(func):
    def wrapper(a, b):
        try:
            return func(a, b)
        except ZeroDivisionError:
            return "Cannot divide by zero"
    return wrapper

@safe_divide
def divide(a, b):
    return a / b

print(divide(10, 0))
```
**Answer:** Prints "Cannot divide by zero" (decorator catches error)

### Question 3: Recursion + Error Handling
```python
# Is this safe?
def factorial(n):
    if n < 0:
        raise ValueError("Negative factorial")
    if n <= 1:
        return 1
    return n * factorial(n - 1)

try:
    print(factorial(-5))
except ValueError as e:
    print(e)
```
**Answer:** Prints "Negative factorial" (error caught and handled)

---

## 💡 Week 2 Key Patterns

### Pattern 1: Input Validation with Loops
```python
def get_positive_number():
    """Get positive number with validation."""
    while True:
        try:
            num = float(input("Enter positive number: "))
            if num > 0:
                return num
            print("Must be positive!")
        except ValueError:
            print("Invalid number!")
```

### Pattern 2: Decorator for Logging
```python
def log_calls(func):
    """Log function calls."""
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__}")
        result = func(*args, **kwargs)
        print(f"Returned: {result}")
        return result
    return wrapper
```

### Pattern 3: Safe Resource Management
```python
def safe_operation(filename):
    """Safe file operation."""
    try:
        with open(filename, 'r') as file:
            return file.read()
    except FileNotFoundError:
        return None
    except Exception as e:
        print(f"Error: {e}")
        return None
```

### Pattern 4: Recursive with Memoization
```python
def memoize(func):
    cache = {}
    def wrapper(n):
        if n not in cache:
            cache[n] = func(n)
        return cache[n]
    return wrapper

@memoize
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)
```

---

## 🚀 Banking System Project

**See:** `day14_banking_system.py` for the complete Banking System.

### Project Features:

**Account Management:**
- Create accounts with unique IDs
- Multiple account types (Savings, Checking)
- Account information display
- Transaction history

**Transactions:**
- Deposit money
- Withdraw money
- Transfer between accounts
- Balance inquiry

**Error Handling:**
- Input validation
- Insufficient funds checking
- Invalid account errors
- Transaction limits

**Advanced Features:**
- Interest calculation (savings accounts)
- Transaction fees
- Account statements
- Search and filter transactions
- Data persistence (simulated)

**Concepts Used:**
✅ for loops - iterating accounts, transactions  
✅ while loops - menu system, input validation  
✅ Functions - modular operations  
✅ *args/**kwargs - flexible parameters  
✅ Decorators - transaction logging  
✅ Recursion - menu navigation  
✅ Error handling - robust operations  
✅ Custom exceptions - banking errors  

---

## 📝 Week 2 Checklist

### Day 8: for Loops
- [ ] Understand range() function
- [ ] Can loop through lists, strings, dictionaries
- [ ] Know enumerate() for index+value
- [ ] Can write nested loops
- [ ] Understand break, continue, pass
- [ ] Can create list comprehensions

### Day 9: while Loops
- [ ] Understand condition-based loops
- [ ] Can write input validation loops
- [ ] Know while True with break pattern
- [ ] Understand infinite loops and how to avoid
- [ ] Can choose between for and while

### Day 10: Functions - Basics
- [ ] Can define and call functions
- [ ] Understand parameters and arguments
- [ ] Know return statement usage
- [ ] Can use default parameters
- [ ] Understand keyword arguments
- [ ] Can write docstrings
- [ ] Understand local vs global scope

### Day 11: Functions - Advanced
- [ ] Can use *args for variable arguments
- [ ] Can use **kwargs for keyword arguments
- [ ] Understand lambda functions
- [ ] Can create basic decorators
- [ ] Understand closures
- [ ] Know when to use each feature

### Day 12: Scope & Recursion
- [ ] Understand LEGB rule
- [ ] Know when to use global/nonlocal
- [ ] Can write recursive functions
- [ ] Understand base case importance
- [ ] Can choose recursion vs iteration
- [ ] Know recursion pitfalls

### Day 13: Error Handling
- [ ] Can write try-except blocks
- [ ] Know common exception types
- [ ] Understand else and finally clauses
- [ ] Can raise exceptions
- [ ] Can create custom exceptions
- [ ] Know best practices
- [ ] Can use with statement

---

## 🎓 Additional Practice Challenges

### Challenge 1: Advanced Calculator
Create a calculator with:
- All basic operations (+, -, *, /, **, //, %)
- Scientific functions (sin, cos, sqrt, log)
- History tracking
- Error handling
- Decorators for logging

### Challenge 2: File Manager
Build a file manager that:
- Lists files in directory
- Creates/deletes files
- Reads/writes file content
- Handles all file errors
- Uses functions for each operation

### Challenge 3: Student Management System
Create a system with:
- Add/remove students
- Record grades
- Calculate averages (use recursion)
- Generate reports
- Full error handling

### Challenge 4: Game Framework
Build a game framework with:
- Menu system (while loops)
- Game loop (for loops)
- Score tracking (functions)
- Save/load (error handling)
- Decorators for game events

### Challenge 5: API Wrapper
Create a simple API wrapper:
- Functions for different endpoints
- Retry decorator for failed requests
- Error handling for network issues
- Response parsing
- Rate limiting

---

## 📊 Week 2 Achievement Summary

**You've learned:**
- ✅ 2 types of loops (for, while)
- ✅ Functions (basic + advanced)
- ✅ 10+ function concepts (*args, **kwargs, decorators, etc.)
- ✅ Scope (LEGB rule)
- ✅ Recursion (base case, recursive case)
- ✅ Error handling (try-except-else-finally)
- ✅ Custom exceptions
- ✅ 7 comprehensive projects

**Lines of code written:** ~1000+  
**Concepts mastered:** 70+  
**Projects completed:** 14 (7 from Week 1 + 7 from Week 2)  

---

## 🎯 Week 3 Preview

Next week you'll learn:
- **Day 15:** List Comprehensions (Advanced)
- **Day 16:** Modules & Packages
- **Day 17:** Object-Oriented Programming - Part 1
- **Day 18:** Object-Oriented Programming - Part 2
- **Day 19:** Working with Libraries
- **Day 20:** Working with JSON & Files
- **Day 21:** Week 3 Review & Contact Management System

---

## 💪 Motivation

> "The only way to learn a new programming language is by writing programs in it." - Dennis Ritchie

You've now completed 2 weeks of intensive Python learning! You've gone from basic variables to building complex, error-handled applications with functions, loops, and proper structure. The fundamentals are solid - now it's time to build on them!

---

## 🎉 Celebration Time!

**Week 2 Milestones:**
- ✅ Mastered loops (for and while)
- ✅ Created reusable functions
- ✅ Used advanced function features
- ✅ Understood variable scope
- ✅ Implemented recursion
- ✅ Handled errors gracefully
- ✅ Built 7 practical projects

**Total Progress:**
- 📅 14 days completed
- 📚 14 comprehensive guides
- 💻 14 practice projects
- 🎯 120+ concepts learned
- 🏆 2000+ lines of code written

---

## 📚 Resources for Review

### Practice More
- **HackerRank**: Python challenges
- **LeetCode**: Algorithm problems
- **Codewars**: Kata exercises
- **Project Euler**: Mathematical problems

### Deepen Understanding
- **Real Python**: Advanced tutorials
- **Python Docs**: Official documentation
- **YouTube**: Corey Schafer's Python series
- **Books**: "Fluent Python" by Luciano Ramalho

### Build Projects
- **GitHub**: Explore Python projects
- **Awesome Python**: Curated list
- **Python Package Index**: Discover libraries

---

## 🔥 Pro Tips Going Forward

1. **Practice Daily** - Even 30 minutes makes a difference
2. **Build Projects** - Apply what you learn immediately
3. **Read Code** - Study well-written Python code
4. **Debug Actively** - Understand errors, don't just fix them
5. **Comment Your Code** - Future you will thank you
6. **Join Communities** - Reddit, Discord, Stack Overflow
7. **Contribute** - Help others learn (best way to solidify knowledge)
8. **Stay Curious** - Explore libraries and frameworks
9. **Refactor Often** - Improve your old code
10. **Have Fun!** - Programming should be enjoyable

---

## 🎊 Congratulations!

You've completed Week 2 of your Python journey! Take a moment to celebrate your progress. You've learned complex concepts like decorators, recursion, and error handling - things that many programmers struggle with. You're building real, practical applications now!

**Next:** Ready for Week 3? We'll dive into Object-Oriented Programming, modules, and working with external libraries!

---

**Keep Coding! You're Doing Amazing! 🐍✨**
