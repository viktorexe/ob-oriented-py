class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def vehicle_info(self):
        print('Brand:', self.brand)
        print('Model:', self.model)


class Car:
    def __init__(self, wheels, fuel):
        self.wheels = wheels
        self.fuel = fuel

    def car_info(self):
        print('Wheels:', self.wheels)
        print('Fuel:', self.fuel)


class Year(Vehicle, Car):
    def __init__(self, brand, model, wheels, fuel, year):
        Vehicle.__init__(self, brand, model)
        Car.__init__(self, wheels, fuel)
        self.year = year

    def year_info(self):
        print('Year:', self.year)


car_1 = Year('BMW', 'X7', 4, 'Petrol', 2011)
car_1.vehicle_info()
car_1.car_info()
car_1.year_info()
