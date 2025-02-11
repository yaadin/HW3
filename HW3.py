from datetime import datetime

class Amount:
    def __init__(self, amount:int,transaction_type:str):
        self.amount = amount
        self.timestamp = datetime.now()
        self.transaction_type = transaction_type

    def __str__(self):
        return f"{self.transaction_type}: ${self.amount} on {self.timestamp.strftime('%Y/%m/%d ')}"

class PersonalAccount:
    def __init__(self, account_number : int, account_holder : str):
        self._account_number = account_number
        self._account_holder = account_holder
        self._balance = 0
        self._transactions = []

    def deposit(self, amount):
        x = Amount(amount, "DEPOSIT")
        self._transactions.append(x)
        self._balance = self._balance + amount

    def withdrowal(self, amount):
        x = Amount(amount, "WITHDROWAL")
        if self._balance - amount < 0:
            return "unsufficial funds"
        else:
            self._balance = self._balance - amount
            self._transactions.append(x)
    
    def print_transaction_history(self):
        for i in self._transactions:
            print(i)

    def get_balance(self):
        return self._balance

    def get_account_number(self):
        return self._account_number
    
    def set_account_number(self, account_number):
        self._account_number = account_number

    def get_account_holder(self):
        return self._account_holder
    
    def set_account_holder(self, account_holder):
        self._account_holder = account_holder
    
    def __str__(self):
        return f"Account holder: {self.get_account_holder()}\nAccount number: {self.get_account_number()}\nBalance: {self.get_balance()}"

    def __add__(self,amount):
        if type(amount) != float and type(amount) != int:
            raise ValueError
        
        self.deposit(amount)
        return self
    
    def __sub__(self,amount):
        if type(amount) != float and type(amount) != int:
            raise ValueError
    
        self.withdrowal(amount)
        return self


meder = PersonalAccount(123,'meder')
meder.deposit(1000)
print(meder.get_balance())

meder.withdrowal(500)
print(meder.get_balance())

meder.print_transaction_history()

print(meder + 1000)
print(meder - 300)
        
