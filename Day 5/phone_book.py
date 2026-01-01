
# Practice Project: Phone Book Application
# Build a comprehensive phone book using dictionaries.

# Phone Book Application

def display_menu():
    """Display main menu"""
    print("\n" + "=" * 60)
    print("                   PHONE BOOK")
    print("=" * 60)
    print("1.  Add new contact")
    print("2.  Search contact")
    print("3.  Update contact")
    print("4.  Delete contact")
    print("5.  View all contacts")
    print("6.  View contacts by category")
    print("7.  Get statistics")
    print("8.  Export contacts")
    print("9.  Remove duplicates")
    print("10. Exit")
    print("=" * 60)

def add_contact(phonebook):
    """Add a new contact"""
    print("\n--- Add New Contact ---")
    name = input("Enter name: ").strip().title()
    
    if name in phonebook:
        print(f"✗ Contact '{name}' already exists!")
        return
    
    phone = input("Enter phone number: ").strip()
    email = input("Enter email (optional): ").strip()
    category = input("Enter category (Family/Friend/Work): ").strip().title()
    
    phonebook[name] = {
        "phone": phone,
        "email": email if email else "N/A",
        "category": category if category else "General"
    }
    
    print(f"✓ Contact '{name}' added successfully!")

def search_contact(phonebook):
    """Search for a contact"""
    if not phonebook:
        print("\n✗ Phone book is empty!")
        return
    
    name = input("\nEnter name to search: ").strip().title()
    
    if name in phonebook:
        contact = phonebook[name]
        print("\n" + "-" * 50)
        print(f"Name:     {name}")
        print(f"Phone:    {contact['phone']}")
        print(f"Email:    {contact['email']}")
        print(f"Category: {contact['category']}")
        print("-" * 50)
    else:
        print(f"\n✗ Contact '{name}' not found!")

def update_contact(phonebook):
    """Update existing contact"""
    if not phonebook:
        print("\n✗ Phone book is empty!")
        return
    
    name = input("\nEnter name to update: ").strip().title()
    
    if name not in phonebook:
        print(f"✗ Contact '{name}' not found!")
        return
    
    print(f"\nCurrent details for {name}:")
    print(f"Phone: {phonebook[name]['phone']}")
    print(f"Email: {phonebook[name]['email']}")
    print(f"Category: {phonebook[name]['category']}")
    
    print("\nEnter new details (press Enter to keep current):")
    
    phone = input("New phone number: ").strip()
    email = input("New email: ").strip()
    category = input("New category: ").strip().title()
    
    if phone:
        phonebook[name]['phone'] = phone
    if email:
        phonebook[name]['email'] = email
    if category:
        phonebook[name]['category'] = category
    
    print(f"✓ Contact '{name}' updated successfully!")

def delete_contact(phonebook):
    """Delete a contact"""
    if not phonebook:
        print("\n✗ Phone book is empty!")
        return
    
    name = input("\nEnter name to delete: ").strip().title()
    
    if name in phonebook:
        confirm = input(f"  Delete '{name}'? (yes/no): ")
        if confirm.lower() == 'yes':
            del phonebook[name]
            print(f"✓ Contact '{name}' deleted successfully!")
        else:
            print("✗ Deletion cancelled")
    else:
        print(f"✗ Contact '{name}' not found!")

def view_all_contacts(phonebook):
    """Display all contacts"""
    if not phonebook:
        print("\n✗ Phone book is empty!")
        return
    
    print("\n" + "=" * 70)
    print(f"{'Name':<20} {'Phone':<15} {'Email':<20} {'Category':<15}")
    print("=" * 70)
    
    for name in sorted(phonebook.keys()):
        contact = phonebook[name]
        print(f"{name:<20} {contact['phone']:<15} {contact['email']:<20} {contact['category']:<15}")
    
    print("=" * 70)
    print(f"Total contacts: {len(phonebook)}")

