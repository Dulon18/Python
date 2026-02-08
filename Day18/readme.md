# Day 18: OOP - Part 2 (Inheritance & Polymorphism)

## Overview
Today we'll master inheritance and polymorphism - two powerful OOP concepts that enable code reuse and flexibility. These are the final two pillars of OOP!

---

## 1. Inheritance Basics

### What is Inheritance?

**Inheritance** allows a class (child/subclass) to inherit attributes and methods from another class (parent/superclass).

**Benefits:**
✅ **Code reuse** - Don't repeat yourself  
✅ **Logical hierarchy** - Model real relationships  
✅ **Easier maintenance** - Update in one place  
✅ **Extensibility** - Add features without changing parent  

### Basic Syntax

```python
class Parent:
    """Parent class."""
    def __init__(self, name):
        self.name = name
    
    def greet(self):
        return f"Hello, I'm {self.name}"

class Child(Parent):  # Child inherits from Parent
    """Child class."""
    pass

# Create child object
child = Child("Alice")
print(child.greet())  # Hello, I'm Alice (inherited method!)
```

---

## 2. Simple Inheritance Example

### Animal Hierarchy

```python
class Animal:
    """Base animal class."""
    
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def speak(self):
        return "Some generic sound"
    
    def info(self):
        return f"{self.name} is {self.age} years old"

class Dog(Animal):
    """Dog class inherits from Animal."""
    
    def speak(self):
        return "Woof! Woof!"
    
    def fetch(self):
        return f"{self.name} is fetching the ball!"

class Cat(Animal):
    """Cat class inherits from Animal."""
    
    def speak(self):
        return "Meow!"
    
    def climb(self):
        return f"{self.name} is climbing a tree!"

# Usage
dog = Dog("Buddy", 3)
cat = Cat("Whiskers", 2)

print(dog.info())    # Inherited method
print(dog.speak())   # Overridden method
print(dog.fetch())   # New method

print(cat.info())    # Inherited method
print(cat.speak())   # Overridden method
print(cat.climb())   # New method
```

---

## 3. Method Overriding

### Overriding Parent Methods

Child classes can provide their own implementation of parent methods.

```python
class Vehicle:
    """Base vehicle class."""
    
    def __init__(self, brand):
        self.brand = brand
    
    def start(self):
        return f"{self.brand} vehicle is starting..."
    
    def stop(self):
        return f"{self.brand} vehicle is stopping..."

class Car(Vehicle):
    """Car class with specific behavior."""
    
    def start(self):
        # Override with car-specific behavior
        return f"{self.brand} car engine started! Vroom!"

class Bicycle(Vehicle):
    """Bicycle class with specific behavior."""
    
    def start(self):
        # Override with bicycle-specific behavior
        return f"Pedaling the {self.brand} bicycle!"

# Usage
car = Car("Toyota")
bike = Bicycle("Trek")

print(car.start())   # Toyota car engine started! Vroom!
print(bike.start())  # Pedaling the Trek bicycle!
```

---

## 4. The super() Function

### Calling Parent Methods

Use `super()` to access parent class methods.

```python
class Person:
    """Base person class."""
    
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def introduce(self):
        return f"Hi, I'm {self.name}, {self.age} years old"

class Student(Person):
    """Student extends Person."""
    
    def __init__(self, name, age, student_id):
        # Call parent constructor
        super().__init__(name, age)
        # Add student-specific attribute
        self.student_id = student_id
        self.grades = []
    
    def introduce(self):
        # Extend parent method
        base = super().introduce()
        return f"{base}. Student ID: {self.student_id}"
    
    def add_grade(self, grade):
        self.grades.append(grade)

# Usage
student = Student("Alice", 20, "S001")
print(student.introduce())
# Output: Hi, I'm Alice, 20 years old. Student ID: S001
```

### super() in Multiple Inheritance

```python
class A:
    def method(self):
        print("A method")
        super().method()

class B:
    def method(self):
        print("B method")

class C(A, B):
    def method(self):
        print("C method")
        super().method()

c = C()
c.method()
# Output:
# C method
# A method
# B method
```

---

## 5. Multiple Inheritance

### Basic Multiple Inheritance

A class can inherit from multiple parent classes.

