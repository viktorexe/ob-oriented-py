# Inheritence means a new class (child) gets all attributes from an existing class (parent)

class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    
    def vehicle_info(self):
        print("Brand:", self.brand)
        print('Model:', self.model)

class Car(Vehicle): # Child Class
    def __init__(self, brand, model, wheels, fuel, year):
        super().__init__(brand, model)
        self.wheels = wheels
        self.fuel = fuel
        self.year = year
    
    def car_info(self):
        print('Wheels',self.wheels)
        print("Fuel",self.fuel)
        print('Year',self.year)

car_1 = Car('BMW', 'X7', 4, 'Petrol', 2019)
car_1.vehicle_info()
car_1.car_info()