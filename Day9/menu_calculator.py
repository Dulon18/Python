# Menu-Driven Calculator - Day 9 Practice Project
# Master while loops through a comprehensive calculator application

import math

def display_main_menu():
    """Display main menu options"""
    print("\n" + "=" * 60)
    print("           ADVANCED CALCULATOR ")
    print("=" * 60)
    print("1. Basic Calculator")
    print("2. Scientific Calculator")
    print("3. Statistics Calculator")
    print("4. Number Converter")
    print("5. View History")
    print("6. Clear History")
    print("7. Exit")
    print("=" * 60)

def get_number(prompt):
    """Get a valid number from user using while loop"""
    while True:
        try:
            value = float(input(prompt))
            return value
        except ValueError:
            print("✗ Invalid input! Please enter a valid number.")

def basic_calculator(history):
    """Basic arithmetic operations"""
    print("\n--- Basic Calculator ---")
    print("Operations: +, -, *, /, %, ** (power)")
    
    while True:
        print("\n" + "-" * 50)
        
        num1 = get_number("Enter first number: ")
        operation = input("Enter operation (+, -, *, /, %, **) or 'back': ").strip()
        
        if operation.lower() == 'back':
            break
        
        if operation not in ['+', '-', '*', '/', '%', '**']:
            print("✗ Invalid operation!")
            continue
        
        num2 = get_number("Enter second number: ")
        
        # Perform calculation
        try:
            if operation == '+':
                result = num1 + num2
            elif operation == '-':
                result = num1 - num2
            elif operation == '*':
                result = num1 * num2
            elif operation == '/':
                if num2 == 0:
                    print("✗ Error: Cannot divide by zero!")
                    continue
                result = num1 / num2
            elif operation == '%':
                if num2 == 0:
                    print("✗ Error: Cannot divide by zero!")
                    continue
                result = num1 % num2
            elif operation == '**':
                result = num1 ** num2
            
            # Display result
            expression = f"{num1} {operation} {num2} = {result}"
            print(f"\n✓ Result: {result}")
            
            # Add to history
            history.append(expression)
            
            # Ask to continue
            cont = input("\nPerform another calculation? (yes/no): ").lower()
            if cont not in ['yes', 'y']:
                break
        
        except Exception as e:
            print(f"✗ Error: {e}")

def scientific_calculator(history):
    """Scientific operations"""
    print("\n--- Scientific Calculator ---")
    
    while True:
        print("\n" + "-" * 50)
        print("1. Square Root")
        print("2. Power")
        print("3. Logarithm (base 10)")
        print("4. Natural Logarithm (ln)")
        print("5. Sine")
        print("6. Cosine")
        print("7. Tangent")
        print("8. Factorial")
        print("9. Absolute Value")
        print("10. Back")
        print("-" * 50)
        
        choice = input("Select operation (1-10): ")
        
        if choice == '10':
            break
        
        if choice in ['1', '2', '3', '4', '5', '6', '7', '8', '9']:
            num = get_number("Enter number: ")
            
            try:
                if choice == '1':
                    if num < 0:
                        print("✗ Cannot calculate square root of negative number!")
                        continue
                    result = math.sqrt(num)
                    expression = f"√{num} = {result}"
                
                elif choice == '2':
                    power = get_number("Enter power: ")
                    result = math.pow(num, power)
                    expression = f"{num}^{power} = {result}"
                
                elif choice == '3':
                    if num <= 0:
                        print("✗ Logarithm only defined for positive numbers!")
                        continue
                    result = math.log10(num)
                    expression = f"log₁₀({num}) = {result}"
                
                elif choice == '4':
                    if num <= 0:
                        print("✗ Natural logarithm only defined for positive numbers!")
                        continue
                    result = math.log(num)
                    expression = f"ln({num}) = {result}"
                
                elif choice == '5':
                    result = math.sin(math.radians(num))
                    expression = f"sin({num}°) = {result}"
                
                elif choice == '6':
                    result = math.cos(math.radians(num))
                    expression = f"cos({num}°) = {result}"
                
                elif choice == '7':
                    result = math.tan(math.radians(num))
                    expression = f"tan({num}°) = {result}"
                
                elif choice == '8':
                    if num < 0 or num != int(num):
                        print("✗ Factorial only defined for non-negative integers!")
                        continue
                    result = math.factorial(int(num))
                    expression = f"{int(num)}! = {result}"
                
                elif choice == '9':
                    result = abs(num)
                    expression = f"|{num}| = {result}"
                
                print(f"\n✓ Result: {result}")
                history.append(expression)
            
            except Exception as e:
                print(f"✗ Error: {e}")
        
        else:
            print("✗ Invalid choice!")

