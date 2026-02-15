# Day 19: Working with Libraries

## Overview
Today we'll explore popular Python libraries! Learn to make HTTP requests, work with data, create visualizations, and leverage the vast Python ecosystem. This unlocks Python's true power!

---

## 1. Introduction to Python Libraries

### The Python Ecosystem

Python has 400,000+ packages available on PyPI (Python Package Index). Libraries extend Python's capabilities for:
- 🌐 Web development (Flask, Django)
- 📊 Data analysis (Pandas, NumPy)
- 🤖 Machine learning (Scikit-learn, TensorFlow)
- 📈 Visualization (Matplotlib, Plotly)
- 🔧 Utilities (Requests, Beautiful Soup)

### Installing Libraries

```bash
# Install a library
pip install requests

# Install specific version
pip install requests==2.28.0

# Install multiple libraries
pip install requests pandas matplotlib

# Upgrade a library
pip install --upgrade requests

# Uninstall
pip uninstall requests
```

---

## 2. requests - HTTP Library

### Making HTTP Requests

```python
import requests

# GET request
response = requests.get('https://api.github.com')
print(response.status_code)  # 200
print(response.json())        # Parse JSON response

# GET with parameters
params = {'q': 'python', 'sort': 'stars'}
response = requests.get('https://api.github.com/search/repositories', params=params)
data = response.json()

# POST request
data = {'username': 'alice', 'password': 'secret'}
response = requests.post('https://httpbin.org/post', json=data)

# Headers
headers = {'Authorization': 'Bearer YOUR_TOKEN'}
response = requests.get('https://api.example.com/data', headers=headers)
```

### Working with APIs

```python
import requests

def get_github_user(username):
    """Get GitHub user information."""
    url = f'https://api.github.com/users/{username}'
    response = requests.get(url)
    
    if response.status_code == 200:
        return response.json()
    else:
        return None

# Usage
user = get_github_user('torvalds')
if user:
    print(f"Name: {user['name']}")
    print(f"Followers: {user['followers']}")
    print(f"Public repos: {user['public_repos']}")
```

### Error Handling

```python
import requests

try:
    response = requests.get('https://api.example.com/data', timeout=5)
    response.raise_for_status()  # Raise exception for bad status codes
    data = response.json()
except requests.exceptions.Timeout:
    print("Request timed out")
except requests.exceptions.ConnectionError:
    print("Connection error")
except requests.exceptions.HTTPError as e:
    print(f"HTTP error: {e}")
except Exception as e:
    print(f"Error: {e}")
```

---

## 3. datetime - Date and Time

### Working with Dates

```python
from datetime import datetime, date, time, timedelta

# Current date and time
now = datetime.now()
print(now)  # 2024-01-31 15:30:45.123456

today = date.today()
print(today)  # 2024-01-31

# Create specific dates
birthday = date(2000, 5, 15)
meeting = datetime(2024, 2, 1, 14, 30)  # 2:30 PM

# Date arithmetic
tomorrow = today + timedelta(days=1)
next_week = today + timedelta(weeks=1)
yesterday = today - timedelta(days=1)

# Calculate age
age = today.year - birthday.year
print(f"Age: {age}")

# Time difference
event = datetime(2024, 12, 31, 23, 59)
time_until = event - now
print(f"Days until: {time_until.days}")
```

### Formatting Dates

```python
from datetime import datetime

now = datetime.now()

# Format date to string
formatted = now.strftime("%Y-%m-%d %H:%M:%S")
print(formatted)  # 2024-01-31 15:30:45

# Common formats
print(now.strftime("%B %d, %Y"))      # January 31, 2024
print(now.strftime("%m/%d/%Y"))       # 01/31/2024
print(now.strftime("%I:%M %p"))       # 03:30 PM

# Parse string to date
date_str = "2024-01-31"
parsed = datetime.strptime(date_str, "%Y-%m-%d")
```

---

## 4. random - Random Numbers

### Random Operations

```python
import random

# Random integer
num = random.randint(1, 100)  # 1 to 100 inclusive

# Random float
flt = random.random()  # 0.0 to 1.0
flt = random.uniform(1.5, 10.5)  # Between 1.5 and 10.5

# Random choice
colors = ['red', 'blue', 'green', 'yellow']
color = random.choice(colors)

# Multiple choices (with replacement)
choices = random.choices(colors, k=3)  # Pick 3 with replacement

# Random sample (without replacement)
sample = random.sample(range(1, 50), 6)  # Pick 6 unique numbers

# Shuffle list
deck = list(range(52))
random.shuffle(deck)

# Random seed (for reproducibility)
random.seed(42)
print(random.randint(1, 10))  # Same result each time
```

---

## 5. json - JSON Handling

### Working with JSON

```python
import json

# Python dict to JSON string
data = {
    "name": "Alice",
    "age": 25,
    "email": "alice@email.com",
    "hobbies": ["reading", "coding"]
}

# Serialize to JSON string
json_string = json.dumps(data, indent=2)
print(json_string)

# Parse JSON string to Python
json_data = '{"name": "Bob", "age": 30}'
parsed = json.loads(json_data)
print(parsed["name"])  # Bob

# Write to JSON file
with open('data.json', 'w') as f:
    json.dump(data, f, indent=2)

# Read from JSON file
with open('data.json', 'r') as f:
    loaded = json.load(f)
```

