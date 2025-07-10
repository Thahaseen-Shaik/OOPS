#Create a class Marks with private math marks. Add methods to update and display the marks safely.
class Marks:
    def __init__(self,name,mathmarks):
        self.name=name
        self.__mathmark=mathmarks
    def getMarks(self):
        return self.__getMarks
    def setMarks(self,getMarks):
        self.__getMarks += getMarks
m=Marks("abc",50)
print(m.getMarks())
m.setMarks(99)
print(m.getMarks())
print(acc.__Marks__getMarks)