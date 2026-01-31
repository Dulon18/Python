# Day 16: Modules & Packages

## Overview
Today we'll learn how to organize code into modules and packages, use Python's standard library, and install external packages. This is essential for writing maintainable, reusable code!

---

## 1. What are Modules?

A module is a Python file containing functions, classes, and variables that you can import and use in other files.

### Why Use Modules?

✅ **Organization** - Keep code structured  
✅ **Reusability** - Use code in multiple projects  
✅ **Namespace** - Avoid naming conflicts  
✅ **Maintainability** - Easier to update and debug  

### Simple Example

**File: `math_utils.py`**
```python
# This is a module!

def add(a, b):
    """Add two numbers."""
    return a + b

def multiply(a, b):
    """Multiply two numbers."""
    return a * b

PI = 3.14159
```

**File: `main.py`**
```python
# Import and use the module
import math_utils

result1 = math_utils.add(5, 3)
result2 = math_utils.multiply(4, 7)
print(f"PI: {math_utils.PI}")
```

---

## 2. Importing Modules

### Different Import Methods

```python
# Method 1: Import entire module
import math
print(math.sqrt(16))  # 4.0

# Method 2: Import specific items
from math import sqrt, pi
print(sqrt(16))  # 4.0
print(pi)        # 3.14159...

# Method 3: Import with alias
import math as m
print(m.sqrt(16))  # 4.0

# Method 4: Import everything (not recommended)
from math import *
print(sqrt(16))  # 4.0
```

### When to Use Each Method

```python
# Use import module when using many functions
import math
math.sqrt(16)
math.sin(0)
math.cos(0)

# Use from module import when using few specific functions
from math import sqrt
sqrt(16)

# Use alias for long module names
import matplotlib.pyplot as plt
plt.plot([1, 2, 3])

# Avoid import * (pollutes namespace)
# from math import *  # Don't do this!
```

---

## 3. Creating Your Own Modules

### Step 1: Create the Module File

**File: `calculator.py`**
```python
"""
Simple calculator module.

This module provides basic arithmetic operations.
"""

def add(a, b):
    """Add two numbers."""
    return a + b

def subtract(a, b):
    """Subtract b from a."""
    return a - b

def multiply(a, b):
    """Multiply two numbers."""
    return a * b

def divide(a, b):
    """Divide a by b."""
    if b == 0:
        raise ValueError("Cannot divide by zero!")
    return a / b

# Module-level variable
VERSION = "1.0"

# Module-level code (runs when imported)
print(f"Calculator module v{VERSION} loaded")
```

### Step 2: Use the Module

**File: `main.py`**
```python
import calculator

print(calculator.add(10, 5))       # 15
print(calculator.subtract(10, 5))  # 5
print(calculator.VERSION)          # 1.0
```

---

## 4. The `__name__` Variable

### Understanding `__name__`

Every Python file has a special variable `__name__`:
- When run directly: `__name__ == "__main__"`
- When imported: `__name__ == "module_name"`

### Practical Use

**File: `utils.py`**
```python
def helper_function():
    """A helper function."""
    return "Hello from utils"

# This code only runs when file is executed directly
if __name__ == "__main__":
    print("Testing utils module...")
    print(helper_function())
    print("Tests complete!")
```

**Usage:**
```python
# Run directly:
# $ python utils.py
# Output: Testing utils module...
#         Hello from utils
#         Tests complete!

# Import in another file:
import utils
result = utils.helper_function()
# No test output (if __name__ block doesn't run)
```

### Common Pattern

```python
# module.py

def main():
    """Main function."""
    print("Running main function")
    # Your code here

if __name__ == "__main__":
    main()
```

---

## 5. Python Standard Library

Python comes with many built-in modules!

### Essential Standard Modules

#### math - Mathematical Functions
```python
import math

print(math.sqrt(16))      # 4.0
print(math.pi)            # 3.14159...
print(math.ceil(4.3))     # 5
print(math.floor(4.7))    # 4
print(math.factorial(5))  # 120
```

#### random - Random Numbers
```python
import random

print(random.randint(1, 10))        # Random int 1-10
print(random.random())              # Random float 0-1
print(random.choice([1, 2, 3]))     # Random choice
random.shuffle([1, 2, 3, 4, 5])     # Shuffle in place
```

#### datetime - Date and Time
```python
from datetime import datetime, timedelta

now = datetime.now()
print(now)  # 2024-01-31 15:30:45.123456

# Create specific date
birthday = datetime(2000, 5, 15)

# Time arithmetic
tomorrow = now + timedelta(days=1)
next_week = now + timedelta(weeks=1)
```

#### os - Operating System Interface
```python
import os

print(os.getcwd())           # Current directory
print(os.listdir('.'))       # List files
# os.mkdir('new_folder')     # Create directory
# os.remove('file.txt')      # Delete file
print(os.path.exists('file.txt'))  # Check if exists
```

