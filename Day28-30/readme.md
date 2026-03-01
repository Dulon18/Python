# Days 28–30: Final Project — Web Scraper with BeautifulSoup

> **Week 4 — Final Project** | 30-Day Python Learning Plan

A fully professional web scraper that collects, stores, and displays data from websites — built with everything learned in 30 days.

---

## 🎯 What We're Building

A **Book Price Scraper** that:
- Scrapes book titles, prices, ratings, and availability from [books.toscrape.com](http://books.toscrape.com) (a free, legal practice site)
- Filters and searches books by rating or price
- Saves results to JSON and CSV files
- Has a clean CLI menu interface
- Includes error handling, logging, and tests
- Follows proper project structure and PEP 8

---

## 🗂️ Project Structure

```
book_scraper/
│
├── venv/                     # virtual environment
│
├── src/
│   ├── __init__.py
│   ├── main.py               # CLI menu entry point
│   ├── scraper.py            # scraping logic
│   ├── models.py             # Book data class
│   ├── storage.py            # save/load JSON and CSV
│   └── display.py            # display results in terminal
│
├── tests/
│   ├── __init__.py
│   └── test_scraper.py       # unit tests
│
├── data/                     # scraped data saved here
│
├── logs/                     # log files
│
├── .gitignore
├── requirements.txt
└── README.md
```

---

## ⚙️ Setup

```bash
# 1. Clone or create project folder
mkdir book_scraper
cd book_scraper

# 2. Create and activate virtual environment
python -m venv venv
venv\Scripts\activate        # Windows
source venv/bin/activate     # Mac/Linux

# 3. Install dependencies
pip install requests beautifulsoup4

# 4. Save dependencies
pip freeze > requirements.txt
```

---

## 📦 Installing Dependencies

```bash
pip install requests beautifulsoup4
```

| Package | Purpose |
|---|---|
| `requests` | Fetch web pages (HTTP requests) |
| `beautifulsoup4` | Parse and extract HTML content |

---

## 📌 Part A — Understanding BeautifulSoup

Before building the full project, let's understand the basics.

### How Web Scraping Works

```
1. Send HTTP request → get HTML page
2. Parse HTML with BeautifulSoup
3. Find the elements you want
4. Extract the data
5. Save to file
```

### Basic BeautifulSoup Usage

```python
import requests
from bs4 import BeautifulSoup

# Step 1: Fetch the page
url = "http://books.toscrape.com"
response = requests.get(url)

# Step 2: Parse HTML
soup = BeautifulSoup(response.text, "html.parser")

# Step 3: Find elements
# Find by tag
title = soup.find("h1")
print(title.text)

# Find by class
books = soup.find_all("article", class_="product_pod")
print(f"Found {len(books)} books")

# Find by CSS selector
prices = soup.select(".price_color")
for price in prices:
    print(price.text)

# Get attribute value
link = soup.find("a")
print(link["href"])  # get href attribute
```

### Navigating the HTML Tree

```python
from bs4 import BeautifulSoup

html = """
<div class="book">
    <h3><a href="/book/1">Python Crash Course</a></h3>
    <p class="price">£29.99</p>
    <p class="rating Three">rating</p>
</div>
"""

soup = BeautifulSoup(html, "html.parser")

# Navigate down
book = soup.find("div", class_="book")
title = book.find("h3").find("a").text
price = book.find("p", class_="price").text
rating = book.find("p", class_="rating")["class"][1]  # get second class

print(title)   # Python Crash Course
print(price)   # £29.99
print(rating)  # Three
```

---

## 📌 Part B — The Book Model

```python
# src/models.py

from dataclasses import dataclass, asdict

RATING_MAP = {
    "One": 1,
    "Two": 2,
    "Three": 3,
    "Four": 4,
    "Five": 5
}

@dataclass
class Book:
    """Represents a single scraped book."""
    title: str
    price: float
    rating: int
    availability: str
    url: str

    def to_dict(self) -> dict:
        """Convert Book to dictionary for saving."""
        return asdict(self)

    def __str__(self) -> str:
        stars = "★" * self.rating + "☆" * (5 - self.rating)
        status = "✓" if "In stock" in self.availability else "✗"
        return (
            f"Title       : {self.title}\n"
            f"Price       : £{self.price:.2f}\n"
            f"Rating      : {stars} ({self.rating}/5)\n"
            f"Availability: {status} {self.availability}"
        )
```

---

## 📌 Part C — The Scraper

```python
# src/scraper.py

import requests
import logging
import time
from bs4 import BeautifulSoup
from models import Book, RATING_MAP

# Setup logging
logging.basicConfig(
    filename="logs/scraper.log",
    level=logging.INFO,
    format="%(asctime)s — %(levelname)s — %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S"
)

BASE_URL = "http://books.toscrape.com/catalogue/"
START_URL = "http://books.toscrape.com/catalogue/page-1.html"


def fetch_page(url: str) -> BeautifulSoup | None:
    """
    Fetch a web page and return a BeautifulSoup object.

    Args:
        url (str): The URL to fetch.

    Returns:
        BeautifulSoup | None: Parsed HTML or None on failure.
    """
    try:
        headers = {"User-Agent": "Mozilla/5.0 (BookScraper/1.0)"}
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
        logging.info(f"Successfully fetched: {url}")
        return BeautifulSoup(response.text, "html.parser")

    except requests.exceptions.ConnectionError:
        logging.error(f"Connection error for: {url}")
        print("❌ No internet connection!")
    except requests.exceptions.Timeout:
        logging.error(f"Timeout for: {url}")
        print("❌ Request timed out!")
    except requests.exceptions.HTTPError as e:
        logging.error(f"HTTP error {e} for: {url}")
        print(f"❌ HTTP Error: {e}")
    return None


def parse_book(article) -> Book | None:
    """
    Parse a single book HTML article into a Book object.

    Args:
        article: BeautifulSoup article tag.

    Returns:
        Book | None: Parsed Book or None on failure.
    """
    try:
        # Title
        title = article.find("h3").find("a")["title"]

        # Price — strip £ and convert to float
        price_text = article.find("p", class_="price_color").text
        price = float(price_text.replace("£", "").replace("Â", "").strip())

        # Rating — from class name e.g. "star-rating Three"
        rating_class = article.find("p", class_="star-rating")["class"][1]
        rating = RATING_MAP.get(rating_class, 0)

        # Availability
        availability = article.find("p", class_="instock").text.strip()

        # URL
        relative_url = article.find("h3").find("a")["href"]
        url = BASE_URL + relative_url.replace("../", "")

        return Book(title, price, rating, availability, url)

    except (AttributeError, ValueError, KeyError) as e:
        logging.warning(f"Failed to parse book: {e}")
        return None


def scrape_page(soup: BeautifulSoup) -> list[Book]:
    """
    Scrape all books from a single page.

    Args:
        soup: Parsed BeautifulSoup page.

    Returns:
        list[Book]: List of Book objects found on the page.
    """
    articles = soup.find_all("article", class_="product_pod")
    books = []
    for article in articles:
        book = parse_book(article)
        if book:
            books.append(book)
    return books


def get_next_page(soup: BeautifulSoup) -> str | None:
    """
    Get the URL of the next page if it exists.

    Args:
        soup: Parsed BeautifulSoup page.

    Returns:
        str | None: Next page URL or None if last page.
    """
    next_btn = soup.find("li", class_="next")
    if next_btn:
        next_href = next_btn.find("a")["href"]
        return BASE_URL + next_href
    return None


def scrape_books(max_pages: int = 5) -> list[Book]:
    """
    Scrape multiple pages of books.

    Args:
        max_pages (int): Maximum number of pages to scrape. Defaults to 5.

    Returns:
        list[Book]: All scraped books.
    """
    all_books = []
    url = START_URL
    page = 1

    print(f"\n🔍 Starting scrape (max {max_pages} pages)...\n")

    while url and page <= max_pages:
        print(f"  Scraping page {page}/{max_pages}...", end=" ")
        soup = fetch_page(url)

        if not soup:
            print("❌ Failed")
            break

        books = scrape_page(soup)
        all_books.extend(books)
        print(f"✓ Found {len(books)} books (total: {len(all_books)})")

        logging.info(f"Page {page}: scraped {len(books)} books")

        url = get_next_page(soup)
        page += 1
        time.sleep(0.5)   # be polite — don't hammer the server

    print(f"\n✅ Scraping complete! Total books: {len(all_books)}\n")
    logging.info(f"Scraping complete. Total: {len(all_books)} books")
    return all_books
```

---

## 📌 Part D — Storage (JSON & CSV)

```python
# src/storage.py

import json
import csv
import os
import logging
from models import Book

DATA_DIR = "data"


def ensure_data_dir():
    """Create data directory if it doesn't exist."""
    os.makedirs(DATA_DIR, exist_ok=True)


def save_to_json(books: list[Book], filename: str = "books.json") -> str:
    """
    Save books list to a JSON file.

    Args:
        books (list[Book]): Books to save.
        filename (str): Output filename.

    Returns:
        str: Full path to saved file.
    """
    ensure_data_dir()
    filepath = os.path.join(DATA_DIR, filename)

    data = [book.to_dict() for book in books]
    with open(filepath, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)

    logging.info(f"Saved {len(books)} books to {filepath}")
    print(f"💾 Saved {len(books)} books → {filepath}")
    return filepath


def load_from_json(filename: str = "books.json") -> list[Book]:
    """
    Load books from a JSON file.

    Args:
        filename (str): JSON file to load.

    Returns:
        list[Book]: Loaded books or empty list.
    """
    filepath = os.path.join(DATA_DIR, filename)

    if not os.path.exists(filepath):
        print(f"❌ File not found: {filepath}")
        return []

    with open(filepath, "r", encoding="utf-8") as f:
        data = json.load(f)

    books = [Book(**item) for item in data]
    logging.info(f"Loaded {len(books)} books from {filepath}")
    return books


def save_to_csv(books: list[Book], filename: str = "books.csv") -> str:
    """
    Save books list to a CSV file.

    Args:
        books (list[Book]): Books to save.
        filename (str): Output filename.

    Returns:
        str: Full path to saved file.
    """
    ensure_data_dir()
    filepath = os.path.join(DATA_DIR, filename)

    with open(filepath, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(
            f,
            fieldnames=["title", "price", "rating", "availability", "url"]
        )
        writer.writeheader()
        writer.writerows([book.to_dict() for book in books])

    logging.info(f"Saved {len(books)} books to {filepath}")
    print(f"💾 Saved {len(books)} books → {filepath}")
    return filepath
```

---

## 📌 Part E — Display

```python
# src/display.py

from models import Book


def print_header(title: str):
    """Print a formatted section header."""
    print(f"\n{'='*55}")
    print(f"  {title}")
    print(f"{'='*55}")


def display_books(books: list[Book], limit: int = None):
    """
    Display books in a formatted list.

    Args:
        books (list[Book]): Books to display.
        limit (int): Max number to show. None = show all.
    """
    if not books:
        print("  No books found.")
        return

    show = books[:limit] if limit else books
    for i, book in enumerate(show, 1):
        print(f"\n[{i}]")
        print(book)
        print("-" * 55)

    if limit and len(books) > limit:
        print(f"\n  ... and {len(books) - limit} more.")


def display_summary(books: list[Book]):
    """Display a summary of the scraped data."""
    if not books:
        print("  No data to summarize.")
        return

    prices = [b.price for b in books]
    ratings = [b.rating for b in books]
    in_stock = [b for b in books if "In stock" in b.availability]

    print_header("📊 SUMMARY")
    print(f"  Total Books    : {len(books)}")
    print(f"  In Stock       : {len(in_stock)}")
    print(f"  Out of Stock   : {len(books) - len(in_stock)}")
    print(f"  Cheapest       : £{min(prices):.2f}")
    print(f"  Most Expensive : £{max(prices):.2f}")
    print(f"  Average Price  : £{sum(prices)/len(prices):.2f}")
    print(f"  Average Rating : {sum(ratings)/len(ratings):.1f} / 5")
    print("=" * 55)


def filter_by_rating(books: list[Book], min_rating: int) -> list[Book]:
    """Filter books by minimum star rating."""
    return [b for b in books if b.rating >= min_rating]


def filter_by_price(books: list[Book], max_price: float) -> list[Book]:
    """Filter books by maximum price."""
    return [b for b in books if b.price <= max_price]


def search_by_title(books: list[Book], keyword: str) -> list[Book]:
    """Search books by keyword in title."""
    keyword = keyword.lower()
    return [b for b in books if keyword in b.title.lower()]


def sort_books(books: list[Book], by: str = "price") -> list[Book]:
    """
    Sort books by a given field.

    Args:
        books: List of books.
        by: Field to sort by — 'price', 'rating', or 'title'.

    Returns:
        Sorted list of books.
    """
    if by == "price":
        return sorted(books, key=lambda b: b.price)
    elif by == "rating":
        return sorted(books, key=lambda b: b.rating, reverse=True)
    elif by == "title":
        return sorted(books, key=lambda b: b.title)
    return books
```

---

## 📌 Part F — Main CLI Menu

```python
# src/main.py

import os
import sys
import logging

from scraper import scrape_books
from storage import save_to_json, save_to_csv, load_from_json
from display import (
    display_books, display_summary,
    filter_by_rating, filter_by_price,
    search_by_title, sort_books,
    print_header
)

# Ensure logs directory exists
os.makedirs("logs", exist_ok=True)

logging.basicConfig(
    filename="logs/scraper.log",
    level=logging.INFO,
    format="%(asctime)s — %(levelname)s — %(message)s"
)

# In-memory storage for current session
current_books = []


def menu_scrape():
    """Scrape books from the website."""
    global current_books
    try:
        pages = input("How many pages to scrape? (1-50, default=5): ").strip()
        pages = int(pages) if pages.isdigit() else 5
        pages = max(1, min(50, pages))
        current_books = scrape_books(max_pages=pages)
    except Exception as e:
        print(f"❌ Error during scraping: {e}")


def menu_view():
    """View scraped books."""
    if not current_books:
        print("⚠️  No books loaded. Please scrape first.")
        return

    print_header(f"📚 ALL BOOKS ({len(current_books)} total)")
    limit_input = input("How many to show? (Enter for all): ").strip()
    limit = int(limit_input) if limit_input.isdigit() else None
    display_books(current_books, limit=limit)


def menu_filter():
    """Filter and search books."""
    if not current_books:
        print("⚠️  No books loaded. Please scrape first.")
        return

    print("\n  Filter by:")
    print("  1. Minimum rating")
    print("  2. Maximum price")
    print("  3. Search by title keyword")
    choice = input("  Choose (1-3): ").strip()

    if choice == "1":
        rating = input("  Minimum rating (1-5): ").strip()
        if rating.isdigit() and 1 <= int(rating) <= 5:
            results = filter_by_rating(current_books, int(rating))
            print_header(f"⭐ Books rated {rating}+ stars ({len(results)} found)")
            display_books(results)
        else:
            print("❌ Invalid rating.")

    elif choice == "2":
        price = input("  Maximum price (£): ").strip()
        try:
            results = filter_by_price(current_books, float(price))
            print_header(f"💰 Books under £{price} ({len(results)} found)")
            display_books(results)
        except ValueError:
            print("❌ Invalid price.")

    elif choice == "3":
        keyword = input("  Search keyword: ").strip()
        if keyword:
            results = search_by_title(current_books, keyword)
            print_header(f"🔍 Results for '{keyword}' ({len(results)} found)")
            display_books(results)
        else:
            print("❌ Keyword cannot be empty.")


def menu_sort():
    """Sort books."""
    if not current_books:
        print("⚠️  No books loaded. Please scrape first.")
        return

    print("\n  Sort by:")
    print("  1. Price (cheapest first)")
    print("  2. Rating (highest first)")
    print("  3. Title (A-Z)")
    choice = input("  Choose (1-3): ").strip()

    sort_map = {"1": "price", "2": "rating", "3": "title"}
    if choice in sort_map:
        sorted_books = sort_books(current_books, by=sort_map[choice])
        print_header(f"Sorted by {sort_map[choice]}")
        display_books(sorted_books, limit=10)
    else:
        print("❌ Invalid choice.")


def menu_save():
    """Save books to file."""
    if not current_books:
        print("⚠️  No books loaded. Please scrape first.")
        return

    print("\n  Save as:")
    print("  1. JSON")
    print("  2. CSV")
    print("  3. Both")
    choice = input("  Choose (1-3): ").strip()

    if choice in ("1", "3"):
        save_to_json(current_books)
    if choice in ("2", "3"):
        save_to_csv(current_books)


def menu_load():
    """Load previously saved books."""
    global current_books
    current_books = load_from_json()
    if current_books:
        print(f"✅ Loaded {len(current_books)} books from file.")


def print_main_menu():
    print("\n" + "=" * 55)
    print("         📚 BOOK SCRAPER — books.toscrape.com")
    print("=" * 55)
    status = f"{len(current_books)} books loaded" if current_books else "No books loaded"
    print(f"  Status: {status}")
    print("-" * 55)
    print("  1. 🔍 Scrape books from website")
    print("  2. 📖 View all books")
    print("  3. 🔎 Filter / Search books")
    print("  4. 🔃 Sort books")
    print("  5. 📊 View summary")
    print("  6. 💾 Save to file (JSON / CSV)")
    print("  7. 📂 Load from saved file")
    print("  8. 🚪 Exit")
    print("=" * 55)


def main():
    print("\n🐍 Welcome to Book Scraper!")
    print("   Built with Python + BeautifulSoup")
    print("   Data source: books.toscrape.com (legal practice site)")

    while True:
        print_main_menu()
        choice = input("  Choose (1-8): ").strip()

        actions = {
            "1": menu_scrape,
            "2": menu_view,
            "3": menu_filter,
            "4": menu_sort,
            "5": lambda: display_summary(current_books),
            "6": menu_save,
            "7": menu_load,
        }

        if choice in actions:
            actions[choice]()
        elif choice == "8":
            print("\n👋 Goodbye! Happy scraping!\n")
            sys.exit(0)
        else:
            print("❌ Invalid choice. Please enter 1-8.")


if __name__ == "__main__":
    main()
```

---

## 📌 Part G — Tests

```python
# tests/test_scraper.py

import unittest
from unittest.mock import patch, MagicMock
from bs4 import BeautifulSoup

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "../src"))

from models import Book, RATING_MAP
from display import filter_by_rating, filter_by_price, search_by_title, sort_books
from storage import save_to_json, load_from_json


# --- Sample HTML for testing ---
SAMPLE_ARTICLE = """
<article class="product_pod">
    <h3><a href="catalogue/a-light-in-the-attic_1000/index.html"
          title="A Light in the Attic">A Light in the Attic</a></h3>
    <p class="star-rating Three"></p>
    <p class="price_color">£51.77</p>
    <p class="instock availability">In stock</p>
</article>
"""


class TestBook(unittest.TestCase):

    def setUp(self):
        self.book = Book(
            title="Test Book",
            price=29.99,
            rating=4,
            availability="In stock",
            url="http://example.com/book"
        )

    def test_book_creation(self):
        self.assertEqual(self.book.title, "Test Book")
        self.assertEqual(self.book.price, 29.99)
        self.assertEqual(self.book.rating, 4)

    def test_to_dict(self):
        d = self.book.to_dict()
        self.assertIsInstance(d, dict)
        self.assertEqual(d["title"], "Test Book")
        self.assertEqual(d["price"], 29.99)

    def test_str_contains_title(self):
        result = str(self.book)
        self.assertIn("Test Book", result)
        self.assertIn("29.99", result)

    def test_rating_map(self):
        self.assertEqual(RATING_MAP["One"], 1)
        self.assertEqual(RATING_MAP["Five"], 5)
        self.assertEqual(RATING_MAP.get("Six", 0), 0)


class TestFiltering(unittest.TestCase):

    def setUp(self):
        self.books = [
            Book("Cheap Book",      10.00, 2, "In stock",     "http://a.com"),
            Book("Medium Book",     25.00, 3, "In stock",     "http://b.com"),
            Book("Expensive Book",  50.00, 5, "Out of stock", "http://c.com"),
            Book("Top Rated Book",  30.00, 5, "In stock",     "http://d.com"),
        ]

    def test_filter_by_rating(self):
        results = filter_by_rating(self.books, min_rating=4)
        self.assertEqual(len(results), 2)
        for book in results:
            self.assertGreaterEqual(book.rating, 4)

    def test_filter_by_price(self):
        results = filter_by_price(self.books, max_price=30.00)
        self.assertEqual(len(results), 3)
        for book in results:
            self.assertLessEqual(book.price, 30.00)

    def test_search_by_title(self):
        results = search_by_title(self.books, "book")
        self.assertEqual(len(results), 4)

        results = search_by_title(self.books, "cheap")
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0].title, "Cheap Book")

    def test_search_case_insensitive(self):
        results = search_by_title(self.books, "CHEAP")
        self.assertEqual(len(results), 1)

    def test_sort_by_price(self):
        sorted_books = sort_books(self.books, by="price")
        prices = [b.price for b in sorted_books]
        self.assertEqual(prices, sorted(prices))

    def test_sort_by_rating(self):
        sorted_books = sort_books(self.books, by="rating")
        ratings = [b.rating for b in sorted_books]
        self.assertEqual(ratings, sorted(ratings, reverse=True))

    def test_sort_by_title(self):
        sorted_books = sort_books(self.books, by="title")
        titles = [b.title for b in sorted_books]
        self.assertEqual(titles, sorted(titles))


class TestStorage(unittest.TestCase):

    TEST_FILE = "test_books.json"

    def setUp(self):
        self.books = [
            Book("Book A", 10.00, 3, "In stock", "http://a.com"),
            Book("Book B", 20.00, 4, "In stock", "http://b.com"),
        ]
        os.makedirs("data", exist_ok=True)

    def tearDown(self):
        filepath = os.path.join("data", self.TEST_FILE)
        if os.path.exists(filepath):
            os.remove(filepath)

    def test_save_and_load_json(self):
        save_to_json(self.books, filename=self.TEST_FILE)
        loaded = load_from_json(filename=self.TEST_FILE)

        self.assertEqual(len(loaded), 2)
        self.assertEqual(loaded[0].title, "Book A")
        self.assertEqual(loaded[1].price, 20.00)

    def test_load_missing_file(self):
        result = load_from_json(filename="nonexistent.json")
        self.assertEqual(result, [])


if __name__ == "__main__":
    unittest.main(verbosity=2)
```

---

## ▶️ How to Run

```bash
# Activate virtual environment
venv\Scripts\activate       # Windows
source venv/bin/activate    # Mac/Linux

# Run the scraper
python src/main.py

# Run tests
python -m unittest discover tests -v
```

---

## 📸 Sample Output

```
🐍 Welcome to Book Scraper!
   Built with Python + BeautifulSoup
   Data source: books.toscrape.com

=======================================================
         📚 BOOK SCRAPER — books.toscrape.com
=======================================================
  Status: No books loaded
-------------------------------------------------------
  1. 🔍 Scrape books from website
  ...

🔍 Starting scrape (max 3 pages)...

  Scraping page 1/3... ✓ Found 20 books (total: 20)
  Scraping page 2/3... ✓ Found 20 books (total: 40)
  Scraping page 3/3... ✓ Found 20 books (total: 60)

✅ Scraping complete! Total books: 60

[1]
Title       : A Light in the Attic
Price       : £51.77
Rating      : ★★★☆☆ (3/5)
Availability: ✓ In stock
```

---

## 📝 All Python Concepts Used in This Project

| Concept | Day Learned | Where Used |
|---|---|---|
| File Handling | Day 15 | `storage.py` — save/load JSON & CSV |
| Modules & Packages | Day 16 | Separate `scraper.py`, `models.py`, etc. |
| List Comprehensions | Day 17 | Filtering, sorting, building book lists |
| OOP — Classes | Day 18 | `Book` dataclass with methods |
| OOP — Encapsulation | Day 19 | Private methods, type hints |
| Libraries & pip | Day 20 | `requests`, `beautifulsoup4` |
| JSON | Day 25 | `save_to_json`, `load_from_json` |
| Error Handling | Day 13 | `try/except` in `fetch_page()` |
| Testing | Day 26 | Full `test_scraper.py` test suite |
| Virtual Env & PEP 8 | Day 27 | Project structure, docstrings, type hints |
| Regex | Day 22 | URL parsing and cleaning |
| Decorators | Day 23 | Logging wrapper pattern |
| Generators | Day 23 | Memory-efficient book processing |

---

## 🔗 Resources

- [BeautifulSoup Docs](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)
- [books.toscrape.com](http://books.toscrape.com) — free legal scraping practice site
- [requests Docs](https://requests.readthedocs.io)
- [Real Python — Web Scraping](https://realpython.com/beautiful-soup-web-scraper-python/)

---

## 🎉 Congratulations!

You have completed the **30-Day Python Learning Plan!**

```
Week 1 ✅ — Python Fundamentals
Week 2 ✅ — Control Flow & Functions
Week 3 ✅ — Intermediate Concepts
Week 4 ✅ — Advanced Topics & Final Project
```

You can now:
- Write clean, professional Python code
- Build real-world applications
- Work with files, APIs, databases
- Use OOP, decorators, generators
- Test and debug your code
- Structure projects professionally

**What's next?**
- 🌐 Learn Flask or FastAPI for web development
- 📊 Dive deeper into pandas and data analysis
- 🤖 Explore machine learning with scikit-learn
- 🗄️ Learn SQL and database integration
- 🐙 Master Git and GitHub for version control

**Keep building. Keep learning. **
