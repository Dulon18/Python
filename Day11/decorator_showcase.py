# Decorator Showcase - Day 11 Practice Project
# Master advanced function concepts through practical decorators

import time
import functools
from datetime import datetime

# ===== UTILITY DECORATORS =====

def timer(func):
    """
    Measure and print function execution time.
    """
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"⏱️  {func.__name__} took {end - start:.4f} seconds")
        return result
    return wrapper


def debug(func):
    """
    Print function call details for debugging.
    """
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        args_repr = [repr(a) for a in args]
        kwargs_repr = [f"{k}={v!r}" for k, v in kwargs.items()]
        signature = ", ".join(args_repr + kwargs_repr)
        
        print(f" Calling {func.__name__}({signature})")
        result = func(*args, **kwargs)
        print(f" {func.__name__} returned {result!r}")
        
        return result
    return wrapper


def count_calls(func):
    """
    Count how many times a function is called.
    """
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        wrapper.calls += 1
        print(f" Call #{wrapper.calls} to {func.__name__}")
        return func(*args, **kwargs)
    
    wrapper.calls = 0
    return wrapper


def validate_types(*expected_types):
    """
    Validate function argument types.
    
    Usage:
        @validate_types(int, int)
        def add(a, b):
            return a + b
    """
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            # Check positional arguments
            for arg, expected_type in zip(args, expected_types):
                if not isinstance(arg, expected_type):
                    raise TypeError(
                        f"Expected {expected_type.__name__}, "
                        f"got {type(arg).__name__}"
                    )
            return func(*args, **kwargs)
        return wrapper
    return decorator


def memoize(func):
    """
    Cache function results for same arguments.
    """
    cache = {}
    
    @functools.wraps(func)
    def wrapper(*args):
        if args in cache:
            print(f" Using cached result for {func.__name__}{args}")
            return cache[args]
        
        result = func(*args)
        cache[args] = result
        print(f" Cached result for {func.__name__}{args}")
        return result
    
    return wrapper


def retry(max_attempts=3, delay=1):
    """
    Retry function on failure.
    
    Args:
        max_attempts: Maximum number of attempts
        delay: Delay between attempts in seconds
    """
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for attempt in range(max_attempts):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    if attempt == max_attempts - 1:
                        print(f" All {max_attempts} attempts failed")
                        raise
                    print(f"  Attempt {attempt + 1} failed: {e}")
                    print(f" Retrying in {delay} seconds...")
                    time.sleep(delay)
        return wrapper
    return decorator


def log_to_file(filename="function_log.txt"):
    """
    Log function calls to a file.
    """
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            log_msg = f"[{timestamp}] {func.__name__} called with args={args}, kwargs={kwargs}\n"
            
            # In real application, write to file
            print(f" Logging: {log_msg.strip()}")
            
            return func(*args, **kwargs)
        return wrapper
    return decorator


def deprecated(message="This function is deprecated"):
    """
    Mark a function as deprecated.
    """
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            print(f" WARNING: {func.__name__} - {message}")
            return func(*args, **kwargs)
        return wrapper
    return decorator


# ===== DEMONSTRATION FUNCTIONS =====

@timer
def slow_operation():
    """Simulate a slow operation."""
    time.sleep(0.5)
    return "Operation completed"


@debug
def calculate_sum(a, b):
    """Add two numbers with debugging."""
    return a + b


@count_calls
def greet(name):
    """Greet a person."""
    return f"Hello, {name}!"


@validate_types(int, int)
def divide(a, b):
    """Divide two integers."""
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b


@memoize
def fibonacci(n):
    """Calculate Fibonacci number (expensive without memoization)."""
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


@retry(max_attempts=3, delay=0.5)
def unstable_operation():
    """Simulate an unstable operation."""
    import random
    if random.random() < 0.7:
        raise Exception("Random failure occurred")
    return "Success!"


@log_to_file()
def process_data(data):
    """Process some data."""
    return f"Processed: {data}"


@deprecated("Use new_function() instead")
def old_function():
    """An old function that's deprecated."""
    return "This is old"


