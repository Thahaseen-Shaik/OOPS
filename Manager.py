#Create class Employee with method work(). Inherit it in Manager and add method manage().
class Employee:
    def work(self):
        print("Hello")
class Manager(Employee):
    def add(self):
        print("add")
m=Manager()
m.work()
m.add()
