# Day 3: Strings

## Overview
Today we'll master Python strings - one of the most commonly used data types. You'll learn string operations, methods, and formatting techniques.

---

## 1. Creating Strings

Strings are sequences of characters enclosed in quotes.

```python
# Single quotes
name = 'John'

# Double quotes
message = "Hello, World!"

# Triple quotes (for multi-line strings)
paragraph = """This is a
multi-line
string"""

# Empty string
empty = ""
```

### Single vs Double Quotes
Both work the same way, but choose based on content:

```python
# Use double quotes when string contains single quotes
sentence = "It's a beautiful day"

# Use single quotes when string contains double quotes
quote = 'He said "Hello"'

# Or use escape character
sentence = 'It\'s a beautiful day'
quote = "He said \"Hello\""
```

---

## 2. String Indexing and Slicing

Strings are indexed starting from 0.

### Indexing
```python
text = "Python"

# Positive indexing (left to right)
print(text[0])   # 'P'
print(text[1])   # 'y'
print(text[5])   # 'n'

# Negative indexing (right to left)
print(text[-1])  # 'n'
print(text[-2])  # 'o'
print(text[-6])  # 'P'
```

### Slicing
Extract a portion of a string using `[start:end:step]`

```python
text = "Python Programming"

# Basic slicing
print(text[0:6])    # 'Python'
print(text[7:18])   # 'Programming'

# Omitting start (starts from beginning)
print(text[:6])     # 'Python'

# Omitting end (goes to end)
print(text[7:])     # 'Programming'

# Negative indices
print(text[-11:])   # 'Programming'

# Step (every nth character)
print(text[::2])    # 'Pto rgamn'
print(text[::3])    # 'Ph ormn'

# Reverse a string
print(text[::-1])   # 'gnimmargorP nohtyP'
```

---

## 3. String Operations

### Concatenation
Joining strings together:

```python
first_name = "John"
last_name = "Doe"

# Using + operator
full_name = first_name + " " + last_name
print(full_name)  # 'John Doe'

# Using * for repetition
print("Ha" * 3)   # 'HaHaHa'
print("-" * 20)   # '--------------------'
```

### Length
```python
text = "Python"
print(len(text))  # 6
```

### Membership
Check if substring exists:

```python
sentence = "Python is awesome"

print("Python" in sentence)     # True
print("Java" in sentence)       # False
print("Java" not in sentence)   # True
```

---

## 4. String Methods

Python provides many built-in methods for string manipulation.

### Case Conversion
```python
text = "Python Programming"

print(text.upper())       # 'PYTHON PROGRAMMING'
print(text.lower())       # 'python programming'
print(text.capitalize())  # 'Python programming'
print(text.title())       # 'Python Programming'
print(text.swapcase())    # 'pYTHON pROGRAMMING'
```

### Searching and Checking
```python
text = "Python Programming"

# Find position of substring
print(text.find("Pro"))      # 7
print(text.find("Java"))     # -1 (not found)

# Check if string starts/ends with
print(text.startswith("Py")) # True
print(text.endswith("ing"))  # True

# Check string content
print("123".isdigit())       # True
print("abc".isalpha())       # True
print("abc123".isalnum())    # True
print("   ".isspace())       # True
```

### Trimming and Cleaning
```python
text = "   Hello World   "

print(text.strip())   # 'Hello World' (remove both ends)
print(text.lstrip())  # 'Hello World   ' (remove left)
print(text.rstrip())  # '   Hello World' (remove right)

# Remove specific characters
text = "***Hello***"
print(text.strip("*"))  # 'Hello'
```

### Replacing
```python
text = "I love Java"

# Replace substring
new_text = text.replace("Java", "Python")
print(new_text)  # 'I love Python'

# Replace all occurrences
text = "ha ha ha"
print(text.replace("ha", "he"))  # 'he he he'
```

### Splitting and Joining
```python
# Split string into list
sentence = "Python is awesome"
words = sentence.split()
print(words)  # ['Python', 'is', 'awesome']

# Split by specific separator
csv = "apple,banana,orange"
fruits = csv.split(",")
print(fruits)  # ['apple', 'banana', 'orange']

# Join list into string
words = ["Python", "is", "awesome"]
sentence = " ".join(words)
print(sentence)  # 'Python is awesome'

# Join with different separator
numbers = ["1", "2", "3", "4"]
result = "-".join(numbers)
print(result)  # '1-2-3-4'
```

