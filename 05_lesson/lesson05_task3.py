# Упражнение 3. Поле ввода
# Открыть браузер FireFox.
# Перейти на страницу: http://the-internet.herokuapp.com/inputs.
# Ввести в поле текст Sky.
# Очистить это поле (метод clear()).
# Ввести в поле текст Pro.
# Закрыть браузер (метод quit()).

from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

driver = webdriver.Firefox()
driver.get("http://the-internet.herokuapp.com/inputs")

input_field = driver.find_element(By.TAG_NAME, "input")
input_field.send_keys("Sky")
sleep(2)
input_field.clear()
sleep(2)
input_field.send_keys("Pro")
sleep(2)

driver.quit()
