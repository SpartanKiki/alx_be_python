# bank_account.py

class BankAccount:
    """Simple BankAccount class with basic operations."""

    def __init__(self, initial_balance=0):
        """
        Initialize account balance.
        initial_balance can be int or float; store as float internally.
        """
        try:
            self._balance = float(initial_balance)
        except (TypeError, ValueError):
            # If initialization value is invalid, set balance to 0.0
            self._balance = 0.0

    def deposit(self, amount):
        """
        Add amount to the account balance.
        Returns the new balance.
        """
        try:
            amt = float(amount)
        except (TypeError, ValueError):
            raise ValueError("Deposit amount must be a number.")
        if amt < 0:
            raise ValueError("Deposit amount must be non-negative.")
        self._balance += amt
        return self._balance

    def withdraw(self, amount):
        """
        Attempt to subtract amount from balance.
        If funds are sufficient, subtract and return True.
        If insufficient funds, do not change balance and return False.
        """
        try:
            amt = float(amount)
        except (TypeError, ValueError):
            raise ValueError("Withdrawal amount must be a number.")
        if amt < 0:
            raise ValueError("Withdrawal amount must be non-negative.")

        if amt <= self._balance:
            self._balance -= amt
            return True
        else:
            return False

    def display_balance(self):
        """
        Print the current balance in a friendly format.
        This prints integers without .0 and floats with decimals.
        """
        # Choose display format: integer if whole number, otherwise show float
        if float(self._balance).is_integer():
            display = int(self._balance)
        else:
            display = self._balance
        print(f"Current Balance: ${display}")
