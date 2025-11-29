class Car:
    def __init__(self, brand, price):
        self.brand = brand
        self.price = price
    
    def __str__(self):
        return f"Car of brand {self.brand} is worth {self.price}"
    
car1 = Car('BMW', 100)
print(car1)