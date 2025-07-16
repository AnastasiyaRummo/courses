# 1) Нажать на кнопку. Напишите скрипт.
# Шаги:
# 1. Перейдите на страницу http://uitestingplayground.com/ajax.
# 2. Нажмите на синюю кнопку.
# 3. Получите текст из зеленой плашки.
# 4. Выведите его в консоль ("Data loaded with AJAX get request.").

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get('http://uitestingplayground.com/ajax')

driver.find_element(By.CSS_SELECTOR, "#ajaxButton").click()
driver.implicitly_wait(17)

txt = driver.find_element(By.CSS_SELECTOR, "p.bg-success").text
print(txt)

driver.quit()
