# In hierarchial inheritence, one parent has multiple child 

class Vehicle:
    def __init__(self, brand):
        self.brand = brand
    
    def vehicle_info(self):
        print('Brand:', self.brand)

class Car(Vehicle):
    def __init__(self, brand, model):
        Vehicle.__init__(self, brand)
        self.model = model
    
    def car_info(self):
        print('Model:', self.model)

class Type(Vehicle):
    def __init__(self, brand, type):
        Vehicle.__init__(self, brand)
        self.type = type 

    def type_info(self):
        print('Type:', self.type)

car_1 = Car('BMW', 'X7')
car_1.vehicle_info()
car_1.car_info()
print('')
car_2 = Type('Audi', 'Sedan')
car_2.vehicle_info()
car_2.type_info()
