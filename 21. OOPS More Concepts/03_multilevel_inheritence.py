# Multilevel Inheritence means Parent -> Child -> Grandchild

class Vehicle:      # Parent Class
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

class Type(Car):   # Grandchild Class
    def __init__(self, brand, model, wheels, fuel, year, type):
        super().__init__(brand, model, wheels, fuel, year)
        self.type = type

    def type_info(self):
        print('Type:',self.type)    

car_1 = Type('BMW', 'X7', 4, 'Petrol', 2019,'Sedan')
car_1.vehicle_info()
car_1.car_info()
car_1.type_info()