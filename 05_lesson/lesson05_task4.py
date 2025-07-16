# Упражнение 4. Форма авторизации
# Открыть браузер FireFox.
# Перейти на страницу http://the-internet.herokuapp.com/login.
# В поле username ввести значение tomsmith.
# В поле password ввести значение SuperSecretPassword!.
# Нажать кнопку Login.
# Вывести текст с зеленой плашки в консоль.
# Закрыть браузер (метод quit()).

from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

driver = webdriver.Firefox()
driver.get("http://the-internet.herokuapp.com/login")

username_field = driver.find_element(By.ID, "username")
username_field.send_keys("tomsmith")
sleep(2)

password_field = driver.find_element(By.ID, "password")
password_field.send_keys("SuperSecretPassword!")
sleep(2)

login_button = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
login_button.click()

message = driver.find_element(By.CSS_SELECTOR, "div.flash.success")
print(message.text)
sleep(5)

driver.quit()
