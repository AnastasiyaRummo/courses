class Card:
    number = '0000 0000 0000 0000'
    validDate = '01/99'
    holder = 'unknown'

    def __init__(self, _number, _date, _holder):
        self.holder = _holder
        self.number = _number
        self.validDate = _date

    def pay(self, amount):
        print("с карты", self.number, "списали", amount)
