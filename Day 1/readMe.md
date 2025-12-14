# Variables and Data Types in Python

What is a Variable?

A variable is like a container that stores data. You can name it and use it throughout your program.

    name = "John"  # This is a variable storing a string
    age = 25       # This is a variable storing an integer


# Python Data Types

Python has several built-in data types that let you store and work with different kinds of information. Here are the main ones:

## Basic Data Types

**Integers (`int`)** - Whole numbers without decimals
```python
age = 25
count = -10
```

**Floats (`float`)** - Numbers with decimal points
```python
price = 19.99
temperature = -3.5
```

**Strings (`str`)** - Text enclosed in quotes
```python
name = "Alice"
message = 'Hello, world!'
```

**Booleans (`bool`)** - True or False values
```python
is_valid = True
is_empty = False
```

## Collection Data Types

**Lists (`list`)** - Ordered, changeable collections
```python
fruits = ["apple", "banana", "orange"]
numbers = [1, 2, 3, 4, 5]
```

**Tuples (`tuple`)** - Ordered, unchangeable collections
```python
coordinates = (10, 20)
rgb = (255, 0, 128)
```

**Dictionaries (`dict`)** - Key-value pairs
```python
person = {"name": "Bob", "age": 30, "city": "NYC"}
```

**Sets (`set`)** - Unordered collections of unique items
```python
unique_numbers = {1, 2, 3, 4, 5}
```

## Special Type

**None (`NoneType`)** - Represents the absence of a value
```python
result = None
```

You can check any variable's type using `type()`:
```python
type(25)  # <class 'int'>
type("hello")  # <class 'str'>
```
