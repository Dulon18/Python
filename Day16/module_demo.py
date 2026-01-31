# Module System Demo - Day 16 Practice Project
# Demonstrates modules, packages, and the standard library

"""
PROJECT STRUCTURE (when creating files):

day16_module_system/
    main.py              # This file
    string_utils.py      # String utilities module
    math_ops.py          # Math operations module
    validators.py        # Data validators module
    file_handler.py      # File operations module
    mypackage/           # Custom package
        __init__.py
        calculator.py
        converter.py
"""

# ===== SIMULATED MODULES (would normally be separate files) =====

# ===== MODULE 1: string_utils.py =====
"""
String utility functions.

This module provides common string operations.
"""

def reverse_string(text):
    """Reverse a string."""
    return text[::-1]

def is_palindrome(text):
    """Check if string is palindrome."""
    cleaned = text.replace(" ", "").lower()
    return cleaned == cleaned[::-1]

def count_vowels(text):
    """Count vowels in string."""
    return sum(1 for char in text.lower() if char in 'aeiou')

def capitalize_words(text):
    """Capitalize first letter of each word."""
    return ' '.join(word.capitalize() for word in text.split())

def remove_extra_spaces(text):
    """Remove extra whitespace."""
    return ' '.join(text.split())

# Module test code
if __name__ == "__main__":
    print("Testing string_utils module...")
    print(f"Reverse: {reverse_string('Python')}")
    print(f"Palindrome: {is_palindrome('radar')}")
    print(f"Vowels: {count_vowels('hello')}")


# ===== MODULE 2: math_ops.py =====
"""
Mathematical operations module.

Provides basic and advanced math functions.
"""

import math

def factorial(n):
    """Calculate factorial."""
    if n < 0:
        raise ValueError("Factorial not defined for negative numbers")
    if n <= 1:
        return 1
    return n * factorial(n - 1)

def is_prime(n):
    """Check if number is prime."""
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def gcd(a, b):
    """Calculate greatest common divisor."""
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    """Calculate least common multiple."""
    return abs(a * b) // gcd(a, b)

def average(numbers):
    """Calculate average of numbers."""
    if not numbers:
        return 0
    return sum(numbers) / len(numbers)

# Constants
PI = 3.14159265359
E = 2.71828182846


# ===== MODULE 3: validators.py =====
"""
Data validation utilities.

Provides validators for common data types.
"""

import re

def is_valid_email(email):
    """
    Validate email format.
    
    Args:
        email: Email string to validate
    
    Returns:
        bool: True if valid email format
    """
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return bool(re.match(pattern, email))

def is_valid_phone(phone):
    """
    Validate phone number (format: XXX-XXX-XXXX).
    
    Args:
        phone: Phone number string
    
    Returns:
        bool: True if valid format
    """
    pattern = r'^\d{3}-\d{3}-\d{4}$'
    return bool(re.match(pattern, phone))

def is_strong_password(password):
    """
    Check if password is strong.
    
    Requirements:
    - At least 8 characters
    - Contains uppercase and lowercase
    - Contains digit
    
    Args:
        password: Password string
    
    Returns:
        bool: True if password is strong
    """
    if len(password) < 8:
        return False
    
    has_upper = any(c.isupper() for c in password)
    has_lower = any(c.islower() for c in password)
    has_digit = any(c.isdigit() for c in password)
    
    return has_upper and has_lower and has_digit

def is_valid_username(username):
    """
    Validate username (alphanumeric, 3-20 chars).
    
    Args:
        username: Username string
    
    Returns:
        bool: True if valid username
    """
    if not username or len(username) < 3 or len(username) > 20:
        return False
    return username.isalnum()


# ===== STANDARD LIBRARY DEMONSTRATIONS =====

import datetime
import random
import json
import os
import sys
from collections import Counter, defaultdict

def demo_datetime_module():
    """Demonstrate datetime module."""
    print("\n--- datetime Module ---")
    
    # Current date and time
    now = datetime.datetime.now()
    print(f"Current datetime: {now}")
    print(f"Date: {now.date()}")
    print(f"Time: {now.time()}")
    
    # Create specific date
    birthday = datetime.date(2000, 5, 15)
    print(f"Birthday: {birthday}")
    
    # Calculate age
    today = datetime.date.today()
    age = today.year - birthday.year
    print(f"Age: {age} years")
    
    # Time arithmetic
    tomorrow = today + datetime.timedelta(days=1)
    next_week = today + datetime.timedelta(weeks=1)
    print(f"Tomorrow: {tomorrow}")
    print(f"Next week: {next_week}")
    
    # Formatting
    formatted = now.strftime("%Y-%m-%d %H:%M:%S")
    print(f"Formatted: {formatted}")


