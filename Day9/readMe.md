# Day 9: Loops - Part 2 (while loops)

## Overview
Today we'll learn about `while` loops - loops that continue executing as long as a condition remains True. Unlike `for` loops that iterate over a sequence, `while` loops are condition-based.

---

## 1. Introduction to while Loops

### for vs while Loops

**for loop:** Use when you know how many iterations you need
```python
# Print 5 times - we know the count
for i in range(5):
    print("Hello")
```

**while loop:** Use when you continue until a condition changes
```python
# Keep asking until correct password - we don't know how many tries
password = ""
while password != "secret":
    password = input("Enter password: ")
```

---

## 2. Basic while Loop

### Syntax

```python
while condition:
    # code to execute while condition is True
```

### Simple Examples

```python
# Count to 5
count = 1
while count <= 5:
    print(count)
    count += 1

# Output: 1 2 3 4 5

# Countdown
count = 5
while count > 0:
    print(count)
    count -= 1
print("Blast off!")

# Output: 5 4 3 2 1 Blast off!
```

### Important: Update the Condition!

```python
# ❌ INFINITE LOOP - Never stops!
count = 1
while count <= 5:
    print(count)
    # Forgot to increment count!

# ✅ Correct
count = 1
while count <= 5:
    print(count)
    count += 1  # Updates condition
```

---

## 3. Common while Loop Patterns

### Pattern 1: Counter-Based Loop

```python
# Sum numbers from 1 to 10
total = 0
number = 1

while number <= 10:
    total += number
    number += 1

print(f"Sum: {total}")  # 55
```

### Pattern 2: Sentinel-Based Loop

```python
# Continue until user enters 'quit'
command = ""

while command != "quit":
    command = input("Enter command (or 'quit' to exit): ")
    if command != "quit":
        print(f"You entered: {command}")
```

### Pattern 3: Flag-Based Loop

```python
# Continue until flag becomes False
found = False
numbers = [1, 2, 3, 4, 5]
search = 3
index = 0

while index < len(numbers) and not found:
    if numbers[index] == search:
        found = True
        print(f"Found {search} at index {index}")
    index += 1

if not found:
    print(f"{search} not found")
```

### Pattern 4: Input Validation

```python
# Keep asking until valid input
age = -1

while age < 0 or age > 120:
    age = int(input("Enter your age (0-120): "))
    if age < 0 or age > 120:
        print("Invalid age! Try again.")

print(f"Your age: {age}")
```

---

## 4. while Loop with break

### Using break to Exit Early

```python
# Search and exit when found
numbers = [10, 20, 30, 40, 50]
search = 30
index = 0

while index < len(numbers):
    if numbers[index] == search:
        print(f"Found {search} at index {index}")
        break
    index += 1
else:
    print(f"{search} not found")
```

### Menu-Driven Programs

```python
while True:
    print("\n1. Option 1")
    print("2. Option 2")
    print("3. Exit")
    
    choice = input("Enter choice: ")
    
    if choice == '1':
        print("You selected option 1")
    elif choice == '2':
        print("You selected option 2")
    elif choice == '3':
        print("Goodbye!")
        break
    else:
        print("Invalid choice!")
```

---

## 5. while Loop with continue

### Skip Current Iteration

```python
# Print odd numbers from 1 to 10
number = 0

while number < 10:
    number += 1
    if number % 2 == 0:
        continue
    print(number)

# Output: 1 3 5 7 9
```

### Skip Invalid Input

```python
count = 0

while count < 5:
    value = input("Enter a positive number: ")
    
    if not value.isdigit():
        print("Invalid input! Try again.")
        continue
    
    number = int(value)
    if number <= 0:
        print("Must be positive! Try again.")
        continue
    
    print(f"You entered: {number}")
    count += 1
```

---

## 6. while Loop with else

The `else` block executes when the loop completes normally (not broken by `break`).

```python
# Search for a number
numbers = [1, 2, 3, 4, 5]
search = 10
index = 0

while index < len(numbers):
    if numbers[index] == search:
        print(f"Found {search}!")
        break
    index += 1
else:
    print(f"{search} not found")  # This runs if break wasn't called
```

---

## 7. Nested while Loops

### Basic Nested Loop