```python
class Flyable:
    """Mixin for flying ability."""
    
    def fly(self):
        return f"{self.name} is flying!"

class Swimmable:
    """Mixin for swimming ability."""
    
    def swim(self):
        return f"{self.name} is swimming!"

class Duck(Flyable, Swimmable):
    """Duck can both fly and swim."""
    
    def __init__(self, name):
        self.name = name

duck = Duck("Donald")
print(duck.fly())   # Donald is flying!
print(duck.swim())  # Donald is swimming!
```

### Method Resolution Order (MRO)

Python uses C3 linearization to determine method lookup order.

```python
class A:
    def method(self):
        return "A"

class B(A):
    def method(self):
        return "B"

class C(A):
    def method(self):
        return "C"

class D(B, C):
    pass

# Check MRO
print(D.mro())
# [<class 'D'>, <class 'B'>, <class 'C'>, <class 'A'>, <class 'object'>]

d = D()
print(d.method())  # "B" (follows MRO)
```

---

## 6. Polymorphism

### What is Polymorphism?

**Polymorphism** means "many forms" - same interface, different implementations.

### Duck Typing Example

```python
class Dog:
    def speak(self):
        return "Woof!"

class Cat:
    def speak(self):
        return "Meow!"

class Cow:
    def speak(self):
        return "Moo!"

def make_sound(animal):
    """Works with any object that has speak() method."""
    print(animal.speak())

# All these work!
make_sound(Dog())  # Woof!
make_sound(Cat())  # Meow!
make_sound(Cow())  # Moo!
```

### Polymorphism with Inheritance

```python
class Shape:
    """Base shape class."""
    
    def area(self):
        raise NotImplementedError("Subclass must implement area()")
    
    def perimeter(self):
        raise NotImplementedError("Subclass must implement perimeter()")

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def area(self):
        return self.width * self.height
    
    def perimeter(self):
        return 2 * (self.width + self.height)

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        import math
        return math.pi * self.radius ** 2
    
    def perimeter(self):
        import math
        return 2 * math.pi * self.radius

# Polymorphic function
def print_shape_info(shape):
    """Works with any Shape subclass."""
    print(f"Area: {shape.area():.2f}")
    print(f"Perimeter: {shape.perimeter():.2f}")

# Works with different shapes!
rect = Rectangle(5, 10)
circle = Circle(7)

print_shape_info(rect)
print_shape_info(circle)
```

---

## 7. Abstract Base Classes (ABC)

### Using ABC Module

```python
from abc import ABC, abstractmethod

class Animal(ABC):
    """Abstract base class."""
    
    def __init__(self, name):
        self.name = name
    
    @abstractmethod
    def speak(self):
        """Must be implemented by subclass."""
        pass
    
    @abstractmethod
    def move(self):
        """Must be implemented by subclass."""
        pass
    
    def info(self):
        """Concrete method (can be used as-is)."""
        return f"I am {self.name}"

class Dog(Animal):
    def speak(self):
        return "Woof!"
    
    def move(self):
        return "Running on four legs"

class Bird(Animal):
    def speak(self):
        return "Tweet!"
    
    def move(self):
        return "Flying in the sky"

# animal = Animal("Generic")  # Error! Can't instantiate abstract class
dog = Dog("Buddy")
bird = Bird("Tweety")

print(dog.speak())   # Woof!
print(bird.move())   # Flying in the sky
```

---

## 8. Composition vs Inheritance

### When to Use Composition

Sometimes composition ("has-a") is better than inheritance ("is-a").

```python
# Inheritance (is-a relationship)
class Engine:
    def start(self):
        return "Engine starting..."

class Car(Engine):  # Car IS-A Engine? No!
    pass

# Composition (has-a relationship) - BETTER!
class Engine:
    def start(self):
        return "Engine starting..."

class Car:
    def __init__(self):
        self.engine = Engine()  # Car HAS-A Engine
    
    def start(self):
        return self.engine.start()

car = Car()
print(car.start())  # Engine starting...
```

### Complex Composition Example

