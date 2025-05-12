class Customer:
    def __init__(self, customer_id, name, email, phone):
        self.customer_id = customer_id
        self.name = name
        self.email = email
        self.phone = phone
        self.accounts = []  # This will hold Account objects

    def add_account(self, account):
        self.accounts.append(account)

    def get_accounts(self):
        return self.accounts

    def get_customer_info(self):
        return {
            "Customer ID": self.customer_id,
            "Name": self.name,
            "Email": self.email,
            "Phone": self.phone,
            "Number of Accounts": len(self.accounts)
        }


class Account:
    def __init__(self, account_number, account_type, initial_balance=0):
        self.account_number = account_number
        self.account_type = account_type  # e.g., "Savings", "Checking"
        self.balance = initial_balance
        self.transactions = []

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            self.transactions.append(f"Deposit: +{amount}")
            return True
        return False

    def withdraw(self, amount):
        if amount > 0 and self.balance >= amount:
            self.balance -= amount
            self.transactions.append(f"Withdrawal: -{amount}")
            return True
        return False

    def get_balance(self):
        return self.balance

    def get_account_statement(self):
        statement = f"Account Statement for #{self.account_number}\n"
        statement += f"Current Balance: {self.balance}\n"
        statement += "Transaction History:\n"
        for transaction in self.transactions:
            statement += f"- {transaction}\n"
        return statement


class Bank:
    def __init__(self, bank_name):
        self.bank_name = bank_name
        self.customers = []  # This will hold Customer objects
        self.accounts = []  # This will hold Account objects

    def add_customer(self, customer):
        self.customers.append(customer)

    def create_account(self, customer, account_type, initial_balance=0):
        # Generate a simple account number (in real system, this would be more complex)
        account_number = f"{customer.customer_id}-{len(self.accounts) + 1}"
        new_account = Account(account_number, account_type, initial_balance)
        customer.add_account(new_account)
        self.accounts.append(new_account)
        return new_account

    def transfer_money(self, from_account_num, to_account_num, amount):
        # Find the accounts
        from_account = None
        to_account = None

        for account in self.accounts:
            if account.account_number == from_account_num:
                from_account = account
            if account.account_number == to_account_num:
                to_account = account

        if not from_account or not to_account:
            return False  # One or both accounts not found

        if from_account.withdraw(amount):
            to_account.deposit(amount)
            from_account.transactions.append(f"Transfer to {to_account_num}: -{amount}")
            to_account.transactions.append(f"Transfer from {from_account_num}: +{amount}")
            return True
        return False

