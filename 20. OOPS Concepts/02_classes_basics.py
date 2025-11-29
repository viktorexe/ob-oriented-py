# Class is a blueprint / template by which objects are made 

# Syntax 
# class student:
#     pass

# Creating objects:
# s1 = Student()
# s2 = Student()

# Object is a real item made from that design 
# 
    # def __init__(self, name, age):
    #     self.name = name
    #     self.age = age
#  setups the object and gives values
# Instance attribute is the personal data

class Student:

    def __init__(self, name, age): # Sets up the object
        self.name = name           # Giving value to that object
        self.age = age             # Giving value to that object 

    def show(self):
        print(self.name, self.age)


s1 = Student("Vansh", 20)
s1.show()
