# Complete Banking System - Week 2 Final Project
# Integrates ALL Week 2 concepts: loops, functions, decorators, recursion, error handling

from datetime import datetime
import time

# ===== CUSTOM EXCEPTIONS =====

class BankingError(Exception):
    """Base exception for banking errors."""
    pass

class InsufficientFundsError(BankingError):
    """Raised when account has insufficient funds."""
    def __init__(self, balance, amount):
        self.balance = balance
        self.amount = amount
        super().__init__(f"Insufficient funds: ${balance:.2f} available, ${amount:.2f} required")

class InvalidAmountError(BankingError):
    """Raised when amount is invalid."""
    pass

class AccountNotFoundError(BankingError):
    """Raised when account doesn't exist."""
    pass

class DailyLimitExceededError(BankingError):
    """Raised when daily transaction limit exceeded."""
    pass


# ===== DECORATORS =====

def log_transaction(func):
    """Decorator to log all transactions."""
    def wrapper(self, *args, **kwargs):
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"[{timestamp}] Transaction: {func.__name__}")
        
        try:
            result = func(self, *args, **kwargs)
            print(f"[{timestamp}] Status: SUCCESS")
            return result
        except Exception as e:
            print(f"[{timestamp}] Status: FAILED - {e}")
            raise
    
    return wrapper


def require_positive_amount(func):
    """Decorator to validate positive amounts."""
    def wrapper(self, amount, *args, **kwargs):
        if amount <= 0:
            raise InvalidAmountError("Amount must be positive")
        return func(self, amount, *args, **kwargs)
    
    return wrapper


def track_daily_limit(max_amount=5000):
    """Decorator to enforce daily transaction limits."""
    def decorator(func):
        def wrapper(self, amount, *args, **kwargs):
            today = datetime.now().date()
            
            # Reset daily total if new day
            if not hasattr(self, '_last_transaction_date') or self._last_transaction_date != today:
                self._daily_total = 0
                self._last_transaction_date = today
            
            # Check limit
            if self._daily_total + amount > max_amount:
                raise DailyLimitExceededError(
                    f"Daily limit of ${max_amount:.2f} exceeded. "
                    f"Already used ${self._daily_total:.2f} today."
                )
            
            result = func(self, amount, *args, **kwargs)
            self._daily_total += amount
            return result
        
        return wrapper
    return decorator


# ===== BANK ACCOUNT CLASS =====

