class Student: 
    def __init__(self, name, age):
        self.name = name # Instance Attribute
        self.age = age # Instance Attribute 
    
    def show(self):
        print(self.name, self.age)

s1 = Student("Vansh", 18) # s1 is an object 
s1.show()