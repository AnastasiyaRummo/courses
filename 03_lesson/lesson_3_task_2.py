from smartphone import Smartphone
catalog = [
    Smartphone('Sony', 'Experia', '+79990009900'),
    Smartphone('Huawei', 'Honor', '+79980009900'),
    Smartphone('Xiaomi', 'Mi', '+79970009900'),
    Smartphone('Sumsung', 'l20', '+79960009900'),
    Smartphone('Iphone', '10', '+79950009900'),
]

for smartphone in catalog:
    print(f'{smartphone.b} - {smartphone.m}. {smartphone.n}')
