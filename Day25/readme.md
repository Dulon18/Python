#  Day 25: Working with JSON in Python

> **Week 4 — Advanced Topics** | 30-Day Python Learning Plan

JSON (JavaScript Object Notation) is the most popular format for **storing and exchanging data** — especially when working with APIs and web services.

---

## 📌 What is JSON?

JSON looks very similar to Python dictionaries. It's human-readable and lightweight.

```json
{
  "name": "Ali",
  "age": 25,
  "is_student": true,
  "skills": ["Python", "SQL", "Git"],
  "address": {
    "city": "Dhaka",
    "country": "Bangladesh"
  },
  "score": null
}
```

### JSON vs Python Types

| JSON | Python |
|---|---|
| `object {}` | `dict` |
| `array []` | `list` |
| `string ""` | `str` |
| `number` | `int` / `float` |
| `true / false` | `True / False` |
| `null` | `None` |

---

## 📌 Part A — Python's `json` Module

```python
import json
```

### Core Functions

| Function | What it does |
|---|---|
| `json.dumps()` | Python object → JSON **string** |
| `json.loads()` | JSON **string** → Python object |
| `json.dump()` | Python object → JSON **file** |
| `json.load()` | JSON **file** → Python object |

> **Memory tip:** `s` in `dumps/loads` stands for **string**. Without `s` means **file**.

---

## 📌 Part B — Converting Between Python and JSON

### Python → JSON String (`dumps`)

```python
import json

data = {
    "name": "Ali",
    "age": 25,
    "skills": ["Python", "SQL"],
    "is_active": True,
    "score": None
}

# Convert to JSON string
json_string = json.dumps(data)
print(json_string)
print(type(json_string))  # <class 'str'>
# {"name": "Ali", "age": 25, "skills": ["Python", "SQL"], "is_active": true, "score": null}

# Pretty print with indentation
pretty = json.dumps(data, indent=4)
print(pretty)
# {
#     "name": "Ali",
#     "age": 25,
#     ...
# }

# Sort keys alphabetically
sorted_json = json.dumps(data, indent=4, sort_keys=True)
print(sorted_json)

# Handle non-ASCII characters (e.g. Bengali, Arabic)
data2 = {"name": "আলী", "city": "ঢাকা"}
print(json.dumps(data2, ensure_ascii=False, indent=2))
# {
#   "name": "আলী",
#   "city": "ঢাকা"
# }
```

---

### JSON String → Python (`loads`)

```python
import json

json_str = '{"name": "Ali", "age": 25, "skills": ["Python", "SQL"]}'

# Convert to Python dict
data = json.loads(json_str)

print(data["name"])    # Ali
print(data["skills"])  # ['Python', 'SQL']
print(type(data))      # <class 'dict'>

# Nested JSON
nested_str = '''
{
    "user": {
        "name": "Sara",
        "address": {
            "city": "Chittagong",
            "zip": "4000"
        }
    }
}
'''
nested = json.loads(nested_str)
print(nested["user"]["address"]["city"])  # Chittagong
```

---

## 📌 Part C — Reading and Writing JSON Files

### Writing to a JSON File (`dump`)

```python
import json

students = [
    {"name": "Ali",  "age": 20, "grade": "A"},
    {"name": "Sara", "age": 22, "grade": "B"},
    {"name": "John", "age": 21, "grade": "A+"}
]

with open("students.json", "w") as f:
    json.dump(students, f, indent=4)

print("File saved!")
```

**Output file `students.json`:**
```json
[
    {
        "name": "Ali",
        "age": 20,
        "grade": "A"
    },
    {
        "name": "Sara",
        "age": 22,
        "grade": "B"
    }
]
```

---

### Reading from a JSON File (`load`)

```python
import json

with open("students.json", "r") as f:
    students = json.load(f)

for student in students:
    print(f"{student['name']} — Grade: {student['grade']}")

# Ali  — Grade: A
# Sara — Grade: B
# John — Grade: A+
```

---

### Updating a JSON File

```python
import json
import os

FILENAME = "students.json"

def load_data():
    if not os.path.exists(FILENAME):
        return []
    with open(FILENAME, "r") as f:
        return json.load(f)

def save_data(data):
    with open(FILENAME, "w") as f:
        json.dump(data, f, indent=4)

# Load → Modify → Save
students = load_data()
students.append({"name": "Riya", "age": 23, "grade": "A"})
save_data(students)
print("Student added!")
```

