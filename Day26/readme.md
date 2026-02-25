# Day 26: Testing & Debugging in Python

> **Week 4 — Advanced Topics** | 30-Day Python Learning Plan

Testing ensures your code works correctly and catches bugs **before** they reach users. Debugging helps you find and fix those bugs efficiently.

---

## 📌 Part A — Why Testing?

Without tests:
- You break one thing while fixing another
- You don't know if old code still works after changes
- Bugs reach production and affect real users

With tests:
- You catch bugs early and automatically
- You can refactor confidently
- Your code becomes self-documenting

---

## 📌 Part B — Python's `unittest` Module

Python's built-in `unittest` module lets you write automated tests.

### Basic Structure

```python
import unittest

class TestMyCode(unittest.TestCase):

    def test_something(self):
        self.assertEqual(2 + 2, 4)

if __name__ == "__main__":
    unittest.main()
```

> Every test method **must start with `test_`** — otherwise unittest won't run it.

---

### The Code We'll Test

```python
# calculator.py

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero!")
    return a / b

def power(base, exp):
    return base ** exp

def is_even(n):
    return n % 2 == 0

def get_grade(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"
```

---

### Writing Tests

```python
# test_calculator.py
import unittest
from calculator import add, subtract, multiply, divide, power, is_even, get_grade

class TestCalculator(unittest.TestCase):

    # --- Basic arithmetic ---
    def test_add(self):
        self.assertEqual(add(3, 5), 8)
        self.assertEqual(add(-1, 1), 0)
        self.assertEqual(add(0, 0), 0)
        self.assertEqual(add(1.5, 2.5), 4.0)

    def test_subtract(self):
        self.assertEqual(subtract(10, 3), 7)
        self.assertEqual(subtract(0, 5), -5)
        self.assertEqual(subtract(-3, -3), 0)

    def test_multiply(self):
        self.assertEqual(multiply(4, 3), 12)
        self.assertEqual(multiply(0, 100), 0)
        self.assertEqual(multiply(-2, 5), -10)

    def test_divide(self):
        self.assertEqual(divide(10, 2), 5)
        self.assertEqual(divide(9, 3), 3)
        self.assertAlmostEqual(divide(1, 3), 0.333, places=3)

    def test_divide_by_zero(self):
        with self.assertRaises(ValueError):
            divide(10, 0)

    def test_power(self):
        self.assertEqual(power(2, 10), 1024)
        self.assertEqual(power(5, 0), 1)
        self.assertEqual(power(3, 3), 27)

    # --- Boolean tests ---
    def test_is_even(self):
        self.assertTrue(is_even(4))
        self.assertTrue(is_even(0))
        self.assertFalse(is_even(7))
        self.assertFalse(is_even(-3))

    # --- Grade tests ---
    def test_get_grade(self):
        self.assertEqual(get_grade(95), "A")
        self.assertEqual(get_grade(85), "B")
        self.assertEqual(get_grade(75), "C")
        self.assertEqual(get_grade(65), "D")
        self.assertEqual(get_grade(50), "F")
        self.assertEqual(get_grade(90), "A")  # boundary test
        self.assertEqual(get_grade(80), "B")  # boundary test


if __name__ == "__main__":
    unittest.main(verbosity=2)
```

---

### Running Tests

```bash
# Basic run
python test_calculator.py

# Verbose output (shows each test name)
python test_calculator.py -v

# Or use unittest directly
python -m unittest test_calculator -v
```

**Output:**
```
test_add ... ok
test_divide ... ok
test_divide_by_zero ... ok
test_get_grade ... ok
test_is_even ... ok
test_multiply ... ok
test_power ... ok
test_subtract ... ok

----------------------------------------------------------------------
Ran 8 tests in 0.002s

OK
```

---

## 📌 Part C — All Common Assertions

