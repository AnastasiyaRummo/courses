class Friend:
    nameFriend = 'Tony'
    surnameFriend = 'Stark'

    def __init__(self, nameFriend, surnameFriend):
        self.nameFr = nameFriend
        self.surnameFr = surnameFriend

    def tell(self, ):
        print("моего друга зовут ", self.nameFr, "фамилия друга ", self.surnameFr)
