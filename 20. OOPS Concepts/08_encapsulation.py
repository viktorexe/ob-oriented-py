# Encapsulation means to show the user only the necessary details and hode compledx details 
# A private attrobute is made using __ 2 underscores
# self.__bankbalance 

class BankAccount:
    def __init__(self, balance):
        self.__balance = balance # Now this is a private attribute 
        
    def deposit(self, amount):
        self.__balance += amount
    
    def withdraw(self, amount):
        if amount <= self.__balance:
            print("Withdraw successful")
        else:
            print("Not enough balance")
    
    def get_balance(self, amount):
        return self.__balance

acc1 = BankAccount(1000)
acc1.deposit(500)
acc1.withdraw(15000)