class BankAccount:
    """Bank account with comprehensive functionality."""
    
    # Class variable for account counter
    _account_counter = 1000
    
    def __init__(self, owner_name, account_type="Checking", initial_balance=0):
        """
        Initialize bank account.
        
        Args:
            owner_name: Name of account owner
            account_type: Type of account (Checking/Savings)
            initial_balance: Starting balance
        """
        self.account_number = self._generate_account_number()
        self.owner_name = owner_name
        self.account_type = account_type
        self.balance = initial_balance
        self.transactions = []
        self.created_date = datetime.now()
        self._daily_total = 0
        self._last_transaction_date = None
        
        # Interest rate for savings accounts
        self.interest_rate = 0.02 if account_type == "Savings" else 0.0
        
        # Log account creation
        self._log_transaction("Account Created", initial_balance, "Initial deposit")
    
    @classmethod
    def _generate_account_number(cls):
        """Generate unique account number."""
        cls._account_counter += 1
        return f"ACC{cls._account_counter:06d}"
    
    def _log_transaction(self, trans_type, amount, description=""):
        """Log transaction to history."""
        transaction = {
            "timestamp": datetime.now(),
            "type": trans_type,
            "amount": amount,
            "balance": self.balance,
            "description": description
        }
        self.transactions.append(transaction)
    
    @log_transaction
    @require_positive_amount
    def deposit(self, amount, description="Deposit"):
        """
        Deposit money into account.
        
        Args:
            amount: Amount to deposit
            description: Transaction description
        
        Raises:
            InvalidAmountError: If amount is not positive
        """
        self.balance += amount
        self._log_transaction("Deposit", amount, description)
        print(f"✓ Deposited ${amount:.2f}")
        print(f"  New balance: ${self.balance:.2f}")
        return True
    
    @log_transaction
    @require_positive_amount
    @track_daily_limit(max_amount=5000)
    def withdraw(self, amount, description="Withdrawal"):
        """
        Withdraw money from account.
        
        Args:
            amount: Amount to withdraw
            description: Transaction description
        
        Raises:
            InvalidAmountError: If amount is not positive
            InsufficientFundsError: If insufficient balance
            DailyLimitExceededError: If daily limit exceeded
        """
        # Check sufficient funds
        if amount > self.balance:
            raise InsufficientFundsError(self.balance, amount)
        
        self.balance -= amount
        self._log_transaction("Withdrawal", amount, description)
        print(f"✓ Withdrew ${amount:.2f}")
        print(f"  New balance: ${self.balance:.2f}")
        return True
    
    @log_transaction
    def transfer(self, target_account, amount, description="Transfer"):
        """
        Transfer money to another account.
        
        Args:
            target_account: Target BankAccount object
            amount: Amount to transfer
            description: Transaction description
        
        Raises:
            InvalidAmountError: If amount is not positive
            InsufficientFundsError: If insufficient balance
        """
        if amount <= 0:
            raise InvalidAmountError("Transfer amount must be positive")
        
        if amount > self.balance:
            raise InsufficientFundsError(self.balance, amount)
        
        # Perform transfer
        self.balance -= amount
        target_account.balance += amount
        
        # Log both sides
        self._log_transaction("Transfer Out", amount, 
                            f"To {target_account.account_number}")
        target_account._log_transaction("Transfer In", amount,
                                       f"From {self.account_number}")
        
        print(f"✓ Transferred ${amount:.2f} to {target_account.account_number}")
        print(f"  Your new balance: ${self.balance:.2f}")
        return True
    
    def apply_interest(self):
        """Apply interest to savings accounts."""
        if self.account_type != "Savings" or self.interest_rate == 0:
            print("Interest not applicable for this account type")
            return False
        
        interest = self.balance * self.interest_rate
        self.balance += interest
        self._log_transaction("Interest", interest, 
                            f"{self.interest_rate*100}% annual interest")
        print(f"✓ Interest applied: ${interest:.2f}")
        print(f"  New balance: ${self.balance:.2f}")
        return True
    
    def get_statement(self, num_transactions=10):
        """
        Display account statement.
        
        Args:
            num_transactions: Number of recent transactions to show
        """
        print("\n" + "=" * 80)
        print("ACCOUNT STATEMENT")
        print("=" * 80)
        print(f"Account Number: {self.account_number}")
        print(f"Owner: {self.owner_name}")
        print(f"Type: {self.account_type}")
        print(f"Current Balance: ${self.balance:.2f}")
        print(f"Created: {self.created_date.strftime('%Y-%m-%d')}")
        print("=" * 80)
        
        if not self.transactions:
            print("No transactions yet")
            return
        
        print(f"\nRECENT TRANSACTIONS (Last {num_transactions}):")
        print("-" * 80)
        print(f"{'Date/Time':<20} {'Type':<15} {'Amount':>12} {'Balance':>12} {'Description':<20}")
        print("-" * 80)
        
        # Show last N transactions
        recent = self.transactions[-num_transactions:]
        for trans in recent:
            date_str = trans['timestamp'].strftime("%Y-%m-%d %H:%M")
            print(f"{date_str:<20} {trans['type']:<15} "
                  f"${trans['amount']:>11.2f} ${trans['balance']:>11.2f} "
                  f"{trans['description']:<20}")
        
        print("=" * 80)
    
    def search_transactions(self, **kwargs):
        """
        Search transactions by criteria.
        
        Kwargs:
            trans_type: Transaction type to filter
            min_amount: Minimum amount
            max_amount: Maximum amount
            start_date: Start date
        
        Returns:
            List of matching transactions
        """
        results = self.transactions.copy()
        
        # Filter by type
        if 'trans_type' in kwargs:
            results = [t for t in results if t['type'] == kwargs['trans_type']]
        
        # Filter by amount range
        if 'min_amount' in kwargs:
            results = [t for t in results if t['amount'] >= kwargs['min_amount']]
        
        if 'max_amount' in kwargs:
            results = [t for t in results if t['amount'] <= kwargs['max_amount']]
        
        return results
    
    def __str__(self):
        """String representation of account."""
        return (f"Account({self.account_number}, {self.owner_name}, "
                f"${self.balance:.2f})")
    
    def __repr__(self):
        """Official string representation."""
        return self.__str__()


