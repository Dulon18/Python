# Day 5: Dictionaries & Sets

## Overview
Today we'll learn about Dictionaries and Sets - two powerful data structures. Dictionaries store key-value pairs, while Sets store unique, unordered elements.

---

## 1. Dictionaries

Dictionaries store data as key-value pairs. Keys must be unique and immutable (strings, numbers, tuples).

### Creating Dictionaries

```python
# Empty dictionary
empty_dict = {}
empty_dict = dict()

# Dictionary with items
student = {
    "name": "John",
    "age": 20,
    "grade": "A",
    "courses": ["Math", "Physics"]
}

# Using dict() constructor
person = dict(name="Alice", age=25, city="NYC")

# From list of tuples
items = [("a", 1), ("b", 2), ("c", 3)]
my_dict = dict(items)
print(my_dict)  # {'a': 1, 'b': 2, 'c': 3}
```

### Accessing Dictionary Values

```python
student = {
    "name": "John",
    "age": 20,
    "grade": "A"
}

# Using square brackets
print(student["name"])   # 'John'
print(student["age"])    # 20

# Using get() method (safer - returns None if key doesn't exist)
print(student.get("name"))      # 'John'
print(student.get("email"))     # None
print(student.get("email", "Not found"))  # 'Not found' (default value)

# KeyError if key doesn't exist with []
# print(student["email"])  # ERROR!
```

### Adding and Modifying Items

```python
student = {"name": "John", "age": 20}

# Add new key-value pair
student["grade"] = "A"
print(student)  # {'name': 'John', 'age': 20, 'grade': 'A'}

# Modify existing value
student["age"] = 21
print(student)  # {'name': 'John', 'age': 21, 'grade': 'A'}

# Update multiple items
student.update({"grade": "A+", "city": "NYC"})
print(student)  # {'name': 'John', 'age': 21, 'grade': 'A+', 'city': 'NYC'}
```

### Removing Items

```python
student = {
    "name": "John",
    "age": 20,
    "grade": "A",
    "city": "NYC"
}

# pop() - Remove and return value
age = student.pop("age")
print(age)      # 20
print(student)  # {'name': 'John', 'grade': 'A', 'city': 'NYC'}

# popitem() - Remove and return last inserted item (Python 3.7+)
last_item = student.popitem()
print(last_item)  # ('city', 'NYC')

# del - Delete specific key
del student["grade"]
print(student)  # {'name': 'John'}

# clear() - Remove all items
student.clear()
print(student)  # {}
```

---

## 2. Dictionary Methods

### Getting Keys, Values, and Items

```python
student = {
    "name": "John",
    "age": 20,
    "grade": "A"
}

# keys() - Get all keys
keys = student.keys()
print(keys)        # dict_keys(['name', 'age', 'grade'])
print(list(keys))  # ['name', 'age', 'grade']

# values() - Get all values
values = student.values()
print(values)        # dict_values(['John', 20, 'A'])
print(list(values))  # ['John', 20, 'A']

# items() - Get all key-value pairs
items = student.items()
print(items)  # dict_items([('name', 'John'), ('age', 20), ('grade', 'A')])

# Convert to list
print(list(items))  # [('name', 'John'), ('age', 20), ('grade', 'A')]
```

### Checking for Keys

```python
student = {"name": "John", "age": 20}

# Check if key exists
print("name" in student)     # True
print("email" in student)    # False
print("age" not in student)  # False
```

### Copying Dictionaries

```python
original = {"a": 1, "b": 2}

# Shallow copy
copy1 = original.copy()
copy2 = dict(original)

# Modify copy (doesn't affect original)
copy1["c"] = 3
print(original)  # {'a': 1, 'b': 2}
print(copy1)     # {'a': 1, 'b': 2, 'c': 3}
```

### Dictionary Comprehension

