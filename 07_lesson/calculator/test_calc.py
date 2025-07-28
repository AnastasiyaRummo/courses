from selenium import webdriver
from page_calc import CalcPage


def test_calculator_addition():
    driver = webdriver.Chrome()

    calc = CalcPage(driver)
    calc.open()
    calc.set_delay(45)

    calc.click_button("7")
    calc.click_button("+")
    calc.click_button("8")
    calc.click_button("=")

    result = calc.get_result()
    assert result == "15", f"Ожидался результат '15', но получен '{result}'"
    driver.quit()
