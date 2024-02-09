class Bank:
    bankname='Bank of India'
    branch='Vadodara'

    #create account
    def __init__(self, username,  pan, address):
        self.username=username
        self.pan=pan
        self.address=address
        self.balance=0.0
        print(f'Hello, Mr/Ms. {username} Congratulation! Your account is sucessfully created')
    #deposit
    def deposit(self, amount):
        self.balance=self.balance+amount
        print(f'{amount} deposited sucessfully, Banlance in your account {self.balance}')

    #withdraw
    def withdraw(self,amount):
        if self.balance>amount:
            self.balance=self.balance-amount
            print(f'{amount} is withdrawn sucessfully! Your  Banlance is {self.balance}')
        else:
            print("Insufficient Balance")
    #Mini Statement or Check Balance
    def ministatement(self):
        print(f'Your account balance is {self.balance}')

print(f'Welcome to {Bank.bankname}, {Bank.branch}')
username=input("Enter your name: ")
pan=input("Enter your pan no: ")
address=input("Enter your address: ")
b=Bank(username, pan, address)

while True:
    option=int(input('Please Select any option: \n1. Deposit\n2. Withdraw\n3. Mini Statement\n4. Exit'))
    if option==1:
        amount=float(input("Enter Deposited Amount: "))
        b.deposit(amount)
    elif option==2:
        amount = float(input("Enter Withdrawal Amount: "))
        b.withdraw(amount)
    elif option==3:
        b.ministatement()
    elif option==4:
        print("Thanks for using Bank of India..")
        break
    else:
        print('Plese enter valid option...')





'''
class Customer:
    def __init__(self, customer_id, name, address):
        self.customer_id = customer_id
        self.name = name
        self.address = address

    def __str__(self):
        return f"Customer ID: {self.customer_id}\nName: {self.name}\nAddress: {self.address}"


class BankAccount:
    def __init__(self, account_number, customer, balance=0.0):
        self.account_number = account_number
        self.customer = customer
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposit of ${amount} successful. New balance: ${self.balance}")
        else:
            print("Invalid deposit amount. Please enter a positive value.")

    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            print(f"Withdrawal of ${amount} successful. New balance: ${self.balance}")
        else:
            print("Invalid withdrawal amount or insufficient funds.")

    def get_balance(self):
        return self.balance

    def __str__(self):
        return f"Account Number: {self.account_number}\n{str(self.customer)}\nBalance: ${self.balance}"


class Bank:
    def __init__(self, name):
        self.name = name
        self.accounts = []

    def add_account(self, account):
        self.accounts.append(account)
        print(f"Account {account.account_number} added to {self.name}.")

    def get_account(self, account_number):
        for account in self.accounts:
            if account.account_number == account_number:
                return account
        return None

    def __str__(self):
        return f"Bank Name: {self.name}\nNumber of Accounts: {len(self.accounts)}"


# Example Usage:
if __name__ == "__main__":
    # Creating a bank
    my_bank = Bank("MyBank")

    # Creating a customer
    customer1 = Customer(1, "John Doe", "123 Main St")

    # Creating a bank account for the customer
    account1 = BankAccount(101, customer1, 1000.0)

    # Adding the account to the bank
    my_bank.add_account(account1)

    # Depositing and withdrawing money
    account1.deposit(500.0)
    account1.withdraw(200.0)

    # Displaying account information
    print("\nAccount Information:")
    print(account1)

    # Accessing the bank's information
    print("\nBank Information:")
    print(my_bank)
'''