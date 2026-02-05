# Day 17: Object-Oriented Programming - Part 1

## Overview
Today we'll learn Object-Oriented Programming (OOP) - a programming paradigm that organizes code around objects and classes. This is fundamental to modern software development!

---

## 1. What is OOP?

### Key Concepts

**Object-Oriented Programming** organizes code into **objects** that contain both data (attributes) and behavior (methods).

**Four Pillars of OOP:**
1. **Encapsulation** - Bundling data and methods
2. **Abstraction** - Hiding complexity
3. **Inheritance** - Reusing code (Day 18)
4. **Polymorphism** - Multiple forms (Day 18)

### Why Use OOP?

✅ **Organization** - Code is structured and logical  
✅ **Reusability** - Create once, use many times  
✅ **Maintainability** - Easier to update and debug  
✅ **Modularity** - Break complex problems into parts  
✅ **Real-world modeling** - Represents real entities  

---

## 2. Classes and Objects

### Understanding Classes

A **class** is a blueprint for creating objects. An **object** is an instance of a class.

**Analogy:**
- **Class** = Cookie cutter (blueprint)
- **Object** = Cookie (instance)

### Basic Class Syntax

```python
class Dog:
    """A simple Dog class."""
    pass

# Create objects (instances)
dog1 = Dog()
dog2 = Dog()

print(type(dog1))  # <class '__main__.Dog'>
```

---

## 3. Attributes (Data)

### Instance Attributes

Attributes are variables that belong to an object.

```python
class Dog:
    """Dog with attributes."""
    
    def __init__(self, name, age):
        """
        Initialize a Dog.
        
        Args:
            name: Dog's name
            age: Dog's age
        """
        self.name = name  # Instance attribute
        self.age = age    # Instance attribute

# Create dogs
dog1 = Dog("Buddy", 3)
dog2 = Dog("Max", 5)

# Access attributes
print(dog1.name)  # Buddy
print(dog2.age)   # 5

# Modify attributes
dog1.age = 4
print(dog1.age)   # 4
```

### The `__init__` Method (Constructor)

The `__init__` method is called automatically when creating an object.

```python
class Person:
    def __init__(self, name, age):
        """Initialize Person."""
        print(f"Creating Person: {name}")
        self.name = name
        self.age = age

person = Person("Alice", 25)
# Output: Creating Person: Alice
```

### Understanding `self`

`self` refers to the current instance of the class.

```python
class Counter:
    def __init__(self):
        self.count = 0  # self.count belongs to this instance
    
    def increment(self):
        self.count += 1  # Access this instance's count

counter1 = Counter()
counter2 = Counter()

counter1.increment()
counter1.increment()

print(counter1.count)  # 2
print(counter2.count)  # 0 (separate instance)
```

---

## 4. Methods (Behavior)

### Instance Methods

Methods are functions that belong to a class.

```python
class Rectangle:
    def __init__(self, width, height):
        """Initialize Rectangle."""
        self.width = width
        self.height = height
    
    def area(self):
        """Calculate area."""
        return self.width * self.height
    
    def perimeter(self):
        """Calculate perimeter."""
        return 2 * (self.width + self.height)
    
    def is_square(self):
        """Check if rectangle is a square."""
        return self.width == self.height

# Create and use
rect = Rectangle(5, 10)
print(rect.area())       # 50
print(rect.perimeter())  # 30
print(rect.is_square())  # False

square = Rectangle(5, 5)
print(square.is_square())  # True
```

### Methods with Parameters

```python
class BankAccount:
    def __init__(self, owner, balance=0):
        """Initialize account."""
        self.owner = owner
        self.balance = balance
    
    def deposit(self, amount):
        """Deposit money."""
        if amount > 0:
            self.balance += amount
            print(f"Deposited ${amount}. New balance: ${self.balance}")
        else:
            print("Amount must be positive!")
    
    def withdraw(self, amount):
        """Withdraw money."""
        if amount > self.balance:
            print("Insufficient funds!")
        elif amount > 0:
            self.balance -= amount
            print(f"Withdrew ${amount}. New balance: ${self.balance}")
        else:
            print("Amount must be positive!")

# Use the account
account = BankAccount("Alice", 1000)
account.deposit(500)   # Deposited $500. New balance: $1500
account.withdraw(200)  # Withdrew $200. New balance: $1300
```