# Multiple decorators
@timer
@debug
def complex_calculation(x, y):
    """Function with multiple decorators."""
    time.sleep(0.2)
    return x ** y


# ===== ADVANCED EXAMPLES =====

def repeat(times=2):
    """
    Repeat function execution multiple times.
    """
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            results = []
            for i in range(times):
                print(f"Execution {i + 1}/{times}")
                result = func(*args, **kwargs)
                results.append(result)
            return results
        return wrapper
    return decorator


@repeat(times=3)
def say_hello(name):
    """Say hello multiple times."""
    return f"Hello, {name}!"


def require_auth(func):
    """
    Simulate authentication requirement.
    """
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        # In real app, check authentication
        authenticated = True  # Simulated
        
        if not authenticated:
            raise PermissionError("Authentication required")
        
        print(" Authenticated")
        return func(*args, **kwargs)
    return wrapper


@require_auth
def access_sensitive_data():
    """Access data that requires authentication."""
    return "Sensitive data accessed"


# ===== DEMONSTRATION MENU =====

def display_menu():
    """Display demonstration menu."""
    print("\n" + "=" * 60)
    print("          DECORATOR SHOWCASE ")
    print("=" * 60)
    print("1.  Timer Decorator")
    print("2.  Debug Decorator")
    print("3.  Count Calls Decorator")
    print("4.  Type Validation Decorator")
    print("5.  Memoization Decorator")
    print("6.  Retry Decorator")
    print("7.  Log to File Decorator")
    print("8.  Deprecated Decorator")
    print("9.  Multiple Decorators")
    print("10. Repeat Decorator")
    print("11. Authentication Decorator")
    print("12. Lambda Functions Demo")
    print("13. Higher-Order Functions Demo")
    print("14. *args and **kwargs Demo")
    print("15. Exit")
    print("=" * 60)


def demo_timer():
    """Demonstrate timer decorator."""
    print("\n--- Timer Decorator Demo ---")
    print("Measuring execution time of slow operation...\n")
    result = slow_operation()
    print(f"Result: {result}")


def demo_debug():
    """Demonstrate debug decorator."""
    print("\n--- Debug Decorator Demo ---")
    print("Debugging function call...\n")
    result = calculate_sum(10, 20)
    print(f"\nFinal result: {result}")


def demo_count_calls():
    """Demonstrate count calls decorator."""
    print("\n--- Count Calls Decorator Demo ---")
    print("Calling greet() multiple times...\n")
    greet("Alice")
    greet("Bob")
    greet("Charlie")
    print(f"\nTotal calls: {greet.calls}")


def demo_validate_types():
    """Demonstrate type validation decorator."""
    print("\n--- Type Validation Decorator Demo ---")
    
    print("Valid call: divide(10, 2)")
    try:
        result = divide(10, 2)
        print(f" Result: {result}")
    except Exception as e:
        print(f" Error: {e}")
    
    print("\nInvalid call: divide('10', 2)")
    try:
        result = divide('10', 2)
        print(f" Result: {result}")
    except TypeError as e:
        print(f" Error: {e}")


def demo_memoize():
    """Demonstrate memoization decorator."""
    print("\n--- Memoization Decorator Demo ---")
    print("Calculating fibonacci(10)...\n")
    
    result = fibonacci(10)
    print(f"\nResult: {result}")
    
    print("\nCalling fibonacci(10) again (should use cache)...")
    result = fibonacci(10)
    print(f"Result: {result}")


def demo_retry():
    """Demonstrate retry decorator."""
    print("\n--- Retry Decorator Demo ---")
    print("Calling unstable operation (will retry on failure)...\n")
    
    try:
        result = unstable_operation()
        print(f" {result}")
    except Exception as e:
        print(f" Final error: {e}")


def demo_log_to_file():
    """Demonstrate log to file decorator."""
    print("\n--- Log to File Decorator Demo ---")
    print("Processing data with logging...\n")
    result = process_data([1, 2, 3, 4, 5])
    print(f"Result: {result}")


def demo_deprecated():
    """Demonstrate deprecated decorator."""
    print("\n--- Deprecated Decorator Demo ---")
    print("Calling deprecated function...\n")
    result = old_function()
    print(f"Result: {result}")


