# Recursion Visualizer - Day 12 Practice Project
# Understand recursion through visualization and interactive examples

import time

# ===== VISUALIZATION HELPERS =====

def indent_print(level, message):
    """Print with indentation based on recursion level."""
    print("  " * level + message)


# ===== BASIC RECURSION EXAMPLES =====

def countdown_visual(n, level=0):
    """
    Countdown with visualization.
    Shows each recursive call clearly.
    """
    indent_print(level, f"→ countdown({n})")
    
    if n <= 0:
        indent_print(level, "✓ Base case reached!")
        indent_print(level, "← Returning from countdown(0)")
        return
    
    print()
    countdown_visual(n - 1, level + 1)
    print()
    indent_print(level, f"← Returning from countdown({n})")


def factorial_visual(n, level=0):
    """
    Factorial with step-by-step visualization.
    """
    indent_print(level, f"→ factorial({n})")
    
    if n <= 1:
        indent_print(level, f"✓ Base case: factorial({n}) = 1")
        indent_print(level, "← Returning 1")
        return 1
    
    indent_print(level, f"Computing {n} * factorial({n-1})...")
    print()
    
    result = n * factorial_visual(n - 1, level + 1)
    
    print()
    indent_print(level, f"✓ factorial({n}) = {result}")
    indent_print(level, f"← Returning {result}")
    
    return result


def fibonacci_visual(n, level=0):
    """
    Fibonacci with visualization showing tree structure.
    """
    indent_print(level, f"→ fib({n})")
    
    if n <= 1:
        indent_print(level, f"✓ Base case: fib({n}) = {n}")
        indent_print(level, f"← Returning {n}")
        return n
    
    indent_print(level, f"Computing fib({n-1}) + fib({n-2})...")
    print()
    
    left = fibonacci_visual(n - 1, level + 1)
    print()
    right = fibonacci_visual(n - 2, level + 1)
    
    result = left + right
    
    print()
    indent_print(level, f"✓ fib({n}) = {left} + {right} = {result}")
    indent_print(level, f"← Returning {result}")
    
    return result


# ===== RECURSIVE ALGORITHMS =====

def sum_list(numbers, level=0, show_steps=False):
    """Sum all numbers in a list recursively."""
    if show_steps:
        indent_print(level, f"→ sum_list({numbers})")
    
    # Base case: empty list
    if not numbers:
        if show_steps:
            indent_print(level, "✓ Empty list, returning 0")
        return 0
    
    # Recursive case
    first = numbers[0]
    rest = numbers[1:]
    
    if show_steps:
        indent_print(level, f"Computing {first} + sum_list({rest})")
        print()
    
    result = first + sum_list(rest, level + 1, show_steps)
    
    if show_steps:
        print()
        indent_print(level, f"← Returning {result}")
    
    return result


def reverse_string(s, level=0, show_steps=False):
    """Reverse string recursively."""
    if show_steps:
        indent_print(level, f"→ reverse('{s}')")
    
    # Base case
    if len(s) <= 1:
        if show_steps:
            indent_print(level, f"✓ Base case, returning '{s}'")
        return s
    
    # Recursive case
    if show_steps:
        indent_print(level, f"Computing '{s[-1]}' + reverse('{s[:-1]}')")
        print()
    
    result = s[-1] + reverse_string(s[:-1], level + 1, show_steps)
    
    if show_steps:
        print()
        indent_print(level, f"← Returning '{result}'")
    
    return result


def is_palindrome(s, level=0, show_steps=False):
    """Check if string is palindrome recursively."""
    s = s.replace(" ", "").lower()
    
    if show_steps:
        indent_print(level, f"→ is_palindrome('{s}')")
    
    # Base case
    if len(s) <= 1:
        if show_steps:
            indent_print(level, "✓ Base case: True")
        return True
    
    # Check first and last
    if s[0] != s[-1]:
        if show_steps:
            indent_print(level, f"✗ '{s[0]}' != '{s[-1]}': False")
        return False
    
    if show_steps:
        indent_print(level, f"✓ '{s[0]}' == '{s[-1]}', checking middle...")
        print()
    
    result = is_palindrome(s[1:-1], level + 1, show_steps)
    
    if show_steps:
        print()
        indent_print(level, f"← Returning {result}")
    
    return result


def gcd(a, b, level=0, show_steps=False):
    """Find GCD using Euclidean algorithm."""
    if show_steps:
        indent_print(level, f"→ gcd({a}, {b})")
    
    # Base case
    if b == 0:
        if show_steps:
            indent_print(level, f"✓ Base case: gcd({a}, 0) = {a}")
        return a
    
    # Recursive case
    if show_steps:
        indent_print(level, f"Computing gcd({b}, {a % b})")
        print()
    
    result = gcd(b, a % b, level + 1, show_steps)
    
    if show_steps:
        print()
        indent_print(level, f"← Returning {result}")
    
    return result