---

## 6. collections - Container Datatypes

### Counter

```python
from collections import Counter

# Count occurrences
words = ['apple', 'banana', 'apple', 'orange', 'banana', 'apple']
counter = Counter(words)

print(counter)  # Counter({'apple': 3, 'banana': 2, 'orange': 1})
print(counter['apple'])  # 3
print(counter.most_common(2))  # [('apple', 3), ('banana', 2)]

# Count characters
text = "hello world"
char_count = Counter(text)
print(char_count)
```

### defaultdict

```python
from collections import defaultdict

# Dict with default values
dd = defaultdict(int)  # Default value: 0
dd['count'] += 1  # No KeyError!

# Group items
dd = defaultdict(list)
pairs = [('fruit', 'apple'), ('veggie', 'carrot'), ('fruit', 'banana')]

for category, item in pairs:
    dd[category].append(item)

print(dict(dd))  # {'fruit': ['apple', 'banana'], 'veggie': ['carrot']}
```

### namedtuple

```python
from collections import namedtuple

# Create named tuple
Point = namedtuple('Point', ['x', 'y'])
p = Point(10, 20)

print(p.x)  # 10
print(p.y)  # 20

# More readable than regular tuple
Person = namedtuple('Person', ['name', 'age', 'city'])
person = Person('Alice', 25, 'NYC')
print(person.name)  # Alice
```

---

## 7. pathlib - File Paths

### Modern Path Handling

```python
from pathlib import Path

# Create path
path = Path('documents/file.txt')

# Path operations
print(path.name)       # file.txt
print(path.stem)       # file
print(path.suffix)     # .txt
print(path.parent)     # documents

# Check existence
if path.exists():
    print("File exists")

# Create directory
Path('new_folder').mkdir(exist_ok=True)

# List files
for file in Path('.').glob('*.py'):
    print(file)

# Read/write files
path.write_text('Hello, World!')
content = path.read_text()
```

---

## 8. re - Regular Expressions

### Pattern Matching

```python
import re

text = "My email is user@example.com and phone is 123-456-7890"

# Search for pattern
email_pattern = r'\w+@\w+\.\w+'
match = re.search(email_pattern, text)
if match:
    print(match.group())  # user@example.com

# Find all matches
phone_pattern = r'\d{3}-\d{3}-\d{4}'
phones = re.findall(phone_pattern, text)
print(phones)  # ['123-456-7890']

# Replace pattern
censored = re.sub(r'\d{3}-\d{3}-\d{4}', 'XXX-XXX-XXXX', text)
print(censored)

# Split by pattern
parts = re.split(r'[,.]', 'apple,banana.orange')
print(parts)  # ['apple', 'banana', 'orange']
```

### Common Patterns

```python
import re

# Email validation
def is_valid_email(email):
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return bool(re.match(pattern, email))

# Extract URLs
def extract_urls(text):
    pattern = r'https?://\S+'
    return re.findall(pattern, text)

# Extract numbers
def extract_numbers(text):
    pattern = r'\d+'
    return [int(n) for n in re.findall(pattern, text)]
```

---

## 9. Working with CSV Files

### Using csv Module

```python
import csv

# Write CSV
data = [
    ['Name', 'Age', 'City'],
    ['Alice', 25, 'NYC'],
    ['Bob', 30, 'LA'],
    ['Charlie', 35, 'Chicago']
]

with open('people.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerows(data)

# Read CSV
with open('people.csv', 'r') as f:
    reader = csv.reader(f)
    header = next(reader)  # Skip header
    for row in reader:
        name, age, city = row
        print(f"{name} is {age} years old from {city}")

# CSV with dict
with open('people.csv', 'r') as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(f"{row['Name']} - {row['City']}")
```

---

## 10. argparse - Command Line Arguments

### Creating CLI Tools

```python
import argparse

def main():
    # Create parser
    parser = argparse.ArgumentParser(description='Process some data')
    
    # Add arguments
    parser.add_argument('filename', help='Input file name')
    parser.add_argument('-o', '--output', help='Output file name')
    parser.add_argument('-v', '--verbose', action='store_true', 
                        help='Verbose output')
    parser.add_argument('-n', '--number', type=int, default=10,
                        help='Number of items')
    
    # Parse arguments
    args = parser.parse_args()
    
    print(f"Input: {args.filename}")
    if args.output:
        print(f"Output: {args.output}")
    if args.verbose:
        print("Verbose mode enabled")
    print(f"Number: {args.number}")

if __name__ == '__main__':
    main()

# Usage:
# python script.py input.txt -o output.txt -v -n 20
```

---

## 11. Practical Examples

### Example 1: Weather Checker

