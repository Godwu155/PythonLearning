"""class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age


    def speak(self):
        print(f"({self.name} is speaking!")
"""


class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 12

    def describe_restaurant(self):
        print(f"{self.restaurant_name} is in {self.cuisine_type}")

    def open_restaurant(self):
        print(f"{self.restaurant_name} is open")

    def set_number_served(self, number):
        self.number_served = number

    def increase_number_served(self, new_number):
        self.number_served += new_number


R1 = Restaurant("niubi","Chinese")
R1.describe_restaurant()
R1.open_restaurant()
R1.number_served = 15
print(f"{R1.number_served} people served")

# R2 = Restaurant("Rest2", "English")
# R2.describe_restaurant()
R1.set_number_served(20)

print(f"{R1.number_served} people served")

R1.increase_number_served(20)
print(f"{R1.number_served} people served")