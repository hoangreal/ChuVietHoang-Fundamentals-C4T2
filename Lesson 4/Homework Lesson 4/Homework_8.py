class Car:
    brand = 'Audi'
    MaxSpeed = 200
    def setBrand(self,brand):
        self.brand = brand
    def setMaxSpeed(self,MaxSpeed):
        self.MaxSpeed = MaxSpeed
    def printData(self):
        print("An",self.brand,"with maximum speed =",self.MaxSpeed)

n= Car()
n.printData()
