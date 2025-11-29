# Method overriding means overriding an attrobute from Parent Class
# Function from parent re used

class Vehicle:
    def __init__(self, brand):
        self.brand = brand
    
    def vehicle_info(self):
        print("Parent Class:", self.brand)

class Car(Vehicle):
    def __init__(self, brand):
        Vehicle.__init__(self, brand)
        
    def vehicle_info(self):
        print("Child class:", self.brand)

car_1 = Car('BMW')
car_1.vehicle_info()