class Email:
    address = 'example@gmail.com'

    def __init__(self, _address):
        self.address = _address

    def get(self, getMail):
        print("получил на почту", self.address, "письмо", getMail)