---

## 5. Class Attributes

Class attributes are shared by all instances.

```python
class Dog:
    # Class attribute (shared by all dogs)
    species = "Canis familiaris"
    
    def __init__(self, name, age):
        # Instance attributes (unique to each dog)
        self.name = name
        self.age = age

dog1 = Dog("Buddy", 3)
dog2 = Dog("Max", 5)

print(dog1.species)  # Canis familiaris
print(dog2.species)  # Canis familiaris

# Class attribute is shared
Dog.species = "Canis lupus"
print(dog1.species)  # Canis lupus
print(dog2.species)  # Canis lupus
```

### Class Attributes vs Instance Attributes

```python
class Counter:
    # Class attribute - shared
    total_instances = 0
    
    def __init__(self, name):
        # Instance attribute - unique
        self.name = name
        self.count = 0
        
        # Increment class attribute
        Counter.total_instances += 1

counter1 = Counter("C1")
counter2 = Counter("C2")
counter3 = Counter("C3")

print(Counter.total_instances)  # 3
```

---

## 6. Special Methods (Magic Methods)

Special methods have double underscores (dunder methods).

### `__str__` and `__repr__`

```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def __str__(self):
        """User-friendly string representation."""
        return f"{self.name}, {self.age} years old"
    
    def __repr__(self):
        """Developer-friendly representation."""
        return f"Person('{self.name}', {self.age})"

person = Person("Alice", 25)
print(str(person))   # Alice, 25 years old
print(repr(person))  # Person('Alice', 25)
print(person)        # Uses __str__
```

### Comparison Methods

```python
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __eq__(self, other):
        """Check equality."""
        return self.x == other.x and self.y == other.y
    
    def __lt__(self, other):
        """Less than comparison."""
        return (self.x ** 2 + self.y ** 2) < (other.x ** 2 + other.y ** 2)

p1 = Point(1, 2)
p2 = Point(1, 2)
p3 = Point(3, 4)

print(p1 == p2)  # True
print(p1 < p3)   # True
```

### Arithmetic Methods

```python
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __add__(self, other):
        """Add two vectors."""
        return Vector(self.x + other.x, self.y + other.y)
    
    def __mul__(self, scalar):
        """Multiply vector by scalar."""
        return Vector(self.x * scalar, self.y * scalar)
    
    def __str__(self):
        return f"Vector({self.x}, {self.y})"

v1 = Vector(1, 2)
v2 = Vector(3, 4)

v3 = v1 + v2
print(v3)  # Vector(4, 6)

v4 = v1 * 3
print(v4)  # Vector(3, 6)
```

### Container Methods

```python
class Playlist:
    def __init__(self):
        self.songs = []
    
    def __len__(self):
        """Return number of songs."""
        return len(self.songs)
    
    def __getitem__(self, index):
        """Get song by index."""
        return self.songs[index]
    
    def __contains__(self, song):
        """Check if song in playlist."""
        return song in self.songs
    
    def add_song(self, song):
        """Add song to playlist."""
        self.songs.append(song)

playlist = Playlist()
playlist.add_song("Song 1")
playlist.add_song("Song 2")
playlist.add_song("Song 3")

print(len(playlist))           # 3
print(playlist[0])             # Song 1
print("Song 2" in playlist)    # True
```

---

## 7. Encapsulation

### Private Attributes

Use single underscore `_` for "protected" and double underscore `__` for "private".

```python
class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner           # Public
        self._account_number = "123" # Protected (convention)
        self.__balance = balance     # Private (name mangling)
    
    def get_balance(self):
        """Public method to access private attribute."""
        return self.__balance
    
    def deposit(self, amount):
        """Public method to modify private attribute."""
        if amount > 0:
            self.__balance += amount

account = BankAccount("Alice", 1000)
print(account.owner)           # Alice (public)
print(account._account_number) # 123 (protected - still accessible)
# print(account.__balance)     # Error! Private
print(account.get_balance())   # 1000 (via public method)
```

### Property Decorators

