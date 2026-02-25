# Day 27: Virtual Environments & Best Practices

> **Week 4 — Advanced Topics** | 30-Day Python Learning Plan

Today we cover how to **structure professional Python projects** — virtual environments, dependency management, PEP 8 style guide, documentation, and project organization. These habits separate beginner code from production-ready code.

---

## 📌 Part A — Virtual Environments

### Why Virtual Environments?

Without virtual environments, all Python packages install **globally** — different projects can conflict with each other.

```
❌ Without venv:
Project A needs requests==2.28
Project B needs requests==2.31
→ One will break!

✅ With venv:
Project A has its own requests==2.28
Project B has its own requests==2.31
→ Both work perfectly!
```

---

### Creating & Using a Virtual Environment

```bash
# Step 1: Create virtual environment
python -m venv myenv

# Step 2: Activate it
# Windows:
myenv\Scripts\activate

# Mac/Linux:
source myenv/bin/activate

# Your terminal now shows: (myenv) $

# Step 3: Install packages INSIDE the venv
pip install requests pandas

# Step 4: Check installed packages
pip list

# Step 5: Deactivate when done
deactivate
```

---

### Virtual Environment — What's Inside

```
myenv/
├── Scripts/          (Windows) or bin/ (Mac/Linux)
│   ├── activate      ← activation script
│   ├── python.exe    ← isolated Python
│   └── pip.exe       ← isolated pip
├── Lib/
│   └── site-packages/  ← all packages installed here
└── pyvenv.cfg
```

> ⚠️ **Never commit your `venv/` folder to Git** — add it to `.gitignore`

---

### Multiple Environments for Different Projects

```bash
# Project 1
cd project1/
python -m venv venv
venv\Scripts\activate
pip install flask==2.3.0

# Project 2 (different versions)
cd project2/
python -m venv venv
venv\Scripts\activate
pip install flask==3.0.0

# Each project is completely isolated
```

---

## 📌 Part B — requirements.txt

`requirements.txt` lists all your project's dependencies so anyone can recreate your environment exactly.

### Generating requirements.txt

```bash
# Activate your venv first, then:
pip freeze > requirements.txt
```

**Example `requirements.txt`:**
```
certifi==2024.2.2
charset-normalizer==3.3.2
idna==3.6
pandas==2.2.0
requests==2.31.0
urllib3==2.2.0
```

---

### Installing from requirements.txt

```bash
# Someone else clones your project:
git clone https://github.com/you/project.git
cd project

# They create their own venv
python -m venv venv
venv\Scripts\activate

# Install all dependencies at once
pip install -r requirements.txt
```

---

### Pinned vs Unpinned Versions

```
# Pinned — exact version (recommended for production)
requests==2.31.0
pandas==2.2.0

# Unpinned — latest version (flexible but risky)
requests
pandas

# Minimum version
requests>=2.28.0

# Range
requests>=2.28.0,<3.0.0
```

---

### Separating Dev and Production Dependencies

```bash
# requirements.txt — production only
requests==2.31.0
pandas==2.2.0

# requirements-dev.txt — development tools
-r requirements.txt     # include production deps
pytest==8.0.0
black==24.1.1
pylint==3.0.3
```

```bash
# Install production only
pip install -r requirements.txt

# Install everything including dev tools
pip install -r requirements-dev.txt
```

---

## 📌 Part C — PEP 8 Style Guide

PEP 8 is Python's official style guide. Following it makes your code readable by any Python developer.

---

### 1. Naming Conventions

```python
# Variables and functions — snake_case
user_name = "Ali"
total_price = 99.99

def calculate_bmi(weight, height):
    pass

# Constants — UPPER_SNAKE_CASE
MAX_RETRIES = 3
PI = 3.14159
DATABASE_URL = "sqlite:///mydb.db"

# Classes — PascalCase
class StudentManager:
    pass

class BankAccount:
    pass

# Private attributes — single underscore prefix
class MyClass:
    def __init__(self):
        self._internal = "private by convention"
        self.__very_private = "name mangled"

# Modules/files — short, lowercase, underscores ok
# contact_manager.py ✅
# ContactManager.py  ❌
# contactmanager.py  ✅ (but underscores preferred)
```

---

### 2. Indentation & Spacing

```python
# ❌ BAD — wrong spacing
def myFunction(a,b,c):
    x=a+b
    if x>10:
        return x
    return c

# ✅ GOOD — proper spacing
def my_function(a, b, c):
    x = a + b
    if x > 10:
        return x
    return c


# Spaces around operators
x = 5            # ✅
x=5              # ❌

result = x + y   # ✅
result = x+y     # ❌

# No space before colon/comma
my_list = [1, 2, 3]         # ✅
my_list = [1 , 2 , 3]       # ❌

my_dict = {"key": "value"}  # ✅
my_dict = {"key" : "value"} # ❌

# Two blank lines between top-level definitions
def function_one():
    pass


def function_two():
    pass


class MyClass:
    pass


# One blank line between methods inside a class
class MyClass:
    def method_one(self):
        pass

    def method_two(self):
        pass
```

