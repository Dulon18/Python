# Robust Application Framework - Day 13 Practice Project
# Master error handling through a comprehensive application

import os
from datetime import datetime

# ===== CUSTOM EXCEPTIONS =====

class ValidationError(Exception):
    """Base exception for validation errors."""
    pass


class InvalidEmailError(ValidationError):
    """Raised when email format is invalid."""
    pass


class InvalidPasswordError(ValidationError):
    """Raised when password doesn't meet requirements."""
    pass


class InsufficientFundsError(Exception):
    """Raised when account has insufficient funds."""
    
    def __init__(self, balance, amount):
        self.balance = balance
        self.amount = amount
        self.shortage = amount - balance
        super().__init__(
            f"Insufficient funds: Need ${amount:.2f}, have ${balance:.2f}"
        )


class TransactionError(Exception):
    """Base exception for transaction errors."""
    pass


# ===== INPUT VALIDATION WITH ERROR HANDLING =====

def get_integer(prompt, min_val=None, max_val=None):
    """
    Get integer input with validation.
    
    Args:
        prompt: Input prompt
        min_val: Minimum allowed value
        max_val: Maximum allowed value
    
    Returns:
        Valid integer
    """
    while True:
        try:
            value = int(input(prompt))
            
            if min_val is not None and value < min_val:
                print(f"✗ Value must be at least {min_val}")
                continue
            
            if max_val is not None and value > max_val:
                print(f"✗ Value must be at most {max_val}")
                continue
            
            return value
        
        except ValueError:
            print("✗ Please enter a valid integer!")
        except KeyboardInterrupt:
            print("\n✗ Input cancelled by user")
            return None


def get_float(prompt, min_val=None, max_val=None):
    """Get float input with validation."""
    while True:
        try:
            value = float(input(prompt))
            
            if min_val is not None and value < min_val:
                print(f"✗ Value must be at least {min_val}")
                continue
            
            if max_val is not None and value > max_val:
                print(f"✗ Value must be at most {max_val}")
                continue
            
            return value
        
        except ValueError:
            print("✗ Please enter a valid number!")
        except KeyboardInterrupt:
            print("\n✗ Input cancelled by user")
            return None


def get_choice(prompt, options):
    """
    Get choice from list of options.
    
    Args:
        prompt: Input prompt
        options: List of valid options
    
    Returns:
        Valid choice
    """
    while True:
        try:
            choice = input(prompt).strip().lower()
            
            if choice in options:
                return choice
            
            print(f"✗ Invalid choice. Options: {', '.join(options)}")
        
        except KeyboardInterrupt:
            print("\n✗ Input cancelled by user")
            return None


# ===== VALIDATION FUNCTIONS =====

def validate_email(email):
    """
    Validate email format.
    
    Raises:
        InvalidEmailError: If email format is invalid
    """
    if '@' not in email:
        raise InvalidEmailError("Email must contain '@'")
    
    parts = email.split('@')
    if len(parts) != 2:
        raise InvalidEmailError("Email must have exactly one '@'")
    
    username, domain = parts
    
    if not username:
        raise InvalidEmailError("Email must have username before '@'")
    
    if not domain or '.' not in domain:
        raise InvalidEmailError("Email domain must contain '.'")
    
    return True


def validate_password(password):
    """
    Validate password strength.
    
    Requirements:
        - At least 8 characters
        - Contains uppercase and lowercase
        - Contains digit
        - Contains special character
    
    Raises:
        InvalidPasswordError: If password doesn't meet requirements
    """
    if len(password) < 8:
        raise InvalidPasswordError("Password must be at least 8 characters")
    
    has_upper = any(c.isupper() for c in password)
    has_lower = any(c.islower() for c in password)
    has_digit = any(c.isdigit() for c in password)
    has_special = any(c in "!@#$%^&*()_+-=[]{}|;:,.<>?" for c in password)
    
    if not has_upper:
        raise InvalidPasswordError("Password must contain uppercase letter")
    
    if not has_lower:
        raise InvalidPasswordError("Password must contain lowercase letter")
    
    if not has_digit:
        raise InvalidPasswordError("Password must contain digit")
    
    if not has_special:
        raise InvalidPasswordError("Password must contain special character")
    
    return True