```python
import requests

def get_weather(city):
    """
    Get weather for a city.
    Note: Requires API key from openweathermap.org
    """
    api_key = "YOUR_API_KEY"
    url = f"http://api.openweathermap.org/data/2.5/weather"
    params = {
        'q': city,
        'appid': api_key,
        'units': 'metric'
    }
    
    try:
        response = requests.get(url, params=params, timeout=5)
        response.raise_for_status()
        data = response.json()
        
        return {
            'city': data['name'],
            'temp': data['main']['temp'],
            'description': data['weather'][0]['description'],
            'humidity': data['main']['humidity']
        }
    except Exception as e:
        return None
```

### Example 2: File Organizer

```python
from pathlib import Path
import shutil

def organize_files(directory):
    """Organize files by extension."""
    path = Path(directory)
    
    for file in path.iterdir():
        if file.is_file():
            # Get file extension
            ext = file.suffix.lstrip('.')
            if not ext:
                ext = 'no_extension'
            
            # Create folder for extension
            ext_folder = path / ext
            ext_folder.mkdir(exist_ok=True)
            
            # Move file
            try:
                shutil.move(str(file), str(ext_folder / file.name))
                print(f"Moved {file.name} to {ext}/")
            except Exception as e:
                print(f"Error moving {file.name}: {e}")
```

### Example 3: Data Analyzer

```python
import json
from collections import Counter
from datetime import datetime

def analyze_log_file(filename):
    """Analyze JSON log file."""
    with open(filename, 'r') as f:
        logs = [json.loads(line) for line in f]
    
    # Count by level
    levels = Counter(log['level'] for log in logs)
    
    # Count by hour
    hours = Counter(
        datetime.fromisoformat(log['timestamp']).hour 
        for log in logs
    )
    
    # Most common errors
    errors = [log for log in logs if log['level'] == 'ERROR']
    error_messages = Counter(log['message'] for log in errors)
    
    return {
        'total_logs': len(logs),
        'by_level': dict(levels),
        'by_hour': dict(hours),
        'top_errors': error_messages.most_common(5)
    }
```

---

## Practice Exercises

### Exercise 1: API Client
Create a program that:
- Fetches data from a public API
- Parses JSON response
- Displays formatted results
- Handles errors gracefully

### Exercise 2: File Converter
Build a tool that:
- Reads CSV files
- Converts to JSON format
- Writes output file
- Uses pathlib for paths

### Exercise 3: Text Analyzer
Create a program that:
- Counts words and characters
- Finds most common words
- Extracts emails/URLs using regex
- Generates statistics

### Exercise 4: Date Calculator
Build a tool that:
- Calculates days between dates
- Finds day of week
- Calculates age
- Formats dates in multiple ways

### Exercise 5: Random Generator
Create a program that generates:
- Random passwords
- Lottery numbers
- Sample data sets
- Shuffled lists

---

## Practice Project

**See:** `day19_api_toolkit.py` for the complete API Toolkit project.

The project includes:
- Multiple API integrations
- Data processing
- File operations
- Error handling
- Real-world utilities

---

## Quick Reference

### Installation
```bash
pip install package_name
pip install -r requirements.txt
pip freeze > requirements.txt
```

### Common Imports
```python
import requests          # HTTP requests
import json             # JSON handling
from datetime import datetime, timedelta
import random           # Random operations
from collections import Counter, defaultdict
from pathlib import Path  # File paths
import re               # Regular expressions
import csv              # CSV files
```

### HTTP Request
```python
response = requests.get(url, params=params, headers=headers)
data = response.json()
```

### JSON
```python
json_str = json.dumps(data, indent=2)
data = json.loads(json_str)
```

### Date Operations
```python
now = datetime.now()
tomorrow = now + timedelta(days=1)
formatted = now.strftime("%Y-%m-%d")
```

---

## Key Takeaways

✅ Python has 400,000+ packages on PyPI  
✅ requests makes HTTP requests easy  
✅ datetime handles dates and times  
✅ json converts between Python and JSON  
✅ collections provides useful containers  
✅ pathlib modernizes file path handling  
✅ re enables pattern matching  
✅ Always handle errors when using libraries  
✅ Read documentation for each library  
✅ Use virtual environments for projects  

---

## Common Mistakes

❌ **Not handling API errors**
```python
# Bad
data = requests.get(url).json()

# Good
try:
    response = requests.get(url, timeout=5)
    response.raise_for_status()
    data = response.json()
except Exception as e:
    print(f"Error: {e}")
```

❌ **Hardcoding API keys**
```python
# Bad
API_KEY = "abc123xyz"

# Good - use environment variables
import os
API_KEY = os.getenv('API_KEY')
```

❌ **Not using virtual environments**
```bash
# Good practice
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install requests
```

---

## Next Steps

Tomorrow (Day 20), we'll learn about **JSON & Files** - comprehensive file handling, JSON operations, and data persistence!

---

## Resources

- [PyPI - Python Package Index](https://pypi.org/)
- [Requests Documentation](https://requests.readthedocs.io/)
- [Python Standard Library](https://docs.python.org/3/library/)

---

**Leverage the Ecosystem! 🐍**
