# Форма
# 1.Откройте страницу:
# https://bonigarcia.dev/selenium-webdriver-java/data-types.html
# в Edge или Safari.
# 2.Заполните форму значениями:
# 3.Нажмите кнопку Submit.
# 4.Проверьте (assert), что поле Zip code  подсвечено красным.
# 5.Проверьте (assert), что остальные поля подсвечены зеленым.

from selenium import webdriver
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.edge.options import Options as EdgeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
options = EdgeOptions()
service = EdgeService(
    executable_path=(
        r'C:\Program Files (x86)\Microsoft\edgedriver\msedgedriver.exe'
    )
)
driver = webdriver.Edge(service=service, options=options)


def test_form():

    driver.maximize_window()
    driver.get(
        "https://bonigarcia.dev/selenium-webdriver-java/data-types.html")

    def check_field_color(driver, element, expected_color):
        WebDriverWait(driver, 10).until(
            lambda driver: element.value_of_css_property(
                'background-color') != 'rgba(0, 0, 0, 0)')

        color = element.value_of_css_property('background-color')
        if expected_color == "red":
            assert "rgba(248, 215, 218, 1)" in color, (
                f"Ожидался красный цвет, получен {color}")
        elif expected_color == "green":
            assert "rgba(209, 231, 221, 1)" in color, (
                f"Ожидался зеленый цвет, получен {color}")

    (driver.find_element(By.CSS_SELECTOR, "[name=first-name]")
     .send_keys("Иван"))
    (driver.find_element(By.CSS_SELECTOR, "[name=last-name]")
     .send_keys("Петров"))
    (driver.find_element(By.CSS_SELECTOR, "[name=address]")
     .send_keys("Ленина, 55-3"))
    (driver.find_element(By.CSS_SELECTOR, "[name=e-mail]")
     .send_keys("test@skypro.com"))
    (driver.find_element(By.CSS_SELECTOR, "[name=phone]")
     .send_keys("+7985899998787"))
    driver.find_element(By.CSS_SELECTOR, "[name=zip-code]").clear()
    (driver.find_element(By.CSS_SELECTOR, "[name=city]")
     .send_keys("Москва"))
    (driver.find_element(By.CSS_SELECTOR, "[name=country]")
     .send_keys("Россия"))
    (driver.find_element(By.CSS_SELECTOR, "[name=job-position]")
     .send_keys("QA"))
    (driver.find_element(By.CSS_SELECTOR, "[name=company]")
     .send_keys("SkyPro"))

    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    submit = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable(
                (By.XPATH, "//button[text()='Submit']"))
            )
    submit.click()

    check_fields = [
        (driver.find_element(By.ID, "zip-code"), "red"),
        (driver.find_element(By.ID, "first-name"), "green"),
        (driver.find_element(By.ID, "last-name"), "green"),
        (driver.find_element(By.ID, "address"), "green"),
        (driver.find_element(By.ID, "e-mail"), "green"),
        (driver.find_element(By.ID, "phone"), "green"),
        (driver.find_element(By.ID, "city"), "green"),
        (driver.find_element(By.ID, "country"), "green"),
        (driver.find_element(By.ID, "job-position"), "green"),
        (driver.find_element(By.ID, "company"), "green")
    ]

    for element, expected_color in check_fields:
        check_field_color(driver, element, expected_color)

    driver.quit()
