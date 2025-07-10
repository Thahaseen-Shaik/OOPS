class Student:
    def __init__(self,name,price):
        self.name=name
        self.price=price
    def getName(self):
        print(self.name)
    def getPrice(self):
        print(self.price)
p1=Student("Thahaseen",50)
p1.getName()
p1.getPrice()
