# Day 6: Conditional Statements

## Overview
Today we'll learn about conditional statements - how to make decisions in your code using if, elif, and else statements. This allows your programs to execute different code based on conditions.

---

## 1. The if Statement

The `if` statement executes code only when a condition is True.

### Basic Syntax

```python
if condition:
    # code to execute if condition is True
```

### Examples

```python
# Simple if statement
age = 18
if age >= 18:
    print("You are an adult")

# With comparison operators
temperature = 35
if temperature > 30:
    print("It's hot outside!")

# With variables
is_raining = True
if is_raining:
    print("Take an umbrella")

# Multiple statements
score = 85
if score >= 80:
    print("Great job!")
    print("You passed with distinction")
```

---

## 2. The if-else Statement

The `else` statement provides an alternative when the condition is False.

### Syntax

```python
if condition:
    # code if condition is True
else:
    # code if condition is False
```

### Examples

```python
# Basic if-else
age = 15
if age >= 18:
    print("You can vote")
else:
    print("You cannot vote yet")

# With numbers
number = 7
if number % 2 == 0:
    print("Even number")
else:
    print("Odd number")

# With user input
password = input("Enter password: ")
if password == "secret123":
    print("Access granted")
else:
    print("Access denied")
```

---

## 3. The if-elif-else Statement

Use `elif` (else if) to check multiple conditions.

### Syntax

```python
if condition1:
    # code if condition1 is True
elif condition2:
    # code if condition2 is True
elif condition3:
    # code if condition3 is True
else:
    # code if all conditions are False
```

### Examples

```python
# Grade calculator
score = 75

if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
elif score >= 60:
    grade = "D"
else:
    grade = "F"

print(f"Your grade is: {grade}")

# Age categories
age = 25

if age < 13:
    category = "Child"
elif age < 20:
    category = "Teenager"
elif age < 60:
    category = "Adult"
else:
    category = "Senior"

print(f"You are a {category}")
```

---

## 4. Nested if Statements

You can place if statements inside other if statements.

### Examples

```python
# Nested conditions
age = 20
has_license = True

if age >= 18:
    if has_license:
        print("You can drive")
    else:
        print("You need a license to drive")
else:
    print("You are too young to drive")

# Multiple nested levels
num = 15

if num > 0:
    if num % 2 == 0:
        print("Positive even number")
    else:
        print("Positive odd number")
else:
    if num % 2 == 0:
        print("Negative even number")
    else:
        print("Negative odd number")
```

---

## 5. Logical Operators in Conditions

Combine multiple conditions using `and`, `or`, and `not`.

### AND Operator

Both conditions must be True.

```python
age = 25
salary = 50000

if age >= 18 and salary >= 30000:
    print("Eligible for loan")

# Multiple AND conditions
score1 = 85
score2 = 90
score3 = 88

if score1 >= 80 and score2 >= 80 and score3 >= 80:
    print("All scores are excellent!")
```

### OR Operator

At least one condition must be True.

```python
day = "Saturday"

if day == "Saturday" or day == "Sunday":
    print("It's weekend!")

# Multiple OR conditions
grade = "A"

if grade == "A" or grade == "B" or grade == "C":
    print("You passed!")
```

### NOT Operator

Reverses the boolean value.

```python
is_raining = False

if not is_raining:
    print("You don't need an umbrella")

# With comparison
age = 15

if not age >= 18:
    print("You are a minor")
```

### Combining Operators

```python
age = 25
is_student = True
has_id = True

# Complex condition
if (age >= 18 and age <= 60) and (is_student or has_id):
    print("Eligible for discount")

# Another example
temperature = 28
is_sunny = True
is_weekend = False

if temperature > 25 and is_sunny and not is_weekend:
    print("Great day for a walk!")
```

---

## 6. Ternary Operator (Conditional Expression)

A shorthand way to write simple if-else statements in one line.

### Syntax

```python
value_if_true if condition else value_if_false
```

### Examples

