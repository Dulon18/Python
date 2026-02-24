#  Day 24: Data Structures & Collections in Python

> **Week 4 — Advanced Topics** | 30-Day Python Learning Plan

Data structures are ways of **organizing and storing data** so it can be accessed and modified efficiently. Today we cover stacks, queues, the powerful `collections` module, and basic time complexity.

---

## 📌 Part A — Stacks

A **Stack** follows **LIFO** — Last In, First Out.

Think of a stack of plates 🍽️ — you always add and remove from the top.

```
Add →  [ A ]  ← Remove
       [ B ]
       [ C ]
```

### Using a List as a Stack

```python
stack = []

# Push — add to top
stack.append("a")
stack.append("b")
stack.append("c")
print(stack)  # ['a', 'b', 'c']

# Pop — remove from top (LIFO)
print(stack.pop())  # c
print(stack.pop())  # b
print(stack)        # ['a']

# Peek — look at top without removing
print(stack[-1])    # a

# Check if empty
print(len(stack) == 0)  # False
```

### Real World Stack Uses
- **Undo/Redo** in text editors
- **Browser back button** history
- **Function call stack** in Python itself
- **Bracket matching** in code editors

---

### Stack Class (OOP way)

```python
class Stack:
    def __init__(self):
        self._items = []

    def push(self, item):
        self._items.append(item)

    def pop(self):
        if self.is_empty():
            raise IndexError("Stack is empty!")
        return self._items.pop()

    def peek(self):
        if self.is_empty():
            raise IndexError("Stack is empty!")
        return self._items[-1]

    def is_empty(self):
        return len(self._items) == 0

    def size(self):
        return len(self._items)

    def __str__(self):
        return str(self._items)


# Usage
s = Stack()
s.push(10)
s.push(20)
s.push(30)
print(s)         # [10, 20, 30]
print(s.peek())  # 30
print(s.pop())   # 30
print(s.size())  # 2
```

---

## 📌 Part B — Queues

A **Queue** follows **FIFO** — First In, First Out.

Think of a line at a shop 🏪 — first person in line gets served first.

```
Add →  [ A ][ B ][ C ]  → Remove
```

### Using `deque` for a Queue

Never use a plain list for queues — removing from the front (`list.pop(0)`) is slow O(n). Use `deque` instead which is O(1).

```python
from collections import deque

queue = deque()

# Enqueue — add to back
queue.append("first")
queue.append("second")
queue.append("third")
print(queue)  # deque(['first', 'second', 'third'])

# Dequeue — remove from front (FIFO)
print(queue.popleft())  # first
print(queue.popleft())  # second
print(queue)            # deque(['third'])

# Peek front
print(queue[0])   # third

# Check if empty
print(len(queue) == 0)  # False
```

### Real World Queue Uses
- **Print spooler** — documents printed in order
- **Task scheduling** — CPU processes tasks in order
- **Message queues** — Emails, notifications
- **BFS** — Breadth First Search in graphs

---

### Queue Class (OOP way)

```python
from collections import deque

class Queue:
    def __init__(self):
        self._items = deque()

    def enqueue(self, item):
        self._items.append(item)

    def dequeue(self):
        if self.is_empty():
            raise IndexError("Queue is empty!")
        return self._items.popleft()

    def peek(self):
        if self.is_empty():
            raise IndexError("Queue is empty!")
        return self._items[0]

    def is_empty(self):
        return len(self._items) == 0

    def size(self):
        return len(self._items)

    def __str__(self):
        return str(list(self._items))


# Usage
q = Queue()
q.enqueue("Ali")
q.enqueue("Sara")
q.enqueue("John")
print(q)           # ['Ali', 'Sara', 'John']
print(q.dequeue()) # Ali  — first in, first out
print(q.size())    # 2
```

---

## 📌 Part C — The `collections` Module

Python's `collections` module provides **specialized data structures** beyond the built-in list, dict, and tuple.

---

### 1. `Counter` — Count occurrences automatically

```python
from collections import Counter

# Count words
words = ["apple", "banana", "apple", "cherry", "banana", "apple"]
count = Counter(words)

print(count)                  # Counter({'apple': 3, 'banana': 2, 'cherry': 1})
print(count["apple"])         # 3
print(count.most_common(2))   # [('apple', 3), ('banana', 2)]
print(count.most_common()[:-3:-1])  # 2 least common

# Count characters in a string
char_count = Counter("mississippi")
print(char_count)  # Counter({'i': 4, 's': 4, 'p': 2, 'm': 1})

# Arithmetic with counters
a = Counter(["cat", "dog", "cat"])
b = Counter(["dog", "fish"])
print(a + b)  # Counter({'cat': 2, 'dog': 2, 'fish': 1})
print(a - b)  # Counter({'cat': 2})
```