#### sys - System Parameters
```python
import sys

print(sys.version)           # Python version
print(sys.platform)          # Platform (win32, linux, darwin)
# sys.exit()                 # Exit program
print(sys.argv)              # Command line arguments
```

#### json - JSON Encoding/Decoding
```python
import json

# Python to JSON
data = {"name": "Alice", "age": 25}
json_string = json.dumps(data)
print(json_string)  # '{"name": "Alice", "age": 25}'

# JSON to Python
parsed = json.loads(json_string)
print(parsed["name"])  # Alice
```

#### re - Regular Expressions
```python
import re

text = "My email is user@example.com"
pattern = r'\w+@\w+\.\w+'
email = re.search(pattern, text)
print(email.group())  # user@example.com
```

#### collections - Container Datatypes
```python
from collections import Counter, defaultdict

# Counter - count occurrences
words = ["apple", "banana", "apple", "orange", "banana", "apple"]
counts = Counter(words)
print(counts)  # Counter({'apple': 3, 'banana': 2, 'orange': 1})

# defaultdict - dict with default values
dd = defaultdict(int)
dd['count'] += 1  # No KeyError!
```

---

## 6. Packages

A package is a directory containing multiple modules and a special `__init__.py` file.

### Package Structure

```
mypackage/
    __init__.py
    module1.py
    module2.py
    subpackage/
        __init__.py
        module3.py
```

### Creating a Package

**Directory: `mymath/`**

**File: `mymath/__init__.py`**
```python
"""
MyMath package for mathematical operations.
"""

__version__ = "1.0.0"

# Import modules to make them available at package level
from .basic import add, subtract
from .advanced import power, factorial

__all__ = ['add', 'subtract', 'power', 'factorial']
```

**File: `mymath/basic.py`**
```python
"""Basic math operations."""

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b
```

**File: `mymath/advanced.py`**
```python
"""Advanced math operations."""

def power(base, exp):
    return base ** exp

def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n - 1)
```

### Using the Package

```python
# Method 1: Import from package
from mymath import add, power
print(add(5, 3))      # 8
print(power(2, 3))    # 8

# Method 2: Import module from package
from mymath import basic
print(basic.add(5, 3))  # 8

# Method 3: Import entire package
import mymath
print(mymath.add(5, 3))  # 8
```

---

## 7. Installing External Packages with pip

### What is pip?

`pip` is Python's package installer. It downloads packages from PyPI (Python Package Index).

### Basic pip Commands

```bash
# Install a package
pip install requests

# Install specific version
pip install requests==2.28.0

# Install latest version
pip install --upgrade requests

# Uninstall package
pip uninstall requests

# List installed packages
pip list

# Show package info
pip show requests

# Install from requirements.txt
pip install -r requirements.txt

# Create requirements.txt
pip freeze > requirements.txt
```

### Common External Packages

```python
# requests - HTTP library
import requests
response = requests.get('https://api.github.com')
print(response.json())

# pandas - Data analysis
import pandas as pd
df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})

# numpy - Numerical computing
import numpy as np
arr = np.array([1, 2, 3, 4, 5])

# matplotlib - Plotting
import matplotlib.pyplot as plt
plt.plot([1, 2, 3, 4])
plt.show()
```

---

## 8. Module Search Path

Python searches for modules in specific locations.

### Understanding sys.path

```python
import sys

# Show where Python looks for modules
for path in sys.path:
    print(path)

# Add custom path
sys.path.append('/path/to/my/modules')
```

### Module Search Order

1. Current directory
2. PYTHONPATH environment variable
3. Installation-dependent default paths

---

## 9. Best Practices

### 1. Use Meaningful Module Names

```python
# Good
import user_management
import database_utils

# Bad
import um
import db
```

### 2. Organize Related Functions

```python
# Good - grouped by purpose
# file_operations.py
def read_file():
    pass

def write_file():
    pass

# Bad - unrelated functions in same module
```

### 3. Document Your Modules

```python
"""
Module for user authentication.

This module provides functions for:
- Login validation
- Password hashing
- Session management

Example:
    >>> from auth import login
    >>> login('user', 'pass')
"""

def login(username, password):
    """Authenticate user."""
    pass
```

### 4. Use `__all__` to Control Exports

```python
# mymodule.py

def public_function():
    """This will be exported."""
    pass

def _private_function():
    """This is private (by convention)."""
    pass

# Explicitly define what to export
__all__ = ['public_function']
```

### 5. Avoid Circular Imports

```python
# ❌ Bad - circular dependency
# module_a.py
from module_b import func_b

# module_b.py
from module_a import func_a

# ✅ Good - restructure or use local imports
```

---

## 10. Practical Examples

