# Day 7: Week 1 Review & Mini Project

## Overview
Congratulations on completing Week 1! 🎉 Today we'll review everything you've learned and build a comprehensive project that combines all Week 1 concepts.

---

## 📚 Week 1 Summary

### Day 1: Variables & Data Types
```python
# Variables
name = "John"           # String
age = 25                # Integer
height = 5.9            # Float
is_student = True       # Boolean

# Type checking
print(type(name))       # <class 'str'>
```

**Key Concepts:**
- Variables store data
- Four basic types: int, float, string, boolean
- Use `type()` to check data type
- Convert types with `int()`, `float()`, `str()`

---

### Day 2: Operators & Input/Output
```python
# Arithmetic operators
result = 10 + 5         # Addition
result = 10 // 3        # Floor division (3)
result = 10 % 3         # Modulus (1)
result = 2 ** 3         # Exponentiation (8)

# Comparison operators
print(5 == 5)           # True
print(5 != 3)           # True
print(5 > 3)            # True

# Logical operators
print(True and False)   # False
print(True or False)    # True
print(not True)         # False

# Input/Output
name = input("Name: ")
age = int(input("Age: "))
print(f"Hello, {name}!")
```

**Key Concepts:**
- 7 arithmetic operators (+, -, *, /, //, %, **)
- 6 comparison operators (==, !=, >, <, >=, <=)
- 3 logical operators (and, or, not)
- `input()` returns strings - convert with `int()` or `float()`
- Use f-strings for formatting: `f"Hello {name}"`

---

### Day 3: Strings
```python
# String methods
text = "  Hello World  "
print(text.upper())         # "  HELLO WORLD  "
print(text.lower())         # "  hello world  "
print(text.strip())         # "Hello World"
print(text.replace("World", "Python"))  # "  Hello Python  "

# Slicing
text = "Python"
print(text[0:3])            # "Pyt"
print(text[::-1])           # "nohtyP"

# Splitting and joining
words = "a,b,c".split(",")  # ['a', 'b', 'c']
result = "-".join(words)    # "a-b-c"
```

**Key Concepts:**
- Strings are immutable
- Indexing starts at 0, negative indices go backwards
- Slicing: `[start:end:step]`
- Common methods: upper(), lower(), strip(), replace(), split(), join()
- f-strings for formatting

---

### Day 4: Lists & Tuples
```python
# Lists (mutable)
fruits = ["apple", "banana", "orange"]
fruits.append("mango")
fruits.remove("banana")
fruits.sort()

# Tuples (immutable)
coordinates = (10, 20)
x, y = coordinates  # Unpacking

# Common operations
print(len(fruits))
print("apple" in fruits)
```

**Key Concepts:**
- Lists use `[]`, tuples use `()`
- Lists are mutable, tuples are immutable
- Indexing and slicing work for both
- List methods: append(), remove(), pop(), sort(), reverse()
- Tuple unpacking for multiple assignment

---

### Day 5: Dictionaries & Sets
```python
# Dictionaries
student = {
    "name": "John",
    "age": 20,
    "grade": "A"
}
print(student["name"])
student["email"] = "john@email.com"

# Sets (unique elements)
numbers = {1, 2, 3, 3, 4}   # {1, 2, 3, 4}
numbers.add(5)
numbers.remove(2)

# Set operations
set1 = {1, 2, 3}
set2 = {3, 4, 5}
print(set1 | set2)          # Union: {1, 2, 3, 4, 5}
print(set1 & set2)          # Intersection: {3}
```

**Key Concepts:**
- Dictionaries store key-value pairs
- Access with `dict[key]` or `dict.get(key)`
- Sets store unique, unordered elements
- Set operations: union (|), intersection (&), difference (-)

---

### Day 6: Conditional Statements
```python
# if-elif-else
score = 85

if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
else:
    grade = "F"

# Logical operators
if age >= 18 and has_license:
    print("Can drive")

# Ternary operator
status = "Pass" if score >= 60 else "Fail"
```

**Key Concepts:**
- `if` for single condition
- `elif` for multiple conditions
- `else` for default case
- Combine conditions with `and`, `or`, `not`
- Ternary: `value_if_true if condition else value_if_false`

---

## 🎯 Concept Integration Quiz

Test your understanding:

### Question 1: Data Types
```python
x = "5"
y = 5
z = 5.0

# What are the types?
# What happens with x + y?
# What happens with y + z?
```

**Answer:**
- `x` is string, `y` is int, `z` is float
- `x + y` gives TypeError (can't add string and int)
- `y + z` gives 10.0 (int + float = float)

### Question 2: String vs List
```python
text = "hello"
items = ["h", "e", "l", "l", "o"]

# Can you do text[0] = "H"?
# Can you do items[0] = "H"?
```

**Answer:**
- `text[0] = "H"` gives error (strings are immutable)
- `items[0] = "H"` works (lists are mutable)

### Question 3: Dictionary vs Set
```python
data1 = {"a": 1, "b": 2}
data2 = {"a", "b", "a", "b"}

# What is data2?
# How to add to each?
```

**Answer:**
- `data2` is a set: `{"a", "b"}` (duplicates removed)
- Dictionary: `data1["c"] = 3`
- Set: `data2.add("c")`

### Question 4: Conditions
```python
age = 17
has_permission = True

# What prints?
if age >= 18 or has_permission:
    print("Allowed")
else:
    print("Not allowed")
```

**Answer:** "Allowed" (because `has_permission` is True, and we use `or`)

---

## 💡 Common Patterns Review

### Pattern 1: Input Validation
```python
while True:
    age = input("Enter age: ")
    if age.isdigit():
        age = int(age)
        if age > 0:
            break
    print("Invalid input!")
```

### Pattern 2: Menu-Driven Program
```python
while True:
    print("1. Option 1")
    print("2. Option 2")
    print("3. Exit")
    choice = input("Choice: ")
    
    if choice == '1':
        # do something
        pass
    elif choice == '2':
        # do something else
        pass
    elif choice == '3':
        break
```

### Pattern 3: Data Processing
```python
# Calculate average from list
numbers = [10, 20, 30, 40, 50]
total = sum(numbers)
average = total / len(numbers)

# Filter list
evens = [x for x in numbers if x % 2 == 0]
```

### Pattern 4: Dictionary Lookup
```python
user_data = {
    "user1": {"name": "John", "age": 25},
    "user2": {"name": "Jane", "age": 30}
}

# Safe access
user = user_data.get("user1", {})
name = user.get("name", "Unknown")
```

---

## 🚀 Mini Project: Number Guessing Game

**See:** `day07_number_guessing_game.py` for the complete project.

### Project Features:
1. **Three Difficulty Levels**
   - Easy: 1-50, 10 attempts
   - Medium: 1-100, 7 attempts
   - Hard: 1-200, 5 attempts

2. **Game Mechanics**
   - Random number generation
   - Hint system (higher/lower)
   - Attempt tracking
   - Score calculation based on attempts

3. **Statistics Tracking**
   - Games played
   - Games won/lost
   - Best score per difficulty
   - Win rate calculation

4. **Advanced Features**
   - Play again option
   - Difficulty selection
   - Input validation
   - Leaderboard display

### Concepts Used:
✅ Variables & data types
✅ Operators (arithmetic, comparison, logical)
✅ Strings (formatting, methods)
✅ Lists (storing attempts, history)
✅ Dictionaries (settings, statistics)
✅ Conditional statements (game logic)

---

## 📝 Week 1 Checklist

Review and check your understanding:

### Day 1: Variables & Data Types
- [ ] Can create variables of different types
- [ ] Understand int, float, string, boolean
- [ ] Can convert between types
- [ ] Can use type() function

### Day 2: Operators & Input/Output
- [ ] Know all arithmetic operators
- [ ] Understand comparison operators
- [ ] Can combine conditions with logical operators
- [ ] Can take user input and display output
- [ ] Understand operator precedence

### Day 3: Strings
- [ ] Can create and manipulate strings
- [ ] Understand string indexing and slicing
- [ ] Know common string methods
- [ ] Can format strings with f-strings
- [ ] Understand string immutability

### Day 4: Lists & Tuples
- [ ] Can create and modify lists
- [ ] Know list methods (append, remove, sort, etc.)
- [ ] Understand list slicing
- [ ] Know when to use lists vs tuples
- [ ] Can unpack tuples

### Day 5: Dictionaries & Sets
- [ ] Can create and access dictionaries
- [ ] Know dictionary methods
- [ ] Understand sets and their operations
- [ ] Can perform set operations (union, intersection)
- [ ] Know when to use dict vs set

### Day 6: Conditional Statements
- [ ] Can write if-elif-else statements
- [ ] Understand logical operators
- [ ] Can use ternary operator
- [ ] Know about truthy/falsy values
- [ ] Can write nested conditions

---

## 🎓 Additional Practice Challenges

### Challenge 1: Data Type Converter
Create a program that:
- Takes input from user
- Detects if it's a number, decimal, or text
- Converts and displays in all possible formats

### Challenge 2: List Operations
Given a list of numbers:
```python
numbers = [12, 45, 23, 67, 34, 89, 56, 78, 90, 11]
```
Find:
- Sum and average
- Maximum and minimum
- Numbers greater than 50
- Even and odd numbers
- Second largest number

### Challenge 3: Dictionary Manipulation
Create a student database:
- Store multiple students
- Each has name, age, grades (list)
- Calculate average grade per student
- Find student with highest average
- Find all students with average > 80

### Challenge 4: String Analyzer
Create a program that analyzes text:
- Count vowels and consonants
- Count words
- Find longest word
- Reverse each word
- Check if palindrome

### Challenge 5: Set Operations
Given two lists of user IDs:
```python
online_users = [101, 102, 103, 104, 105]
premium_users = [103, 104, 106, 107]
```
Find:
- Premium users currently online
- All users (union)
- Free users online
- Offline premium users

---

## 🔥 Pro Tips for Week 2

### 1. Practice Daily
- Code every day, even if just 30 minutes
- Type code yourself, don't copy-paste
- Experiment with modifications

### 2. Debug Like a Pro
```python
# Use print() to debug
print(f"Value of x: {x}")
print(f"Type: {type(x)}")

# Check conditions
if condition:
    print("Condition is True")
else:
    print("Condition is False")
```

### 3. Read Error Messages
```python
# TypeError: can only concatenate str (not "int") to str
# This means you're trying to add string + integer
# Solution: Convert one type to match the other
```

### 4. Use Meaningful Names
```python
# Bad
x = 25
y = x * 2

# Good
age = 25
age_in_months = age * 12
```

### 5. Comment Your Code
```python
# Calculate discount based on purchase amount
if amount > 100:
    discount = 0.2  # 20% discount
else:
    discount = 0.1  # 10% discount
```

---

## 📊 Week 1 Achievement Summary

You've learned:
- ✅ 4 data types (int, float, string, boolean)
- ✅ 16+ operators (arithmetic, comparison, logical)
- ✅ 20+ string methods
- ✅ 10+ list methods
- ✅ Dictionaries and sets
- ✅ Conditional statements
- ✅ Input/output operations
- ✅ Built 7 practice projects

**Lines of code written:** ~500+  
**Concepts mastered:** 50+  
**Projects completed:** 7  

---

## 🎯 Week 2 Preview

Next week you'll learn:
- **Day 8:** Loops - Part 1 (for loops)
- **Day 9:** Loops - Part 2 (while loops)
- **Day 10:** Functions - Basics
- **Day 11:** Functions - Advanced
- **Day 12:** Scope & Recursion
- **Day 13:** Error Handling
- **Day 14:** Week 2 Review & Banking System Project

---

## 💪 Motivation

> "The expert in anything was once a beginner." - Helen Hayes

You've taken the first major step in your Python journey. The fundamentals you learned this week are the foundation for everything else. Keep practicing, stay curious, and remember - every expert was once where you are now!

---

## 📚 Resources for Review

### Practice Platforms
- **Codewars**: Python kata for beginners
- **HackerRank**: Python challenges
- **LeetCode**: Easy problems
- **Exercism**: Python track with mentoring

### Documentation
- [Python Official Tutorial](https://docs.python.org/3/tutorial/)
- [W3Schools Python](https://www.w3schools.com/python/)
- [Real Python](https://realpython.com/)

### When You're Stuck
1. Read the error message carefully
2. Use print() to debug
3. Check Python documentation
4. Search on Stack Overflow
5. Ask in Python communities (Reddit r/learnpython)

---

## 🎉 Congratulations!

You've completed Week 1 of your Python learning journey! Take a moment to celebrate your progress. Tomorrow, you'll dive into loops and unlock even more programming power!

**Next:** Day 8 - Loops Part 1 (for loops)

---

**Keep Coding! 🐍**