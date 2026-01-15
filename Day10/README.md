# Day 10: Functions - Basics

## Overview
Today we'll learn about functions - reusable blocks of code that make your programs more organized, maintainable, and efficient. Functions are one of the most important concepts in programming!

---

## 1. What are Functions?

### Why Use Functions?

**Without functions (repetitive code):**
```python
# Calculate area of rectangle 1
length1 = 10
width1 = 5
area1 = length1 * width1
print(f"Area 1: {area1}")

# Calculate area of rectangle 2
length2 = 8
width2 = 6
area2 = length2 * width2
print(f"Area 2: {area2}")

# Calculate area of rectangle 3
length3 = 12
width3 = 4
area3 = length3 * width3
print(f"Area 3: {area3}")
```

**With functions (clean and reusable):**
```python
def calculate_area(length, width):
    area = length * width
    return area

# Use the function
area1 = calculate_area(10, 5)
area2 = calculate_area(8, 6)
area3 = calculate_area(12, 4)

print(f"Area 1: {area1}")
print(f"Area 2: {area2}")
print(f"Area 3: {area3}")
```

### Benefits of Functions:
✅ **Reusability** - Write once, use many times  
✅ **Organization** - Break complex problems into smaller parts  
✅ **Maintainability** - Fix bugs in one place  
✅ **Readability** - Code is easier to understand  
✅ **Testing** - Test individual functions  

---

## 2. Defining Functions

### Basic Syntax

```python
def function_name():
    # code to execute
    pass
```

### Simple Function

```python
# Define function
def greet():
    print("Hello, World!")

# Call function
greet()  # Output: Hello, World!
```

### Function Naming Rules

✅ Use lowercase with underscores: `calculate_total`  
✅ Start with letter or underscore: `_helper`, `get_data`  
✅ Be descriptive: `calculate_average` not `calc_avg`  
❌ Avoid: numbers at start (`2calculate`), spaces, special characters  

```python
# Good names
def calculate_total():
    pass

def get_user_input():
    pass

def is_valid():
    pass

# Bad names
def calc():  # Too short, unclear
    pass

def function1():  # Not descriptive
    pass

def CALCULATE():  # Should be lowercase
    pass
```

---

## 3. Function Parameters

Parameters allow you to pass data into functions.

### Single Parameter

```python
def greet(name):
    print(f"Hello, {name}!")

greet("Alice")  # Output: Hello, Alice!
greet("Bob")    # Output: Hello, Bob!
```

### Multiple Parameters

```python
def calculate_rectangle_area(length, width):
    area = length * width
    print(f"Area: {area}")

calculate_rectangle_area(10, 5)   # Area: 50
calculate_rectangle_area(8, 6)    # Area: 48
```

### Parameters vs Arguments

- **Parameters:** Variables in function definition
- **Arguments:** Actual values passed when calling

```python
def add(a, b):      # a and b are parameters
    return a + b

result = add(5, 3)  # 5 and 3 are arguments
```

---

## 4. Return Statement

Functions can return values to the caller.

### Basic Return

```python
def add(a, b):
    return a + b

result = add(5, 3)
print(result)  # 8
```

### Without Return

```python
def greet(name):
    print(f"Hello, {name}")
    # No return statement - returns None

result = greet("Alice")  # Prints: Hello, Alice
print(result)            # None
```

### Multiple Return Statements

```python
def absolute_value(number):
    if number >= 0:
        return number
    else:
        return -number

print(absolute_value(5))   # 5
print(absolute_value(-5))  # 5
```

### Returning Multiple Values

```python
def get_min_max(numbers):
    return min(numbers), max(numbers)

minimum, maximum = get_min_max([1, 2, 3, 4, 5])
print(f"Min: {minimum}, Max: {maximum}")  # Min: 1, Max: 5
```

### Early Return

```python
def divide(a, b):
    if b == 0:
        return "Cannot divide by zero"
    return a / b

print(divide(10, 2))  # 5.0
print(divide(10, 0))  # Cannot divide by zero
```

---

## 5. Default Parameters

Parameters can have default values.

### Basic Default Parameters

```python
def greet(name, greeting="Hello"):
    print(f"{greeting}, {name}!")

greet("Alice")              # Hello, Alice!
greet("Bob", "Hi")          # Hi, Bob!
greet("Charlie", "Hey")     # Hey, Charlie!
```

### Multiple Default Parameters

```python
def make_profile(name, age=18, city="Unknown"):
    print(f"Name: {name}")
    print(f"Age: {age}")
    print(f"City: {city}")

make_profile("Alice")                    # Uses both defaults
make_profile("Bob", 25)                  # Uses city default
make_profile("Charlie", 30, "New York")  # No defaults used
```

### Important Rule

Default parameters must come after non-default parameters.

```python
# ✅ Correct
def func(a, b, c=10, d=20):
    pass

# ❌ Wrong - SyntaxError
def func(a, b=10, c, d=20):
    pass
```

