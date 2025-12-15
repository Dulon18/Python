from datetime import datetime

# Get user's birth date
print("== Welcome to Age in Days Calculator ==\n")

birth_year = int(input("Enter your birth year (e.g., 2000): "))
birth_month = int(input("Enter your birth month (1-12): "))
birth_day = int(input("Enter your birth day (1-31): "))

# Create date objects
birth_date = datetime(birth_year, birth_month, birth_day)
today = datetime.now()

# Calculate the difference
age_difference = today - birth_date

# Extract days
age_in_days = age_difference.days

# Display results
print(f"\n--- Results ---")
print(f"Birth date: {birth_date.strftime('%B %d, %Y')}")
print(f"Today's date: {today.strftime('%B %d, %Y')}")
print(f"You are {age_in_days:,} days old!")

# Bonus: Convert to years and remaining days
years = age_in_days // 365
remaining_days = age_in_days % 365
print(f"That's approximately {years} years and {remaining_days} days!")