def demo_multiple_decorators():
    """Demonstrate multiple decorators."""
    print("\n--- Multiple Decorators Demo ---")
    print("Function with both @timer and @debug...\n")
    result = complex_calculation(2, 10)
    print(f"\nFinal result: {result}")


def demo_repeat():
    """Demonstrate repeat decorator."""
    print("\n--- Repeat Decorator Demo ---")
    print("Repeating function 3 times...\n")
    results = say_hello("World")
    print(f"\nAll results: {results}")


def demo_auth():
    """Demonstrate authentication decorator."""
    print("\n--- Authentication Decorator Demo ---")
    print("Accessing sensitive data...\n")
    try:
        result = access_sensitive_data()
        print(f" {result}")
    except PermissionError as e:
        print(f" Error: {e}")


def demo_lambda():
    """Demonstrate lambda functions."""
    print("\n--- Lambda Functions Demo ---")
    
    # Basic lambda
    square = lambda x: x ** 2
    print(f"Square of 5: {square(5)}")
    
    # Lambda with map
    numbers = [1, 2, 3, 4, 5]
    squares = list(map(lambda x: x ** 2, numbers))
    print(f"Squares: {squares}")
    
    # Lambda with filter
    evens = list(filter(lambda x: x % 2 == 0, numbers))
    print(f"Even numbers: {evens}")
    
    # Lambda with sorted
    words = ["python", "is", "awesome", "fun"]
    sorted_words = sorted(words, key=lambda x: len(x))
    print(f"Sorted by length: {sorted_words}")


def demo_higher_order():
    """Demonstrate higher-order functions."""
    print("\n--- Higher-Order Functions Demo ---")
    
    def apply_twice(func, value):
        """Apply function twice."""
        return func(func(value))
    
    def add_5(x):
        return x + 5
    
    result = apply_twice(add_5, 10)
    print(f"Apply add_5 twice to 10: {result}")  # (10 + 5) + 5 = 20
    
    # Function returning function
    def make_multiplier(n):
        return lambda x: x * n
    
    times_3 = make_multiplier(3)
    times_5 = make_multiplier(5)
    
    print(f"3 * 10 = {times_3(10)}")
    print(f"5 * 10 = {times_5(10)}")


def demo_args_kwargs():
    """Demonstrate *args and **kwargs."""
    print("\n--- *args and **kwargs Demo ---")
    
    def flexible_function(*args, **kwargs):
        """Function accepting any arguments."""
        print(f"Positional arguments (*args): {args}")
        print(f"Keyword arguments (**kwargs): {kwargs}")
        
        total = sum(args)
        print(f"Sum of positional args: {total}")
        
        if kwargs:
            print("\nKeyword arguments:")
            for key, value in kwargs.items():
                print(f"  {key}: {value}")
    
    print("Calling: flexible_function(1, 2, 3, name='Alice', age=25)")
    flexible_function(1, 2, 3, name='Alice', age=25)


def main():
    """Main program."""
    print("Welcome to Decorator Showcase!")
    print("Explore advanced Python function concepts!")
    
    while True:
        display_menu()
        choice = input("\nEnter your choice (1-15): ")
        
        if choice == '1':
            demo_timer()
        elif choice == '2':
            demo_debug()
        elif choice == '3':
            demo_count_calls()
        elif choice == '4':
            demo_validate_types()
        elif choice == '5':
            demo_memoize()
        elif choice == '6':
            demo_retry()
        elif choice == '7':
            demo_log_to_file()
        elif choice == '8':
            demo_deprecated()
        elif choice == '9':
            demo_multiple_decorators()
        elif choice == '10':
            demo_repeat()
        elif choice == '11':
            demo_auth()
        elif choice == '12':
            demo_lambda()
        elif choice == '13':
            demo_higher_order()
        elif choice == '14':
            demo_args_kwargs()
        elif choice == '15':
            print("\n Thanks for exploring decorators!")
            print("Keep coding with style! ")
            break
        else:
            print("\n✗ Invalid choice! Please select 1-15.")
        
        input("\nPress Enter to continue...")


# Run the program
if __name__ == "__main__":
    main()
