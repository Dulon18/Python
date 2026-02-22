# manager.py

import csv
import os
from contact import Contact

class ContactManager:
    
    FILENAME = "contacts.csv"
    FIELDS = ["name", "phone", "email", "city"]

    def __init__(self):
        self.contacts = []
        self.load_from_file()  # load existing contacts on startup

    # -------- File Handling --------

    def load_from_file(self):
        """Load contacts from CSV file at startup"""
        if not os.path.exists(self.FILENAME):
            return  # no file yet, start fresh
        
        try:
            with open(self.FILENAME, "r", newline="") as f:
                reader = csv.DictReader(f)
                self.contacts = [
                    Contact(row["name"], row["phone"], row["email"], row["city"])
                    for row in reader  # list comprehension (Day 17)
                ]
            print(f"Loaded {len(self.contacts)} contacts from file.")
        except Exception as e:
            print(f"Error loading file: {e}")

    def save_to_file(self):
        """Save all contacts to CSV file"""
        try:
            with open(self.FILENAME, "w", newline="") as f:
                writer = csv.DictWriter(f, fieldnames=self.FIELDS)
                writer.writeheader()
                writer.writerows([c.to_dict() for c in self.contacts])  # list comprehension
        except Exception as e:
            print(f"Error saving file: {e}")

    # -------- Core Features --------

    def add_contact(self, name, phone, email, city):
        """Add a new contact"""
        # Check for duplicate phone number
        existing = [c for c in self.contacts if c.phone == phone]
        if existing:
            print("A contact with this phone number already exists!")
            return
        
        new_contact = Contact(name, phone, email, city)
        self.contacts.append(new_contact)
        self.save_to_file()
        print(f"Contact '{name}' added successfully!")

    def view_all(self):
        """Display all contacts"""
        if not self.contacts:
            print("No contacts found.")
            return
        
        print(f"\n{'='*40}")
        print(f"   ALL CONTACTS ({len(self.contacts)} total)")
        print(f"{'='*40}")
        for i, contact in enumerate(self.contacts, 1):
            print(f"\n[{i}]")
            print(contact)  # calls __str__
            print("-" * 40)

    def search_contact(self, keyword):
        """Search contacts by name or city"""
        keyword = keyword.lower()
        results = [
            c for c in self.contacts
            if keyword in c.name.lower() or keyword in c.city.lower()
        ]  # list comprehension with condition (Day 17)

        if not results:
            print("No matching contacts found.")
            return
        
        print(f"\nFound {len(results)} result(s):")
        for contact in results:
            print(f"\n{contact}")
            print("-" * 40)

    def update_contact(self, phone):
        """Update a contact by phone number"""
        for contact in self.contacts:
            if contact.phone == phone:
                print(f"\nFound: {contact.name}")
                print("Leave blank to keep existing value.\n")

                new_name = input(f"New name ({contact.name}): ").strip()
                new_phone = input(f"New phone ({contact.phone}): ").strip()
                new_email = input(f"New email ({contact.email}): ").strip()
                new_city = input(f"New city ({contact.city}): ").strip()

                # Only update if user entered something
                if new_name:
                    contact.name = new_name
                if new_phone:
                    contact.phone = new_phone
                if new_email:
                    contact.email = new_email
                if new_city:
                    contact.city = new_city

                self.save_to_file()
                print("Contact updated successfully!")
                return
        
        print("No contact found with that phone number.")

    def delete_contact(self, phone):
        """Delete a contact by phone number"""
        original_count = len(self.contacts)
        
        # Keep all contacts except the one to delete
        self.contacts = [c for c in self.contacts if c.phone != phone]

        if len(self.contacts) < original_count:
            self.save_to_file()
            print("Contact deleted successfully!")
        else:
            print("No contact found with that phone number.")

    def show_summary(self):
        """Show a quick summary using list comprehensions"""
        if not self.contacts:
            print("No contacts to summarize.")
            return
        
        cities = list(set([c.city for c in self.contacts]))  # unique cities
        names = [c.name for c in self.contacts]

        print(f"\n--- Summary ---")
        print(f"Total Contacts : {len(self.contacts)}")
        print(f"Cities covered : {', '.join(cities)}")
        print(f"All names      : {', '.join(names)}")