def statistics_calculator(history):
    """Statistical operations on a list of numbers"""
    print("\n--- Statistics Calculator ---")
    
    numbers = []
    
    # Get numbers from user
    print("\nEnter numbers (type 'done' when finished):")
    
    while True:
        value = input(f"Number {len(numbers) + 1}: ").strip()
        
        if value.lower() == 'done':
            if len(numbers) == 0:
                print("✗ No numbers entered!")
                return
            break
        
        try:
            num = float(value)
            numbers.append(num)
        except ValueError:
            print("✗ Invalid number! Try again.")
    
    # Calculate statistics
    while True:
        print("\n" + "-" * 50)
        print(f"Numbers: {numbers}")
        print("-" * 50)
        print("1. Sum")
        print("2. Average (Mean)")
        print("3. Median")
        print("4. Minimum")
        print("5. Maximum")
        print("6. Range")
        print("7. Count")
        print("8. All Statistics")
        print("9. Back")
        print("-" * 50)
        
        choice = input("Select operation (1-9): ")
        
        if choice == '9':
            break
        
        if choice == '1':
            result = sum(numbers)
            print(f"\n✓ Sum: {result}")
            history.append(f"Sum of {len(numbers)} numbers = {result}")
        
        elif choice == '2':
            result = sum(numbers) / len(numbers)
            print(f"\n✓ Average: {result:.2f}")
            history.append(f"Average of {len(numbers)} numbers = {result:.2f}")
        
        elif choice == '3':
            sorted_nums = sorted(numbers)
            n = len(sorted_nums)
            if n % 2 == 0:
                result = (sorted_nums[n//2 - 1] + sorted_nums[n//2]) / 2
            else:
                result = sorted_nums[n//2]
            print(f"\n✓ Median: {result}")
            history.append(f"Median = {result}")
        
        elif choice == '4':
            result = min(numbers)
            print(f"\n✓ Minimum: {result}")
            history.append(f"Minimum = {result}")
        
        elif choice == '5':
            result = max(numbers)
            print(f"\n✓ Maximum: {result}")
            history.append(f"Maximum = {result}")
        
        elif choice == '6':
            result = max(numbers) - min(numbers)
            print(f"\n✓ Range: {result}")
            history.append(f"Range = {result}")
        
        elif choice == '7':
            print(f"\n✓ Count: {len(numbers)}")
        
        elif choice == '8':
            print("\n" + "=" * 50)
            print("ALL STATISTICS")
            print("=" * 50)
            print(f"Count:      {len(numbers)}")
            print(f"Sum:        {sum(numbers)}")
            print(f"Average:    {sum(numbers) / len(numbers):.2f}")
            print(f"Minimum:    {min(numbers)}")
            print(f"Maximum:    {max(numbers)}")
            print(f"Range:      {max(numbers) - min(numbers)}")
            
            sorted_nums = sorted(numbers)
            n = len(sorted_nums)
            if n % 2 == 0:
                median = (sorted_nums[n//2 - 1] + sorted_nums[n//2]) / 2
            else:
                median = sorted_nums[n//2]
            print(f"Median:     {median}")
            print("=" * 50)
        
        else:
            print("✗ Invalid choice!")

def number_converter(history):
    """Convert numbers between different bases"""
    print("\n--- Number Converter ---")
    
    while True:
        print("\n" + "-" * 50)
        print("1. Decimal to Binary")
        print("2. Decimal to Octal")
        print("3. Decimal to Hexadecimal")
        print("4. Binary to Decimal")
        print("5. Octal to Decimal")
        print("6. Hexadecimal to Decimal")
        print("7. Back")
        print("-" * 50)
        
        choice = input("Select conversion (1-7): ")
        
        if choice == '7':
            break
        
        try:
            if choice == '1':
                num = int(get_number("Enter decimal number: "))
                result = bin(num)[2:]  # Remove '0b' prefix
                print(f"\n✓ Binary: {result}")
                history.append(f"Decimal {num} = Binary {result}")
            
            elif choice == '2':
                num = int(get_number("Enter decimal number: "))
                result = oct(num)[2:]  # Remove '0o' prefix
                print(f"\n✓ Octal: {result}")
                history.append(f"Decimal {num} = Octal {result}")
            
            elif choice == '3':
                num = int(get_number("Enter decimal number: "))
                result = hex(num)[2:].upper()  # Remove '0x' prefix
                print(f"\n✓ Hexadecimal: {result}")
                history.append(f"Decimal {num} = Hexadecimal {result}")
            
            elif choice == '4':
                num = input("Enter binary number: ")
                result = int(num, 2)
                print(f"\n✓ Decimal: {result}")
                history.append(f"Binary {num} = Decimal {result}")
            
            elif choice == '5':
                num = input("Enter octal number: ")
                result = int(num, 8)
                print(f"\n✓ Decimal: {result}")
                history.append(f"Octal {num} = Decimal {result}")
            
            elif choice == '6':
                num = input("Enter hexadecimal number: ")
                result = int(num, 16)
                print(f"\n✓ Decimal: {result}")
                history.append(f"Hexadecimal {num} = Decimal {result}")
            
            else:
                print("✗ Invalid choice!")
        
        except Exception as e:
            print(f"✗ Error: {e}")

def view_history(history):
    """Display calculation history"""
    print("\n" + "=" * 60)
    print("CALCULATION HISTORY")
    print("=" * 60)
    
    if not history:
        print("No calculations yet!")
    else:
        for i, calc in enumerate(history, 1):
            print(f"{i}. {calc}")
    
    print("=" * 60)

def main():
    """Main program"""
    history = []
    
    print("Welcome to Advanced Calculator!")
    print("Perform various calculations with ease!")
    
    # Main loop
    while True:
        display_main_menu()
        choice = input("\nEnter your choice (1-7): ")
        
        if choice == '1':
            basic_calculator(history)
        
        elif choice == '2':
            scientific_calculator(history)
        
        elif choice == '3':
            statistics_calculator(history)
        
        elif choice == '4':
            number_converter(history)
        
        elif choice == '5':
            view_history(history)
        
        elif choice == '6':
            confirm = input("Clear all history? (yes/no): ").lower()
            if confirm in ['yes', 'y']:
                history.clear()
                print("✓ History cleared!")
        
        elif choice == '7':
            print("\n" + "=" * 60)
            print("Thank you for using Advanced Calculator!")
            
            if history:
                print(f"\nYou performed {len(history)} calculations.")
                save = input("Save history before exit? (yes/no): ").lower()
                if save in ['yes', 'y']:
                    print("\nYour calculation history:")
                    view_history(history)
            
            print("\nGoodbye! ")
            print("=" * 60)
            break
        
        else:
            print("\n✗ Invalid choice! Please select 1-7.")

# Run the program
if __name__ == "__main__":
    main()