```python
import unittest

class TestAssertions(unittest.TestCase):

    def test_equality(self):
        self.assertEqual(2 + 2, 4)          # a == b
        self.assertNotEqual(2 + 2, 5)       # a != b

    def test_boolean(self):
        self.assertTrue(5 > 3)              # x is True
        self.assertFalse(5 < 3)             # x is False

    def test_none(self):
        self.assertIsNone(None)             # x is None
        self.assertIsNotNone(42)            # x is not None

    def test_membership(self):
        self.assertIn("a", ["a", "b", "c"])       # a in b
        self.assertNotIn("z", ["a", "b", "c"])    # a not in b

    def test_type(self):
        self.assertIsInstance("hello", str)        # isinstance(a, b)
        self.assertIsInstance(42, int)

    def test_comparison(self):
        self.assertGreater(10, 5)           # a > b
        self.assertLess(3, 7)              # a < b
        self.assertGreaterEqual(5, 5)      # a >= b
        self.assertLessEqual(4, 5)         # a <= b

    def test_float(self):
        # Never use assertEqual for floats!
        self.assertAlmostEqual(0.1 + 0.2, 0.3, places=5)

    def test_exceptions(self):
        with self.assertRaises(ValueError):
            int("not a number")
        with self.assertRaises(ZeroDivisionError):
            result = 1 / 0
        with self.assertRaises(KeyError):
            d = {}
            _ = d["missing"]
```

---

## 📌 Part D — setUp and tearDown

Use these to **prepare** and **clean up** before/after each test.

```python
import unittest
import os
import json

class TestFileOperations(unittest.TestCase):

    def setUp(self):
        """Runs BEFORE each test — set up test data"""
        self.test_file = "test_data.json"
        self.sample_data = {"name": "Ali", "age": 25}

        with open(self.test_file, "w") as f:
            json.dump(self.sample_data, f)

    def tearDown(self):
        """Runs AFTER each test — clean up"""
        if os.path.exists(self.test_file):
            os.remove(self.test_file)

    def test_file_exists(self):
        self.assertTrue(os.path.exists(self.test_file))

    def test_read_file(self):
        with open(self.test_file, "r") as f:
            data = json.load(f)
        self.assertEqual(data["name"], "Ali")
        self.assertEqual(data["age"], 25)

    def test_modify_file(self):
        with open(self.test_file, "r") as f:
            data = json.load(f)
        data["age"] = 30
        with open(self.test_file, "w") as f:
            json.dump(data, f)

        with open(self.test_file, "r") as f:
            updated = json.load(f)
        self.assertEqual(updated["age"], 30)
```

---

## 📌 Part E — Test-Driven Development (TDD)

TDD means you **write the test first**, then write the code to make it pass.

### The TDD Cycle: Red → Green → Refactor

```
1. RED    — Write a test that FAILS (feature doesn't exist yet)
2. GREEN  — Write just enough code to make the test PASS
3. REFACTOR — Clean up the code while keeping tests passing
```

### TDD Example — Building a `BankAccount` class

**Step 1: Write tests FIRST (they will fail)**

```python
# test_bank.py
import unittest
from bank import BankAccount

class TestBankAccount(unittest.TestCase):

    def setUp(self):
        self.account = BankAccount("Ali", 1000)

    def test_initial_balance(self):
        self.assertEqual(self.account.balance, 1000)

    def test_deposit(self):
        self.account.deposit(500)
        self.assertEqual(self.account.balance, 1500)

    def test_withdraw(self):
        self.account.withdraw(200)
        self.assertEqual(self.account.balance, 800)

    def test_overdraft(self):
        with self.assertRaises(ValueError):
            self.account.withdraw(9999)

    def test_negative_deposit(self):
        with self.assertRaises(ValueError):
            self.account.deposit(-100)

    def test_transaction_history(self):
        self.account.deposit(500)
        self.account.withdraw(200)
        self.assertEqual(len(self.account.history), 2)
```

**Step 2: Write the code to make tests pass**

```python
# bank.py
class BankAccount:
    def __init__(self, owner, initial_balance=0):
        self.owner = owner
        self.balance = initial_balance
        self.history = []

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit amount must be positive!")
        self.balance += amount
        self.history.append(f"Deposited: +{amount}")

    def withdraw(self, amount):
        if amount > self.balance:
            raise ValueError("Insufficient funds!")
        self.balance -= amount
        self.history.append(f"Withdrew: -{amount}")

    def __str__(self):
        return f"Account({self.owner}, Balance: {self.balance})"
```