def binary_search(arr, target, left=0, right=None, level=0, show_steps=False):
    """Binary search recursively."""
    if right is None:
        right = len(arr) - 1
    
    if show_steps:
        indent_print(level, f"→ search({arr[left:right+1]}, target={target})")
    
    # Base case: not found
    if left > right:
        if show_steps:
            indent_print(level, "✗ Not found")
        return -1
    
    mid = (left + right) // 2
    
    if show_steps:
        indent_print(level, f"Middle element: arr[{mid}] = {arr[mid]}")
    
    # Base case: found
    if arr[mid] == target:
        if show_steps:
            indent_print(level, f"✓ Found at index {mid}!")
        return mid
    
    # Recursive cases
    if arr[mid] > target:
        if show_steps:
            indent_print(level, f"{arr[mid]} > {target}, searching left half")
            print()
        return binary_search(arr, target, left, mid - 1, level + 1, show_steps)
    else:
        if show_steps:
            indent_print(level, f"{arr[mid]} < {target}, searching right half")
            print()
        return binary_search(arr, target, mid + 1, right, level + 1, show_steps)


# ===== ADVANCED RECURSION =====

def hanoi(n, source='A', target='C', auxiliary='B', level=0):
    """Tower of Hanoi with visualization."""
    if n == 1:
        indent_print(level, f"Move disk 1: {source} → {target}")
        return
    
    indent_print(level, f"Moving {n} disks: {source} → {target} (using {auxiliary})")
    
    # Move n-1 disks to auxiliary
    hanoi(n - 1, source, auxiliary, target, level + 1)
    
    # Move largest disk to target
    indent_print(level, f"Move disk {n}: {source} → {target}")
    
    # Move n-1 disks from auxiliary to target
    hanoi(n - 1, auxiliary, target, source, level + 1)


def permutations(s):
    """Generate all permutations of a string."""
    # Base case
    if len(s) <= 1:
        return [s]
    
    result = []
    
    # For each character
    for i, char in enumerate(s):
        # Get remaining characters
        remaining = s[:i] + s[i+1:]
        
        # Get permutations of remaining
        for perm in permutations(remaining):
            result.append(char + perm)
    
    return result


def flatten_list(nested_list):
    """Flatten a nested list recursively."""
    result = []
    
    for item in nested_list:
        if isinstance(item, list):
            # Recursively flatten
            result.extend(flatten_list(item))
        else:
            result.append(item)
    
    return result


# ===== PERFORMANCE COMPARISON =====

def fibonacci_recursive(n):
    """Standard recursive Fibonacci (slow)."""
    if n <= 1:
        return n
    return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)


def fibonacci_iterative(n):
    """Iterative Fibonacci (fast)."""
    if n <= 1:
        return n
    
    a, b = 0, 1
    for _ in range(n - 1):
        a, b = b, a + b
    
    return b


def fibonacci_memoized(n, memo=None):
    """Memoized Fibonacci (fast)."""
    if memo is None:
        memo = {}
    
    if n in memo:
        return memo[n]
    
    if n <= 1:
        return n
    
    memo[n] = fibonacci_memoized(n - 1, memo) + fibonacci_memoized(n - 2, memo)
    return memo[n]


# ===== INTERACTIVE MENU =====

def display_menu():
    """Display main menu."""
    print("\n" + "=" * 60)
    print("         🔄 RECURSION VISUALIZER 🔄")
    print("=" * 60)
    print("Basic Examples:")
    print("  1.  Countdown (Simple recursion)")
    print("  2.  Factorial (With return values)")
    print("  3.  Fibonacci (Tree recursion)")
    print("\nRecursive Algorithms:")
    print("  4.  Sum List")
    print("  5.  Reverse String")
    print("  6.  Palindrome Checker")
    print("  7.  GCD (Greatest Common Divisor)")
    print("  8.  Binary Search")
    print("\nAdvanced:")
    print("  9.  Tower of Hanoi")
    print("  10. Permutations")
    print("  11. Flatten Nested List")
    print("\nPerformance:")
    print("  12. Fibonacci Performance Comparison")
    print("\n  13. Exit")
    print("=" * 60)


def run_countdown():
    """Run countdown demo."""
    print("\n--- Countdown Demo ---")
    n = int(input("Enter starting number: "))
    print()
    countdown_visual(n)


def run_factorial():
    """Run factorial demo."""
    print("\n--- Factorial Demo ---")
    n = int(input("Enter number: "))
    print()
    result = factorial_visual(n)
    print(f"\nFinal result: {n}! = {result}")