def view_by_category(phonebook):
    """View contacts by category"""
    if not phonebook:
        print("\n✗ Phone book is empty!")
        return
    
    # Get all unique categories
    categories = set(contact['category'] for contact in phonebook.values())
    
    print("\nAvailable categories:")
    for i, cat in enumerate(sorted(categories), 1):
        print(f"{i}. {cat}")
    
    category = input("\nEnter category name: ").strip().title()
    
    # Filter contacts by category
    filtered = {name: info for name, info in phonebook.items() 
                if info['category'] == category}
    
    if filtered:
        print(f"\n--- Contacts in '{category}' ---")
        for name, info in sorted(filtered.items()):
            print(f"{name}: {info['phone']}")
        print(f"\nTotal: {len(filtered)} contacts")
    else:
        print(f"\n✗ No contacts found in category '{category}'")

def get_statistics(phonebook):
    """Show phone book statistics"""
    if not phonebook:
        print("\n✗ Phone book is empty!")
        return
    
    # Count by category
    categories = {}
    for contact in phonebook.values():
        cat = contact['category']
        categories[cat] = categories.get(cat, 0) + 1
    
    # Count emails
    with_email = sum(1 for c in phonebook.values() if c['email'] != "N/A")
    
    print("\n" + "=" * 50)
    print("STATISTICS")
    print("=" * 50)
    print(f"Total contacts:        {len(phonebook)}")
    print(f"Contacts with email:   {with_email}")
    print(f"Contacts without email: {len(phonebook) - with_email}")
    
    print("\nContacts by category:")
    for cat, count in sorted(categories.items()):
        print(f"  {cat}: {count}")
    print("=" * 50)

def export_contacts(phonebook):
    """Export contacts to formatted text"""
    if not phonebook:
        print("\n✗ Phone book is empty!")
        return
    
    print("\n--- Exported Contacts ---")
    for name in sorted(phonebook.keys()):
        contact = phonebook[name]
        print(f"\nName: {name}")
        print(f"Phone: {contact['phone']}")
        print(f"Email: {contact['email']}")
        print(f"Category: {contact['category']}")
        print("-" * 30)
    
    print("\n✓ Export complete!")

def remove_duplicates(phonebook):
    """Remove duplicate phone numbers"""
    if not phonebook:
        print("\n✗ Phone book is empty!")
        return
    
    # Find duplicates
    phone_numbers = {}
    for name, info in phonebook.items():
        phone = info['phone']
        if phone in phone_numbers:
            phone_numbers[phone].append(name)
        else:
            phone_numbers[phone] = [name]
    
    # Filter duplicates
    duplicates = {phone: names for phone, names in phone_numbers.items() 
                  if len(names) > 1}
    
    if not duplicates:
        print("\n✓ No duplicate phone numbers found!")
        return
    
    print("\n  Duplicate phone numbers found:")
    for phone, names in duplicates.items():
        print(f"\nPhone: {phone}")
        print(f"Names: {', '.join(names)}")
        print("Which one to keep?")
        for i, name in enumerate(names, 1):
            print(f"{i}. {name}")
        
        choice = input("Enter number to keep (others will be deleted): ")
        try:
            keep_index = int(choice) - 1
            if 0 <= keep_index < len(names):
                keep_name = names[keep_index]
                for name in names:
                    if name != keep_name:
                        del phonebook[name]
                        print(f"✓ Deleted '{name}'")
        except ValueError:
            print("✗ Invalid input!")

def main():
    """Main program"""
    phonebook = {}
    
    print("Welcome to Phone Book Application!")
    
    while True:
        display_menu()
        choice = input("\nEnter your choice (1-10): ")
        
        if choice == '1':
            add_contact(phonebook)
        elif choice == '2':
            search_contact(phonebook)
        elif choice == '3':
            update_contact(phonebook)
        elif choice == '4':
            delete_contact(phonebook)
        elif choice == '5':
            view_all_contacts(phonebook)
        elif choice == '6':
            view_by_category(phonebook)
        elif choice == '7':
            get_statistics(phonebook)
        elif choice == '8':
            export_contacts(phonebook)
        elif choice == '9':
            remove_duplicates(phonebook)
        elif choice == '10':
            print("\n Thank you for using Phone Book!")
            print("Stay connected! ")
            break
        else:
            print("\n✗ Invalid choice! Please try again.")

# Run the program
if __name__ == "__main__":
    main()

