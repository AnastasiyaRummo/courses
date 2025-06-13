from address import Address
from mail import Mailing

to_adrs = Address('111111', 'Санкт-Петербург', 'Ленинский проспект', '115', '56')
from_adrs = Address('222222', 'Санкт-Петербург', 'улица Лесная', '45', '22')

mail = Mailing(to_address=to_adrs, from_address=from_adrs, track='3456789', cost=500)
print(f"Отправление {mail.track} из {mail.from_address.i}, {mail.from_address.c}, "
      f"{mail.from_address.s}, {mail.from_address.h} - {mail.from_address.f} "
      f"в {mail.to_address.i}, {mail.to_address.c}, {mail.to_address.s}, {mail.to_address.h} - {mail.to_address.f}. "
      f"Стоимость {mail.cost} рублей.")
