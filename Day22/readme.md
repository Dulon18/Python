# Week 4: Advanced Topics
Let's go day by day!
#  Day 22: Regular Expressions (Regex) in Python

> **Week 4 — Advanced Topics** | 30-Day Python Learning Plan

Regular expressions are patterns used to **search, match, and manipulate text**. Python has a built-in `re` module for this.

---

## 📦 Importing the `re` Module

```python
import re
```

---

## ⚙️ Basic Functions

| Function | What it does |
|---|---|
| `re.match()` | Match pattern at the **start** of string |
| `re.search()` | Search **anywhere** in string |
| `re.findall()` | Return **all matches** as a list |
| `re.sub()` | **Replace** matches with something else |
| `re.split()` | **Split** string by pattern |

```python
import re

text = "My phone is 0123456789 and email is ali@gmail.com"

# search — finds first match anywhere
result = re.search(r'\d+', text)
print(result.group())  # 0123456789

# findall — finds all matches
numbers = re.findall(r'\d+', text)
print(numbers)  # ['0123456789']

# sub — replace matches
clean = re.sub(r'\d+', '***', text)
print(clean)  # My phone is *** and email is ali@gmail.com

# split
parts = re.split(r'\s+', "Hello   World   Python")
print(parts)  # ['Hello', 'World', 'Python']
```

---

## 🔣 Common Patterns

| Pattern | Matches |
|---|---|
| `\d` | Any digit (0–9) |
| `\D` | Any non-digit |
| `\w` | Any word character (a-z, A-Z, 0-9, _) |
| `\W` | Any non-word character |
| `\s` | Any whitespace |
| `\S` | Any non-whitespace |
| `.` | Any character except newline |
| `^` | Start of string |
| `$` | End of string |
| `+` | One or more |
| `*` | Zero or more |
| `?` | Zero or one |
| `{n}` | Exactly n times |
| `{n,m}` | Between n and m times |

---

## 💡 Practical Examples

```python
import re

# --- Email Validator ---
def is_valid_email(email):
    pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z]{2,}$'
    return bool(re.match(pattern, email))

print(is_valid_email("ali@gmail.com"))     # True
print(is_valid_email("ali@.com"))          # False
print(is_valid_email("notanemail"))        # False


# --- Phone Number Validator ---
def is_valid_phone(phone):
    pattern = r'^\+?\d{10,13}$'
    return bool(re.match(pattern, phone))

print(is_valid_phone("01712345678"))        # True
print(is_valid_phone("123"))               # False
print(is_valid_phone("+8801712345678"))     # True


# --- Extract all emails from text ---
text = "Contact us at support@site.com or sales@company.org for help."
emails = re.findall(r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z]{2,}', text)
print(emails)  # ['support@site.com', 'sales@company.org']


# --- Extract dates ---
text = "Meeting on 2024-01-15 and deadline is 2024-02-28"
dates = re.findall(r'\d{4}-\d{2}-\d{2}', text)
print(dates)  # ['2024-01-15', '2024-02-28']
```

---

## 🎯 Groups — Extracting Specific Parts

Use `()` to capture specific parts of a match.

```python
import re

# Extract username and domain from email separately
email = "ali@gmail.com"
match = re.match(r'([a-zA-Z0-9_.+-]+)@([a-zA-Z0-9-]+\.[a-zA-Z]{2,})', email)

if match:
    print(match.group(0))  # full match : ali@gmail.com
    print(match.group(1))  # username   : ali
    print(match.group(2))  # domain     : gmail.com
```

---

## 🛠️ Practice Project — Email & Phone Validator Tool

```python
import re

def validate_email(email):
    pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z]{2,}$'
    if re.match(pattern, email):
        print(f"✓ '{email}' is a valid email.")
    else:
        print(f"✗ '{email}' is NOT a valid email.")

def validate_phone(phone):
    pattern = r'^\+?\d{10,13}$'
    if re.match(pattern, phone):
        print(f"✓ '{phone}' is a valid phone number.")
    else:
        print(f"✗ '{phone}' is NOT a valid phone number.")

def extract_info(text):
    emails = re.findall(r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z]{2,}', text)
    phones = re.findall(r'\+?\d{10,13}', text)
    print(f"Emails found : {emails}")
    print(f"Phones found : {phones}")

# --- Menu ---
while True:
    print("\n1. Validate Email")
    print("2. Validate Phone")
    print("3. Extract from text")
    print("4. Exit")

    choice = input("Choose: ")

    if choice == "1":
        email = input("Enter email: ")
        validate_email(email)
    elif choice == "2":
        phone = input("Enter phone: ")
        validate_phone(phone)
    elif choice == "3":
        text = input("Paste your text: ")
        extract_info(text)
    elif choice == "4":
        break
```

---

## 📝 Quick Summary

| Concept | Key Point |
|---|---|
| `re.match()` | Matches only at the **start** of string |
| `re.search()` | Matches **anywhere** in string |
| `re.findall()` | Returns a **list** of all matches |
| `re.sub()` | **Replaces** matched patterns |
| `re.split()` | **Splits** string on a pattern |
| `()` groups | Extracts **specific parts** of a match |
| Raw strings `r''` | Always use `r''` to avoid escape issues |

---

## 🔗 Resources

- [Python `re` Module Docs](https://docs.python.org/3/library/re.html)
- [Regex101 — Test your patterns online](https://regex101.com)
- [RegexLearn — Interactive regex tutorial](https://regexlearn.com)

---

> 📅 Part of the **30-Day Python Learning Plan**
> Previous: [Day 21 - OOP & File Persistence Project](#) | Next: [Day 23 - Decorators & Generators](#)