# ===== BANK MANAGER CLASS =====

class BankManager:
    """Manages multiple bank accounts."""
    
    def __init__(self):
        """Initialize bank manager."""
        self.accounts = {}
    
    def create_account(self, owner_name, account_type="Checking", initial_balance=0):
        """Create new account."""
        try:
            account = BankAccount(owner_name, account_type, initial_balance)
            self.accounts[account.account_number] = account
            print(f"\n✓ Account created successfully!")
            print(f"  Account Number: {account.account_number}")
            print(f"  Owner: {owner_name}")
            print(f"  Type: {account_type}")
            print(f"  Initial Balance: ${initial_balance:.2f}")
            return account
        except Exception as e:
            print(f"✗ Error creating account: {e}")
            return None
    
    def get_account(self, account_number):
        """Get account by number."""
        if account_number not in self.accounts:
            raise AccountNotFoundError(f"Account {account_number} not found")
        return self.accounts[account_number]
    
    def list_accounts(self):
        """List all accounts."""
        if not self.accounts:
            print("No accounts found")
            return
        
        print("\n" + "=" * 80)
        print("ALL ACCOUNTS")
        print("=" * 80)
        print(f"{'Account #':<15} {'Owner':<25} {'Type':<12} {'Balance':>15}")
        print("-" * 80)
        
        for acc_num, account in self.accounts.items():
            print(f"{acc_num:<15} {account.owner_name:<25} "
                  f"{account.account_type:<12} ${account.balance:>14.2f}")
        
        print("=" * 80)
        print(f"Total accounts: {len(self.accounts)}")
    
    def total_deposits(self):
        """Calculate total deposits across all accounts."""
        return sum(account.balance for account in self.accounts.values())


# ===== HELPER FUNCTIONS =====

def get_validated_input(prompt, input_type=str, min_val=None, max_val=None):
    """
    Get validated input from user.
    
    Args:
        prompt: Input prompt
        input_type: Expected type (str, int, float)
        min_val: Minimum value (for numbers)
        max_val: Maximum value (for numbers)
    
    Returns:
        Validated input
    """
    while True:
        try:
            value = input(prompt).strip()
            
            if input_type == str:
                if value:
                    return value
                print("✗ Input cannot be empty!")
                continue
            
            # Convert to number type
            value = input_type(value)
            
            # Check range
            if min_val is not None and value < min_val:
                print(f"✗ Value must be at least {min_val}")
                continue
            
            if max_val is not None and value > max_val:
                print(f"✗ Value must be at most {max_val}")
                continue
            
            return value
        
        except ValueError:
            print(f"✗ Please enter a valid {input_type.__name__}!")
        except KeyboardInterrupt:
            print("\n✗ Input cancelled")
            return None


# ===== MAIN MENU SYSTEM =====

def display_main_menu():
    """Display main menu."""
    print("\n" + "=" * 60)
    print("           🏦 BANKING SYSTEM 🏦")
    print("=" * 60)
    print("1.  Create Account")
    print("2.  Deposit Money")
    print("3.  Withdraw Money")
    print("4.  Transfer Money")
    print("5.  Check Balance")
    print("6.  View Statement")
    print("7.  Apply Interest (Savings)")
    print("8.  List All Accounts")
    print("9.  Search Transactions")
    print("10. Exit")
    print("=" * 60)