---

## 📌 Part D — Working with APIs

APIs return data in JSON format. We use `requests` to fetch it and `json` to process it.

### Basic API Call

```python
import requests

response = requests.get("https://jsonplaceholder.typicode.com/users/1")

# Response is already JSON — use .json() to parse
data = response.json()

print(data["name"])            # Leanne Graham
print(data["email"])           # Sincere@april.biz
print(data["address"]["city"]) # Gwenborough
```

---

### Fetching a List of Items

```python
import requests
import json

# Fetch all posts
response = requests.get("https://jsonplaceholder.typicode.com/posts")
posts = response.json()

print(f"Total posts: {len(posts)}")

# Show first 3
for post in posts[:3]:
    print(f"\nID    : {post['id']}")
    print(f"Title : {post['title']}")
    print(f"Body  : {post['body'][:60]}...")

# Save to file
with open("posts.json", "w") as f:
    json.dump(posts, f, indent=4)
print("\nAll posts saved to posts.json")
```

---

### Sending Data to an API (POST request)

```python
import requests
import json

new_post = {
    "title": "My Python Journey",
    "body": "Learning Python day by day!",
    "userId": 1
}

response = requests.post(
    "https://jsonplaceholder.typicode.com/posts",
    json=new_post  # automatically converts dict to JSON
)

print(f"Status Code : {response.status_code}")  # 201 = Created
print(f"Response    : {response.json()}")
```

---

### Handling API Errors Properly

```python
import requests

def fetch_user(user_id):
    try:
        response = requests.get(
            f"https://jsonplaceholder.typicode.com/users/{user_id}",
            timeout=5  # wait max 5 seconds
        )
        response.raise_for_status()  # raises error for 4xx/5xx status
        return response.json()

    except requests.exceptions.ConnectionError:
        print("Error: No internet connection!")
    except requests.exceptions.Timeout:
        print("Error: Request timed out!")
    except requests.exceptions.HTTPError as e:
        print(f"HTTP Error: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")
    return None

user = fetch_user(1)
if user:
    print(f"Name: {user['name']}")

# Test with invalid ID
fetch_user(9999)  # HTTPError: 404
```

---

## 📌 Part E — JSON with Custom Python Objects

By default, `json.dumps()` can't handle custom class objects — you need to convert them first.

```python
import json
from datetime import datetime

# --- Problem: custom objects can't be serialized directly ---
class Student:
    def __init__(self, name, age, enrolled):
        self.name = name
        self.age = age
        self.enrolled = enrolled  # datetime object

s = Student("Ali", 20, datetime(2024, 9, 1))
# json.dumps(s)  # TypeError!

# --- Solution 1: Convert to dict manually ---
def student_to_dict(student):
    return {
        "name": student.name,
        "age": student.age,
        "enrolled": student.enrolled.strftime("%Y-%m-%d")
    }

print(json.dumps(student_to_dict(s), indent=2))

# --- Solution 2: Custom JSON Encoder ---
class StudentEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Student):
            return {
                "name": obj.name,
                "age": obj.age,
                "enrolled": obj.enrolled.strftime("%Y-%m-%d")
            }
        if isinstance(obj, datetime):
            return obj.isoformat()
        return super().default(obj)

print(json.dumps(s, cls=StudentEncoder, indent=2))
```

---

## 🛠️ Practice Project — Weather App using JSON & API