---

### 3. Line Length

```python
# Max 79 characters per line

# ❌ BAD — too long
result = some_function(very_long_argument_one, very_long_argument_two, very_long_argument_three)

# ✅ GOOD — break with backslash or parentheses
result = some_function(
    very_long_argument_one,
    very_long_argument_two,
    very_long_argument_three
)

# Long strings
message = (
    "This is a very long message that "
    "spans multiple lines using "
    "implicit string concatenation."
)

# Long conditions
if (first_condition
        and second_condition
        and third_condition):
    do_something()
```

---

### 4. Imports

```python
# ✅ GOOD — one import per line
import os
import sys
import json

# ❌ BAD — multiple on one line
import os, sys, json

# Order: standard library → third party → local
import os                    # 1. standard library
import json
import sys

import requests              # 2. third party
import pandas as pd

from mymodule import helper  # 3. local modules

# Avoid wildcard imports
from math import *    # ❌ pollutes namespace
from math import pi, sqrt  # ✅ explicit is better
```

---

### 5. Strings

```python
# Use f-strings (Python 3.6+) — most readable
name = "Ali"
age = 25
print(f"My name is {name} and I am {age} years old.")  # ✅

# Older ways (still valid but less clean)
print("My name is {} and I am {} years old.".format(name, age))
print("My name is %s and I am %d years old." % (name, age))

# Consistent quote style — pick one and stick to it
greeting = "Hello"   # ✅
greeting = 'Hello'   # ✅ (both fine, just be consistent)
```

---

### 6. Comments

```python
# ✅ GOOD — explains WHY not WHAT
# Retry 3 times to handle temporary network failures
for attempt in range(3):
    try:
        connect()
        break
    except ConnectionError:
        time.sleep(1)

# ❌ BAD — states the obvious
# Loop 3 times
for attempt in range(3):
    connect()

# Inline comments — use sparingly
x = x + 1  # compensate for off-by-one error  ✅
x = x + 1  # increment x  ❌ (obvious)
```

---

## 📌 Part D — Code Documentation

Good documentation makes your code usable by others (and your future self).

### Docstrings — Document every function and class

```python
def calculate_bmi(weight_kg: float, height_m: float) -> float:
    """
    Calculate Body Mass Index (BMI).

    Args:
        weight_kg (float): Weight in kilograms. Must be positive.
        height_m (float): Height in meters. Must be positive.

    Returns:
        float: The BMI value rounded to 2 decimal places.

    Raises:
        ValueError: If weight or height is zero or negative.

    Example:
        >>> calculate_bmi(70, 1.75)
        22.86
        >>> calculate_bmi(90, 1.80)
        27.78
    """
    if weight_kg <= 0:
        raise ValueError(f"Weight must be positive, got {weight_kg}")
    if height_m <= 0:
        raise ValueError(f"Height must be positive, got {height_m}")
    return round(weight_kg / (height_m ** 2), 2)


class BankAccount:
    """
    A simple bank account with deposit and withdrawal functionality.

    Attributes:
        owner (str): The name of the account holder.
        balance (float): Current account balance.

    Example:
        >>> account = BankAccount("Ali", 1000)
        >>> account.deposit(500)
        >>> account.balance
        1500
    """

    def __init__(self, owner: str, initial_balance: float = 0):
        """
        Initialize BankAccount.

        Args:
            owner (str): Account holder's name.
            initial_balance (float): Starting balance. Defaults to 0.
        """
        self.owner = owner
        self.balance = initial_balance
        self._history = []

    def deposit(self, amount: float) -> None:
        """
        Deposit money into the account.

        Args:
            amount (float): Amount to deposit. Must be positive.

        Raises:
            ValueError: If amount is not positive.
        """
        if amount <= 0:
            raise ValueError("Deposit amount must be positive!")
        self.balance += amount
        self._history.append(f"+{amount}")
```

---

### Type Hints — Make code self-documenting

```python
# Without type hints — unclear what types are expected
def process(data, limit, flag):
    pass

# With type hints — immediately clear
from typing import List, Dict, Optional, Tuple

def process(data: List[str], limit: int, flag: bool) -> Dict[str, int]:
    pass

def find_user(user_id: int) -> Optional[str]:
    """Returns username or None if not found"""
    pass

def get_coordinates() -> Tuple[float, float]:
    """Returns (latitude, longitude)"""
    pass

# Python 3.10+ simplified syntax
def greet(name: str, times: int = 1) -> str:
    return f"Hello {name}! " * times

# Use | for union types (Python 3.10+)
def process_id(user_id: int | str) -> str:
    return str(user_id)
```

---

## 📌 Part E — Proper Project Structure

