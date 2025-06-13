# из лекции
from user import User
from card import Card
from email import Email
from friend import Friend

friend = Friend('Tony', 'SS')
friend.tell()

alex = User("Alex", friend)

alex.sayName()
alex.setAge(33)
alex.sayAge()

card = Card("4343 5667 7890", "11/28", "Alex F")
alex.addCard(card)
alex.getCard().pay(1000)

address = Email("example@gmail.com")
alex.addEmail(address)
alex.getMail().get('letter')

print(alex.friend.nameFriend, alex.friend.surnameFriend)
