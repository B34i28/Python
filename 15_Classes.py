class Car():
    # Attributes
    def __init__(self,make,model,year):
        self.make = make
        self.model = model
        self.year = year
        self.battery = "200amp" #defalut Attribute
    # Behaviour
    def descriptionCar(self):
        print(f"The make of car is {self.make}")
        print(f"The make of car is {self.model}")
        print(f"The Year of car is {self.year}")
    def move(self):
        print(f"{self.make} is moving with speed")
    def applyingBreak(self):
        print(f"{self.model} has applied the Break")
    def desBattery(self):
        print(f"The of Car is {self.battery}")
    def setBattreySize(self,newSize):
        self.battery = newSize
    def getBatterySize(self):
        print(f"The size of Your battery is {self.battery}")

# Creating object of Class
car1 = Car("Honda","Civic",2019)
car2 = Car("Suzuki","Mehran", 2000)
#car1.applyingBreak()
#car1.descriptionCar()

# Changing an Attribute Value

# car1.make = "Yamaha"
# print(car1.make)
# print(car1.make)
# print(car1.battery)
# car1.battery = "500amp"
# print(car1.battery)
# print(car2.battery)

car1.getBatterySize()
car2.getBatterySize()
car1.setBattreySize("500amp")
car1.getBatterySize()