```python
import requests
import json
import os
from datetime import datetime

CACHE_FILE = "weather_cache.json"

def load_cache():
    """Load cached weather data"""
    if os.path.exists(CACHE_FILE):
        with open(CACHE_FILE, "r") as f:
            return json.load(f)
    return {}

def save_cache(cache):
    """Save weather data to cache"""
    with open(CACHE_FILE, "w") as f:
        json.dump(cache, f, indent=4)

def get_weather(city):
    """Fetch weather for a city with caching"""
    cache = load_cache()

    # Check cache first
    if city.lower() in cache:
        cached = cache[city.lower()]
        print(f"(Loaded from cache — saved at {cached['saved_at']})\n")
        return cached["data"]

    # Fetch from API
    try:
        url = f"https://wttr.in/{city}?format=j1"
        response = requests.get(url, timeout=5)
        response.raise_for_status()
        data = response.json()

        # Save to cache
        cache[city.lower()] = {
            "saved_at": datetime.now().strftime("%Y-%m-%d %H:%M"),
            "data": data
        }
        save_cache(cache)
        return data

    except requests.exceptions.ConnectionError:
        print("No internet connection!")
    except requests.exceptions.Timeout:
        print("Request timed out!")
    except Exception as e:
        print(f"Error: {e}")
    return None

def display_weather(city, data):
    """Display weather info nicely"""
    try:
        current = data["current_condition"][0]
        area = data["nearest_area"][0]
        area_name = area["areaName"][0]["value"]
        country = area["country"][0]["value"]

        print(f"\n{'='*45}")
        print(f"  Weather in {area_name}, {country}")
        print(f"{'='*45}")
        print(f"  Temperature   : {current['temp_C']}°C / {current['temp_F']}°F")
        print(f"  Feels Like    : {current['FeelsLikeC']}°C")
        print(f"  Description   : {current['weatherDesc'][0]['value']}")
        print(f"  Humidity      : {current['humidity']}%")
        print(f"  Wind Speed    : {current['windspeedKmph']} km/h")
        print(f"  Visibility    : {current['visibility']} km")
        print(f"{'='*45}")

        # Save full report to JSON
        report = {
            "city": city,
            "fetched_at": datetime.now().strftime("%Y-%m-%d %H:%M"),
            "temperature_c": current["temp_C"],
            "feels_like_c": current["FeelsLikeC"],
            "description": current["weatherDesc"][0]["value"],
            "humidity": current["humidity"],
            "wind_kmph": current["windspeedKmph"]
        }
        filename = f"{city.lower()}_weather.json"
        with open(filename, "w") as f:
            json.dump(report, f, indent=4)
        print(f"  Report saved → {filename}")

    except (KeyError, IndexError) as e:
        print(f"Error reading weather data: {e}")

def show_cache():
    """Show all cached cities"""
    cache = load_cache()
    if not cache:
        print("No cached data found.")
        return
    print("\nCached cities:")
    for city, info in cache.items():
        print(f"  • {city.capitalize()} (saved: {info['saved_at']})")

def clear_cache():
    """Clear weather cache"""
    if os.path.exists(CACHE_FILE):
        os.remove(CACHE_FILE)
        print("Cache cleared!")
    else:
        print("No cache to clear.")

# --- Main Menu ---
while True:
    print("\n" + "="*45)
    print("        WEATHER APP — JSON + API")
    print("="*45)
    print("1. Get Weather")
    print("2. Show Cached Cities")
    print("3. Clear Cache")
    print("4. Exit")
    print("="*45)

    choice = input("Choose (1-4): ").strip()

    if choice == "1":
        city = input("Enter city name: ").strip()
        if city:
            data = get_weather(city)
            if data:
                display_weather(city, data)
    elif choice == "2":
        show_cache()
    elif choice == "3":
        clear_cache()
    elif choice == "4":
        print("Goodbye!")
        break
    else:
        print("Invalid choice!")
```

---

## 📝 Quick Summary

| Concept | Function | Direction |
|---|---|---|
| Dict → JSON string | `json.dumps()` | Python → String |
| JSON string → Dict | `json.loads()` | String → Python |
| Dict → JSON file | `json.dump()` | Python → File |
| JSON file → Dict | `json.load()` | File → Python |
| Pretty print | `indent=4` | Makes JSON readable |
| Non-ASCII support | `ensure_ascii=False` | Supports all languages |
| Sort keys | `sort_keys=True` | Alphabetical order |
| API fetch | `requests.get().json()` | URL → Python dict |

---

## 🔗 Resources

- [Python `json` Module Docs](https://docs.python.org/3/library/json.html)
- [JSONPlaceholder — Free Test API](https://jsonplaceholder.typicode.com)
- [wttr.in — Free Weather API](https://wttr.in)
- [Real Python — Working with JSON](https://realpython.com/python-json/)

---

> 📅 Part of the **30-Day Python Learning Plan**
> Previous: [Day 24 - Data Structures & Collections](#) | Next: [Day 26 - Testing & Debugging](#)