---

## 6. Keyword Arguments

Call functions using parameter names.

### Positional vs Keyword Arguments

```python
def describe_pet(animal, name, age):
    print(f"{name} is a {age}-year-old {animal}")

# Positional arguments
describe_pet("dog", "Buddy", 3)

# Keyword arguments
describe_pet(name="Buddy", animal="dog", age=3)

# Mixed (positional first, then keyword)
describe_pet("dog", age=3, name="Buddy")
```

### Benefits of Keyword Arguments

✅ More readable  
✅ Order doesn't matter  
✅ Clear what each argument represents  

```python
# Without keyword arguments
send_email("user@email.com", "Subject", "Body", True, False)

# With keyword arguments (much clearer!)
send_email(
    to="user@email.com",
    subject="Subject",
    body="Body",
    urgent=True,
    send_copy=False
)
```

---

## 7. Docstrings

Document your functions using docstrings.

### Basic Docstring

```python
def calculate_area(length, width):
    """Calculate the area of a rectangle."""
    return length * width
```

### Detailed Docstring

```python
def calculate_circle_area(radius):
    """
    Calculate the area of a circle.
    
    Parameters:
        radius (float): The radius of the circle
    
    Returns:
        float: The area of the circle
    
    Example:
        >>> calculate_circle_area(5)
        78.53981633974483
    """
    import math
    return math.pi * radius ** 2
```

### Accessing Docstrings

```python
def greet(name):
    """Greet a person by name."""
    print(f"Hello, {name}!")

print(greet.__doc__)  # Greet a person by name.
help(greet)           # Shows full documentation
```

---

## 8. Scope

Variables have different scopes (where they can be accessed).

### Local Scope

```python
def my_function():
    x = 10  # Local variable
    print(x)

my_function()  # 10
# print(x)     # Error! x doesn't exist outside function
```

### Global Scope

```python
x = 10  # Global variable

def my_function():
    print(x)  # Can access global variable

my_function()  # 10
print(x)       # 10
```

### Local vs Global

```python
x = 10  # Global

def my_function():
    x = 5  # Local (different from global x)
    print(f"Inside function: {x}")

my_function()        # Inside function: 5
print(f"Outside: {x}")  # Outside: 10
```

### Modifying Global Variables

```python
count = 0

def increment():
    global count  # Declare we're using global count
    count += 1

increment()
print(count)  # 1

increment()
print(count)  # 2
```

**Note:** Using `global` is generally discouraged. Better to return values.

---

## 9. Practical Examples

### Example 1: Temperature Converter

```python
def celsius_to_fahrenheit(celsius):
    """Convert Celsius to Fahrenheit."""
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

def fahrenheit_to_celsius(fahrenheit):
    """Convert Fahrenheit to Celsius."""
    celsius = (fahrenheit - 32) * 5/9
    return celsius

# Usage
temp_c = 25
temp_f = celsius_to_fahrenheit(temp_c)
print(f"{temp_c}°C = {temp_f}°F")

temp_f = 77
temp_c = fahrenheit_to_celsius(temp_f)
print(f"{temp_f}°F = {temp_c}°C")
```

### Example 2: Grade Calculator

```python
def calculate_grade(score):
    """
    Convert numerical score to letter grade.
    
    Parameters:
        score (int): Score from 0-100
    
    Returns:
        str: Letter grade (A, B, C, D, F)
    """
    if score >= 90:
        return 'A'
    elif score >= 80:
        return 'B'
    elif score >= 70:
        return 'C'
    elif score >= 60:
        return 'D'
    else:
        return 'F'

# Usage
print(calculate_grade(95))  # A
print(calculate_grade(75))  # C
print(calculate_grade(55))  # F
```

### Example 3: Is Prime Number

```python
def is_prime(number):
    """
    Check if a number is prime.
    
    Parameters:
        number (int): Number to check
    
    Returns:
        bool: True if prime, False otherwise
    """
    if number < 2:
        return False
    
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    
    return True

# Usage
print(is_prime(7))   # True
print(is_prime(10))  # False
print(is_prime(13))  # True
```

### Example 4: List Statistics

```python
def calculate_statistics(numbers):
    """
    Calculate statistics for a list of numbers.
    
    Returns:
        tuple: (sum, average, min, max)
    """
    total = sum(numbers)
    average = total / len(numbers)
    minimum = min(numbers)
    maximum = max(numbers)
    
    return total, average, minimum, maximum

# Usage
data = [10, 20, 30, 40, 50]
total, avg, min_val, max_val = calculate_statistics(data)

print(f"Total: {total}")
print(f"Average: {avg}")
print(f"Min: {min_val}")
print(f"Max: {max_val}")
```

### Example 5: Password Validator

