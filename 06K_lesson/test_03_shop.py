# Покупка
# 1.Откройте сайт магазина: https://www.saucedemo.com/ в FireFox.
# 2.Авторизуйтесь как пользователь standard_user.
# 3.Добавьте в корзину товары:
# Sauce Labs Backpack, Sauce Labs Bolt T-Shirt, Sauce Labs Onesie.
# 4.Перейдите в корзину.
# 5.Нажмите Checkout.
# 6.Заполните форму своими данными: имя, фамилия, почтовый индекс.
# 7.Нажмите кнопку Continue.
# 8.Прочитайте со страницы итоговую стоимость (Total).
# 9.Проверьте, что итоговая сумма равна $58.29
# 10.Закройте браузер.

from selenium import webdriver
from selenium.webdriver.common.by import By


def test_form():
    driver = webdriver.Firefox()
    driver.get("https://www.saucedemo.com/")

    username = driver.find_element(By.ID, "user-name")
    username.send_keys("standard_user")

    password = driver.find_element(By.CSS_SELECTOR, ".login_password").text
    colon_index = password.find(':')

    if colon_index != -1:
        password_input = password[colon_index + 1:]
        driver.find_element(By.ID, "password").send_keys(password_input)

    login = driver.find_element(By.ID, "login-button")
    login.click()

    backpack = driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack")
    backpack.click()

    bolt_t_shirt = driver.find_element(
        By.ID, "add-to-cart-sauce-labs-bolt-t-shirt")
    bolt_t_shirt.click()

    onesie = driver.find_element(By.ID, "add-to-cart-sauce-labs-onesie")
    onesie.click()

    basket = driver.find_element(By.ID, "shopping_cart_container")
    basket.click()

    checkout = driver.find_element(By.ID, "checkout")
    checkout.click()

    first_name = driver.find_element(By.ID, "first-name")
    first_name.send_keys("Anastasiya")

    last_name = driver.find_element(By.ID, "last-name")
    last_name.send_keys("Rummo")

    postal_code = driver.find_element(By.ID, "postal-code")
    postal_code.send_keys("198207")

    continue_button = driver.find_element(By.ID, "continue")
    continue_button.click()

    total = driver.find_element(By.CLASS_NAME, "summary_total_label").text

    total_index = total.find('$')
    if total_index != -1:

        total_input = total[total_index + 1:]

        total_value = float(total_input)

        assert abs(total_value - 58.29) < 0.001, \
            f"Expected 58.29, but got {total_value}"
    driver.quit()
