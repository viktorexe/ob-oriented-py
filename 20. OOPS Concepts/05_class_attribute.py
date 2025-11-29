# Class attribute is a value which is commone for all attributes 
# Let us do this by using same car class

class Car:
    vehicle_type = '4 Wheeler'

    def __init__(self, name, type):
        self.name = name
        self.type = type
    
    def show(self):
        print(self.name, self.type, self.vehicle_type)

car_1 = Car("BMW", "Sedan")
car_2 = Car("Audi", "SUV")

car_1.show()
car_2.show()