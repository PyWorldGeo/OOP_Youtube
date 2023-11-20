import csv

class Car:
    discount_rate = 0.8
    all = []
    def __init__(self, name: str, price: float, quantity=0):

        assert len(name) > 0, "You entered empty name!"
        assert len(name) < 15, "You entered long name!"
        assert price > 0, "Price must be more than 0"

        self.__name = name
        self.price = price
        self.quantity = quantity

        Car.all.append(self)

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        assert len(value) > 0, "You entered empty name!"
        assert len(value) < 15, "You entered long name!"
        self.__name = value

    def total_price(self):
        print(f"Total Price is: {self.price * self.quantity}")

    def calculate_discount(self):
        return self.price * self.discount_rate

    def __repr__(self):
        return f"{self.__class__.__name__}({self.__name}, {self.price}, {self.quantity})"

    @classmethod
    def create_car(cls):
        with open("cars.csv", "r") as file:
            cars_info = list(csv.DictReader(file))

            for car in cars_info:
                Car(
                    name=car["name"],
                    price=float(car["price"]),
                    quantity=float(car["quantity"])
                )

    @staticmethod
    def check_data_type(x):
        return type(x)

    def __check_somthing(self):
        pass

    def answer(self):
        self.__check_somthing()
        print("Checked!")