def run_fibonacci():
    """Run fibonacci demo."""
    print("\n--- Fibonacci Demo ---")
    n = int(input("Enter term number (recommend ≤ 5 for clarity): "))
    print()
    result = fibonacci_visual(n)
    print(f"\nFinal result: fib({n}) = {result}")


def run_sum_list():
    """Run sum list demo."""
    print("\n--- Sum List Demo ---")
    numbers = input("Enter numbers (space-separated): ").split()
    numbers = [int(x) for x in numbers]
    print()
    result = sum_list(numbers, show_steps=True)
    print(f"\nSum = {result}")


def run_reverse():
    """Run reverse string demo."""
    print("\n--- Reverse String Demo ---")
    text = input("Enter text to reverse: ")
    print()
    result = reverse_string(text, show_steps=True)
    print(f"\nReversed: '{result}'")


def run_palindrome():
    """Run palindrome demo."""
    print("\n--- Palindrome Checker Demo ---")
    text = input("Enter text to check: ")
    print()
    result = is_palindrome(text, show_steps=True)
    print(f"\nIs palindrome: {result}")


def run_gcd():
    """Run GCD demo."""
    print("\n--- GCD Demo ---")
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    print()
    result = gcd(a, b, show_steps=True)
    print(f"\nGCD({a}, {b}) = {result}")


def run_binary_search():
    """Run binary search demo."""
    print("\n--- Binary Search Demo ---")
    print("Array: [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]")
    target = int(input("Enter number to search: "))
    
    arr = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
    print()
    result = binary_search(arr, target, show_steps=True)
    
    if result != -1:
        print(f"\n✓ Found at index {result}")
    else:
        print("\n✗ Not found")


def run_hanoi():
    """Run Tower of Hanoi demo."""
    print("\n--- Tower of Hanoi Demo ---")
    n = int(input("Enter number of disks (recommend ≤ 4): "))
    print()
    hanoi(n)


def run_permutations():
    """Run permutations demo."""
    print("\n--- Permutations Demo ---")
    text = input("Enter text (recommend ≤ 4 chars): ")
    print()
    result = permutations(text)
    print("All permutations:")
    for i, perm in enumerate(result, 1):
        print(f"{i:2}. {perm}")
    print(f"\nTotal: {len(result)} permutations")


def run_flatten():
    """Run flatten list demo."""
    print("\n--- Flatten Nested List Demo ---")
    print("Example: [[1, 2], [3, [4, 5]], 6]")
    
    # Predefined example
    nested = [[1, 2], [3, [4, 5]], 6]
    print(f"\nNested: {nested}")
    result = flatten_list(nested)
    print(f"Flattened: {result}")


def run_performance():
    """Run performance comparison."""
    print("\n--- Fibonacci Performance Comparison ---")
    n = int(input("Enter term number (recommend ≤ 35): "))
    
    print("\n1. Recursive (slow):")
    start = time.time()
    result1 = fibonacci_recursive(n)
    time1 = time.time() - start
    print(f"   Result: {result1}")
    print(f"   Time: {time1:.6f} seconds")
    
    print("\n2. Iterative (fast):")
    start = time.time()
    result2 = fibonacci_iterative(n)
    time2 = time.time() - start
    print(f"   Result: {result2}")
    print(f"   Time: {time2:.6f} seconds")
    
    print("\n3. Memoized (fast):")
    start = time.time()
    result3 = fibonacci_memoized(n)
    time3 = time.time() - start
    print(f"   Result: {result3}")
    print(f"   Time: {time3:.6f} seconds")
    
    print(f"\nSpeedup: Iterative is {time1/time2:.0f}x faster than recursive")
    print(f"Speedup: Memoized is {time1/time3:.0f}x faster than recursive")


def main():
    """Main program."""
    print("Welcome to Recursion Visualizer!")
    print("See how recursion works step-by-step!")
    
    while True:
        display_menu()
        choice = input("\nEnter your choice (1-13): ")
        
        try:
            if choice == '1':
                run_countdown()
            elif choice == '2':
                run_factorial()
            elif choice == '3':
                run_fibonacci()
            elif choice == '4':
                run_sum_list()
            elif choice == '5':
                run_reverse()
            elif choice == '6':
                run_palindrome()
            elif choice == '7':
                run_gcd()
            elif choice == '8':
                run_binary_search()
            elif choice == '9':
                run_hanoi()
            elif choice == '10':
                run_permutations()
            elif choice == '11':
                run_flatten()
            elif choice == '12':
                run_performance()
            elif choice == '13':
                print("\n👋 Thanks for exploring recursion!")
                print("Think recursively! 🔄")
                break
            else:
                print("\n✗ Invalid choice! Please select 1-13.")
        
        except Exception as e:
            print(f"\n✗ Error: {e}")
        
        input("\nPress Enter to continue...")


# Run the program
if __name__ == "__main__":
    main()
