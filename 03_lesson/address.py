class Address:

    def __init__(self, index, city, street, house, flat):
        self.i = index
        self.c = city
        self.s = street
        self.h = house
        self.f = flat

    def __str__(self):
        return f"{self.i}, {self.c}, {self.s}, {self.h} - {self.f}"