**Step 3: Run tests — all should pass ✓**

```bash
python -m unittest test_bank -v
# test_deposit ... ok
# test_initial_balance ... ok
# test_negative_deposit ... ok
# test_overdraft ... ok
# test_transaction_history ... ok
# test_withdraw ... ok
# Ran 6 tests in 0.001s
# OK
```

---

## 📌 Part F — Debugging Techniques

### 1. Print Debugging (simplest)

```python
def find_max(numbers):
    print(f"DEBUG: input = {numbers}")   # see what comes in
    max_val = numbers[0]
    for n in numbers:
        print(f"DEBUG: comparing {n} with {max_val}")
        if n > max_val:
            max_val = n
    print(f"DEBUG: result = {max_val}")  # see what goes out
    return max_val

find_max([3, 1, 7, 2, 9, 4])
```

---

### 2. `assert` Statements

Use `assert` to catch problems early with a clear message.

```python
def calculate_bmi(weight, height):
    assert weight > 0, f"Weight must be positive, got {weight}"
    assert height > 0, f"Height must be positive, got {height}"
    return round(weight / (height ** 2), 2)

print(calculate_bmi(70, 1.75))   # 22.86
# calculate_bmi(-5, 1.75)        # AssertionError: Weight must be positive, got -5
```

---

### 3. `breakpoint()` — Built-in Debugger

Pauses execution so you can inspect variables interactively.

```python
def process_data(data):
    results = []
    for item in data:
        breakpoint()  # execution stops here
        # In the debugger, type:
        # n  → next line
        # c  → continue
        # p item  → print variable
        # l  → show code around current line
        # q  → quit debugger
        processed = item * 2
        results.append(processed)
    return results

process_data([1, 2, 3])
```

---

### 4. Logging — Better than Print for Real Projects

```python
import logging

# Configure logging level and format
logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s — %(levelname)s — %(message)s",
    datefmt="%H:%M:%S"
)

def divide(a, b):
    logging.debug(f"divide() called with a={a}, b={b}")
    if b == 0:
        logging.error("Division by zero attempted!")
        raise ValueError("Cannot divide by zero")
    result = a / b
    logging.info(f"divide({a}, {b}) = {result}")
    return result

divide(10, 2)
divide(5, 0)

# Output:
# 14:32:01 — DEBUG — divide() called with a=10, b=2
# 14:32:01 — INFO — divide(10, 2) = 5.0
# 14:32:01 — DEBUG — divide() called with a=5, b=0
# 14:32:01 — ERROR — Division by zero attempted!
```

### Logging Levels

| Level | When to use |
|---|---|
| `DEBUG` | Detailed info for diagnosing problems |
| `INFO` | Confirmation things are working |
| `WARNING` | Something unexpected but not breaking |
| `ERROR` | A serious problem occurred |
| `CRITICAL` | A fatal error, program may stop |

---

### 5. Logging to a File

```python
import logging

logging.basicConfig(
    filename="app.log",      # save logs to file
    level=logging.DEBUG,
    format="%(asctime)s — %(levelname)s — %(message)s"
)

logging.info("Application started")
logging.warning("Low disk space")
logging.error("Failed to connect to database")
```

---

## 🛠️ Practice Project — Fully Tested Contact Manager

Write tests for the Contact Manager we built on Day 21.

