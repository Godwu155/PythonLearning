"""模块及描述文档"""


class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer = 0
        # self.mile = 0

    def describe_car(self):
        long_name = f"{self.make} {self.model} {self.year}"
        return long_name

    def update_odometer(self, mile):
        self.odometer += mile
        # if self.odometer >= self.odometer:
        #     self.odometer = self.odometer
        #
        # else:
        #     print("you can't roll back it")



class ElectricCar(Car):
    def __init__(self, make, model, year):

        super().__init__(make, model, year)
        self.battery = 40


    def describe_battery(self):
        print(f"This car has {self.battery} battery.")




# My_leaf = ElectricCar("Nissan", "Leaf", 2025)
# print(My_leaf.describe_car())
# My_leaf.describe_battery()