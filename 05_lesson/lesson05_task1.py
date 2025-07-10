# Упражнение 1. Клик по кнопке с CSS-классом
# Открыть браузер Google Chrome.
# Перейти на страницу: http://uitestingplayground.com/classattr.
# Кликнуть на синюю кнопку.
# Запустите скрипт три раза подряд. Убедитесь, что он отработает одинаково.

from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

driver = webdriver.Chrome()
driver.get("http://uitestingplayground.com/classattr")
sleep(2)

button = driver.find_element(By.XPATH,
                             "//button[contains(@class, 'btn-primary')]")
button.click()
sleep(10)
