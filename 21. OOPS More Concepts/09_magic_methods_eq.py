class Car:
    def __init__(self, price):
        self.price = price
    
    def __eq__(self, other):
        return self.price == other.price
    
car1 = (100)
car2 = (100)
print(car1 == car2) # True or False output 
