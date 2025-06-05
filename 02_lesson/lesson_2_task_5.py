# 5)Месяц-сезон

def month_to_season(n):
    if n == 12 or n == 1 or n == 2:
        print("Зима")
    elif 3 <= n <= 5:
        print("Весна")
    elif 6 <= n <= 8:
        print("Лето")
    elif 9 <= n <= 11:
        print("Осень")
    else:
        print("Введите номер месяца от 1 до 12")


n = int(input("Введите номер месяца: "))
month_to_season(n)
