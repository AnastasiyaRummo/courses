# 2)Високосный год
# Выведите в консоль ответ: год <номер года>: <True|False>
def is_year_leap(n):
    return (True if n % 4 == 0 else False)


n = int(input("Введите год: "))
result = is_year_leap(n)
print(f"год {n}: {result}")
