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


class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = []

    def describe_flavors(self):
        for flavor in self.flavors:
            print(flavor)


Ice1 = IceCreamStand("Ice333", "Eng")
Ice1.flavors = ['333', '222', '111']
Ice1.describe_flavors()