```python
class Temperature:
    def __init__(self, celsius):
        self._celsius = celsius
    
    @property
    def celsius(self):
        """Get temperature in Celsius."""
        return self._celsius
    
    @celsius.setter
    def celsius(self, value):
        """Set temperature in Celsius."""
        if value < -273.15:
            raise ValueError("Temperature below absolute zero!")
        self._celsius = value
    
    @property
    def fahrenheit(self):
        """Get temperature in Fahrenheit."""
        return self._celsius * 9/5 + 32
    
    @fahrenheit.setter
    def fahrenheit(self, value):
        """Set temperature in Fahrenheit."""
        self.celsius = (value - 32) * 5/9

temp = Temperature(25)
print(temp.celsius)      # 25
print(temp.fahrenheit)   # 77.0

temp.fahrenheit = 100
print(temp.celsius)      # 37.77...
```

---

## 8. Class Methods and Static Methods

### Class Methods

Use `@classmethod` decorator. First parameter is `cls` (the class itself).

```python
class Date:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day
    
    @classmethod
    def from_string(cls, date_string):
        """Create Date from string (YYYY-MM-DD)."""
        year, month, day = map(int, date_string.split('-'))
        return cls(year, month, day)
    
    @classmethod
    def today(cls):
        """Create Date with today's date."""
        import datetime
        today = datetime.date.today()
        return cls(today.year, today.month, today.day)
    
    def __str__(self):
        return f"{self.year}-{self.month:02d}-{self.day:02d}"

# Regular constructor
date1 = Date(2024, 1, 31)

# Class method constructors
date2 = Date.from_string("2024-01-31")
date3 = Date.today()

print(date1)  # 2024-01-31
print(date2)  # 2024-01-31
```

### Static Methods

Use `@staticmethod` decorator. No automatic first parameter.

```python
class MathUtils:
    @staticmethod
    def is_even(n):
        """Check if number is even."""
        return n % 2 == 0
    
    @staticmethod
    def is_prime(n):
        """Check if number is prime."""
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

# Call without creating instance
print(MathUtils.is_even(4))   # True
print(MathUtils.is_prime(7))  # True
```

---

## 9. Practical Examples

### Example 1: Student Class

```python
class Student:
    """Represents a student."""
    
    def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id
        self.grades = []
    
    def add_grade(self, grade):
        """Add a grade."""
        if 0 <= grade <= 100:
            self.grades.append(grade)
        else:
            print("Grade must be 0-100!")
    
    def get_average(self):
        """Calculate average grade."""
        if not self.grades:
            return 0
        return sum(self.grades) / len(self.grades)
    
    def is_passing(self):
        """Check if student is passing (>=60)."""
        return self.get_average() >= 60
    
    def __str__(self):
        return f"Student({self.name}, ID: {self.student_id})"

# Usage
student = Student("Alice", "S001")
student.add_grade(85)
student.add_grade(90)
student.add_grade(78)

print(student)
print(f"Average: {student.get_average():.2f}")
print(f"Passing: {student.is_passing()}")
```

### Example 2: Shopping Cart

```python
class ShoppingCart:
    """Shopping cart for e-commerce."""
    
    def __init__(self):
        self.items = []
    
    def add_item(self, name, price, quantity=1):
        """Add item to cart."""
        self.items.append({
            "name": name,
            "price": price,
            "quantity": quantity
        })
        print(f"Added {quantity}x {name}")
    
    def remove_item(self, name):
        """Remove item from cart."""
        self.items = [item for item in self.items if item["name"] != name]
        print(f"Removed {name}")
    
    def get_total(self):
        """Calculate total cost."""
        return sum(item["price"] * item["quantity"] for item in self.items)
    
    def get_item_count(self):
        """Get total number of items."""
        return sum(item["quantity"] for item in self.items)
    
    def display_cart(self):
        """Display cart contents."""
        if not self.items:
            print("Cart is empty")
            return
        
        print("\n--- Shopping Cart ---")
        for item in self.items:
            total = item["price"] * item["quantity"]
            print(f"{item['name']}: ${item['price']:.2f} x {item['quantity']} = ${total:.2f}")
        print(f"\nTotal: ${self.get_total():.2f}")
        print(f"Items: {self.get_item_count()}")

# Usage
cart = ShoppingCart()
cart.add_item("Laptop", 999.99)
cart.add_item("Mouse", 25.50, 2)
cart.add_item("Keyboard", 75.00)
cart.display_cart()
```

