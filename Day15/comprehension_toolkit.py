# Comprehension Toolkit - Day 15 Practice Project
# Master list, dictionary, and set comprehensions

import random
import string

# ===== LIST COMPREHENSION EXAMPLES =====

def demo_basic_list_comp():
    """Demonstrate basic list comprehensions."""
    print("\n--- Basic List Comprehensions ---")
    
    # Squares
    squares = [x**2 for x in range(10)]
    print(f"Squares 0-9: {squares}")
    
    # Even numbers
    evens = [x for x in range(20) if x % 2 == 0]
    print(f"Even 0-19: {evens}")
    
    # Uppercase words
    words = ["hello", "world", "python"]
    upper = [word.upper() for word in words]
    print(f"Uppercase: {upper}")
    
    # With condition
    numbers = [1, -2, 3, -4, 5, -6]
    positive = [x for x in numbers if x > 0]
    print(f"Positive only: {positive}")
    
    # If-else expression
    labels = ["even" if x % 2 == 0 else "odd" for x in range(10)]
    print(f"Labels: {labels}")


def demo_nested_list_comp():
    """Demonstrate nested list comprehensions."""
    print("\n--- Nested List Comprehensions ---")
    
    # Flatten 2D list
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    flat = [num for row in matrix for num in row]
    print(f"Original matrix: {matrix}")
    print(f"Flattened: {flat}")
    
    # Create multiplication table
    table = [[i * j for j in range(1, 6)] for i in range(1, 6)]
    print("\nMultiplication Table:")
    for row in table:
        print(row)
    
    # Cartesian product
    colors = ["Red", "Blue"]
    sizes = ["S", "M", "L"]
    products = [f"{color}-{size}" for color in colors for size in sizes]
    print(f"\nProducts: {products}")


def demo_string_operations():
    """String processing with comprehensions."""
    print("\n--- String Operations ---")
    
    # Extract vowels
    text = "Hello World"
    vowels = [char for char in text.lower() if char in 'aeiou']
    print(f"Text: {text}")
    print(f"Vowels: {vowels}")
    
    # Remove spaces and uppercase
    cleaned = [char.upper() for char in text if char != ' ']
    print(f"Cleaned: {''.join(cleaned)}")
    
    # Word lengths
    sentence = "Python is awesome and powerful"
    words = sentence.split()
    lengths = [len(word) for word in words]
    print(f"\nSentence: {sentence}")
    print(f"Word lengths: {lengths}")
    
    # Filter long words
    long_words = [word for word in words if len(word) > 5]
    print(f"Long words (>5 chars): {long_words}")


# ===== DICTIONARY COMPREHENSION EXAMPLES =====

def demo_basic_dict_comp():
    """Demonstrate basic dictionary comprehensions."""
    print("\n--- Basic Dictionary Comprehensions ---")
    
    # Squares dictionary
    squares = {x: x**2 for x in range(6)}
    print(f"Squares: {squares}")
    
    # Word lengths
    words = ["cat", "elephant", "dog", "butterfly"]
    lengths = {word: len(word) for word in words}
    print(f"Word lengths: {lengths}")
    
    # Character positions
    text = "Python"
    positions = {char: idx for idx, char in enumerate(text)}
    print(f"Character positions in '{text}': {positions}")
    
    # Filter by condition
    prices = {"apple": 0.5, "banana": 0.3, "orange": 0.8, "grape": 0.4}
    cheap = {item: price for item, price in prices.items() if price < 0.6}
    print(f"Original prices: {prices}")
    print(f"Cheap items (<$0.6): {cheap}")


def demo_dict_transformations():
    """Dictionary transformation examples."""
    print("\n--- Dictionary Transformations ---")
    
    # Original data
    students = {"Alice": 85, "Bob": 92, "Charlie": 78, "Diana": 95}
    print(f"Original grades: {students}")
    
    # Add bonus points
    bonus = {name: grade + 5 for name, grade in students.items()}
    print(f"With +5 bonus: {bonus}")
    
    # Filter passing grades
    passing = {name: grade for name, grade in students.items() if grade >= 80}
    print(f"Passing (>=80): {passing}")
    
    # Swap keys and values
    swapped = {grade: name for name, grade in students.items()}
    print(f"Swapped: {swapped}")
    
    # Grade categories
    categories = {name: "A" if grade >= 90 else "B" if grade >= 80 else "C" 
                  for name, grade in students.items()}
    print(f"Categories: {categories}")


