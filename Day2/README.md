# Day 2: Operators & Input/Output

## Overview
Today we'll learn about different types of operators in Python and how to build interactive programs using input/output.

---

## 1. Arithmetic Operators

Arithmetic operators perform mathematical operations.

| Operator | Description | Example | Result |
|----------|-------------|---------|--------|
| `+` | Addition | `5 + 3` | `8` |
| `-` | Subtraction | `5 - 3` | `2` |
| `*` | Multiplication | `5 * 3` | `15` |
| `/` | Division | `5 / 2` | `2.5` |
| `//` | Floor Division | `5 // 2` | `2` |
| `%` | Modulus (Remainder) | `5 % 2` | `1` |
| `**` | Exponentiation | `5 ** 2` | `25` |

### Examples:
```python
# Basic arithmetic
a = 10
b = 3

print(a + b)   # 13
print(a - b)   # 7
print(a * b)   # 30
print(a / b)   # 3.333...
print(a // b)  # 3 (floor division)
print(a % b)   # 1 (remainder)
print(a ** b)  # 1000 (10^3)
```

---

## 2. Comparison Operators

Comparison operators compare two values and return `True` or `False`.

| Operator | Description | Example | Result |
|----------|-------------|---------|--------|
| `==` | Equal to | `5 == 5` | `True` |
| `!=` | Not equal to | `5 != 3` | `True` |
| `>` | Greater than | `5 > 3` | `True` |
| `<` | Less than | `5 < 3` | `False` |
| `>=` | Greater than or equal | `5 >= 5` | `True` |
| `<=` | Less than or equal | `3 <= 5` | `True` |

### Examples:
```python
x = 10
y = 5

print(x == y)   # False
print(x != y)   # True
print(x > y)    # True
print(x < y)    # False
print(x >= 10)  # True
print(y <= 5)   # True
```

---

## 3. Logical Operators

Logical operators combine conditional statements.

| Operator | Description | Example | Result |
|----------|-------------|---------|--------|
| `and` | Returns True if both are true | `True and False` | `False` |
| `or` | Returns True if one is true | `True or False` | `True` |
| `not` | Reverses the result | `not True` | `False` |

### Examples:
```python
age = 20
has_license = True

# AND: Both conditions must be True
can_drive = age >= 18 and has_license
print(can_drive)  # True

# OR: At least one condition must be True
is_eligible = age >= 18 or has_license
print(is_eligible)  # True

# NOT: Reverses the boolean
is_minor = not (age >= 18)
print(is_minor)  # False
```

---

## 4. Input/Output in Python

### Output with `print()`
```python
print("Hello, World!")
print("My age is", 25)
print(f"My age is {25}")  # f-string (formatted)
```

### Input with `input()`
The `input()` function always returns a **string**, so you need to convert it if you need numbers.

```python
# Taking string input
name = input("Enter your name: ")
print(f"Hello, {name}!")

# Taking integer input
age = int(input("Enter your age: "))
print(f"You are {age} years old")

# Taking float input
height = float(input("Enter your height in meters: "))
print(f"Your height is {height}m")
```

### Important Notes:
- `input()` returns a **string**
- Use `int()` to convert to integer
- Use `float()` to convert to decimal number
- If user enters invalid data, program will crash (we'll handle this later)

---

## 5. Operator Precedence

Python follows the standard mathematical order of operations (PEMDAS/BODMAS):

1. `**` (Exponentiation)
2. `*`, `/`, `//`, `%` (Multiplication, Division)
3. `+`, `-` (Addition, Subtraction)
4. Comparison operators
5. Logical operators (`not`, `and`, `or`)

```python
result = 2 + 3 * 4      # 14 (not 20)
result = (2 + 3) * 4    # 20 (parentheses first)
result = 10 / 2 * 3     # 15.0 (left to right)
```
## Additional Exercises

### Exercise 1: Temperature Converter
Create a program that converts Celsius to Fahrenheit and vice versa.
```
Formula: F = (C * 9/5) + 32
Formula: C = (F - 32) * 5/9
```

### Exercise 2: Even or Odd Checker
Create a program that checks if a number is even or odd using the modulus operator.

### Exercise 3: Comparison Tool
Take two numbers and display all comparison results (==, !=, >, <, >=, <=).

### Exercise 4: Logical Quiz
Create a simple eligibility checker using logical operators (e.g., voting eligibility based on age and citizenship).

---

## Key Takeaways

✅ Arithmetic operators perform mathematical calculations  
✅ Comparison operators compare values and return True/False  
✅ Logical operators combine multiple conditions  
✅ `input()` always returns a string - convert with `int()` or `float()`  
✅ Use f-strings for formatted output: `f"Hello {name}"`  
✅ Always check for division by zero  

---

## Next Steps

Tomorrow (Day 3), we'll dive into **Strings** and learn about string methods and manipulation!

---

## Resources

- [Python Operators Documentation](https://docs.python.org/3/library/operator.html)
- [Python Input/Output Tutorial](https://docs.python.org/3/tutorial/inputoutput.html)

---

**Happy Coding! 🐍**
