class Car :
     
    @staticmethod
    def startCar():
        print("car started....")

    @staticmethod
    def stopCar():
        print("car stopped....")

class ToyotaCar(Car): #------ inherits the properties of Car---------------------

    def printCar(self,type):
        self.type = type
        print("this is a : ", self.type," car")

class fortuner(ToyotaCar): #------------multi-level inheritence------------------

    def __init__(self,type):
        self.type = type


c1= fortuner("diesel")
c1.printCar("diesel")
c1.startCar()
c1.stopCar()
del c1
print("-----------next------------")
# c2.printCar("prius")
# c2.startCar()
# c2.stopCar()