```
my_project/
│
├── venv/                    # virtual environment (in .gitignore)
│
├── src/                     # source code
│   ├── __init__.py
│   ├── main.py              # entry point
│   ├── models/
│   │   ├── __init__.py
│   │   ├── user.py
│   │   └── product.py
│   ├── services/
│   │   ├── __init__.py
│   │   ├── auth.py
│   │   └── payment.py
│   └── utils/
│       ├── __init__.py
│       ├── helpers.py
│       └── validators.py
│
├── tests/                   # all tests here
│   ├── __init__.py
│   ├── test_models.py
│   ├── test_services.py
│   └── test_utils.py
│
├── data/                    # data files
│   ├── sample.csv
│   └── config.json
│
├── docs/                    # documentation
│   └── README.md
│
├── .gitignore               # files to exclude from git
├── requirements.txt         # production dependencies
├── requirements-dev.txt     # development dependencies
└── README.md                # project documentation
```

---

### .gitignore for Python Projects

```gitignore
# Virtual environment
venv/
env/
.venv/

# Python cache
__pycache__/
*.pyc
*.pyo
*.pyd

# Distribution / packaging
dist/
build/
*.egg-info/

# Testing
.pytest_cache/
.coverage
htmlcov/

# Environment variables
.env
.env.local

# IDE files
.vscode/
.idea/
*.swp

# OS files
.DS_Store
Thumbs.db

# Log files
*.log
logs/

# Data files you don't want to share
data/private/
```

---

### README.md Template for Your Projects

````markdown
# Project Name

Brief description of what this project does.

## Features
- Feature 1
- Feature 2
- Feature 3

## Installation

```bash
git clone https://github.com/username/project.git
cd project
python -m venv venv
venv\Scripts\activate        # Windows
source venv/bin/activate     # Mac/Linux
pip install -r requirements.txt
```

## Usage

```python
python src/main.py
```

## Project Structure

```
project/
├── src/
├── tests/
├── requirements.txt
└── README.md
```

## Running Tests

```bash
python -m unittest discover tests -v
```

## License
MIT
````

---

## 📌 Part F — Code Quality Tools

```bash
# Install tools
pip install black pylint isort

# black — auto-formats your code to PEP 8
black myfile.py           # format single file
black src/                # format entire directory

# pylint — checks for errors and style issues
pylint myfile.py
pylint src/

# isort — automatically sorts your imports
isort myfile.py
isort src/
```

**Example — Before and after `black`:**

```python
# BEFORE
def my_function(a,b,c,d):
    x=a+b
    if x>10:
        return {'result':x,'input':[a,b,c,d]}
    return None

# AFTER black
def my_function(a, b, c, d):
    x = a + b
    if x > 10:
        return {"result": x, "input": [a, b, c, d]}
    return None
```

---

## 🛠️ Full Professional Project Setup — Step by Step

```bash
# 1. Create project folder
mkdir my_python_project
cd my_python_project

# 2. Initialize git
git init

# 3. Create virtual environment
python -m venv venv
venv\Scripts\activate        # Windows
source venv/bin/activate     # Mac/Linux

# 4. Install dependencies
pip install requests pandas

# 5. Save dependencies
pip freeze > requirements.txt

# 6. Create project structure
mkdir src tests data docs
touch src/__init__.py
touch src/main.py
touch tests/__init__.py
touch .gitignore
touch README.md

# 7. Install dev tools
pip install black pylint pytest
pip freeze > requirements-dev.txt

# 8. Format code before committing
black src/

# 9. Check code quality
pylint src/

# 10. Run tests
python -m unittest discover tests -v

# 11. Commit to git
git add .
git commit -m "Initial project setup"
```

---

## 📝 Quick Summary

| Topic | Key Point |
|---|---|
| Virtual Environment | Isolated Python environment per project |
| `python -m venv venv` | Creates a virtual environment |
| `activate` | Activates the environment |
| `pip freeze > requirements.txt` | Saves all dependencies |
| `pip install -r requirements.txt` | Installs all dependencies |
| PEP 8 | Official Python style guide |
| snake_case | Variables, functions, modules |
| PascalCase | Classes |
| UPPER_CASE | Constants |
| Docstrings | Document functions and classes with `"""` |
| Type hints | `def func(x: int) -> str:` |
| `.gitignore` | Exclude `venv/`, `__pycache__/`, `.env` |
| `black` | Auto-formatter for PEP 8 compliance |
| `pylint` | Linter to catch errors and style issues |

---

## 🔗 Resources

- [PEP 8 Official Guide](https://peps.python.org/pep-0008/)
- [Python Type Hints Docs](https://docs.python.org/3/library/typing.html)
- [black formatter](https://black.readthedocs.io)
- [Real Python — Virtual Environments](https://realpython.com/python-virtual-environments-a-primer/)

---

> 📅 Part of the **30-Day Python Learning Plan**
> Previous: [Day 26 - Testing & Debugging](#) | Next: [Days 28-30 - Final Project](#)
