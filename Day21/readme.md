## Day 21 Project: Contact Management System
This project uses everything from Week 3 together in one real application.
Features:

1. Add, view, search, update, delete contacts
2. Data saved to CSV file (persists after closing)
3. Built with OOP (classes)
4. Uses list comprehensions, modules, file handling

# Project Structure

contact_manager/

      │
      ├── contact.py        # Contact class
      ├── manager.py        # ContactManager class
      └── main.py           # Menu / entry point


How to Run

        # Make sure all 3 files are in the same folder, then:
        python main.py

# Week 3 Concepts Used in This Project

| Concept | Where Used |
|---------|------------|
| File Handling (Day 15) | `load_from_file()`, `save_to_file()` with CSV |
| Modules (Day 16) | `contact.py`, `manager.py`, `main.py` as separate modules |
| List Comprehensions (Day 17) | Loading contacts, searching, deleting, summary |
| OOP Part 1 (Day 18) | `Contact` class with `__init__`, attributes, methods |
| OOP Part 2 (Day 19) | Encapsulation, `__str__`, class-level variables |
| Libraries (Day 20) | `csv`, `os` built-in modules |

You've now completed Week 3 fully! Ready to move into Week 4 — Advanced Topics.
