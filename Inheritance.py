from oop import *


class SomeClass:
    def __init__(self, message):
        self.message = message

    def print_message(self):
        print(self.message)


class ElectricCar(Car, SomeClass):
    def __init__(self, charged, message, name, price, quantity):
        Car.__init__(self, name, price, quantity)
        SomeClass.__init__(self, message)
        self.charged = charged

    @staticmethod
    def charging():
        print("Car is charging!")

    @staticmethod
    def check_data_type(x):
        return x*3

electric1 = ElectricCar(80, "My Message", "Electra", 2000, 4)
electric1.print_message()


