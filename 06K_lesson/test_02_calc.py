# Калькулятор
# 1.Откройте страницу в Google Chrome:
# https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html
# 2.В поле ввода по локатору #delay введите значение 45.
# 3.Нажмите на кнопки: 7 + 8 =
# 4.Проверьте (assert), что в окне отобразится результат 15 через 45 секунд.

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_form():
    driver = webdriver.Chrome()
    driver.get(
        'https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html')
    WebDriverWait(driver, 10)

    delay = driver.find_element(By.CSS_SELECTOR, "#delay")
    delay.clear()
    delay.send_keys("45")

    seven = driver.find_element(By.XPATH, "//span[text()='7']")
    seven.click()

    plus = driver.find_element(By.XPATH, "//span[text()='+']")
    plus.click()

    eight = driver.find_element(By.XPATH, "//span[text()='8']")
    eight.click()

    equal = driver.find_element(By.XPATH, "//span[text()='=']")
    equal.click()

    wait = WebDriverWait(driver, 50)
    wait.until(EC.text_to_be_present_in_element(
        (By.CSS_SELECTOR, "div.top div.screen"), "15"))
    result = driver.find_element(By.CSS_SELECTOR, "div.top div.screen")
    result_text = result.text
    assert result_text == "15", (f"Expected result '15', "
                                 f"but got '{result_text}'")

    driver.quit()
