class Account:
    bank_name = "ABSA"
    def __init__(self, account_name, account_no, balance):
        self.account_name = account_name
        self.account_no = account_no
        self.balance = balance
    def deposit(self, amount):
        self.balance+= amount
        return f"{self.account_name} has deposited {amount}, the balance is {self.balance}."
    def withdraw(self, amount):
        self.balance -= amount
        return f"{self.account_name} has withdrawn {amount}, the balance is {self.balance}."
    def display_account_details(self):
        return f"{self.account_no}, {self.account_name}, {self.balance}"