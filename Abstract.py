from abc import ABC, abstractmethod
class Abstract(ABC):
    @abstractmethod
    def pay(self,amount):
        pass
class Credit(Abstract):
    def pay(self, amount):
        print(amount,"Paid using Credit Card.")

class UPI(Abstract):
    def pay(self, amount):
        print(amount,"Paid using UPI.")
credit = Credit()
credit.pay(1500)
upi = UPI()
upi.pay(900)