def main():
    """Main banking system program."""
    bank = BankManager()
    
    print("=" * 60)
    print("   Welcome to the Complete Banking System!")
    print("=" * 60)
    print("\nThis system demonstrates all Week 2 concepts:")
    print("✓ Loops (for, while)")
    print("✓ Functions (basic & advanced)")
    print("✓ Decorators (@log_transaction, @require_positive_amount)")
    print("✓ Error Handling (custom exceptions)")
    print("✓ Classes & Objects")
    
    # Main loop
    while True:
        display_main_menu()
        choice = input("\nEnter your choice (1-10): ")
        
        try:
            if choice == '1':
                # Create account
                print("\n--- Create New Account ---")
                name = get_validated_input("Enter owner name: ", str)
                if not name:
                    continue
                
                print("\nAccount types:")
                print("1. Checking")
                print("2. Savings")
                type_choice = get_validated_input("Choose type (1-2): ", int, 1, 2)
                account_type = "Checking" if type_choice == 1 else "Savings"
                
                initial = get_validated_input("Initial deposit ($): ", float, 0)
                if initial is None:
                    continue
                
                bank.create_account(name, account_type, initial)
            
            elif choice == '2':
                # Deposit
                print("\n--- Deposit Money ---")
                acc_num = get_validated_input("Enter account number: ", str)
                account = bank.get_account(acc_num)
                
                amount = get_validated_input("Amount to deposit ($): ", float, 0.01)
                if amount:
                    account.deposit(amount)
            
            elif choice == '3':
                # Withdraw
                print("\n--- Withdraw Money ---")
                acc_num = get_validated_input("Enter account number: ", str)
                account = bank.get_account(acc_num)
                
                amount = get_validated_input("Amount to withdraw ($): ", float, 0.01)
                if amount:
                    account.withdraw(amount)
            
            elif choice == '4':
                # Transfer
                print("\n--- Transfer Money ---")
                from_acc = get_validated_input("From account number: ", str)
                to_acc = get_validated_input("To account number: ", str)
                
                source = bank.get_account(from_acc)
                target = bank.get_account(to_acc)
                
                amount = get_validated_input("Amount to transfer ($): ", float, 0.01)
                if amount:
                    source.transfer(target, amount)
            
            elif choice == '5':
                # Check balance
                print("\n--- Check Balance ---")
                acc_num = get_validated_input("Enter account number: ", str)
                account = bank.get_account(acc_num)
                
                print(f"\nAccount: {account.account_number}")
                print(f"Owner: {account.owner_name}")
                print(f"Balance: ${account.balance:.2f}")
            
            elif choice == '6':
                # View statement
                print("\n--- Account Statement ---")
                acc_num = get_validated_input("Enter account number: ", str)
                account = bank.get_account(acc_num)
                account.get_statement()
            
            elif choice == '7':
                # Apply interest
                print("\n--- Apply Interest ---")
                acc_num = get_validated_input("Enter account number: ", str)
                account = bank.get_account(acc_num)
                account.apply_interest()
            
            elif choice == '8':
                # List all accounts
                bank.list_accounts()
                print(f"\nTotal deposits in bank: ${bank.total_deposits():.2f}")
            
            elif choice == '9':
                # Search transactions
                print("\n--- Search Transactions ---")
                acc_num = get_validated_input("Enter account number: ", str)
                account = bank.get_account(acc_num)
                
                print("\nFilter by:")
                print("1. Transaction type")
                print("2. Amount range")
                filter_choice = get_validated_input("Choose (1-2): ", int, 1, 2)
                
                if filter_choice == 1:
                    trans_type = get_validated_input("Enter type (Deposit/Withdrawal/Transfer): ", str)
                    results = account.search_transactions(trans_type=trans_type)
                else:
                    min_amt = get_validated_input("Minimum amount: ", float, 0)
                    max_amt = get_validated_input("Maximum amount: ", float, min_amt)
                    results = account.search_transactions(min_amount=min_amt, max_amount=max_amt)
                
                print(f"\nFound {len(results)} transactions")
                for trans in results:
                    print(f"  {trans['timestamp'].strftime('%Y-%m-%d %H:%M')} - "
                          f"{trans['type']}: ${trans['amount']:.2f}")
            
            elif choice == '10':
                # Exit
                print("\n" + "=" * 60)
                print("Thank you for using the Banking System!")
                print(f"Total accounts: {len(bank.accounts)}")
                print(f"Total deposits: ${bank.total_deposits():.2f}")
                print("\nGoodbye!")
                print("=" * 60)
                break
            
            else:
                print("\n✗ Invalid choice! Please select 1-10.")
        
        except AccountNotFoundError as e:
            print(f"\n✗ {e}")
        except InsufficientFundsError as e:
            print(f"\n✗ {e}")
        except InvalidAmountError as e:
            print(f"\n✗ {e}")
        except DailyLimitExceededError as e:
            print(f"\n✗ {e}")
        except BankingError as e:
            print(f"\n✗ Banking error: {e}")
        except KeyboardInterrupt:
            print("\n\n✗ Operation cancelled by user")
        except Exception as e:
            print(f"\n✗ Unexpected error: {e}")
            print("Please try again or contact support.")
        
        input("\nPress Enter to continue...")


# Run the banking system
if __name__ == "__main__":
    main()
