# Magic Methods = Python's hidden features 

class Car:
    def __init__(self, price):
        self.price = price 
    
    def __add__(self, other):
        return self.price + other.price
    
car1 = Car(120)
car2 = Car (82)
print(car1 + car2)