---

### 2. `defaultdict` — Dictionary that never throws KeyError

```python
from collections import defaultdict

# Regular dict — throws KeyError for missing keys
regular = {}
# regular["missing"]  # KeyError!

# defaultdict — returns a default value for missing keys
scores = defaultdict(list)  # default is an empty list
scores["Ali"].append(90)
scores["Ali"].append(85)
scores["Sara"].append(95)
print(scores)
# defaultdict(<class 'list'>, {'Ali': [90, 85], 'Sara': [95]})

# defaultdict with int — perfect for counting
word_count = defaultdict(int)  # default is 0
for word in ["hi", "hello", "hi", "bye", "hi"]:
    word_count[word] += 1
print(dict(word_count))  # {'hi': 3, 'hello': 1, 'bye': 1}

# defaultdict with set
groups = defaultdict(set)
groups["fruits"].add("apple")
groups["fruits"].add("banana")
groups["veggies"].add("carrot")
print(dict(groups))
# {'fruits': {'apple', 'banana'}, 'veggies': {'carrot'}}
```

---

### 3. `namedtuple` — Tuple with named fields

```python
from collections import namedtuple

# Like a lightweight class
Point = namedtuple("Point", ["x", "y"])
p = Point(10, 20)
print(p.x)     # 10
print(p.y)     # 20
print(p)       # Point(x=10, y=20)

# Unpack like a regular tuple
x, y = p
print(x, y)   # 10 20

# Real world example
Student = namedtuple("Student", ["name", "age", "grade"])
students = [
    Student("Ali",  20, "A"),
    Student("Sara", 22, "B"),
    Student("John", 21, "A+"),
]

for s in students:
    print(f"{s.name} | Age: {s.age} | Grade: {s.grade}")

# namedtuple is immutable — can't change values
# p.x = 99  # AttributeError!

# Convert to dict
print(p._asdict())  # {'x': 10, 'y': 20}
```

---

### 4. `deque` — Double-ended Queue

```python
from collections import deque

d = deque([1, 2, 3, 4, 5])

# Add to both ends
d.append(6)       # add right
d.appendleft(0)   # add left
print(d)          # deque([0, 1, 2, 3, 4, 5, 6])

# Remove from both ends
d.pop()           # remove right
d.popleft()       # remove left
print(d)          # deque([1, 2, 3, 4, 5])

# Rotate — shift all elements
d.rotate(2)       # rotate right by 2
print(d)          # deque([4, 5, 1, 2, 3])

d.rotate(-2)      # rotate left by 2
print(d)          # deque([1, 2, 3, 4, 5])

# Fixed-size deque — automatically discards old items
recent = deque(maxlen=3)
for i in range(6):
    recent.append(i)
    print(list(recent))
# [0]
# [0, 1]
# [0, 1, 2]
# [1, 2, 3]  ← 0 dropped
# [2, 3, 4]  ← 1 dropped
# [3, 4, 5]  ← 2 dropped
```

---

### 5. `OrderedDict` — Dictionary that remembers insertion order

```python
from collections import OrderedDict

# In Python 3.7+ regular dicts maintain order too
# But OrderedDict has extra features

od = OrderedDict()
od["banana"] = 3
od["apple"] = 5
od["cherry"] = 1

print(od)
# OrderedDict([('banana', 3), ('apple', 5), ('cherry', 1)])

# Move item to end or beginning
od.move_to_end("banana")        # move to end
od.move_to_end("cherry", last=False)  # move to beginning
print(list(od.keys()))  # ['cherry', 'apple', 'banana']
```

---

## 📌 Part D — Time Complexity Basics

Time complexity describes **how fast an operation runs** as data grows. Written as **Big O notation**.

| Complexity | Name | Example |
|---|---|---|
| O(1) | Constant | Dictionary lookup, list append |
| O(log n) | Logarithmic | Binary search |
| O(n) | Linear | Loop through a list |
| O(n²) | Quadratic | Nested loops |
| O(2ⁿ) | Exponential | Recursive fibonacci (naive) |

---

### List vs Dictionary — Speed Comparison