```python
# Simple ternary
age = 20
status = "Adult" if age >= 18 else "Minor"
print(status)  # "Adult"

# With numbers
a = 10
b = 20
max_value = a if a > b else b
print(max_value)  # 20

# In print statement
score = 75
print("Pass" if score >= 60 else "Fail")

# Nested ternary (not recommended - hard to read)
score = 85
grade = "A" if score >= 90 else "B" if score >= 80 else "C"
print(grade)  # "B"
```

---

## 7. Common Patterns and Idioms

### Checking Multiple Values

```python
# Using 'in' with a tuple/list
fruit = "apple"

if fruit in ("apple", "banana", "orange"):
    print("Common fruit")

# Checking range
age = 25

if 18 <= age <= 65:
    print("Working age")

# Multiple conditions with same result
day = "Monday"

if day == "Saturday" or day == "Sunday":
    print("Weekend")
# Better way:
if day in ["Saturday", "Sunday"]:
    print("Weekend")
```

### Truthy and Falsy Values

In Python, some values are considered False in boolean context.

**Falsy values:** `False`, `0`, `0.0`, `""` (empty string), `[]` (empty list), `{}` (empty dict), `None`

**Truthy values:** Everything else

```python
# Empty string is False
name = ""
if name:
    print("Name provided")
else:
    print("Name is empty")

# Empty list is False
items = []
if items:
    print("List has items")
else:
    print("List is empty")

# Zero is False
count = 0
if count:
    print("Count is non-zero")
else:
    print("Count is zero")

# None is False
data = None
if data:
    print("Data exists")
else:
    print("No data")
```

### Guard Clauses

Check for invalid conditions first and return/exit early.

```python
def process_age(age):
    # Guard clauses
    if age < 0:
        print("Invalid age")
        return
    
    if age < 18:
        print("Minor")
        return
    
    # Main logic
    print("Adult")

# vs nested conditions (harder to read)
def process_age_nested(age):
    if age >= 0:
        if age >= 18:
            print("Adult")
        else:
            print("Minor")
    else:
        print("Invalid age")
```

---

## 8. Match-Case Statement (Python 3.10+)

A newer way to handle multiple conditions (similar to switch-case in other languages).

### Syntax

```python
match variable:
    case pattern1:
        # code
    case pattern2:
        # code
    case _:
        # default case
```

### Examples

```python
# Simple match-case
day = 3

match day:
    case 1:
        print("Monday")
    case 2:
        print("Tuesday")
    case 3:
        print("Wednesday")
    case 4:
        print("Thursday")
    case 5:
        print("Friday")
    case 6 | 7:  # Multiple patterns
        print("Weekend")
    case _:  # Default
        print("Invalid day")

# With strings
command = "start"

match command:
    case "start":
        print("Starting...")
    case "stop":
        print("Stopping...")
    case "pause":
        print("Pausing...")
    case _:
        print("Unknown command")

# Pattern matching with conditions
score = 85

match score:
    case s if s >= 90:
        print("Grade: A")
    case s if s >= 80:
        print("Grade: B")
    case s if s >= 70:
        print("Grade: C")
    case _:
        print("Grade: F")
```

---

## 9. Best Practices

### Do's

✅ Use meaningful condition names
```python
# Good
is_valid_age = age >= 18
if is_valid_age:
    print("Valid")

# Bad
if age >= 18:
    print("Valid")
```

✅ Keep conditions simple
```python
# Good
is_eligible = age >= 18 and has_license
if is_eligible:
    print("Can drive")

# Bad
if age >= 18 and has_license and not is_suspended and has_insurance:
    print("Can drive")
```

✅ Use positive conditions when possible
```python
# Good
if is_active:
    process()

# Avoid double negatives
if not is_inactive:
    process()
```

### Don'ts

❌ Don't compare boolean values with True/False
```python
# Bad
if is_active == True:
    print("Active")

# Good
if is_active:
    print("Active")
```

