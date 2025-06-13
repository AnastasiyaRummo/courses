from address import Address
from mail import Mailing

to_adrs = Address('111111', 'Санкт-Петербург', 'Ленинский', '115', '56')
from_adrs = Address('222222', 'Санкт-Петербург', 'улица Лесная', '45', '22')

mail = Mailing(to_address=to_adrs, from_address=from_adrs,
               track='3456789', cost=500)

print(f"Отправление {mail.track} из {mail.from_address} в {mail.to_address}. "
      f"Стоимость {mail.cost} рублей.")
