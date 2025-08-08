import allure
import pytest
from selenium import webdriver
from page_calc_allure import CalcPage


@pytest.fixture
def driver():
    """
       Фикстура для инициализации и завершения работы драйвера.
       :return: WebDriver – экземпляр браузера Chrome.
    """
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()


@pytest.mark.parametrize(
    "num1, operation, num2, expected_result, delay",
    [
        ("7", "+", "8", "15", 45),
        ("9", "-", "3", "6", 45),
        ("4", "x", "5", "20", 45),
        ("8", "÷", "2", "4", 45),
    ],
)
@allure.title("Проверка: {num1} {operation} {num2} = {expected_result}")
@allure.description("Проверка корректности арифметических "
                    "операций в калькуляторе.")
@allure.feature("Калькулятор")
@allure.severity(allure.severity_level.CRITICAL)
def test_calculator_addition(driver, num1, operation, num2,
                             expected_result, delay):
    """
       Тест арифметических операций на калькуляторе.
       :param driver: WebDriver – экземпляр драйвера.
       :param num1: str – первое число.
       :param operation: str – операция: +, -, x, ÷.
       :param num2: str – второе число.
       :param expected_result: str – ожидаемый результат.
       :param delay: int – задержка перед отображением результата.
    """

    with allure.step("Открытие страницы калькулятора"):
        calc = CalcPage(driver)
        calc.open()

    with allure.step(f"Установка задержки в {delay} секунд"):
        calc.set_delay(delay)

    with allure.step(f"Ввод выражения: {num1} {operation} {num2}"):
        calc.click_button(num1)
        calc.click_button(operation)
        calc.click_button(num2)
        calc.click_button("=")

    with allure.step("Получение и проверка результата"):
        result = calc.get_result(expected_result)
        allure.attach(result, name="Полученный результат",
                      attachment_type=allure.attachment_type.TEXT)
        assert result == expected_result, \
            f"Ожидался результат '{expected_result}', но получен '{result}'"
