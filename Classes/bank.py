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

class Account:
    balance=20000
    def __init__(self,name,number,deposit):
        self.name=name
        self.number=number
        self.deposit=deposit
    def get_new_balance(self):
        return self.balance+self.deposit
    def get_details(self):
        return f"The owner of Account{self.number} is {self.name}."
    def confirm(self):
        return f"{self.name} is a KCB customer."
account1=Account("Mia Imali","2009876",20)
account2=Account("Princess Diana", "0987654",57600)
account3=Account("Pink Brown","45675432",0)
