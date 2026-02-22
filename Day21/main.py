# main.py

from manager import ContactManager

def print_menu():
    print("\n" + "="*40)
    print("     CONTACT MANAGEMENT SYSTEM")
    print("="*40)
    print("1. Add Contact")
    print("2. View All Contacts")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Show Summary")
    print("7. Exit")
    print("="*40)

def get_input(prompt, required=True):
    """Helper to get non-empty input"""
    while True:
        value = input(prompt).strip()
        if value or not required:
            return value
        print("This field cannot be empty.")

def main():
    manager = ContactManager()

    while True:
        print_menu()
        choice = input("Enter your choice (1-7): ").strip()

        if choice == "1":
            print("\n-- Add New Contact --")
            name  = get_input("Name  : ")
            phone = get_input("Phone : ")
            email = get_input("Email : ")
            city  = get_input("City  : ")
            manager.add_contact(name, phone, email, city)

        elif choice == "2":
            manager.view_all()

        elif choice == "3":
            print("\n-- Search Contact --")
            keyword = get_input("Enter name or city to search: ")
            manager.search_contact(keyword)

        elif choice == "4":
            print("\n-- Update Contact --")
            phone = get_input("Enter phone number of contact to update: ")
            manager.update_contact(phone)

        elif choice == "5":
            print("\n-- Delete Contact --")
            phone = get_input("Enter phone number of contact to delete: ")
            confirm = input(f"Are you sure you want to delete? (yes/no): ")
            if confirm.lower() == "yes":
                manager.delete_contact(phone)
            else:
                print("Deletion cancelled.")

        elif choice == "6":
            manager.show_summary()

        elif choice == "7":
            print("\nGoodbye! Your contacts are saved.")
            break

        else:
            print("Invalid choice. Please enter 1-7.")

if __name__ == "__main__":
    main()