# ===== FILE OPERATIONS WITH ERROR HANDLING =====

def safe_read_file(filename):
    """
    Read file with comprehensive error handling.
    
    Returns:
        File content or None if error occurred
    """
    try:
        with open(filename, 'r') as file:
            content = file.read()
            print(f"✓ Successfully read {len(content)} characters")
            return content
    
    except FileNotFoundError:
        print(f"✗ Error: File '{filename}' not found")
        return None
    
    except PermissionError:
        print(f"✗ Error: No permission to read '{filename}'")
        return None
    
    except IsADirectoryError:
        print(f"✗ Error: '{filename}' is a directory, not a file")
        return None
    
    except Exception as e:
        print(f"✗ Unexpected error reading file: {e}")
        return None


def safe_write_file(filename, content):
    """
    Write to file with error handling.
    
    Returns:
        True if successful, False otherwise
    """
    try:
        with open(filename, 'w') as file:
            file.write(content)
            print(f"✓ Successfully wrote to '{filename}'")
            return True
    
    except PermissionError:
        print(f"✗ Error: No permission to write to '{filename}'")
        return False
    
    except IsADirectoryError:
        print(f"✗ Error: '{filename}' is a directory")
        return False
    
    except Exception as e:
        print(f"✗ Unexpected error writing file: {e}")
        return False


def safe_delete_file(filename):
    """Delete file with error handling."""
    try:
        os.remove(filename)
        print(f"✓ File '{filename}' deleted")
        return True
    
    except FileNotFoundError:
        print(f"✗ File '{filename}' not found")
        return False
    
    except PermissionError:
        print(f"✗ No permission to delete '{filename}'")
        return False
    
    except IsADirectoryError:
        print(f"✗ '{filename}' is a directory")
        return False
    
    except Exception as e:
        print(f"✗ Error deleting file: {e}")
        return False


# ===== BANKING SYSTEM WITH ERROR HANDLING =====

class BankAccount:
    """Bank account with robust error handling."""
    
    def __init__(self, account_number, initial_balance=0):
        """Initialize account."""
        self.account_number = account_number
        self.balance = initial_balance
        self.transaction_history = []
    
    def deposit(self, amount):
        """
        Deposit money.
        
        Raises:
            ValueError: If amount is invalid
        """
        if not isinstance(amount, (int, float)):
            raise TypeError("Amount must be a number")
        
        if amount <= 0:
            raise ValueError("Deposit amount must be positive")
        
        self.balance += amount
        self._log_transaction("Deposit", amount)
        print(f"✓ Deposited ${amount:.2f}")
        print(f"  New balance: ${self.balance:.2f}")
    
    def withdraw(self, amount):
        """
        Withdraw money.
        
        Raises:
            ValueError: If amount is invalid
            InsufficientFundsError: If insufficient balance
        """
        if not isinstance(amount, (int, float)):
            raise TypeError("Amount must be a number")
        
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive")
        
        if amount > self.balance:
            raise InsufficientFundsError(self.balance, amount)
        
        self.balance -= amount
        self._log_transaction("Withdrawal", amount)
        print(f"✓ Withdrew ${amount:.2f}")
        print(f"  New balance: ${self.balance:.2f}")
    
    def transfer(self, other_account, amount):
        """
        Transfer money to another account.
        
        Raises:
            ValueError: If amount is invalid
            InsufficientFundsError: If insufficient balance
            TypeError: If other_account is not BankAccount
        """
        if not isinstance(other_account, BankAccount):
            raise TypeError("Can only transfer to BankAccount")
        
        if amount <= 0:
            raise ValueError("Transfer amount must be positive")
        
        if amount > self.balance:
            raise InsufficientFundsError(self.balance, amount)
        
        # Perform transfer
        self.balance -= amount
        other_account.balance += amount
        
        self._log_transaction(f"Transfer to {other_account.account_number}", amount)
        other_account._log_transaction(f"Transfer from {self.account_number}", amount)
        
        print(f"✓ Transferred ${amount:.2f} to account {other_account.account_number}")
        print(f"  Your new balance: ${self.balance:.2f}")
    
    def _log_transaction(self, transaction_type, amount):
        """Log transaction to history."""
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.transaction_history.append({
            "timestamp": timestamp,
            "type": transaction_type,
            "amount": amount,
            "balance": self.balance
        })
    
    def show_history(self):
        """Display transaction history."""
        if not self.transaction_history:
            print("No transactions yet")
            return
        
        print("\n" + "=" * 70)
        print("TRANSACTION HISTORY")
        print("=" * 70)
        print(f"{'Date/Time':<20} {'Type':<25} {'Amount':>10} {'Balance':>10}")
        print("-" * 70)
        
        for trans in self.transaction_history:
            print(f"{trans['timestamp']:<20} {trans['type']:<25} "
                  f"${trans['amount']:>9.2f} ${trans['balance']:>9.2f}")
        
        print("=" * 70)


