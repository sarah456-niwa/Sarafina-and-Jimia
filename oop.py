# Create a class called Car with attributes brand and color. Instantiate an object of the Car class and print its attributes.
class Car:
    def __init__(self, brand, color):
        self.brand = brand
        self.color = color
my_car = Car("Toyota", "Red")
print(f'Car Brand: {my_car.brand}')
print(f'Car Color: {my_car.color}')

#  Add a method called start_engine to the Car class that prints a message saying the engine of the car has started. Create an instance of Car and call the method.
class Car:
    def __init__(self, brand, color):
        self.brand = brand
        self.color = color
    def start_engine(self):
        print(f"The engine of the {self.brand} {self.color} car has started.")
my_car = Car("Toyota", "Red")
my_car.start_engine()

# Advanced: Create a class called BankAccount with attributes account_number and balance. Add methods to:
# Deposit an amount.
# Withdraw an amount (only if sufficient balance exists).
# Print the account balance.
class BankAccount:
    def __init__(self, account_number, balance=0):
        self.account_number = account_number
        self.balance = balance
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited ${amount}. New balance is ${self.balance}.")
        else:
            print("Deposit amount must be positive.")
    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew ${amount}. New balance is ${self.balance}.")
        else:
            print("Insufficient balance for this withdrawal.")
    def print_balance(self):
        print(f"Account balance: ${self.balance}")
my_account = BankAccount("123456", 500)
my_account.deposit(200)
my_account.withdraw(100)
my_account.print_balance
my_account.withdraw(700)

# # Implement a class called Library that manages a collection of books. Each book has a title, author, and available status. The Library class should have methods to:
# Add a book to the library.
# Remove a book from the library.
# Check if a book is available by title.
# Borrow a book (mark it as unavailable if it’s available).
# Return a book (mark it as available again if it was borrowed).




