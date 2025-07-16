# 3) Дождаться картинки. Напишите скрипт.
# Шаги:
# 1. Перейдите на сайт
# https://bonigarcia.dev/selenium-webdriver-java/loading-images.html.
# 2. Дождитесь загрузки всех картинок.
# 3. Получите значение атрибута src у 3-й картинки.
# 4. Выведите значение в консоль.

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get(
    'https://bonigarcia.dev/selenium-webdriver-java/loading-images.html')
wait = WebDriverWait(driver, 15)

wait.until(EC.text_to_be_present_in_element((By.ID, "text"), "Done!"))

images = driver.find_elements(By.TAG_NAME, 'img')
try:
    img = images[2]
    print("Значение атрибута src у третьей картинки:",
          img.get_attribute('src'))
except IndexError:
    print("На странице меньше трех изображений.")

driver.quit()
