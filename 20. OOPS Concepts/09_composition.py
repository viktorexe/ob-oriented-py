# Composition means using object of other class

class Info:
    def __init__(self, name, country, state):
        self.name = name
        self.country = country
        self.state = state
        
class Car:
    def __init__(self, brand, country, state):
        self.brand = brand
        self.location = Info(brand, country, state)

    
    def show(self):
        print('Brand:',self.brand)
        print('Country',self.location.country)
        print('State',self.location.state)
    
car_1 = Car('BMW', 'India', 'Delhi')
car_1.show()    