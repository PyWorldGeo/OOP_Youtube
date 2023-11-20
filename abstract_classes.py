from abc import ABC, abstractmethod

class Plan(ABC):

    @abstractmethod
    def read(self):
        pass

    @abstractmethod
    def write(self):
        pass

    @staticmethod
    def greetings():
        print("Hello!")

class Person(Plan):
    def __init__(self, name):
        self.name = name

    def read(self):
        print(self.name, "is reading!")

    def write(self):
        print(self.name, "is writing!")


obj = Person("Nika")
obj.greetings()
obj.read()