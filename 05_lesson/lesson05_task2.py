# Упражнение 2. Клик по кнопке без ID
# Открыть браузер Google Chrome.
# Перейти на страницу: http://uitestingplayground.com/dynamicid.
# Кликнуть на синюю кнопку.
# Запустите скрипт три раза подряд. Убедитесь, что он отработает одинаково

from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

driver = webdriver.Chrome()
driver.get("http://uitestingplayground.com/dynamicid")
sleep(5)

button = driver.find_element(By.CSS_SELECTOR, "button.btn.btn-primary")
button.click()
sleep(5)
