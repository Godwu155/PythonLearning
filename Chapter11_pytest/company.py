
class Employee:
    def __init__(self, first_name, last_name, salary):
        self.first_name = first_name
        self.last_name = last_name
        self.salary = int(salary)

    def add_salary(self, add_money = 5000):
        self.salary += add_money


    def get_salary(self):
        return self.salary

    def get_name(self):
        return self.first_name + ' ' + self.last_name
