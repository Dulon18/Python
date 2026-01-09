# Pattern Generator - Day 8 Practice Project
# Master nested loops by creating various patterns

def display_menu():
    """Display main menu with all pattern options"""
    print("\n" + "=" * 60)
    print("               PATTERN GENERATOR ")
    print("=" * 60)
    print("1.  Right Triangle (Stars)")
    print("2.  Inverted Right Triangle")
    print("3.  Pyramid")
    print("4.  Inverted Pyramid")
    print("5.  Diamond")
    print("6.  Number Triangle")
    print("7.  Number Pyramid")
    print("8.  Hollow Square")
    print("9.  Hollow Diamond")
    print("10. Multiplication Table")
    print("11. Custom Pattern")
    print("12. View All Patterns")
    print("13. Exit")
    print("=" * 60)

def get_size():
    """Get pattern size from user"""
    while True:
        try:
            size = int(input("\nEnter pattern size (1-20): "))
            if 1 <= size <= 20:
                return size
            else:
                print("✗ Size must be between 1 and 20!")
        except ValueError:
            print("✗ Please enter a valid number!")

def get_character():
    """Get character to use for pattern"""
    char = input("Enter character to use (default: *): ").strip()
    return char if char else "*"

def pattern_right_triangle(size, char):
    """
    Pattern 1: Right Triangle
    *
    **
    ***
    ****
    """
    print("\n--- Right Triangle ---")
    for i in range(1, size + 1):
        for j in range(i):
            print(char, end="")
        print()

def pattern_inverted_triangle(size, char):
    """
    Pattern 2: Inverted Right Triangle
    ****
    ***
    **
    *
    """
    print("\n--- Inverted Right Triangle ---")
    for i in range(size, 0, -1):
        for j in range(i):
            print(char, end="")
        print()

def pattern_pyramid(size, char):
    """
    Pattern 3: Pyramid
        *
       ***
      *****
     *******
    """
    print("\n--- Pyramid ---")
    for i in range(1, size + 1):
        # Print spaces
        for j in range(size - i):
            print(" ", end="")
        # Print characters
        for j in range(2 * i - 1):
            print(char, end="")
        print()

def pattern_inverted_pyramid(size, char):
    """
    Pattern 4: Inverted Pyramid
    *********
     *******
      *****
       ***
        *
    """
    print("\n--- Inverted Pyramid ---")
    for i in range(size, 0, -1):
        # Print spaces
        for j in range(size - i):
            print(" ", end="")
        # Print characters
        for j in range(2 * i - 1):
            print(char, end="")
        print()

def pattern_diamond(size, char):
    """
    Pattern 5: Diamond
        *
       ***
      *****
     *******
      *****
       ***
        *
    """
    print("\n--- Diamond ---")
    # Upper half (including middle)
    for i in range(1, size + 1):
        for j in range(size - i):
            print(" ", end="")
        for j in range(2 * i - 1):
            print(char, end="")
        print()
    
    # Lower half
    for i in range(size - 1, 0, -1):
        for j in range(size - i):
            print(" ", end="")
        for j in range(2 * i - 1):
            print(char, end="")
        print()

def pattern_number_triangle(size):
    """
    Pattern 6: Number Triangle
    1
    1 2
    1 2 3
    1 2 3 4
    """
    print("\n--- Number Triangle ---")
    for i in range(1, size + 1):
        for j in range(1, i + 1):
            print(j, end=" ")
        print()

def pattern_number_pyramid(size):
    """
    Pattern 7: Number Pyramid
        1
       121
      12321
     1234321
    """
    print("\n--- Number Pyramid ---")
    for i in range(1, size + 1):
        # Print spaces
        for j in range(size - i):
            print(" ", end="")
        
        # Print increasing numbers
        for j in range(1, i + 1):
            print(j, end="")
        
        # Print decreasing numbers
        for j in range(i - 1, 0, -1):
            print(j, end="")
        
        print()

def pattern_hollow_square(size, char):
    """
    Pattern 8: Hollow Square
    *****
    *   *
    *   *
    *   *
    *****
    """
    print("\n--- Hollow Square ---")
    for i in range(size):
        for j in range(size):
            # Print char on borders
            if i == 0 or i == size - 1 or j == 0 or j == size - 1:
                print(char, end=" ")
            else:
                print(" ", end=" ")
        print()

def pattern_hollow_diamond(size, char):
    """
    Pattern 9: Hollow Diamond
        *
       * *
      *   *
     *     *
      *   *
       * *
        *
    """
    print("\n--- Hollow Diamond ---")
    # Upper half
    for i in range(1, size + 1):
        # Print spaces
        for j in range(size - i):
            print(" ", end="")
        
        # Print characters
        for j in range(2 * i - 1):
            if j == 0 or j == 2 * i - 2:
                print(char, end="")
            else:
                print(" ", end="")
        print()
    
    # Lower half
    for i in range(size - 1, 0, -1):
        for j in range(size - i):
            print(" ", end="")
        
        for j in range(2 * i - 1):
            if j == 0 or j == 2 * i - 2:
                print(char, end="")
            else:
                print(" ", end="")
        print()