```python
# test_contact_manager.py
import unittest
import os
import csv
from contact import Contact
from manager import ContactManager

class TestContact(unittest.TestCase):
    """Test the Contact class"""

    def setUp(self):
        self.contact = Contact("Ali", "01711111111", "ali@gmail.com", "Dhaka")

    def test_contact_creation(self):
        self.assertEqual(self.contact.name, "Ali")
        self.assertEqual(self.contact.phone, "01711111111")
        self.assertEqual(self.contact.email, "ali@gmail.com")
        self.assertEqual(self.contact.city, "Dhaka")

    def test_to_dict(self):
        d = self.contact.to_dict()
        self.assertIsInstance(d, dict)
        self.assertIn("name", d)
        self.assertIn("phone", d)
        self.assertEqual(d["name"], "Ali")

    def test_str_representation(self):
        result = str(self.contact)
        self.assertIn("Ali", result)
        self.assertIn("01711111111", result)


class TestContactManager(unittest.TestCase):
    """Test the ContactManager class"""

    TEST_FILE = "test_contacts.csv"

    def setUp(self):
        """Create a fresh manager before each test"""
        ContactManager.FILENAME = self.TEST_FILE
        self.manager = ContactManager()

    def tearDown(self):
        """Remove test file after each test"""
        if os.path.exists(self.TEST_FILE):
            os.remove(self.TEST_FILE)

    def test_add_contact(self):
        self.manager.add_contact("Ali", "01711111111", "ali@gmail.com", "Dhaka")
        self.assertEqual(len(self.manager.contacts), 1)
        self.assertEqual(self.manager.contacts[0].name, "Ali")

    def test_add_duplicate_phone(self):
        self.manager.add_contact("Ali",  "01711111111", "ali@gmail.com",  "Dhaka")
        self.manager.add_contact("Sara", "01711111111", "sara@gmail.com", "Dhaka")
        # Duplicate phone — should still be 1 contact
        self.assertEqual(len(self.manager.contacts), 1)

    def test_delete_contact(self):
        self.manager.add_contact("Ali", "01711111111", "ali@gmail.com", "Dhaka")
        self.manager.delete_contact("01711111111")
        self.assertEqual(len(self.manager.contacts), 0)

    def test_delete_nonexistent(self):
        initial_count = len(self.manager.contacts)
        self.manager.delete_contact("0000000000")
        self.assertEqual(len(self.manager.contacts), initial_count)

    def test_search_by_name(self):
        self.manager.add_contact("Ali",  "01711111111", "ali@gmail.com",  "Dhaka")
        self.manager.add_contact("Sara", "01722222222", "sara@gmail.com", "Dhaka")
        results = [c for c in self.manager.contacts if "ali" in c.name.lower()]
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0].name, "Ali")

    def test_file_persistence(self):
        """Test that contacts are saved and reloaded from file"""
        self.manager.add_contact("Ali", "01711111111", "ali@gmail.com", "Dhaka")

        # Create a new manager — should load from file
        new_manager = ContactManager()
        self.assertEqual(len(new_manager.contacts), 1)
        self.assertEqual(new_manager.contacts[0].name, "Ali")


if __name__ == "__main__":
    unittest.main(verbosity=2)
```

---

## 📝 Quick Summary

| Concept | Key Point |
|---|---|
| `unittest` | Built-in Python testing framework |
| Test methods | Must start with `test_` |
| `assertEqual` | Most common assertion — checks equality |
| `assertRaises` | Checks that an exception is raised |
| `assertAlmostEqual` | Use for float comparisons, never `assertEqual` |
| `setUp` | Runs before each test — prepare data |
| `tearDown` | Runs after each test — clean up |
| TDD | Write test → fail → write code → pass → refactor |
| `print()` debugging | Quick and simple for small bugs |
| `assert` | Catches wrong values early with a clear message |
| `breakpoint()` | Interactive debugger, pause and inspect |
| `logging` | Professional alternative to print for real projects |

---

## 🔗 Resources

- [Python `unittest` Docs](https://docs.python.org/3/library/unittest.html)
- [Python `logging` Docs](https://docs.python.org/3/library/logging.html)
- [Real Python — Getting Started with Testing](https://realpython.com/python-testing/)
- [Real Python — Python Debugging](https://realpython.com/python-debugging-pdb/)

---

> 📅 Part of the **30-Day Python Learning Plan**
> Previous: [Day 25 - Working with JSON](#) | Next: [Day 27 - Virtual Environments & Best Practices](#)
