class Pub:
    def __init__(self, name, till, drink_list):
        self.name = name
        self.till = till
        self.drink_list = drink_list


    def increase_till(self, amount):
        self.till += amount