# Utility Functions Library - Day 10 Practice Project
# A comprehensive collection of useful functions organized by category

import math

# ===== STRING UTILITIES =====

def count_vowels(text):
    """
    Count the number of vowels in a string.
    
    Parameters:
        text (str): Input string
    
    Returns:
        int: Number of vowels
    """
    vowels = "aeiouAEIOU"
    count = 0
    for char in text:
        if char in vowels:
            count += 1
    return count


def reverse_string(text):
    """
    Reverse a string.
    
    Parameters:
        text (str): Input string
    
    Returns:
        str: Reversed string
    """
    return text[::-1]


def is_palindrome(text):
    """
    Check if a string is a palindrome.
    
    Parameters:
        text (str): Input string
    
    Returns:
        bool: True if palindrome, False otherwise
    """
    # Remove spaces and convert to lowercase
    cleaned = text.replace(" ", "").lower()
    return cleaned == cleaned[::-1]


def count_words(text):
    """
    Count the number of words in a string.
    
    Parameters:
        text (str): Input string
    
    Returns:
        int: Number of words
    """
    return len(text.split())


def capitalize_words(text):
    """
    Capitalize the first letter of each word.
    
    Parameters:
        text (str): Input string
    
    Returns:
        str: String with capitalized words
    """
    return text.title()


# ===== NUMBER UTILITIES =====

def is_even(number):
    """
    Check if a number is even.
    
    Parameters:
        number (int): Input number
    
    Returns:
        bool: True if even, False otherwise
    """
    return number % 2 == 0


def is_odd(number):
    """
    Check if a number is odd.
    
    Parameters:
        number (int): Input number
    
    Returns:
        bool: True if odd, False otherwise
    """
    return number % 2 != 0


def factorial(n):
    """
    Calculate factorial of a number.
    
    Parameters:
        n (int): Non-negative integer
    
    Returns:
        int: Factorial of n
    """
    if n < 0:
        return "Error: Factorial not defined for negative numbers"
    if n == 0 or n == 1:
        return 1
    
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


def is_prime(number):
    """
    Check if a number is prime.
    
    Parameters:
        number (int): Input number
    
    Returns:
        bool: True if prime, False otherwise
    """
    if number < 2:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True


def gcd(a, b):
    """
    Find Greatest Common Divisor using Euclidean algorithm.
    
    Parameters:
        a (int): First number
        b (int): Second number
    
    Returns:
        int: GCD of a and b
    """
    while b:
        a, b = b, a % b
    return a


def fibonacci(n):
    """
    Generate Fibonacci sequence up to n terms.
    
    Parameters:
        n (int): Number of terms
    
    Returns:
        list: List of Fibonacci numbers
    """
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    
    sequence = [0, 1]
    for i in range(2, n):
        sequence.append(sequence[-1] + sequence[-2])
    return sequence


# ===== LIST UTILITIES =====

def find_second_largest(numbers):
    """
    Find the second largest number in a list.
    
    Parameters:
        numbers (list): List of numbers
    
    Returns:
        int/float: Second largest number or None if not found
    """
    if len(numbers) < 2:
        return None
    
    unique_numbers = list(set(numbers))
    if len(unique_numbers) < 2:
        return None
    
    unique_numbers.sort()
    return unique_numbers[-2]


def remove_duplicates(items):
    """
    Remove duplicates from a list while preserving order.
    
    Parameters:
        items (list): Input list
    
    Returns:
        list: List without duplicates
    """
    seen = []
    for item in items:
        if item not in seen:
            seen.append(item)
    return seen


def flatten_list(nested_list):
    """
    Flatten a nested list.
    
    Parameters:
        nested_list (list): Nested list
    
    Returns:
        list: Flattened list
    """
    flat = []
    for item in nested_list:
        if isinstance(item, list):
            flat.extend(flatten_list(item))
        else:
            flat.append(item)
    return flat


def chunk_list(items, chunk_size):
    """
    Split a list into chunks of specified size.
    
    Parameters:
        items (list): Input list
        chunk_size (int): Size of each chunk
    
    Returns:
        list: List of chunks
    """
    chunks = []
    for i in range(0, len(items), chunk_size):
        chunks.append(items[i:i + chunk_size])
    return chunks


# ===== MATH UTILITIES =====

def calculate_average(numbers):
    """
    Calculate the average of numbers.
    
    Parameters:
        numbers (list): List of numbers
    
    Returns:
        float: Average value
    """
    if not numbers:
        return 0
    return sum(numbers) / len(numbers)


