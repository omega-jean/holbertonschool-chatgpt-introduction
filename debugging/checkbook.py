#!/usr/bin/python3
class Checkbook:
    def __init__(self):
        self.balance = 0.0

    def __deposit(self, amount):
        self.balance += amount
        print(f"Deposited ${amount:.2f}")
        self.__display_balance()

    def __withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds to complete the withdrawal.")
        else:
            self.balance -= amount
            print(f"Withdrew ${amount:.2f}")
            self.__display_balance()

    def __display_balance(self):
        print(f"Current Balance: ${self.balance:.2f}")

    def process_transaction(self, action):
        if action == 'deposit':
            amount = self.__get_valid_amount("Enter the amount to deposit: $")
            self.__deposit(amount)
        elif action == 'withdraw':
            amount = self.__get_valid_amount("Enter the amount to withdraw: $")
            self.__withdraw(amount)
        elif action == 'balance':
            self.__display_balance()
        else:
            print("Invalid command. Please try again.")

    def __get_valid_amount(self, prompt):
        while True:
            try:
                amount = float(input(prompt))
                if amount <= 0:
                    print("Amount must be positive.")
                else:
                    return amount
            except ValueError:
                print("Invalid amount. Please enter a valid number.")

def main():
    cb = Checkbook()
    while True:
        action = input("What would you like to do? (deposit, withdraw, balance, exit): ").lower()
        if action == 'exit':
            break
        cb.process_transaction(action)

if __name__ == "__main__":
    main()