```python
# Create dictionary from range
squares = {x: x**2 for x in range(6)}
print(squares)  # {0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

# With condition
even_squares = {x: x**2 for x in range(10) if x % 2 == 0}
print(even_squares)  # {0: 0, 2: 4, 4: 16, 6: 36, 8: 64}

# From two lists
keys = ["name", "age", "city"]
values = ["John", 20, "NYC"]
person = {k: v for k, v in zip(keys, values)}
print(person)  # {'name': 'John', 'age': 20, 'city': 'NYC'}
```

---

## 3. Looping Through Dictionaries

```python
student = {
    "name": "John",
    "age": 20,
    "grade": "A"
}

# Loop through keys (default)
for key in student:
    print(key)

# Loop through keys explicitly
for key in student.keys():
    print(key)

# Loop through values
for value in student.values():
    print(value)

# Loop through key-value pairs
for key, value in student.items():
    print(f"{key}: {value}")

# Output:
# name: John
# age: 20
# grade: A
```

---

## 4. Nested Dictionaries

```python
# Dictionary of dictionaries
students = {
    "student1": {
        "name": "John",
        "age": 20,
        "grades": [85, 90, 88]
    },
    "student2": {
        "name": "Alice",
        "age": 22,
        "grades": [92, 88, 95]
    }
}

# Accessing nested values
print(students["student1"]["name"])        # 'John'
print(students["student2"]["grades"][0])   # 92

# Loop through nested dictionary
for student_id, info in students.items():
    print(f"\n{student_id}:")
    for key, value in info.items():
        print(f"  {key}: {value}")
```

---

## 5. Sets

Sets are unordered collections of unique elements.

### Creating Sets

```python
# Empty set (cannot use {} - that's for dict)
empty_set = set()

# Set with items
fruits = {"apple", "banana", "orange"}
numbers = {1, 2, 3, 4, 5}

# From list (removes duplicates)
my_list = [1, 2, 2, 3, 3, 3, 4]
my_set = set(my_list)
print(my_set)  # {1, 2, 3, 4}

# From string
letters = set("hello")
print(letters)  # {'h', 'e', 'l', 'o'}
```

### Set Operations

```python
fruits = {"apple", "banana", "orange"}

# Add single item
fruits.add("mango")
print(fruits)  # {'apple', 'banana', 'orange', 'mango'}

# Add multiple items
fruits.update(["grape", "kiwi"])
print(fruits)  # {'apple', 'banana', 'orange', 'mango', 'grape', 'kiwi'}

# Remove item (raises error if not found)
fruits.remove("banana")
print(fruits)  # {'apple', 'orange', 'mango', 'grape', 'kiwi'}

# Discard (doesn't raise error if not found)
fruits.discard("banana")  # No error even though banana is not there

# Pop (removes random item)
item = fruits.pop()
print(f"Removed: {item}")

# Clear all items
fruits.clear()
print(fruits)  # set()
```

### Set Mathematical Operations

```python
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

# Union (all elements from both sets)
union = set1 | set2
union = set1.union(set2)
print(union)  # {1, 2, 3, 4, 5, 6, 7, 8}

# Intersection (common elements)
intersection = set1 & set2
intersection = set1.intersection(set2)
print(intersection)  # {4, 5}

# Difference (in set1 but not in set2)
diff = set1 - set2
diff = set1.difference(set2)
print(diff)  # {1, 2, 3}

# Symmetric difference (in either set but not both)
sym_diff = set1 ^ set2
sym_diff = set1.symmetric_difference(set2)
print(sym_diff)  # {1, 2, 3, 6, 7, 8}
```

### Set Relationships

```python
set1 = {1, 2, 3}
set2 = {1, 2, 3, 4, 5}

# Subset (all elements of set1 are in set2)
print(set1.issubset(set2))     # True
print(set1 <= set2)            # True

# Superset (set2 contains all elements of set1)
print(set2.issuperset(set1))   # True
print(set2 >= set1)            # True

# Disjoint (no common elements)
set3 = {6, 7, 8}
print(set1.isdisjoint(set3))   # True
```

### Set Comprehension

```python
# Create set of squares
squares = {x**2 for x in range(10)}
print(squares)  # {0, 1, 4, 9, 16, 25, 36, 49, 64, 81}

# With condition
even_squares = {x**2 for x in range(10) if x % 2 == 0}
print(even_squares)  # {0, 4, 16, 36, 64}
```