```python
# List search — O(n) — checks every element
numbers = list(range(1000000))
print(999999 in numbers)  # slow for large lists

# Dictionary search — O(1) — instant lookup
number_dict = {i: True for i in range(1000000)}
print(999999 in number_dict)  # always fast regardless of size
```

### Common Operations and Their Complexity

```python
my_list = [1, 2, 3, 4, 5]
my_dict = {"a": 1, "b": 2}

# O(1) — instant
my_list.append(6)     # add to end
my_list[-1]           # access last item
my_dict["a"]          # access by key
my_dict["c"] = 3      # insert key

# O(n) — gets slower as data grows
my_list[0]            # access first (fine)
my_list.pop(0)        # remove from front (slow! shifts all elements)
3 in my_list          # search in list
my_list.insert(0, 0)  # insert at front (slow!)

# Use deque for fast front operations
from collections import deque
d = deque([1, 2, 3])
d.popleft()   # O(1) — fast!
d.appendleft(0)  # O(1) — fast!
```

---

## 🛠️ Practice Project — Stack-Based Calculator

Evaluates **postfix expressions** (also called Reverse Polish Notation) using a stack.

In postfix: `3 4 +` means `3 + 4 = 7`, and `3 4 + 2 *` means `(3 + 4) * 2 = 14`

```python
def stack_calculator(expression):
    """
    Evaluate a postfix (RPN) expression using a stack.

    Examples:
        "3 4 +"       → 7       (3 + 4)
        "3 4 + 2 *"   → 14      (3 + 4) * 2
        "10 2 /"      → 5       10 / 2
    """
    stack = []
    tokens = expression.split()
    operators = {'+', '-', '*', '/'}

    for token in tokens:
        if token not in operators:
            stack.append(float(token))
        else:
            if len(stack) < 2:
                print("Error: Not enough operands!")
                return None
            b = stack.pop()
            a = stack.pop()

            if token == '+':
                stack.append(a + b)
            elif token == '-':
                stack.append(a - b)
            elif token == '*':
                stack.append(a * b)
            elif token == '/':
                if b == 0:
                    print("Error: Division by zero!")
                    return None
                stack.append(a / b)

    if len(stack) != 1:
        print("Error: Invalid expression!")
        return None

    return stack[0]


# --- Menu ---
print("=" * 45)
print("   STACK-BASED POSTFIX CALCULATOR")
print("=" * 45)
print("Enter expression in postfix (RPN) format.")
print("Example: '3 4 +' means 3 + 4 = 7")
print("         '5 1 2 + 4 * + 3 -' = 14")
print("Type 'quit' to exit.\n")

while True:
    expr = input("Enter expression: ").strip()
    if expr.lower() == "quit":
        print("Goodbye!")
        break
    result = stack_calculator(expr)
    if result is not None:
        print(f"Result: {result}\n")


# Test cases
print("\n--- Test Cases ---")
tests = [
    ("3 4 +",           7),
    ("3 4 + 2 *",       14),
    ("10 2 /",          5),
    ("5 1 2 + 4 * + 3 -", 14),
    ("2 3 4 * +",       14),
]

for expr, expected in tests:
    result = stack_calculator(expr)
    status = "✓" if result == expected else "✗"
    print(f"{status} '{expr}' = {result} (expected {expected})")
```

---

## 📝 Quick Summary

| Structure | Type | Add | Remove | Use When |
|---|---|---|---|---|
| `list` as Stack | LIFO | `append()` | `pop()` | Undo, back button |
| `deque` as Queue | FIFO | `append()` | `popleft()` | Task scheduling, BFS |
| `Counter` | Dict | auto | — | Counting occurrences |
| `defaultdict` | Dict | auto default | — | Grouping, counting |
| `namedtuple` | Tuple | at creation | immutable | Lightweight records |
| `deque` | Double-ended | both ends | both ends | Sliding window, rotation |
| `OrderedDict` | Dict | ordered | — | Order-sensitive dicts |

---

## 🔗 Resources

- [Python `collections` Module Docs](https://docs.python.org/3/library/collections.html)
- [Big O Cheat Sheet](https://www.bigocheatsheet.com)
- [Real Python — Stacks & Queues](https://realpython.com/queue-in-python/)

---

> 📅 Part of the **30-Day Python Learning Plan**
> Previous: [Day 23 - Decorators & Generators](#) | Next: [Day 25 - Working with JSON](#)