```python
def is_valid_password(password):
    """
    Check if password meets requirements.
    
    Requirements:
        - At least 8 characters
        - Contains uppercase and lowercase
        - Contains a digit
    
    Returns:
        bool: True if valid, False otherwise
    """
    if len(password) < 8:
        return False
    
    has_upper = False
    has_lower = False
    has_digit = False
    
    for char in password:
        if char.isupper():
            has_upper = True
        elif char.islower():
            has_lower = True
        elif char.isdigit():
            has_digit = True
    
    return has_upper and has_lower and has_digit

# Usage
print(is_valid_password("Pass123"))     # True
print(is_valid_password("password"))    # False (no upper, no digit)
print(is_valid_password("PASSWORD123")) # False (no lower)
```

---

## 10. Function Best Practices

### 1. Single Responsibility

Each function should do ONE thing well.

```python
# ✅ Good - Each function has one job
def calculate_total(items):
    return sum(items)

def calculate_average(items):
    return sum(items) / len(items)

# ❌ Bad - Function does too much
def process_numbers(items):
    total = sum(items)
    average = total / len(items)
    maximum = max(items)
    # Too many responsibilities!
    return total, average, maximum
```

### 2. Descriptive Names

```python
# ✅ Good
def calculate_monthly_payment(principal, rate, years):
    pass

# ❌ Bad
def calc(p, r, y):
    pass
```

### 3. Keep Functions Short

Aim for functions that fit on one screen (roughly 20-30 lines).

### 4. Use Type Hints (Optional but Recommended)

```python
def add(a: int, b: int) -> int:
    """Add two integers."""
    return a + b

def greet(name: str) -> None:
    """Print greeting."""
    print(f"Hello, {name}!")
```

### 5. Handle Edge Cases

```python
def divide(a, b):
    """Divide a by b with error handling."""
    if b == 0:
        return "Error: Division by zero"
    return a / b

def get_first_item(items):
    """Get first item from list."""
    if not items:
        return None
    return items[0]
```

---

## Practice Exercises

### Exercise 1: Area Calculator
Create functions to calculate area of:
- Circle (πr²)
- Rectangle (length × width)
- Triangle (½ × base × height)

### Exercise 2: String Utilities
Create functions that:
- Count vowels in a string
- Reverse a string
- Check if string is palindrome
- Count words in a string

### Exercise 3: Number Utilities
Create functions that:
- Check if number is even/odd
- Find factorial
- Find GCD of two numbers
- Generate Fibonacci sequence up to n

### Exercise 4: List Operations
Create functions that:
- Find second largest number
- Remove duplicates
- Merge two sorted lists
- Rotate list by n positions

### Exercise 5: Validator Functions
Create functions that validate:
- Email address format
- Phone number format
- Credit card number (Luhn algorithm)
- Date format (DD/MM/YYYY)

---

## Practice Project

**See:** `day10_utility_functions.py` for the complete Utility Functions Library project.

The project includes:
- 20+ utility functions organized by category
- String utilities
- Number utilities
- List utilities
- Validation utilities
- Interactive menu to test all functions

---

## Quick Reference

### Function Syntax

```python
# Basic function
def function_name():
    # code
    pass

# With parameters
def function_name(param1, param2):
    # code
    pass

# With return
def function_name(param):
    return value

# With default parameters
def function_name(param1, param2=default):
    # code
    pass

# With docstring
def function_name(param):
    """Documentation here."""
    return value
```

### Calling Functions

```python
# No arguments
function_name()

# Positional arguments
function_name(arg1, arg2)

# Keyword arguments
function_name(param1=value1, param2=value2)

# Mixed
function_name(arg1, param2=value2)
```

---

## Key Takeaways

✅ Functions make code reusable and organized  
✅ Use `def` to define functions  
✅ Parameters pass data into functions  
✅ `return` sends data back from functions  
✅ Default parameters provide fallback values  
✅ Keyword arguments improve readability  
✅ Docstrings document function behavior  
✅ Variables have local or global scope  
✅ Functions should do one thing well  
✅ Use descriptive function names  

---

## Common Mistakes to Avoid

 **Forgetting to call function**
```python
def greet():
    print("Hello")

greet  # Wrong - doesn't call function
greet()  # Correct
```

 **Forgetting return statement**
```python
def add(a, b):
    result = a + b
    # Forgot to return!

x = add(5, 3)
print(x)  # None
```

 **Modifying global variables**
```python
# Bad practice
count = 0
def increment():
    global count
    count += 1

# Better
def increment(count):
    return count + 1

count = increment(count)
```

**Too many parameters**
```python
# Hard to use
def create_user(name, age, email, phone, address, city, zip):
    pass

# Better - use dictionary
def create_user(user_data):
    pass
```

---

## Next Steps

Tomorrow (Day 11), we'll dive into **Functions - Advanced** including *args, **kwargs, lambda functions, and decorators!

---

## Resources

- [Python Functions Documentation](https://docs.python.org/3/tutorial/controlflow.html#defining-functions)
- [PEP 8 Function Guidelines](https://peps.python.org/pep-0008/#function-and-variable-names)

---

**Function It Up! 🐍**
