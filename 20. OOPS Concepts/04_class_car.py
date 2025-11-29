class Car:
    def __init__(self, brand, type):
        self.brand = brand              # Instance Attribute
        self.type = type                # Instance Attribute 

car_1 = Car("BMW", "Sports Car")        # car_1 is an object
car_2 = Car("Mercedese Benz", "Luxury") # car_2 is an object

print(car_1.brand, car_1.type) 
print(car_2.brand, car_2.type)