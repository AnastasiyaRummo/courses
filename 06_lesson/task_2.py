# 2) Переименовать кнопку. Напишите скрипт.
# Шаги:
# 1.Перейдите на сайт http://uitestingplayground.com/textinput.
# 2.Укажите в поле ввода текст SkyPro.
# 3.Нажмите на синюю кнопку.
# 4.Получите текст кнопки и выведите в консоль ("SkyPro").

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get('http://uitestingplayground.com/textinput')

input = driver.find_element(By.CSS_SELECTOR, "#newButtonName")
input.clear()
input.send_keys("SkyPro")

blue_button = driver.find_element(By.CSS_SELECTOR, "#updatingButton")
blue_button.click()

blue_button = driver.find_element(By.CSS_SELECTOR, "#updatingButton").text
print(blue_button)

driver.quit()
