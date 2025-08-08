import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webdriver import WebDriver


class CalcPage:
    """
       Класс представляет страницу калькулятора и методы для
       взаимодействия с ней.
    """
    def __init__(self, driver: WebDriver):
        """
            Инициализация страницы калькулятора.
            :param driver: WebDriver – экземпляр драйвера Selenium.
        """
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 50)

    @allure.step("Открытие страницы калькулятора")
    def open(self) -> None:
        """
           Открывает веб-страницу калькулятора.
           :return: None
        """
        self.driver.get("https://bonigarcia.dev/"
                        "selenium-webdriver-java/slow-calculator.html")

    @allure.step("Установка задержки: {seconds} секунд")
    def set_delay(self, seconds: int) -> None:
        """
           Устанавливает задержку выполнения операций в калькуляторе.
           :param seconds: int – количество секунд для задержки.
           :return: None
        """
        delay = self.driver.find_element(By.ID, "delay")
        delay.clear()
        delay.send_keys(str(seconds))

    @allure.step("Нажатие кнопки: {value}")
    def click_button(self, value: str) -> None:
        """
           Нажимает на кнопку калькулятора по значению (число или операция).
           :param value: str – текст кнопки (например, '7', '+', '=' и т.д.).
           :return: None
        """
        button = self.driver.find_element(
            By.XPATH, f"//span[text()='{value}']")
        button.click()

    @allure.step("Получение результата с экрана калькулятора")
    def get_result(self, expected_result: str) -> str:
        """
            Ожидает отображения заданного результата на экране
            калькулятора и возвращает его.
            :param expected_result: str – ожидаемый результат (например, "15").
            :return: str – текст, отображаемый на экране калькулятора.
        """
        result_locator = (By.CSS_SELECTOR, "div.top div.screen")

        with allure.step(f"Ожидание появления текста '{expected_result}' "
                         f"в элементе {result_locator}"):
            self.wait.until(EC.text_to_be_present_in_element(
                result_locator, expected_result))

        result_text = self.driver.find_element(*result_locator).text
        allure.attach(result_text, name="Результат на экране",
                      attachment_type=allure.attachment_type.TEXT)
        return result_text