### Example 3: Book Class

```python
class Book:
    """Represents a book."""
    
    total_books = 0  # Class attribute
    
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages
        self.current_page = 0
        self.is_finished = False
        
        Book.total_books += 1
    
    def read(self, pages):
        """Read a number of pages."""
        if self.is_finished:
            print("Already finished this book!")
            return
        
        self.current_page += pages
        
        if self.current_page >= self.pages:
            self.current_page = self.pages
            self.is_finished = True
            print(f"Finished reading '{self.title}'!")
        else:
            progress = (self.current_page / self.pages) * 100
            print(f"Progress: {progress:.1f}% ({self.current_page}/{self.pages} pages)")
    
    def get_progress(self):
        """Get reading progress percentage."""
        return (self.current_page / self.pages) * 100
    
    def __str__(self):
        return f"'{self.title}' by {self.author}"
    
    def __repr__(self):
        return f"Book('{self.title}', '{self.author}', {self.pages})"

# Usage
book = Book("Python Programming", "John Doe", 300)
print(book)
book.read(100)
book.read(150)
book.read(100)
```

---

## Practice Exercises

### Exercise 1: Car Class
Create a `Car` class with:
- Attributes: make, model, year, mileage
- Methods: drive(), display_info()

### Exercise 2: Circle Class
Create a `Circle` class with:
- Attribute: radius
- Methods: area(), circumference(), diameter()
- Use math.pi

### Exercise 3: TodoList Class
Create a `TodoList` class with:
- Methods: add_task(), remove_task(), mark_complete()
- Display all tasks with status

### Exercise 4: Employee Class
Create an `Employee` class with:
- Attributes: name, position, salary
- Methods: give_raise(), display_info()
- Class attribute: company_name

### Exercise 5: Dice Class
Create a `Dice` class with:
- Attribute: sides (default 6)
- Method: roll() returns random number
- Track roll history

---

## Practice Project

**See:** `day17_oop_library.py` for the complete Library Management System project.

The project includes:
- Multiple classes (Book, Member, Library)
- Encapsulation and properties
- Class and instance methods
- Special methods
- Real-world application

---

## Quick Reference

### Class Definition
```python
class MyClass:
    class_attr = "shared"  # Class attribute
    
    def __init__(self, value):
        self.instance_attr = value  # Instance attribute
    
    def method(self):
        return self.instance_attr
    
    @classmethod
    def class_method(cls):
        return cls.class_attr
    
    @staticmethod
    def static_method():
        return "static"
```

### Creating Objects
```python
obj = MyClass("value")
obj.method()
MyClass.class_method()
MyClass.static_method()
```

### Special Methods
```python
__init__     # Constructor
__str__      # str(obj)
__repr__     # repr(obj)
__len__      # len(obj)
__eq__       # obj1 == obj2
__lt__       # obj1 < obj2
__add__      # obj1 + obj2
__getitem__  # obj[key]
```

---

## Key Takeaways

✅ Classes are blueprints, objects are instances  
✅ `__init__` initializes new objects  
✅ `self` refers to the current instance  
✅ Instance attributes are unique per object  
✅ Class attributes are shared by all instances  
✅ Methods are functions inside classes  
✅ Use `@property` for controlled access  
✅ `@classmethod` and `@staticmethod` for utilities  
✅ Special methods customize behavior  
✅ Encapsulation protects data  

---

## Common Mistakes to Avoid

❌ **Forgetting self parameter**
```python
class MyClass:
    def method():  # Wrong! Missing self
        pass
```

❌ **Not using self to access attributes**
```python
class MyClass:
    def __init__(self, value):
        value = value  # Wrong! Should be self.value
```

❌ **Modifying class attributes incorrectly**
```python
class MyClass:
    count = 0
    
    def increment(self):
        count += 1  # Wrong! Should be MyClass.count or self.count
```

---

## Next Steps

Tomorrow (Day 18), we'll learn **OOP - Part 2** covering inheritance, polymorphism, and advanced OOP concepts!

---

## Resources

- [Python Classes Documentation](https://docs.python.org/3/tutorial/classes.html)
- [OOP in Python](https://realpython.com/python3-object-oriented-programming/)

---

**Think in Objects! 🐍**
