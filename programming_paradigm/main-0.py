# main-0.py
import sys
from bank_account import BankAccount

def main():
    # start with $100 by default (matches the project example)
    account = BankAccount(100)

    if len(sys.argv) < 2:
        print("Usage: python main-0.py <command>:<amount>")
        print("Commands: deposit, withdraw, display")
        sys.exit(1)

    command, *params = sys.argv[1].split(':')
    amount = float(params[0]) if params else None

    if command == "deposit" and amount is not None:
        account.deposit(amount)
        # match the sample expected message exactly
        if float(amount).is_integer():
            amount_display = int(amount)
        else:
            amount_display = amount
        print(f"Deposited: ${amount_display}")
    elif command == "withdraw" and amount is not None:
        if account.withdraw(amount):
            if float(amount).is_integer():
                amount_display = int(amount)
            else:
                amount_display = amount
            print(f"Withdrew: ${amount_display}")
        else:
            print("Insufficient funds.")
    elif command == "display":
        account.display_balance()
    else:
        print("Invalid command.")

if __name__ == "__main__":
    main()