```python
class Processor:
    def __init__(self, speed):
        self.speed = speed
    
    def info(self):
        return f"{self.speed}GHz Processor"

class RAM:
    def __init__(self, size):
        self.size = size
    
    def info(self):
        return f"{self.size}GB RAM"

class Computer:
    """Computer has-a Processor and RAM."""
    
    def __init__(self, processor_speed, ram_size):
        self.processor = Processor(processor_speed)
        self.ram = RAM(ram_size)
    
    def specifications(self):
        return f"{self.processor.info()}, {self.ram.info()}"

computer = Computer(3.5, 16)
print(computer.specifications())
# Output: 3.5GHz Processor, 16GB RAM
```

---

## 9. Advanced Inheritance Patterns

### Multilevel Inheritance

```python
class GrandParent:
    def method(self):
        return "GrandParent"

class Parent(GrandParent):
    def method(self):
        return f"{super().method()} -> Parent"

class Child(Parent):
    def method(self):
        return f"{super().method()} -> Child"

child = Child()
print(child.method())
# Output: GrandParent -> Parent -> Child
```

### Mixin Classes

```python
class JSONMixin:
    """Mixin to add JSON serialization."""
    
    def to_json(self):
        import json
        return json.dumps(self.__dict__)

class LogMixin:
    """Mixin to add logging."""
    
    def log(self, message):
        print(f"[LOG] {message}")

class User(JSONMixin, LogMixin):
    """User with JSON and logging capabilities."""
    
    def __init__(self, name, email):
        self.name = name
        self.email = email

user = User("Alice", "alice@email.com")
print(user.to_json())  # {"name": "Alice", "email": "alice@email.com"}
user.log("User created")  # [LOG] User created
```

---

## 10. isinstance() and issubclass()

### Checking Types and Relationships

```python
class Animal:
    pass

class Dog(Animal):
    pass

class Cat(Animal):
    pass

dog = Dog()
cat = Cat()

# isinstance - check if object is instance of class
print(isinstance(dog, Dog))     # True
print(isinstance(dog, Animal))  # True (Dog is subclass of Animal)
print(isinstance(dog, Cat))     # False

# issubclass - check if class is subclass of another
print(issubclass(Dog, Animal))  # True
print(issubclass(Cat, Animal))  # True
print(issubclass(Dog, Cat))     # False
```

---

## 11. Practical Examples

### Example 1: Employee Hierarchy

```python
class Employee:
    """Base employee class."""
    
    def __init__(self, name, employee_id, salary):
        self.name = name
        self.employee_id = employee_id
        self.salary = salary
    
    def get_details(self):
        return f"{self.name} (ID: {self.employee_id})"
    
    def calculate_bonus(self):
        return self.salary * 0.1  # 10% base bonus

class Manager(Employee):
    """Manager with team management."""
    
    def __init__(self, name, employee_id, salary, department):
        super().__init__(name, employee_id, salary)
        self.department = department
        self.team = []
    
    def add_team_member(self, employee):
        self.team.append(employee)
    
    def calculate_bonus(self):
        # Managers get 20% bonus
        return self.salary * 0.2
    
    def get_details(self):
        base = super().get_details()
        return f"{base}, Department: {self.department}"

class Developer(Employee):
    """Developer with programming skills."""
    
    def __init__(self, name, employee_id, salary, language):
        super().__init__(name, employee_id, salary)
        self.language = language
        self.projects = []
    
    def add_project(self, project):
        self.projects.append(project)
    
    def get_details(self):
        base = super().get_details()
        return f"{base}, Language: {self.language}"

# Usage
manager = Manager("Alice", "M001", 100000, "Engineering")
dev1 = Developer("Bob", "D001", 80000, "Python")
dev2 = Developer("Charlie", "D002", 75000, "JavaScript")

manager.add_team_member(dev1)
manager.add_team_member(dev2)

print(manager.get_details())
print(f"Bonus: ${manager.calculate_bonus()}")

print(dev1.get_details())
print(f"Bonus: ${dev1.calculate_bonus()}")
```

### Example 2: Payment System