def demo_nested_dict_comp():
    """Nested dictionary comprehensions."""
    print("\n--- Nested Dictionary Comprehensions ---")
    
    # Student data
    students = [
        {"name": "Alice", "age": 20, "grade": 85},
        {"name": "Bob", "age": 22, "grade": 92},
        {"name": "Charlie", "age": 21, "grade": 78}
    ]
    
    # Extract specific fields
    grades = {s["name"]: s["grade"] for s in students}
    print(f"Grades: {grades}")
    
    # Filter and extract
    high_achievers = {s["name"]: s["grade"] for s in students if s["grade"] >= 80}
    print(f"High achievers (>=80): {high_achievers}")
    
    # Complex mapping
    info = {s["name"]: {"age": s["age"], "pass": s["grade"] >= 60} 
            for s in students}
    print(f"Student info: {info}")


# ===== SET COMPREHENSION EXAMPLES =====

def demo_basic_set_comp():
    """Demonstrate basic set comprehensions."""
    print("\n--- Basic Set Comprehensions ---")
    
    # Unique squares
    squares = {x**2 for x in range(10)}
    print(f"Unique squares: {squares}")
    
    # Remove duplicates
    numbers = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5]
    unique = {x for x in numbers}
    print(f"Original: {numbers}")
    print(f"Unique: {unique}")
    
    # Unique characters (no spaces)
    text = "hello world"
    chars = {char for char in text if char != ' '}
    print(f"Unique chars in '{text}': {chars}")
    
    # First letters of words
    words = ["apple", "banana", "apricot", "blueberry", "avocado"]
    first_letters = {word[0] for word in words}
    print(f"Words: {words}")
    print(f"First letters: {first_letters}")


def demo_set_operations():
    """Set operations with comprehensions."""
    print("\n--- Set Operations ---")
    
    # Multiples of 2 and 3
    multiples_2 = {x for x in range(30) if x % 2 == 0}
    multiples_3 = {x for x in range(30) if x % 3 == 0}
    
    print(f"Multiples of 2: {sorted(multiples_2)}")
    print(f"Multiples of 3: {sorted(multiples_3)}")
    print(f"Both (intersection): {sorted(multiples_2 & multiples_3)}")
    print(f"Either (union): {sorted(multiples_2 | multiples_3)}")


# ===== PRACTICAL APPLICATIONS =====

def data_filtering():
    """Practical data filtering examples."""
    print("\n--- Data Filtering ---")
    
    # Sample data
    data = [
        {"name": "Alice", "age": 25, "salary": 50000},
        {"name": "Bob", "age": 30, "salary": 60000},
        {"name": "Charlie", "age": 35, "salary": 75000},
        {"name": "Diana", "age": 28, "salary": 55000}
    ]
    
    # Extract names
    names = [person["name"] for person in data]
    print(f"All names: {names}")
    
    # High earners
    high_earners = [p["name"] for p in data if p["salary"] > 55000]
    print(f"High earners (>$55k): {high_earners}")
    
    # Name-salary mapping
    salaries = {p["name"]: p["salary"] for p in data}
    print(f"Salaries: {salaries}")
    
    # Age groups
    age_groups = {p["name"]: "Young" if p["age"] < 30 else "Senior" 
                  for p in data}
    print(f"Age groups: {age_groups}")


def matrix_operations():
    """Matrix operations using comprehensions."""
    print("\n--- Matrix Operations ---")
    
    # Create 4x4 matrix
    matrix = [[i * 4 + j for j in range(4)] for i in range(4)]
    print("Matrix:")
    for row in matrix:
        print(row)
    
    # Transpose
    transposed = [[row[i] for row in matrix] for i in range(len(matrix[0]))]
    print("\nTransposed:")
    for row in transposed:
        print(row)
    
    # Diagonal
    diagonal = [matrix[i][i] for i in range(len(matrix))]
    print(f"\nDiagonal: {diagonal}")
    
    # Sum each row
    row_sums = [sum(row) for row in matrix]
    print(f"Row sums: {row_sums}")
    
    # Flatten and filter
    evens = [num for row in matrix for num in row if num % 2 == 0]
    print(f"Even numbers: {evens}")


def text_analysis():
    """Text analysis with comprehensions."""
    print("\n--- Text Analysis ---")
    
    text = "Python is awesome. Python is powerful. Python is fun!"
    
    # Word frequency
    words = text.lower().replace(".", "").split()
    word_freq = {word: words.count(word) for word in set(words)}
    print(f"Word frequency: {word_freq}")
    
    # Words by length
    by_length = {length: [w for w in set(words) if len(w) == length] 
                 for length in set(len(w) for w in words)}
    print(f"Words by length: {by_length}")
    
    # Vowel count per word
    vowel_counts = {word: sum(1 for char in word if char in 'aeiou') 
                    for word in set(words)}
    print(f"Vowel counts: {vowel_counts}")


