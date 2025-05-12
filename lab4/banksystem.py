from bankclasses import *
# Create a bank
my_bank = Bank("Simple Bank")

# Create customers
customer1 = Customer("C1001", "Alice Johnson", "alice@example.com", "555-1234")
customer2 = Customer("C1002", "Bob Smith", "bob@example.com", "555-5678")

# Add customers to the bank
my_bank.add_customer(customer1)
my_bank.add_customer(customer2)

# Create accounts for customers
account1 = my_bank.create_account(customer1, "Savings", 1000)
account2 = my_bank.create_account(customer1, "Checking", 500)
account3 = my_bank.create_account(customer2, "Savings", 1500)

# Perform some transactions
account1.deposit(200)
account2.withdraw(100)
my_bank.transfer_money(account1.account_number, account3.account_number, 300)

# Print some information
print("Customer 1 Info:")
print(customer1.get_customer_info())
print("\nAccount 1 Statement:")
print(account1.get_account_statement())
print("\nAccount 3 Statement:")
print(account3.get_account_statement())