### Counting
```python
text = "hello world"

print(text.count("l"))     # 3
print(text.count("o"))     # 2
print(text.count("xyz"))   # 0
```

---

## 5. String Formatting

### Method 1: f-strings (Recommended - Python 3.6+)
```python
name = "Alice"
age = 25
height = 5.6

# Basic f-string
print(f"My name is {name}")
print(f"I am {age} years old")

# Expressions inside f-strings
print(f"Next year I'll be {age + 1}")
print(f"Double my age is {age * 2}")

# Formatting numbers
price = 19.99
print(f"Price: ${price:.2f}")  # 'Price: $19.99'

# Alignment
print(f"{name:>10}")   # Right align (width 10)
print(f"{name:<10}")   # Left align
print(f"{name:^10}")   # Center align
```

### Method 2: format() method
```python
name = "Bob"
age = 30

print("My name is {} and I am {} years old".format(name, age))
print("My name is {0} and I am {1} years old".format(name, age))
print("My name is {n} and I am {a} years old".format(n=name, a=age))
```

### Method 3: % operator (Old style)
```python
name = "Charlie"
age = 35

print("My name is %s and I am %d years old" % (name, age))
```

---

## 6. Escape Characters

Special characters in strings:

| Escape Sequence | Description |
|-----------------|-------------|
| `\n` | New line |
| `\t` | Tab |
| `\\` | Backslash |
| `\'` | Single quote |
| `\"` | Double quote |

```python
# New line
print("Hello\nWorld")

# Tab
print("Name:\tJohn")

# Backslash
print("C:\\Users\\Python")

# Quotes
print("He said \"Hello\"")
print('It\'s a nice day')
```
## Additional Exercises

### Exercise 1: Palindrome Checker
Create a program that checks if a string is a palindrome (reads same forwards and backwards).

```python
# Example: "radar", "level", "madam" are palindromes
```

### Exercise 2: Word Counter
Create a program that counts how many times each word appears in a sentence.

### Exercise 3: Password Validator
Check if a password meets criteria:
- At least 8 characters
- Contains uppercase and lowercase
- Contains digits
- Contains special characters

### Exercise 4: Email Formatter
Extract username and domain from an email address.

```python
# Input: "john.doe@example.com"
# Output: Username: john.doe, Domain: example.com
```

---

## Quick Reference Table

| Method | Description | Example |
|--------|-------------|---------|
| `.upper()` | Convert to uppercase | `"hello".upper()` → `"HELLO"` |
| `.lower()` | Convert to lowercase | `"HELLO".lower()` → `"hello"` |
| `.strip()` | Remove whitespace | `" hi ".strip()` → `"hi"` |
| `.replace(old, new)` | Replace substring | `"hi".replace("i", "o")` → `"ho"` |
| `.split()` | Split into list | `"a b".split()` → `["a", "b"]` |
| `.join()` | Join list to string | `"-".join(["a","b"])` → `"a-b"` |
| `.find()` | Find substring | `"hello".find("ll")` → `2` |
| `.count()` | Count occurrences | `"hello".count("l")` → `2` |
| `.startswith()` | Check start | `"hello".startswith("he")` → `True` |
| `.endswith()` | Check end | `"hello".endswith("lo")` → `True` |

---

## Key Takeaways

✅ Strings are immutable (cannot be changed, only create new ones)  
✅ Use f-strings for modern string formatting  
✅ Indexing starts at 0, negative indices go backwards  
✅ Slicing syntax: `[start:end:step]`  
✅ Many built-in methods available for string manipulation  
✅ Use `.strip()` to remove unwanted whitespace  
✅ Use `.split()` and `.join()` for list-string conversions  

---

## Common Mistakes to Avoid

❌ Trying to modify strings directly (they're immutable)
```python
text = "hello"
text[0] = "H"  # ERROR!
```

✅ Create a new string instead:
```python
text = "hello"
text = "H" + text[1:]  # "Hello"
```

---

## Next Steps

Tomorrow (Day 4), we'll explore **Lists and Tuples** - powerful data structures for storing collections!

---

## Resources

- [Python String Methods Documentation](https://docs.python.org/3/library/stdtypes.html#string-methods)
- [Python String Formatting Guide](https://docs.python.org/3/tutorial/inputoutput.html#formatted-string-literals)

---

**Keep Coding! 🐍**