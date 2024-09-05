class BankAccount:
    def __init__(self, first_name, last_name, account_id, account_type, pin, balance):
        self.first_name = first_name
        self.last_name = last_name
        self.account_id = account_id
        self.account_type = account_type
        self.pin = pin
        self.balance = balance
    
    def deposit(self, amount):
        self.balance = self.balance + amount
        return self.balance

    def withdraw(self, amount):
        self.balance = self.balance - amount
        return self.balance

    def display_balance(self):
        print(self.balance)
    

business_account = BankAccount('Ozzy', 'TheGolden', 12345, 'business', 1212, 250.00)    

business_account.display_balance()

business_account.deposit(100)

business_account.display_balance()

business_account.withdraw(100)

business_account.display_balance()