```python
# Multiplication table
i = 1
while i <= 3:
    j = 1
    while j <= 3:
        print(f"{i} x {j} = {i * j}")
        j += 1
    print()  # Empty line
    i += 1
```

### Pattern with while Loops

```python
# Right triangle pattern
row = 1
size = 5

while row <= size:
    col = 1
    while col <= row:
        print("*", end="")
        col += 1
    print()
    row += 1

# Output:
# *
# **
# ***
# ****
# *****
```

---

## 8. Infinite Loops

### Intentional Infinite Loops

```python
# Server or game loop (runs until explicitly stopped)
while True:
    command = input("Enter command: ")
    
    if command == "exit":
        break
    elif command == "help":
        print("Available commands: help, exit")
    else:
        print(f"Unknown command: {command}")
```

### Avoiding Accidental Infinite Loops

```python
# ❌ Infinite loop - condition never changes
x = 5
while x > 0:
    print(x)
    # Forgot to decrement x!

# ✅ Correct
x = 5
while x > 0:
    print(x)
    x -= 1  # Updates condition
```

---

## 9. Practical Examples

### Example 1: Sum Until Zero

```python
# Sum numbers until user enters 0
total = 0

while True:
    number = int(input("Enter a number (0 to stop): "))
    
    if number == 0:
        break
    
    total += number

print(f"Total sum: {total}")
```

### Example 2: Guessing Game

```python
import random

secret = random.randint(1, 100)
attempts = 0
max_attempts = 10

while attempts < max_attempts:
    guess = int(input("Guess the number (1-100): "))
    attempts += 1
    
    if guess == secret:
        print(f"Correct! You won in {attempts} attempts!")
        break
    elif guess < secret:
        print("Too low!")
    else:
        print("Too high!")
    
    print(f"Attempts left: {max_attempts - attempts}")
else:
    print(f"Game over! The number was {secret}")
```

### Example 3: Password Validator

```python
# Password must be at least 8 characters with a digit
password = ""

while True:
    password = input("Create a password (min 8 chars, must include digit): ")
    
    # Check length
    if len(password) < 8:
        print("✗ Too short! Must be at least 8 characters.")
        continue
    
    # Check for digit
    has_digit = False
    for char in password:
        if char.isdigit():
            has_digit = True
            break
    
    if not has_digit:
        print("✗ Must include at least one digit!")
        continue
    
    print("✓ Password accepted!")
    break
```

### Example 4: ATM Simulation

```python
balance = 1000

while True:
    print(f"\nBalance: ${balance}")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Exit")
    
    choice = input("Choose option: ")
    
    if choice == '1':
        amount = float(input("Enter deposit amount: $"))
        if amount > 0:
            balance += amount
            print(f"✓ Deposited ${amount}")
        else:
            print("✗ Invalid amount!")
    
    elif choice == '2':
        amount = float(input("Enter withdrawal amount: $"))
        if amount > 0 and amount <= balance:
            balance -= amount
            print(f"✓ Withdrew ${amount}")
        elif amount > balance:
            print("✗ Insufficient funds!")
        else:
            print("✗ Invalid amount!")
    
    elif choice == '3':
        print("Thank you for using ATM!")
        break
    
    else:
        print("✗ Invalid choice!")
```

### Example 5: Find Factorial

```python
# Calculate factorial using while loop
number = int(input("Enter a number: "))
factorial = 1
temp = number

while temp > 0:
    factorial *= temp
    temp -= 1

print(f"Factorial of {number} is {factorial}")
```

---

## 10. for vs while: When to Use Which?

### Use for Loop When:
✅ You know the number of iterations  
✅ Iterating over a collection  
✅ Working with ranges  

```python
# Print all items in a list
fruits = ["apple", "banana", "orange"]
for fruit in fruits:
    print(fruit)

# Count to 10
for i in range(1, 11):
    print(i)
```

### Use while Loop When:
✅ Condition-based iteration  
✅ Unknown number of iterations  
✅ Input validation  
✅ Game loops  
✅ Server loops  

```python
# Keep asking until valid input
valid = False
while not valid:
    age = int(input("Enter age: "))
    if age > 0:
        valid = True

# Menu-driven programs
while True:
    choice = input("Enter choice: ")
    if choice == 'quit':
        break
```

---

## 11. Common Patterns and Idioms

### Input Validation Loop

