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

class Fruit:
    ripeness=True
    def __init__(self,price,quantity,name):
        self.price=price
        self.quantity=quantity
        self.name=name
    def growth_rate(self):
        return f"{self.name} is {self.ripeness}."
    def find_cost(self):
        return self.price*self.quantity
    def get_quantity(self):
        return f"There are {self.quantity} {self.name}"
fruit1=Fruit(20,5,"Apples")
fruit2=Fruit(50,30,"Watermelons")
fruit3=Fruit(100,2,"Pawpaws")