def multiplication_table(size):
    """
    Pattern 10: Multiplication Table
    1  2  3  4  5
    2  4  6  8  10
    3  6  9  12 15
    4  8  12 16 20
    5  10 15 20 25
    """
    print("\n--- Multiplication Table ---")
    
    # Header
    print("   ", end="")
    for i in range(1, size + 1):
        print(f"{i:4}", end="")
    print()
    print("   " + "-" * (size * 4))
    
    # Table
    for i in range(1, size + 1):
        print(f"{i:2} |", end="")
        for j in range(1, size + 1):
            print(f"{i * j:4}", end="")
        print()

def custom_pattern():
    """Create custom pattern with user choices"""
    print("\n--- Custom Pattern Creator ---")
    
    print("\nSelect pattern type:")
    print("1. Increasing")
    print("2. Decreasing")
    print("3. Both")
    
    pattern_type = input("Choice (1-3): ")
    size = get_size()
    char = get_character()
    
    print()
    
    if pattern_type == '1':
        # Increasing pattern
        for i in range(1, size + 1):
            print(char * i)
    
    elif pattern_type == '2':
        # Decreasing pattern
        for i in range(size, 0, -1):
            print(char * i)
    
    elif pattern_type == '3':
        # Both (diamond shape without spaces)
        for i in range(1, size + 1):
            print(char * i)
        for i in range(size - 1, 0, -1):
            print(char * i)
    
    else:
        print("✗ Invalid choice!")

def view_all_patterns():
    """Display all patterns with default size"""
    size = 5
    char = "*"
    
    print("\n" + "=" * 60)
    print("             PATTERN GALLERY")
    print("=" * 60)
    
    patterns = [
        ("Right Triangle", lambda: pattern_right_triangle(size, char)),
        ("Inverted Triangle", lambda: pattern_inverted_triangle(size, char)),
        ("Pyramid", lambda: pattern_pyramid(size, char)),
        ("Inverted Pyramid", lambda: pattern_inverted_pyramid(size, char)),
        ("Diamond", lambda: pattern_diamond(size, char)),
        ("Number Triangle", lambda: pattern_number_triangle(size)),
        ("Number Pyramid", lambda: pattern_number_pyramid(size)),
        ("Hollow Square", lambda: pattern_hollow_square(size, char)),
        ("Hollow Diamond", lambda: pattern_hollow_diamond(size, char))
    ]
    
    for name, func in patterns:
        func()
        print()
    
    print("=" * 60)

def practice_mode():
    """Practice creating patterns with hints"""
    print("\n" + "=" * 60)
    print("              PRACTICE MODE")
    print("=" * 60)
    print("\nTry to create this pattern:")
    print("*")
    print("**")
    print("***")
    print("****")
    print("*****")
    
    print("\nHint: Use two nested loops")
    print("Outer loop: rows (1 to 5)")
    print("Inner loop: columns (stars in each row)")
    
    input("\nPress Enter when you've tried...")
    
    print("\nSolution:")
    print("for i in range(1, 6):")
    print("    for j in range(i):")
    print("        print('*', end='')")
    print("    print()")

def main():
    """Main program"""
    print("Welcome to Pattern Generator!")
    print("Learn nested loops through pattern creation!")
    
    while True:
        display_menu()
        choice = input("\nEnter your choice (1-13): ")
        
        if choice == '1':
            size = get_size()
            char = get_character()
            pattern_right_triangle(size, char)
        
        elif choice == '2':
            size = get_size()
            char = get_character()
            pattern_inverted_triangle(size, char)
        
        elif choice == '3':
            size = get_size()
            char = get_character()
            pattern_pyramid(size, char)
        
        elif choice == '4':
            size = get_size()
            char = get_character()
            pattern_inverted_pyramid(size, char)
        
        elif choice == '5':
            size = get_size()
            char = get_character()
            pattern_diamond(size, char)
        
        elif choice == '6':
            size = get_size()
            pattern_number_triangle(size)
        
        elif choice == '7':
            size = get_size()
            pattern_number_pyramid(size)
        
        elif choice == '8':
            size = get_size()
            char = get_character()
            pattern_hollow_square(size, char)
        
        elif choice == '9':
            size = get_size()
            char = get_character()
            pattern_hollow_diamond(size, char)
        
        elif choice == '10':
            size = get_size()
            multiplication_table(size)
        
        elif choice == '11':
            custom_pattern()
        
        elif choice == '12':
            view_all_patterns()
        
        elif choice == '13':
            print("\n Thanks for using Pattern Generator!")
            print("Keep practicing nested loops! ")
            break
        
        else:
            print("\n✗ Invalid choice! Please select 1-13.")
        
        # Ask if user wants to continue
        if choice != '13':
            continue_choice = input("\nGenerate another pattern? (yes/no): ").lower()
            if continue_choice != 'yes' and continue_choice != 'y':
                print("\n Thanks for using Pattern Generator!")
                print("Keep practicing nested loops! ")
                break

# Run the program
if __name__ == "__main__":
    main()
