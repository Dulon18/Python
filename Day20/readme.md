# Day 20: File Handling — Complete Guide

---

## 1. Opening & Closing Files

The basic way to open a file in Python is using `open()`.

```python
f = open("notes.txt", "w")
f.write("Hello!")
f.close()  # always close after using
```

But manually closing is risky — if an error happens before `f.close()`, the file stays open. That's why we use `with` instead.

---

## 2. The `with` Statement (Context Manager)

`with` automatically closes the file for you, even if an error occurs.

```python
with open("notes.txt", "w") as f:
    f.write("Hello, Python!")
# file is automatically closed here
```

Always prefer `with` over manually opening and closing files.

---

## 3. File Modes

When you open a file, you tell Python what you want to do with it using a mode.

| Mode | Meaning |
|---|---|
| `"r"` | Read (default) — file must exist |
| `"w"` | Write — creates file or overwrites existing |
| `"a"` | Append — adds to end without deleting |
| `"x"` | Create — fails if file already exists |
| `"rb"` | Read in binary mode (images, PDFs etc.) |
| `"wb"` | Write in binary mode |

```python
# Write mode — creates or overwrites
with open("demo.txt", "w") as f:
    f.write("First line\n")

# Append mode — adds to existing content
with open("demo.txt", "a") as f:
    f.write("Second line\n")

# Read mode
with open("demo.txt", "r") as f:
    print(f.read())
```

---

## 4. Writing to Files

```python
with open("story.txt", "w") as f:
    f.write("Once upon a time...\n")
    f.write("There was a Python developer.\n")
```

To write multiple lines at once use `writelines()`:

```python
lines = ["Line 1\n", "Line 2\n", "Line 3\n"]

with open("story.txt", "w") as f:
    f.writelines(lines)
```

Note that `writelines()` does not add `\n` automatically — you have to include it yourself.

---

## 5. Reading from Files

There are three ways to read a file:

```python
# read() — reads entire file as one string
with open("story.txt", "r") as f:
    content = f.read()
    print(content)
```

```python
# readline() — reads one line at a time
with open("story.txt", "r") as f:
    line1 = f.readline()
    line2 = f.readline()
    print(line1)
    print(line2)
```

```python
# readlines() — reads all lines into a list
with open("story.txt", "r") as f:
    lines = f.readlines()
    print(lines)  # ['Line 1\n', 'Line 2\n', 'Line 3\n']
```

The most common and cleanest way to read line by line:

```python
with open("story.txt", "r") as f:
    for line in f:
        print(line.strip())  # strip() removes the \n at the end
```

---

## 6. Checking if a File Exists

Before reading a file, it's good practice to check if it exists to avoid errors.

```python
import os

if os.path.exists("notes.txt"):
    with open("notes.txt", "r") as f:
        print(f.read())
else:
    print("File not found!")
```

---

## 7. Working with CSV Files

CSV (Comma Separated Values) is one of the most common formats for storing data. Python has a built-in `csv` module for this.

### Writing a CSV file:

```python
import csv

students = [
    ["Name", "Age", "Grade"],  # header row
    ["Ali", 20, "A"],
    ["Sara", 22, "B"],
    ["John", 21, "A+"]
]

with open("students.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerows(students)
```

Always use `newline=""` when opening CSV files on Windows to avoid extra blank lines.

### Reading a CSV file:

```python
import csv

with open("students.csv", "r") as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)

# Output:
# ['Name', 'Age', 'Grade']
# ['Ali', '20', 'A']
# ['Sara', '22', 'B']
```

### Using DictReader and DictWriter (cleaner way):

Instead of using index numbers like `row[0]`, `row[1]`, you can use column names.

```python
import csv

# Writing with DictWriter
students = [
    {"Name": "Ali", "Age": 20, "Grade": "A"},
    {"Name": "Sara", "Age": 22, "Grade": "B"},
]

with open("students.csv", "w", newline="") as f:
    fieldnames = ["Name", "Age", "Grade"]
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(students)

# Reading with DictReader
with open("students.csv", "r") as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(row["Name"], row["Grade"])
```

---

## 8. File Handling with Exception Handling

Always combine file handling with try/except to handle errors gracefully (you learned this on Day 13).

```python
try:
    with open("data.txt", "r") as f:
        content = f.read()
        print(content)
except FileNotFoundError:
    print("Error: File does not exist!")
except PermissionError:
    print("Error: You don't have permission to read this file!")
```

---

## 9. Practical Mini Project — Note Taking App

This pulls everything together:

```python
import os

FILENAME = "notes.txt"

def add_note(note):
    with open(FILENAME, "a") as f:
        f.write(note + "\n")
    print("Note saved!")

def view_notes():
    if not os.path.exists(FILENAME):
        print("No notes yet.")
        return
    with open(FILENAME, "r") as f:
        notes = f.readlines()
    if not notes:
        print("No notes found.")
    else:
        print("\n--- Your Notes ---")
        for i, note in enumerate(notes, 1):
            print(f"{i}. {note.strip()}")

def delete_notes():
    with open(FILENAME, "w") as f:
        f.write("")
    print("All notes deleted.")

# Menu
while True:
    print("\n1. Add Note")
    print("2. View Notes")
    print("3. Delete All Notes")
    print("4. Quit")
    
    choice = input("Choose: ")
    
    if choice == "1":
        note = input("Enter your note: ")
        add_note(note)
    elif choice == "2":
        view_notes()
    elif choice == "3":
        delete_notes()
    elif choice == "4":
        break
    else:
        print("Invalid choice, try again.")
```

---

## Quick Summary

| Topic | Key Point |
|---|---|
| `open()` | Opens a file, always specify mode |
| `with` statement | Best practice, auto-closes file |
| File modes | `r`, `w`, `a`, `x`, `rb`, `wb` |
| `read()` | Entire file as string |
| `readline()` | One line at a time |
| `readlines()` | All lines as a list |
| `write()` | Write a string to file |
| `writelines()` | Write a list to file |
| `csv` module | Read/write structured data |
| `DictReader/Writer` | Access CSV columns by name |
| `os.path.exists()` | Check if file exists before opening |

---

You now have a complete understanding of Day 20. You're fully caught up and ready to move forward confidently!