```python
while True:
    user_input = input("Enter a positive number: ")
    
    if user_input.isdigit():
        number = int(user_input)
        if number > 0:
            break
    
    print("Invalid input! Try again.")
```

### Accumulator Pattern

```python
# Calculate average
total = 0
count = 0

while True:
    value = input("Enter a number (or 'done'): ")
    
    if value == 'done':
        break
    
    total += float(value)
    count += 1

if count > 0:
    average = total / count
    print(f"Average: {average}")
```

### Search Pattern

```python
# Linear search
items = [10, 20, 30, 40, 50]
target = 30
index = 0
found = False

while index < len(items) and not found:
    if items[index] == target:
        found = True
        print(f"Found at index {index}")
    index += 1
```

---

## Practice Exercises

### Exercise 1: Number Reversal
Write a program that reverses the digits of a number using a while loop.
```
Input: 12345
Output: 54321
```

### Exercise 2: Sum of Digits
Calculate the sum of digits in a number.
```
Input: 12345
Output: 15 (1+2+3+4+5)
```

### Exercise 3: Prime Number Generator
Generate all prime numbers up to a given number using while loops.

### Exercise 4: Fibonacci Sequence
Generate Fibonacci sequence until a number exceeds 1000.

### Exercise 5: Login System
Create a login system with:
- Maximum 3 attempts
- Lock account after failed attempts
- Success message on correct login

---

## Practice Project

**See:** `day09_menu_driven_app.py` for the complete Menu-Driven Calculator project.

The project includes:
- Multiple calculator modes
- Input validation with while loops
- Menu navigation
- History tracking
- Continuous operation until user exits

---

## Quick Reference

### while Loop Syntax

```python
# Basic while
while condition:
    # code

# while with break
while True:
    if condition:
        break

# while with continue
while condition:
    if skip_condition:
        continue
    # code

# while with else
while condition:
    # code
else:
    # runs if loop completes normally
```

### Common Patterns

```python
# Counter
count = 0
while count < 10:
    # code
    count += 1

# Sentinel
value = ""
while value != "quit":
    value = input()

# Flag
done = False
while not done:
    if condition:
        done = True

# Infinite with break
while True:
    if condition:
        break
```

---

## Key Takeaways

✅ `while` loops run as long as condition is True  
✅ Always update the condition variable to avoid infinite loops  
✅ Use `break` to exit loop early  
✅ Use `continue` to skip current iteration  
✅ `else` clause runs if loop completes without break  
✅ Use `for` when iterations are known, `while` for conditions  
✅ `while True` with `break` is common for menu-driven programs  
✅ Always validate user input in while loops  

---

## Common Mistakes to Avoid

❌ **Infinite loops (forgetting to update condition)**
```python
# Bad
count = 0
while count < 5:
    print(count)
    # Forgot count += 1

# Good
count = 0
while count < 5:
    print(count)
    count += 1
```

❌ **Off-by-one errors**
```python
# Prints 0-4 (5 times)
count = 0
while count < 5:
    print(count)
    count += 1

# Prints 1-5 (5 times)
count = 1
while count <= 5:
    print(count)
    count += 1
```

❌ **Not handling edge cases**
```python
# Bad - crashes if list is empty
index = 0
while index < len(items):
    print(items[index])
    index += 1

# Good - check if list has items
if items:
    index = 0
    while index < len(items):
        print(items[index])
        index += 1
```

---

## Debugging while Loops

### Technique 1: Print Condition
```python
count = 0
while count < 5:
    print(f"Count: {count}, Condition: {count < 5}")
    count += 1
```

### Technique 2: Add Safety Counter
```python
count = 0
safety = 0

while count < target:
    count += 1
    safety += 1
    
    if safety > 1000:  # Prevent infinite loop
        print("Loop limit reached!")
        break
```

### Technique 3: Use IDE Debugger
- Set breakpoints
- Step through iterations
- Watch variable values

---

## Next Steps

Tomorrow (Day 10), we'll learn about **Functions - Basics** - how to create reusable blocks of code!

---

## Resources

- [Python while Loops Documentation](https://docs.python.org/3/reference/compound_stmts.html#while)
- [Loop Control Statements](https://docs.python.org/3/tutorial/controlflow.html#break-and-continue-statements-and-else-clauses-on-loops)

---

**Loop with Conditions! 🐍**
