# Inspecting an object means gathering information about that object 

def extra_info(cls):
    cls.country = 'India'
    return cls

@extra_info
class Car:
    car_color = 'Black'
    def __init__(self, brand, age):
        self.brand =brand
        self.age = age
    
    def show(self):
        print('Car brand is:',self.brand,'\nCar is',self.age,'years old.','Color of car is',self.car_color)

car_1 = Car('BMW', '10')
car_1.show()
print('Country of car is:',car_1.country)
print('\n')
print('Object information below:\n')\

# Type of object 
print('Type of car_1 object is:',type(car_1))

# Unique memory address
print('Unique memory address of object is:',id(car_1))

# Attributes of object
print('Attributes of object are:',dir(car_1))

# Object attribute in dictionary
print('Attributes of object in dictionary:',vars(car_1))

# Boolean to check what class object belongs to 
print(isinstance(car_1, Car))

# To check if object has that attribute
print(hasattr(car_1, "age"))

# To fetch an attribute 
print(getattr(car_1, "brand"))

# To set a new attribute 
setattr(car_1, 'color', 'black')
print(car_1.color)