❌ Don't use nested conditions when not needed
```python
# Bad
if age >= 18:
    if has_license:
        print("Can drive")

# Better (when appropriate)
if age >= 18 and has_license:
    print("Can drive")
```

❌ Don't repeat code in branches
```python
# Bad
if condition:
    print("Processing...")
    do_something()
else:
    print("Processing...")
    do_something_else()

# Good
print("Processing...")
if condition:
    do_something()
else:
    do_something_else()
```

---

## Practice Exercises

### Exercise 1: Leap Year Checker
Write a program to check if a year is a leap year.
Rules:
- Divisible by 4
- If divisible by 100, must also be divisible by 400

### Exercise 2: BMI Calculator
Calculate BMI and categorize:
- Below 18.5: Underweight
- 18.5-24.9: Normal
- 25-29.9: Overweight
- 30+: Obese

### Exercise 3: Triangle Validator
Check if three sides can form a valid triangle.
Rule: Sum of any two sides must be greater than the third side.

### Exercise 4: Login System
Create a simple login with:
- Username and password check
- 3 attempts limit
- Lock account after failed attempts

### Exercise 5: Discount Calculator
Calculate discount based on:
- Purchase amount
- Customer type (regular/premium)
- Day of week (weekend bonus)

---

## Practice Project

**See:** `day06_grade_calculator.py` for the complete Grade Calculator project.

The project includes:
- Multiple student grade management
- Letter grade calculation with +/- modifiers
- GPA calculation
- Pass/Fail determination
- Statistics (average, highest, lowest)
- Grade distribution report

---

## Quick Reference

### Comparison Operators

| Operator | Meaning | Example |
|----------|---------|---------|
| `==` | Equal to | `x == y` |
| `!=` | Not equal to | `x != y` |
| `>` | Greater than | `x > y` |
| `<` | Less than | `x < y` |
| `>=` | Greater than or equal | `x >= y` |
| `<=` | Less than or equal | `x <= y` |

### Logical Operators

| Operator | Description | Example |
|----------|-------------|---------|
| `and` | True if both are true | `x > 0 and y > 0` |
| `or` | True if at least one is true | `x > 0 or y > 0` |
| `not` | Reverses the result | `not x > 0` |

### Truth Table

| A | B | A and B | A or B | not A |
|---|---|---------|--------|-------|
| T | T | T | T | F |
| T | F | F | T | F |
| F | T | F | T | T |
| F | F | F | F | T |

---

## Key Takeaways

✅ `if` statements control program flow based on conditions  
✅ Use `elif` for multiple exclusive conditions  
✅ `else` provides a fallback when no conditions match  
✅ Logical operators (`and`, `or`, `not`) combine conditions  
✅ Ternary operator provides one-line conditional assignment  
✅ Falsy values: `False`, `0`, `""`, `[]`, `{}`, `None`  
✅ Keep conditions simple and readable  
✅ Use guard clauses for cleaner code  

---

## Common Mistakes to Avoid

❌ **Using = instead of ==**
```python
if x = 5:  # ERROR! This is assignment
if x == 5: # Correct
```

❌ **Forgetting indentation**
```python
if age >= 18:
print("Adult")  # ERROR! Must be indented
```

❌ **Using semicolons**
```python
if age >= 18; print("Adult")  # Wrong syntax
```

❌ **Confusing and/or**
```python
# Wrong: Always true
if age >= 18 or age <= 65:

# Correct
if age >= 18 and age <= 65:
# Or better:
if 18 <= age <= 65:
```

---

## Next Steps

Tomorrow (Day 7), we'll do a **Week 1 Review** and build a comprehensive mini-project combining everything we've learned!

---

## Resources

- [Python If Statements Documentation](https://docs.python.org/3/tutorial/controlflow.html#if-statements)
- [Python Boolean Operations](https://docs.python.org/3/library/stdtypes.html#boolean-operations-and-or-not)

---

**Make Smart Decisions! 🐍**