### Example 1: String Utilities Module

**File: `string_utils.py`**
```python
"""String utility functions."""

def reverse(text):
    """Reverse a string."""
    return text[::-1]

def is_palindrome(text):
    """Check if string is palindrome."""
    cleaned = text.replace(" ", "").lower()
    return cleaned == cleaned[::-1]

def count_vowels(text):
    """Count vowels in string."""
    return sum(1 for char in text.lower() if char in 'aeiou')

if __name__ == "__main__":
    # Test functions
    print(reverse("Python"))
    print(is_palindrome("radar"))
    print(count_vowels("hello"))
```

### Example 2: File Operations Module

**File: `file_ops.py`**
```python
"""File operation utilities."""

import os
import json

def read_text_file(filename):
    """Read text file."""
    try:
        with open(filename, 'r') as f:
            return f.read()
    except FileNotFoundError:
        return None

def write_text_file(filename, content):
    """Write to text file."""
    with open(filename, 'w') as f:
        f.write(content)

def read_json(filename):
    """Read JSON file."""
    with open(filename, 'r') as f:
        return json.load(f)

def write_json(filename, data):
    """Write to JSON file."""
    with open(filename, 'w') as f:
        json.dump(data, f, indent=2)
```

### Example 3: Data Validation Module

**File: `validators.py`**
```python
"""Data validation utilities."""

import re

def is_valid_email(email):
    """Validate email format."""
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return re.match(pattern, email) is not None

def is_valid_phone(phone):
    """Validate phone number."""
    pattern = r'^\d{3}-\d{3}-\d{4}$'
    return re.match(pattern, phone) is not None

def is_strong_password(password):
    """Check password strength."""
    if len(password) < 8:
        return False
    has_upper = any(c.isupper() for c in password)
    has_lower = any(c.islower() for c in password)
    has_digit = any(c.isdigit() for c in password)
    return has_upper and has_lower and has_digit
```

---

## Practice Exercises

### Exercise 1: Create a Math Module
Create a module with functions for:
- Square root
- Power
- Absolute value
- Average of list

### Exercise 2: Create a Date Utils Module
Functions for:
- Days between two dates
- Add days to date
- Format date
- Is weekend?

### Exercise 3: Create a String Module
Functions for:
- Capitalize each word
- Remove extra spaces
- Count words
- Extract numbers from text

### Exercise 4: Build a Package
Create a package with:
- basic module (add, subtract, multiply, divide)
- advanced module (power, factorial, gcd)
- constants module (PI, E, GOLDEN_RATIO)

### Exercise 5: Use Standard Library
Write a program using:
- os (list files in directory)
- datetime (calculate age)
- random (generate random password)
- json (save/load data)

---

## Practice Project

**See:** `day16_module_system/` for the complete Module System project.

The project includes:
- Multiple custom modules
- Package structure
- Standard library usage
- Module documentation
- Practical utilities

---

## Quick Reference

### Import Syntax

```python
import module                    # Import module
from module import func         # Import specific function
from module import *            # Import everything (avoid)
import module as alias          # Import with alias
from package import module      # Import from package
```

### Creating Module

```python
# mymodule.py
def function():
    pass

if __name__ == "__main__":
    # Test code
    pass
```

### Creating Package

```
package/
    __init__.py       # Makes it a package
    module1.py
    module2.py
```

### pip Commands

```bash
pip install package        # Install
pip uninstall package     # Uninstall
pip list                  # List installed
pip freeze                # Export requirements
```

---

## Key Takeaways

✅ Modules organize code into reusable files  
✅ Packages organize multiple modules  
✅ Use `import` to access module code  
✅ `__name__ == "__main__"` for test code  
✅ Python Standard Library has many useful modules  
✅ pip installs external packages  
✅ Use `__init__.py` to create packages  
✅ Document modules with docstrings  
✅ Follow naming conventions  
✅ Avoid circular imports  

---

## Common Mistakes to Avoid

❌ **Naming module same as standard library**
```python
# Don't name your file "random.py" or "math.py"
```

❌ **Using `from module import *`**
```python
# Bad - pollutes namespace
from math import *

# Good - explicit imports
from math import sqrt, pi
```

❌ **Forgetting `__init__.py`**
```python
# Package needs __init__.py to be recognized
```

❌ **Circular imports**
```python
# module_a imports module_b
# module_b imports module_a
# Causes import errors!
```

---

## Next Steps

Tomorrow (Day 17), we'll dive into **Object-Oriented Programming - Part 1** - learn classes, objects, and encapsulation!

---

## Resources

- [Python Modules Documentation](https://docs.python.org/3/tutorial/modules.html)
- [Python Package Index (PyPI)](https://pypi.org/)
- [pip Documentation](https://pip.pypa.io/)

---

**Organize Your Code! **