def demo_random_module():
    """Demonstrate random module."""
    print("\n--- random Module ---")
    
    # Random integer
    rand_int = random.randint(1, 100)
    print(f"Random int (1-100): {rand_int}")
    
    # Random float
    rand_float = random.random()
    print(f"Random float (0-1): {rand_float:.4f}")
    
    # Random choice
    colors = ["red", "blue", "green", "yellow"]
    choice = random.choice(colors)
    print(f"Random choice: {choice}")
    
    # Random sample
    sample = random.sample(range(1, 50), 5)
    print(f"Random sample: {sample}")
    
    # Shuffle
    numbers = [1, 2, 3, 4, 5]
    random.shuffle(numbers)
    print(f"Shuffled: {numbers}")
    
    # Random password
    chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$"
    password = ''.join(random.choice(chars) for _ in range(12))
    print(f"Random password: {password}")


def demo_json_module():
    """Demonstrate json module."""
    print("\n--- json Module ---")
    
    # Python dict to JSON
    data = {
        "name": "Alice",
        "age": 25,
        "city": "New York",
        "hobbies": ["reading", "coding", "gaming"]
    }
    
    json_string = json.dumps(data, indent=2)
    print("Python to JSON:")
    print(json_string)
    
    # JSON to Python
    parsed = json.loads(json_string)
    print(f"\nJSON to Python: {parsed}")
    print(f"Name: {parsed['name']}")


def demo_os_module():
    """Demonstrate os module."""
    print("\n--- os Module ---")
    
    # Current directory
    cwd = os.getcwd()
    print(f"Current directory: {cwd}")
    
    # Platform info
    print(f"Operating system: {os.name}")
    
    # Environment variables
    print(f"User: {os.environ.get('USER', 'Unknown')}")
    
    # Path operations
    path = "/home/user/documents/file.txt"
    print(f"\nPath: {path}")
    print(f"Directory: {os.path.dirname(path)}")
    print(f"Filename: {os.path.basename(path)}")
    print(f"Extension: {os.path.splitext(path)[1]}")


def demo_sys_module():
    """Demonstrate sys module."""
    print("\n--- sys Module ---")
    
    # Python version
    print(f"Python version: {sys.version}")
    
    # Platform
    print(f"Platform: {sys.platform}")
    
    # Module search path (first 3)
    print("\nModule search paths:")
    for i, path in enumerate(sys.path[:3], 1):
        print(f"  {i}. {path}")


def demo_collections_module():
    """Demonstrate collections module."""
    print("\n--- collections Module ---")
    
    # Counter
    words = ["apple", "banana", "apple", "orange", "banana", "apple"]
    counter = Counter(words)
    print(f"Word counts: {counter}")
    print(f"Most common: {counter.most_common(2)}")
    
    # defaultdict
    dd = defaultdict(int)
    for word in words:
        dd[word] += 1
    print(f"defaultdict counts: {dict(dd)}")
    
    # defaultdict with list
    groups = defaultdict(list)
    data = [("fruit", "apple"), ("fruit", "banana"), ("veggie", "carrot")]
    for category, item in data:
        groups[category].append(item)
    print(f"Grouped: {dict(groups)}")


# ===== MODULE DEMONSTRATION FUNCTIONS =====

def demo_string_utils():
    """Demonstrate string_utils module."""
    print("\n--- String Utils Module ---")
    
    test_strings = [
        "Python",
        "radar",
        "Hello World",
        "programming"
    ]
    
    for text in test_strings:
        print(f"\nText: '{text}'")
        print(f"  Reversed: {reverse_string(text)}")
        print(f"  Palindrome: {is_palindrome(text)}")
        print(f"  Vowels: {count_vowels(text)}")
        print(f"  Capitalized: {capitalize_words(text)}")


def demo_math_ops():
    """Demonstrate math_ops module."""
    print("\n--- Math Operations Module ---")
    
    # Factorial
    print(f"Factorial of 5: {factorial(5)}")
    print(f"Factorial of 10: {factorial(10)}")
    
    # Prime check
    numbers = [2, 3, 4, 5, 15, 17, 20, 23]
    primes = [n for n in numbers if is_prime(n)]
    print(f"\nPrime numbers in {numbers}: {primes}")
    
    # GCD and LCM
    a, b = 48, 18
    print(f"\nGCD of {a} and {b}: {gcd(a, b)}")
    print(f"LCM of {a} and {b}: {lcm(a, b)}")
    
    # Average
    nums = [10, 20, 30, 40, 50]
    print(f"\nAverage of {nums}: {average(nums):.2f}")
    
    # Constants
    print(f"\nPI: {PI}")
    print(f"E: {E}")


