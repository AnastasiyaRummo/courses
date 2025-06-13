class User:
    age = 0

    def __init__(self, name, friend):
        print("я создался")
        self.username = name
        self.friend = friend

    def sayName(self):
        print("меня зовут", self.username)

    def sayAge(self):
        print(self.age)

    def setAge(self, newAge):
        self.age = newAge

    def addCard(self, card):
        self.card = card

    def getCard(self):
        return self.card

    def addEmail(self, _address):
        self.address = _address

    def getMail(self):
        return self.address
