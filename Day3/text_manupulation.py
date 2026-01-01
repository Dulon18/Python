# Practice Project: Text Manipulation Tool

print("=" * 50)
print("          TEXT MANIPULATION TOOL")
print("=" * 50)

# Get input from user
text = input("\nEnter a text: ")

# Display menu
while True:
    print("\n" + "-" * 50)
    print("Select an operation:")
    print("1.  Convert to UPPERCASE")
    print("2.  Convert to lowercase")
    print("3.  Convert to Title Case")
    print("4.  Reverse the text")
    print("5.  Count characters")
    print("6.  Count words")
    print("7.  Count specific character")
    print("8.  Replace text")
    print("9.  Remove extra spaces")
    print("10. Check if text contains substring")
    print("0.  Exit")
    print("-" * 50)
    
    choice = input("\nEnter your choice (0-10): ")
    
    if choice == '1':
        print(f"\nResult: {text.upper()}")
    
    elif choice == '2':
        print(f"\nResult: {text.lower()}")
    
    elif choice == '3':
        print(f"\nResult: {text.title()}")
    
    elif choice == '4':
        print(f"\nResult: {text[::-1]}")
    
    elif choice == '5':
        print(f"\nTotal characters: {len(text)}")
        print(f"Characters (no spaces): {len(text.replace(' ', ''))}")
    
    elif choice == '6':
        words = text.split()
        print(f"\nTotal words: {len(words)}")
    
    elif choice == '7':
        char = input("Enter character to count: ")
        count = text.count(char)
        print(f"\n'{char}' appears {count} times")
    
    elif choice == '8':
        old = input("Enter text to replace: ")
        new = input("Enter replacement text: ")
        result = text.replace(old, new)
        print(f"\nResult: {result}")
        update = input("Update original text? (yes/no): ")
        if update.lower() == 'yes':
            text = result
            print("Text updated!")
    
    elif choice == '9':
        result = " ".join(text.split())
        print(f"\nResult: {result}")
    
    elif choice == '10':
        substring = input("Enter text to search: ")
        if substring in text:
            position = text.find(substring)
            print(f"\n✓ Found at position {position}")
        else:
            print(f"\n✗ Not found")
    
    elif choice == '0':
        print("\nThank you for using Text Manipulation Tool!")
        break
    
    else:
        print("\n✗ Invalid choice! Please try again.")