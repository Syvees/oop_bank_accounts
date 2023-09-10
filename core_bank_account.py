class BankAccount:
    all_accounts = []

    def __init__(self, balance):
        self.balance = balance
        self.int_rate = 0.01
        BankAccount.all_accounts.append(self)

    def deposit(self, amount):
        self.balance += amount
        return self

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
        else:
            self.balance -= 5  
            print("Insufficient funds: Charging a $5 fee")
        return self
    
    def display_account_info (self):
        print(f"Balance: {self.balance}")
        return self
    
    def yield_interest(self):
        if self.balance > 0:
            interest = self.balance * self.int_rate
            self.balance += interest
            self.balance = round(self.balance,2)
        return self
    
    @classmethod #Ninja Bonus
    def all_accounts_info(cls):
        for account in cls.all_accounts:
            print(account.balance)
    
harry = BankAccount (500.75) #User Account 1
hermione = BankAccount (123.45) #User Account 2

harry.deposit(100).deposit(50).deposit(30).withdraw(80).yield_interest().display_account_info()
hermione.deposit(30).deposit(50).withdraw(10).withdraw(25).withdraw(33).withdraw(5.45).yield_interest().display_account_info()

BankAccount.all_accounts_info() #Ninja Bonus