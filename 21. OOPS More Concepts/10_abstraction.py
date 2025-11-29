class Account:
    def __init__(self, balance):
        self.__balance = balance    # private attribute

    def deposit(self, amount):      
        self.__balance += amount

    def get_balance(self):          
        return self.__balance
    
acc = Account(1000)
acc.deposit(500)
print(acc.get_balance())