---

## 6. Frozen Sets

Immutable version of sets (can be used as dictionary keys).

```python
# Create frozen set
frozen = frozenset([1, 2, 3, 4])
print(frozen)  # frozenset({1, 2, 3, 4})

# Can't be modified
# frozen.add(5)  # ERROR!

# Can be used as dictionary key
my_dict = {frozen: "value"}
print(my_dict)  # {frozenset({1, 2, 3, 4}): 'value'}
```
---
## Additional Exercises

### Exercise 1: Word Frequency Counter
Create a program that counts word frequency in a sentence using dictionaries.

```python
# Input: "hello world hello python world"
# Output: {'hello': 2, 'world': 2, 'python': 1}
```

### Exercise 2: Student Grade Manager
Create a dictionary to store student names and their grades. Calculate:
- Average grade
- Highest and lowest grades
- Students above/below average

### Exercise 3: Set Operations Practice
Given two sets of student IDs:
- Find students enrolled in both courses
- Find students in only one course
- Find total unique students

### Exercise 4: Inventory System
Create an inventory system using nested dictionaries:
```python
inventory = {
    "item1": {"name": "Laptop", "price": 999, "quantity": 5},
    "item2": {"name": "Mouse", "price": 25, "quantity": 50}
}
```

---

## Quick Reference

### Dictionary Methods

```python
dict.get(key, default)      # Get value safely
dict.keys()                 # Get all keys
dict.values()               # Get all values
dict.items()                # Get all key-value pairs
dict.update(other)          # Update with another dict
dict.pop(key)               # Remove and return value
dict.popitem()              # Remove and return last item
dict.clear()                # Remove all items
dict.copy()                 # Create shallow copy
dict.setdefault(key, val)   # Get value or set default
```

### Set Methods

```python
set.add(item)               # Add single item
set.update(items)           # Add multiple items
set.remove(item)            # Remove (error if not found)
set.discard(item)           # Remove (no error)
set.pop()                   # Remove random item
set.clear()                 # Remove all items
set.union(other)            # Combine sets
set.intersection(other)     # Common elements
set.difference(other)       # Elements only in first
set.symmetric_difference()  # Elements in either, not both
```

---

## Dictionaries vs Sets

| Feature | Dictionary | Set |
|---------|-----------|-----|
| Structure | Key-value pairs | Unique values |
| Syntax | `{key: value}` | `{value}` |
| Ordered | Yes (Python 3.7+) | No |
| Duplicates | Keys must be unique | No duplicates |
| Mutable | Yes | Yes |
| Access | By key | Iteration only |
| Use Case | Store related data | Unique items, math ops |

---

## Key Takeaways

✅ **Dictionaries** store key-value pairs for structured data  
✅ **Sets** store unique elements for membership testing  
✅ Dictionary keys must be immutable (strings, numbers, tuples)  
✅ Sets automatically remove duplicates  
✅ Use `.get()` for safe dictionary access  
✅ Set operations: union (`|`), intersection (`&`), difference (`-`)  
✅ Dictionary/set comprehensions create efficient code  
✅ `frozenset` is an immutable set  

---

## Common Mistakes to Avoid

❌ **Using mutable types as dictionary keys**
```python
my_dict = {[1, 2]: "value"}  # ERROR! Lists can't be keys
```

❌ **Confusing empty dict and set**
```python
empty = {}        # This is a dict!
empty = set()     # This is a set!
```

❌ **Forgetting sets are unordered**
```python
my_set = {3, 1, 2}
print(my_set[0])  # ERROR! Sets don't support indexing
```

---

## Next Steps

Tomorrow (Day 6), we'll learn about **Conditional Statements** - making decisions in your code with if, elif, and else!

---

## Resources

- [Python Dictionaries Documentation](https://docs.python.org/3/tutorial/datastructures.html#dictionaries)
- [Python Sets Documentation](https://docs.python.org/3/tutorial/datastructures.html#sets)

---

**Master the Data! 🐍**