# ===== RETRY MECHANISM =====

def retry_operation(func, max_attempts=3, *args, **kwargs):
    """
    Retry an operation multiple times.
    
    Args:
        func: Function to retry
        max_attempts: Maximum number of attempts
        *args, **kwargs: Arguments to pass to function
    
    Returns:
        Function result if successful
    
    Raises:
        Exception from last failed attempt
    """
    last_exception = None
    
    for attempt in range(max_attempts):
        try:
            result = func(*args, **kwargs)
            if attempt > 0:
                print(f"✓ Succeeded on attempt {attempt + 1}")
            return result
        
        except Exception as e:
            last_exception = e
            print(f"  Attempt {attempt + 1}/{max_attempts} failed: {e}")
            
            if attempt < max_attempts - 1:
                print("   Retrying...")
    
    print(f"✗ All {max_attempts} attempts failed")
    raise last_exception


# ===== DEMONSTRATION FUNCTIONS =====

def demo_input_validation():
    """Demonstrate input validation."""
    print("\n--- Input Validation Demo ---")
    
    print("\n1. Integer input (1-100):")
    age = get_integer("Enter your age: ", min_val=1, max_val=100)
    if age:
        print(f"✓ You entered: {age}")
    
    print("\n2. Float input:")
    price = get_float("Enter price: ", min_val=0)
    if price:
        print(f"✓ Price: ${price:.2f}")
    
    print("\n3. Choice input:")
    choice = get_choice("Choose (yes/no): ", ['yes', 'no', 'y', 'n'])
    if choice:
        print(f"✓ You chose: {choice}")


def demo_email_validation():
    """Demonstrate email validation."""
    print("\n--- Email Validation Demo ---")
    
    test_emails = [
        "user@example.com",
        "invalid.email",
        "@example.com",
        "user@",
        "user@@example.com"
    ]
    
    for email in test_emails:
        try:
            validate_email(email)
            print(f"✓ '{email}' is valid")
        except InvalidEmailError as e:
            print(f"✗ '{email}' is invalid: {e}")


def demo_password_validation():
    """Demonstrate password validation."""
    print("\n--- Password Validation Demo ---")
    
    test_passwords = [
        "SecurePass123!",
        "weak",
        "NoDigitsHere!",
        "noupppercase123!",
        "NOLOWERCASE123!"
    ]
    
    for password in test_passwords:
        try:
            validate_password(password)
            print(f"✓ '{password}' is valid")
        except InvalidPasswordError as e:
            print(f"✗ '{password}' is invalid: {e}")


