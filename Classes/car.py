# Create 3 files in the classes directory car.py, fruit.py, and bank.py. Define the following classes in each module respectively. 
# Car
# Fruit
# Account
# Each class should have one class attribute and three instance variables.
# Discuss in your group and come up with the attributes and three methods (behaviours)
# for each class and implement them
# Then do the following in the interpreter 
# Create two instances of each class. 
# Call each of the methods you defined.

class Car:
    wheels=4
    def __init__(self,make,model,mileage):
        self.make=make
        self.model=model
        self.mileage=mileage
    def hoot(self):
        return f"Time for the {self.make} to peeeeeeeep."
    def advertise(self):
        return f"{self.make} {self.model} has {self.wheels} and a mileage of {self.mileage}."
    def get_distance(self):
        fuel_quantity=6
        distance=self.mileage*fuel_quantity
        return distance
car1=Car("Toyota","Corolla",12000)
car2=Car("Mercedes-Benz","CTS",24000)
car3=Car("BMW","X3",30000)