def calculate_percentage(part, whole):
    """
    Calculate percentage.
    
    Parameters:
        part (float): Part value
        whole (float): Whole value
    
    Returns:
        float: Percentage
    """
    if whole == 0:
        return 0
    return (part / whole) * 100


def circle_area(radius):
    """
    Calculate area of a circle.
    
    Parameters:
        radius (float): Radius of circle
    
    Returns:
        float: Area of circle
    """
    return math.pi * radius ** 2


def rectangle_area(length, width):
    """
    Calculate area of a rectangle.
    
    Parameters:
        length (float): Length of rectangle
        width (float): Width of rectangle
    
    Returns:
        float: Area of rectangle
    """
    return length * width


def triangle_area(base, height):
    """
    Calculate area of a triangle.
    
    Parameters:
        base (float): Base of triangle
        height (float): Height of triangle
    
    Returns:
        float: Area of triangle
    """
    return 0.5 * base * height


# ===== VALIDATION UTILITIES =====

def is_valid_email(email):
    """
    Basic email validation.
    
    Parameters:
        email (str): Email address
    
    Returns:
        bool: True if valid format, False otherwise
    """
    if '@' not in email:
        return False
    
    parts = email.split('@')
    if len(parts) != 2:
        return False
    
    username, domain = parts
    
    if not username or not domain:
        return False
    
    if '.' not in domain:
        return False
    
    return True


def is_valid_password(password):
    """
    Check if password meets requirements.
    - At least 8 characters
    - Contains uppercase and lowercase
    - Contains a digit
    
    Parameters:
        password (str): Password string
    
    Returns:
        bool: True if valid, False otherwise
    """
    if len(password) < 8:
        return False
    
    has_upper = any(c.isupper() for c in password)
    has_lower = any(c.islower() for c in password)
    has_digit = any(c.isdigit() for c in password)
    
    return has_upper and has_lower and has_digit


# ===== INTERACTIVE MENU =====

def display_menu():
    """Display main menu."""
    print("\n" + "=" * 60)
    print("         🔧 UTILITY FUNCTIONS LIBRARY 🔧")
    print("=" * 60)
    print("1.  String Utilities")
    print("2.  Number Utilities")
    print("3.  List Utilities")
    print("4.  Math Utilities")
    print("5.  Validation Utilities")
    print("6.  Exit")
    print("=" * 60)


def string_utilities_menu():
    """Test string utility functions."""
    while True:
        print("\n--- String Utilities ---")
        print("1. Count Vowels")
        print("2. Reverse String")
        print("3. Check Palindrome")
        print("4. Count Words")
        print("5. Capitalize Words")
        print("6. Back")
        
        choice = input("\nSelect option (1-6): ")
        
        if choice == '1':
            text = input("Enter text: ")
            result = count_vowels(text)
            print(f"✓ Vowels: {result}")
        
        elif choice == '2':
            text = input("Enter text: ")
            result = reverse_string(text)
            print(f"✓ Reversed: {result}")
        
        elif choice == '3':
            text = input("Enter text: ")
            result = is_palindrome(text)
            print(f"✓ Is palindrome: {result}")
        
        elif choice == '4':
            text = input("Enter text: ")
            result = count_words(text)
            print(f"✓ Word count: {result}")
        
        elif choice == '5':
            text = input("Enter text: ")
            result = capitalize_words(text)
            print(f"✓ Capitalized: {result}")
        
        elif choice == '6':
            break
        
        else:
            print("✗ Invalid choice!")


def number_utilities_menu():
    """Test number utility functions."""
    while True:
        print("\n--- Number Utilities ---")
        print("1. Check Even/Odd")
        print("2. Calculate Factorial")
        print("3. Check Prime")
        print("4. Find GCD")
        print("5. Generate Fibonacci")
        print("6. Back")
        
        choice = input("\nSelect option (1-6): ")
        
        if choice == '1':
            num = int(input("Enter number: "))
            if is_even(num):
                print(f" {num} is even")
            else:
                print(f" {num} is odd")
        
        elif choice == '2':
            num = int(input("Enter number: "))
            result = factorial(num)
            print(f" Factorial: {result}")
        
        elif choice == '3':
            num = int(input("Enter number: "))
            result = is_prime(num)
            print(f" Is prime: {result}")
        
        elif choice == '4':
            a = int(input("Enter first number: "))
            b = int(input("Enter second number: "))
            result = gcd(a, b)
            print(f" GCD: {result}")
        
        elif choice == '5':
            n = int(input("How many terms: "))
            result = fibonacci(n)
            print(f" Fibonacci: {result}")
        
        elif choice == '6':
            break
        
        else:
            print("✗ Invalid choice!")


