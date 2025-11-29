# Same like decorators in functions

# Decorator function to add extra info in class
# Cls -> Class
def extra_info(cls):
    cls.model = 2010
    return cls

@extra_info
class Car:
    car_type = '4 Wheeler' # Class Attribute

    def __init__(self, name, segment):
        self.name = name
        self.segment = segment

    def show(self):
        print(self.name, self.segment, self.car_type)

car_1 = Car("BMW", "Sports Car") 
car_1.show()
print(car_1.model)
car_2 = Car("Mercedes Benz", "Luxury")
car_2.show()
print(car_2.model)
car_3 = Car("Range Rover", "Off-Roading")
car_3.show()
print(car_3.model)