def demo_validators():
    """Demonstrate validators module."""
    print("\n--- Validators Module ---")
    
    # Email validation
    emails = [
        "user@example.com",
        "invalid.email",
        "test@domain.co.uk"
    ]
    print("Email validation:")
    for email in emails:
        valid = is_valid_email(email)
        print(f"  {email}: {'✓ Valid' if valid else '✗ Invalid'}")
    
    # Phone validation
    phones = [
        "123-456-7890",
        "1234567890",
        "555-123-4567"
    ]
    print("\nPhone validation:")
    for phone in phones:
        valid = is_valid_phone(phone)
        print(f"  {phone}: {'✓ Valid' if valid else '✗ Invalid'}")
    
    # Password validation
    passwords = [
        "weak",
        "StrongPass123",
        "NoDigits",
        "alllowercase123"
    ]
    print("\nPassword validation:")
    for pwd in passwords:
        valid = is_strong_password(pwd)
        print(f"  {pwd}: {'✓ Strong' if valid else '✗ Weak'}")


# ===== MAIN MENU =====

def display_menu():
    """Display main menu."""
    print("\n" + "=" * 60)
    print("          📦 MODULE SYSTEM DEMO 📦")
    print("=" * 60)
    print("Custom Modules:")
    print("  1. String Utils Demo")
    print("  2. Math Operations Demo")
    print("  3. Validators Demo")
    print("\nStandard Library Modules:")
    print("  4. datetime Module")
    print("  5. random Module")
    print("  6. json Module")
    print("  7. os Module")
    print("  8. sys Module")
    print("  9. collections Module")
    print("\n  10. Exit")
    print("=" * 60)


def main():
    """Main program."""
    print("=" * 60)
    print("   Welcome to Python Module System Demo!")
    print("=" * 60)
    print("\nThis demonstrates:")
    print("✓ Creating custom modules")
    print("✓ Using Python's standard library")
    print("✓ Module organization")
    print("✓ Best practices")
    
    while True:
        display_menu()
        choice = input("\nEnter your choice (1-10): ")
        
        try:
            if choice == '1':
                demo_string_utils()
            elif choice == '2':
                demo_math_ops()
            elif choice == '3':
                demo_validators()
            elif choice == '4':
                demo_datetime_module()
            elif choice == '5':
                demo_random_module()
            elif choice == '6':
                demo_json_module()
            elif choice == '7':
                demo_os_module()
            elif choice == '8':
                demo_sys_module()
            elif choice == '9':
                demo_collections_module()
            elif choice == '10':
                print("\n" + "=" * 60)
                print("Thanks for exploring Python modules!")
                print("\nKey Points to Remember:")
                print("• Modules organize code into reusable files")
                print("• Use import to access module functionality")
                print("• Python's standard library is extensive")
                print("• Create packages with __init__.py")
                print("• Document your modules with docstrings")
                print("\nHappy coding! 📦")
                print("=" * 60)
                break
            else:
                print("\n✗ Invalid choice! Please select 1-10.")
        
        except Exception as e:
            print(f"\n✗ Error: {e}")
        
        input("\nPress Enter to continue...")


# Module test code
if __name__ == "__main__":
    main()
else:
    print(f"Module '{__name__}' imported successfully")


# ===== BONUS: Creating Modules Guide =====

def print_module_creation_guide():
    """
    Print guide for creating actual module files.
    
    This function shows how to organize the project into separate files.
    """
    guide = """
    
    TO CREATE ACTUAL MODULE FILES:
    ================================
    
    1. Create project directory:
       mkdir day16_module_system
       cd day16_module_system
    
    2. Create string_utils.py:
       Copy all string utility functions into this file
    
    3. Create math_ops.py:
       Copy all math operation functions into this file
    
    4. Create validators.py:
       Copy all validator functions into this file
    
    5. Create main.py:
       Import modules and use their functions:
       
       import string_utils
       import math_ops
       import validators
       
       result = string_utils.reverse_string("Python")
       factorial = math_ops.factorial(5)
       valid = validators.is_valid_email("test@example.com")
    
    6. Create package (optional):
       mkdir mypackage
       touch mypackage/__init__.py
       # Add modules inside mypackage/
    
    7. Run the main file:
       python main.py
    
    Module Best Practices:
    ======================
    • One module per file
    • Clear, descriptive names
    • Comprehensive docstrings
    • Group related functions
    • Use if __name__ == "__main__" for tests
    • Keep modules focused and cohesive
    """
    print(guide)


# Uncomment to see the module creation guide
# print_module_creation_guide()