def list_utilities_menu():
    """Test list utility functions."""
    while True:
        print("\n--- List Utilities ---")
        print("1. Find Second Largest")
        print("2. Remove Duplicates")
        print("3. Flatten List")
        print("4. Chunk List")
        print("5. Back")
        
        choice = input("\nSelect option (1-5): ")
        
        if choice == '1':
            numbers = input("Enter numbers (space-separated): ").split()
            numbers = [int(x) for x in numbers]
            result = find_second_largest(numbers)
            print(f" Second largest: {result}")
        
        elif choice == '2':
            items = input("Enter items (space-separated): ").split()
            result = remove_duplicates(items)
            print(f"Without duplicates: {result}")
        
        elif choice == '3':
            print("Example: [[1, 2], [3, [4, 5]], 6]")
            # For simplicity, using a predefined example
            nested = [[1, 2], [3, [4, 5]], 6]
            result = flatten_list(nested)
            print(f" Flattened: {result}")
        
        elif choice == '4':
            items = input("Enter items (space-separated): ").split()
            size = int(input("Chunk size: "))
            result = chunk_list(items, size)
            print(f" Chunks: {result}")
        
        elif choice == '5':
            break
        
        else:
            print("✗ Invalid choice!")


def math_utilities_menu():
    """Test math utility functions."""
    while True:
        print("\n--- Math Utilities ---")
        print("1. Calculate Average")
        print("2. Calculate Percentage")
        print("3. Circle Area")
        print("4. Rectangle Area")
        print("5. Triangle Area")
        print("6. Back")
        
        choice = input("\nSelect option (1-6): ")
        
        if choice == '1':
            numbers = input("Enter numbers (space-separated): ").split()
            numbers = [float(x) for x in numbers]
            result = calculate_average(numbers)
            print(f"✓ Average: {result:.2f}")
        
        elif choice == '2':
            part = float(input("Enter part: "))
            whole = float(input("Enter whole: "))
            result = calculate_percentage(part, whole)
            print(f"✓ Percentage: {result:.2f}%")
        
        elif choice == '3':
            radius = float(input("Enter radius: "))
            result = circle_area(radius)
            print(f"✓ Area: {result:.2f}")
        
        elif choice == '4':
            length = float(input("Enter length: "))
            width = float(input("Enter width: "))
            result = rectangle_area(length, width)
            print(f"✓ Area: {result:.2f}")
        
        elif choice == '5':
            base = float(input("Enter base: "))
            height = float(input("Enter height: "))
            result = triangle_area(base, height)
            print(f"✓ Area: {result:.2f}")
        
        elif choice == '6':
            break
        
        else:
            print("✗ Invalid choice!")


def validation_utilities_menu():
    """Test validation utility functions."""
    while True:
        print("\n--- Validation Utilities ---")
        print("1. Validate Email")
        print("2. Validate Password")
        print("3. Back")
        
        choice = input("\nSelect option (1-3): ")
        
        if choice == '1':
            email = input("Enter email: ")
            result = is_valid_email(email)
            if result:
                print("✓ Valid email format")
            else:
                print("✗ Invalid email format")
        
        elif choice == '2':
            password = input("Enter password: ")
            result = is_valid_password(password)
            if result:
                print("✓ Valid password")
            else:
                print("✗ Invalid password (need 8+ chars, upper, lower, digit)")
        
        elif choice == '3':
            break
        
        else:
            print("✗ Invalid choice!")


def main():
    """Main program."""
    print("Welcome to Utility Functions Library!")
    print("Test various utility functions organized by category.")
    
    while True:
        display_menu()
        choice = input("\nEnter your choice (1-6): ")
        
        if choice == '1':
            string_utilities_menu()
        elif choice == '2':
            number_utilities_menu()
        elif choice == '3':
            list_utilities_menu()
        elif choice == '4':
            math_utilities_menu()
        elif choice == '5':
            validation_utilities_menu()
        elif choice == '6':
            print("\n Thanks for using Utility Functions Library!")
            print("Happy coding! 🔧")
            break
        else:
            print("\n✗ Invalid choice! Please select 1-6.")


# Run the program
if __name__ == "__main__":
    main()
