class Account:
    _id_counter = 1  # Class variable for unique IDs

    def __init__(self, name, balance):
        self.id = Account._id_counter
        Account._id_counter += 1
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds.")
        elif amount <= 0:
            print("Withdrawal amount must be positive.")
        else:
            self.balance -= amount

    def __str__(self):
        return f"{self.name}'s account (ID: {self.id}). Balance: {self.balance}"


# New class for testing and development purposes
class DevAccount(Account):
    def get_balance(self):
        return self.balance

    def set_balance(self, amount):
        if amount < 0:
            print("Balance cannot be negative.")
        else:
            self.balance = amount
            print(f"Balance set to {self.balance}")

    def transfer_to(self, other_account, amount):
        if not isinstance(other_account, Account):
            print("Invalid target account.")
            return

        if amount <= 0:
            print("Transfer amount must be positive.")
        elif amount > self.balance:
            print("Insufficient funds for transfer.")
        else:
            self.balance -= amount
            other_account.balance += amount
            print(f"Transferred {amount} to {other_account.name}'s account.")

# Example usage for testing
dev_acc = DevAccount("Developer", 1000)
user_acc = Account("User", 500)

print(dev_acc)
print(user_acc)

dev_acc.transfer_to(user_acc, 300)
print(dev_acc)
print(user_acc)

dev_acc.set_balance(1500)
print(f"Updated balance: {dev_acc.get_balance()}")