def number_utilities():
    """Number utilities using comprehensions."""
    print("\n--- Number Utilities ---")
    
    numbers = list(range(1, 21))
    
    # Categorize
    categories = {
        "even": [x for x in numbers if x % 2 == 0],
        "odd": [x for x in numbers if x % 2 != 0],
        "prime": [x for x in numbers if x > 1 and 
                  all(x % i != 0 for i in range(2, int(x**0.5) + 1))]
    }
    print("Number categories:")
    for category, nums in categories.items():
        print(f"  {category}: {nums}")
    
    # Math operations
    operations = {
        "squares": [x**2 for x in numbers[:5]],
        "cubes": [x**3 for x in numbers[:5]],
        "factorials": [1] + [eval('*'.join(map(str, range(1, i+1)))) 
                             for i in range(2, 6)]
    }
    print("\nMath operations:")
    for op, results in operations.items():
        print(f"  {op}: {results}")


# ===== INTERACTIVE DEMONSTRATIONS =====

def custom_filter():
    """Interactive custom filter."""
    print("\n--- Custom Filter ---")
    
    numbers = list(range(1, 51))
    print(f"Numbers 1-50: {numbers[:10]}... (showing first 10)")
    
    try:
        threshold = int(input("\nEnter threshold value: "))
        
        print("\nFilter options:")
        print("1. Greater than threshold")
        print("2. Less than threshold")
        print("3. Divisible by threshold")
        
        choice = input("Choose (1-3): ")
        
        if choice == '1':
            result = [x for x in numbers if x > threshold]
            print(f"Numbers > {threshold}: {result}")
        elif choice == '2':
            result = [x for x in numbers if x < threshold]
            print(f"Numbers < {threshold}: {result}")
        elif choice == '3':
            result = [x for x in numbers if x % threshold == 0]
            print(f"Numbers divisible by {threshold}: {result}")
        else:
            print("Invalid choice")
    
    except ValueError:
        print("Invalid input")


def generate_data():
    """Generate sample data using comprehensions."""
    print("\n--- Generate Sample Data ---")
    
    # Random numbers
    random_nums = [random.randint(1, 100) for _ in range(10)]
    print(f"10 random numbers: {random_nums}")
    
    # Random strings
    random_strings = [''.join(random.choices(string.ascii_lowercase, k=5)) 
                      for _ in range(5)]
    print(f"5 random strings: {random_strings}")
    
    # Sample user data
    names = ["Alice", "Bob", "Charlie", "Diana", "Eve"]
    users = [{"id": i, "name": name, "score": random.randint(50, 100)} 
             for i, name in enumerate(names, 1)]
    print("\nSample users:")
    for user in users:
        print(f"  {user}")


# ===== MAIN MENU =====

def display_menu():
    """Display main menu."""
    print("\n" + "=" * 60)
    print("         COMPREHENSION TOOLKIT ")
    print("=" * 60)
    print("List Comprehensions:")
    print("  1. Basic List Comprehensions")
    print("  2. Nested List Comprehensions")
    print("  3. String Operations")
    print("\nDictionary Comprehensions:")
    print("  4. Basic Dictionary Comprehensions")
    print("  5. Dictionary Transformations")
    print("  6. Nested Dictionary Comprehensions")
    print("\nSet Comprehensions:")
    print("  7. Basic Set Comprehensions")
    print("  8. Set Operations")
    print("\nPractical Applications:")
    print("  9.  Data Filtering")
    print("  10. Matrix Operations")
    print("  11. Text Analysis")
    print("  12. Number Utilities")
    print("\nInteractive:")
    print("  13. Custom Filter")
    print("  14. Generate Sample Data")
    print("\n  15. Exit")
    print("=" * 60)


def main():
    """Main program."""
    print("Welcome to Comprehension Toolkit!")
    print("Explore Python's powerful comprehension syntax!")
    
    while True:
        display_menu()
        choice = input("\nEnter your choice (1-15): ")
        
        try:
            if choice == '1':
                demo_basic_list_comp()
            elif choice == '2':
                demo_nested_list_comp()
            elif choice == '3':
                demo_string_operations()
            elif choice == '4':
                demo_basic_dict_comp()
            elif choice == '5':
                demo_dict_transformations()
            elif choice == '6':
                demo_nested_dict_comp()
            elif choice == '7':
                demo_basic_set_comp()
            elif choice == '8':
                demo_set_operations()
            elif choice == '9':
                data_filtering()
            elif choice == '10':
                matrix_operations()
            elif choice == '11':
                text_analysis()
            elif choice == '12':
                number_utilities()
            elif choice == '13':
                custom_filter()
            elif choice == '14':
                generate_data()
            elif choice == '15':
                print("\n Thanks for exploring comprehensions!")
                print("Write elegant Python! 📋")
                break
            else:
                print("\n✗ Invalid choice! Please select 1-15.")
        
        except Exception as e:
            print(f"\n✗ Error: {e}")
        
        input("\nPress Enter to continue...")


# Run the program
if __name__ == "__main__":
    main()
