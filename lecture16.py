#encapsulation
class Car:
    def __init__(self, brand):
        self._brand = brand

    def drive(self):
        print(self._brand + " is driving")

car = Car("Toyota")
car.drive()

#abstraction