```python
from abc import ABC, abstractmethod

class Payment(ABC):
    """Abstract payment base class."""
    
    def __init__(self, amount):
        self.amount = amount
    
    @abstractmethod
    def process(self):
        """Process the payment."""
        pass
    
    def receipt(self):
        """Generate receipt."""
        return f"Payment of ${self.amount:.2f} processed"

class CreditCardPayment(Payment):
    def __init__(self, amount, card_number):
        super().__init__(amount)
        self.card_number = card_number[-4:]  # Last 4 digits
    
    def process(self):
        return f"Processing credit card ****{self.card_number} for ${self.amount:.2f}"

class PayPalPayment(Payment):
    def __init__(self, amount, email):
        super().__init__(amount)
        self.email = email
    
    def process(self):
        return f"Processing PayPal payment for {self.email}: ${self.amount:.2f}"

class CashPayment(Payment):
    def process(self):
        return f"Processing cash payment: ${self.amount:.2f}"

# Polymorphic function
def process_payment(payment):
    """Works with any Payment subclass."""
    print(payment.process())
    print(payment.receipt())
    print()

# All payment types work!
payments = [
    CreditCardPayment(100.50, "1234567890123456"),
    PayPalPayment(75.25, "user@email.com"),
    CashPayment(50.00)
]

for payment in payments:
    process_payment(payment)
```

---

## Practice Exercises

### Exercise 1: Vehicle Hierarchy
Create a vehicle hierarchy:
- Base: Vehicle (brand, model, year)
- Derived: Car, Motorcycle, Truck
- Each with specific attributes and methods

### Exercise 2: Shape Calculator
Create shape classes:
- Abstract base: Shape
- Derived: Circle, Rectangle, Triangle
- All implement area() and perimeter()

### Exercise 3: Bank Accounts
Create account types:
- Base: BankAccount
- Derived: SavingsAccount, CheckingAccount
- Different interest rates and rules

### Exercise 4: Game Characters
Create character classes:
- Base: Character (health, attack)
- Derived: Warrior, Mage, Archer
- Each with unique abilities

### Exercise 5: Document System
Create document hierarchy:
- Base: Document
- Derived: PDF, Word, Excel
- Methods: open(), save(), print()

---

## Practice Project

**See:** `day18_game_characters.py` for the complete RPG Character System project.

The project includes:
- Inheritance hierarchy
- Abstract base classes
- Polymorphism
- Method overriding
- Complex interactions

---

## Quick Reference

### Inheritance Syntax
```python
class Parent:
    def method(self):
        pass

class Child(Parent):  # Inherit from Parent
    def method(self):  # Override
        super().method()  # Call parent method
```

### Multiple Inheritance
```python
class Child(Parent1, Parent2):
    pass
```

### Abstract Base Class
```python
from abc import ABC, abstractmethod

class Base(ABC):
    @abstractmethod
    def method(self):
        pass
```

### Type Checking
```python
isinstance(obj, Class)   # Check if obj is instance
issubclass(Child, Parent)  # Check if Child inherits from Parent
```

---

## Key Takeaways

✅ Inheritance enables code reuse  
✅ Child classes inherit parent attributes/methods  
✅ super() accesses parent class  
✅ Method overriding customizes behavior  
✅ Polymorphism allows different implementations  
✅ ABC enforces subclass implementation  
✅ Use composition for "has-a" relationships  
✅ isinstance() and issubclass() check types  
✅ MRO determines method lookup order  
✅ Mixins add functionality without main inheritance  

---

## Common Mistakes

❌ **Deep inheritance hierarchies**
```python
# Bad - too many levels
class A: pass
class B(A): pass
class C(B): pass
class D(C): pass  # Too deep!
```

❌ **Forgetting super().__init__()**
```python
class Child(Parent):
    def __init__(self, x):
        # Forgot super().__init__()!
        self.x = x
```

❌ **Using inheritance for "has-a"**
```python
# Bad
class Car(Engine):  # Car is-a Engine? No!
    pass

# Good
class Car:
    def __init__(self):
        self.engine = Engine()  # Car has-a Engine
```

---

## Next Steps

Tomorrow (Day 19), we'll learn about **Working with Libraries** - using popular Python packages for data analysis, web requests, and more!

---

## Resources

- [Python Inheritance](https://docs.python.org/3/tutorial/classes.html#inheritance)
- [ABC Module](https://docs.python.org/3/library/abc.html)

---

**Inherit Wisely! 🐍**
