# Single Inheritence means One Parent to One Child
# Sample code for single inheritence 

class Vehicle:                     # Parent
    def __init__(self, brand):
        self.brand = brand

    def show_brand(self):
        print("Brand:", self.brand)


class Car(Vehicle):                # Child
    def __init__(self, brand, model):
        super().__init__(brand)    # Parent constructor
        self.model = model

    def show_model(self):
        print("Model:", self.model)


# Object of child class
c1 = Car("BMW", "X7")

c1.show_brand()   # Parent method
c1.show_model()   # Child method

