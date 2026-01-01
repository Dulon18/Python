# Simple Calculator Program

print("=" * 40)
print("        SIMPLE CALCULATOR")
print("=" * 40)

# Take input from user
num1 = float(input("\nEnter first number: "))
num2 = float(input("Enter second number: "))

# Display menu
print("\nSelect operation:")
print("1. Addition (+)")
print("2. Subtraction (-)")
print("3. Multiplication (*)")
print("4. Division (/)")
print("5. Floor Division (//)")
print("6. Modulus (%)")
print("7. Exponentiation (**)")

# Get user choice
choice = input("\nEnter choice (1-7): ")

# Perform calculation based on choice
print("\n" + "=" * 40)
print("RESULT:")
print("=" * 40)

if choice == '1':
    result = num1 + num2
    print(f"{num1} + {num2} = {result}")
elif choice == '2':
    result = num1 - num2
    print(f"{num1} - {num2} = {result}")
elif choice == '3':
    result = num1 * num2
    print(f"{num1} * {num2} = {result}")
elif choice == '4':
    if num2 != 0:
        result = num1 / num2
        print(f"{num1} / {num2} = {result}")
    else:
        print("Error: Cannot divide by zero!")
elif choice == '5':
    if num2 != 0:
        result = num1 // num2
        print(f"{num1} // {num2} = {result}")
    else:
        print("Error: Cannot divide by zero!")
elif choice == '6':
    if num2 != 0:
        result = num1 % num2
        print(f"{num1} % {num2} = {result}")
    else:
        print("Error: Cannot divide by zero!")
elif choice == '7':
    result = num1 ** num2
    print(f"{num1} ** {num2} = {result}")
else:
    print("Invalid choice!")

print("=" * 40)