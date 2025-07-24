class Account:
    _id_counter = 1  # Class variable to assign unique IDs to each account

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

# Create 3 unique account instances
account1 = Account("Alice", 1000)
account2 = Account("Bob", 500)
account3 = Account("Charlie", 750)

# Store accounts in a list
accounts = [account1, account2, account3]

# Display each account
for acc in accounts:
    print(acc)