def demo_file_operations():
    """Demonstrate file operations."""
    print("\n--- File Operations Demo ---")
    
    # Write file
    print("\n1. Writing file:")
    safe_write_file("test_file.txt", "Hello, World!\nThis is a test.")
    
    # Read file
    print("\n2. Reading file:")
    content = safe_read_file("test_file.txt")
    if content:
        print(f"Content: {content[:50]}...")
    
    # Read non-existent file
    print("\n3. Reading non-existent file:")
    safe_read_file("nonexistent.txt")
    
    # Delete file
    print("\n4. Deleting file:")
    safe_delete_file("test_file.txt")


def demo_banking_system():
    """Demonstrate banking system with error handling."""
    print("\n--- Banking System Demo ---")
    
    # Create accounts
    account1 = BankAccount("ACC001", 1000)
    account2 = BankAccount("ACC002", 500)
    
    # Successful operations
    print("\n1. Successful deposit:")
    try:
        account1.deposit(500)
    except Exception as e:
        print(f"Error: {e}")
    
    print("\n2. Successful withdrawal:")
    try:
        account1.withdraw(200)
    except Exception as e:
        print(f"Error: {e}")
    
    # Error cases
    print("\n3. Invalid deposit:")
    try:
        account1.deposit(-100)
    except ValueError as e:
        print(f"✗ Error: {e}")
    
    print("\n4. Insufficient funds:")
    try:
        account1.withdraw(10000)
    except InsufficientFundsError as e:
        print(f"✗ Error: {e}")
        print(f"   Short by: ${e.shortage:.2f}")
    
    print("\n5. Transfer:")
    try:
        account1.transfer(account2, 300)
    except Exception as e:
        print(f"Error: {e}")
    
    # Show history
    print("\n6. Transaction history:")
    account1.show_history()


def demo_retry_mechanism():
    """Demonstrate retry mechanism."""
    print("\n--- Retry Mechanism Demo ---")
    
    import random
    
    def unstable_operation():
        """Simulated unstable operation."""
        if random.random() < 0.6:
            raise ConnectionError("Network timeout")
        return "Operation successful!"
    
    print("\nAttempting unstable operation with retry:")
    try:
        result = retry_operation(unstable_operation, max_attempts=5)
        print(f"✓ Result: {result}")
    except Exception as e:
        print(f"✗ Final error: {e}")


# ===== MAIN MENU =====

def display_menu():
    """Display main menu."""
    print("\n" + "=" * 60)
    print("        ROBUST APPLICATION FRAMEWORK 🛡️")
    print("=" * 60)
    print("1. Input Validation Demo")
    print("2. Email Validation Demo")
    print("3. Password Validation Demo")
    print("4. File Operations Demo")
    print("5. Banking System Demo")
    print("6. Retry Mechanism Demo")
    print("7. Exit")
    print("=" * 60)


def main():
    """Main program."""
    print("Welcome to Robust Application Framework!")
    print("Learn error handling through practical examples!")
    
    while True:
        display_menu()
        choice = input("\nEnter your choice (1-7): ")
        
        try:
            if choice == '1':
                demo_input_validation()
            elif choice == '2':
                demo_email_validation()
            elif choice == '3':
                demo_password_validation()
            elif choice == '4':
                demo_file_operations()
            elif choice == '5':
                demo_banking_system()
            elif choice == '6':
                demo_retry_mechanism()
            elif choice == '7':
                print("\n Thanks for exploring error handling!")
                print("Write robust code! 🛡️")
                break
            else:
                print("\n✗ Invalid choice! Please select 1-7.")
        
        except KeyboardInterrupt:
            print("\n\n✗ Program interrupted by user")
            break
        except Exception as e:
            print(f"\n✗ Unexpected error: {e}")
            print("The program will continue...")
        
        input("\nPress Enter to continue...")


# Run the program
if __name__ == "__main__":
    main()
