from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CalcPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 50)

    def open(self):
        self.driver.get("https://bonigarcia.dev/"
                        "selenium-webdriver-java/slow-calculator.html")

    def set_delay(self, seconds):
        delay = self.driver.find_element(By.ID, "delay")
        delay.clear()
        delay.send_keys(str(seconds))

    def click_button(self, value):
        button = self.driver.find_element(
            By.XPATH, f"//span[text()='{value}']")
        button.click()

    def get_result(self):
        result_locator = (By.CSS_SELECTOR, "div.top div.screen")
        self.wait.until(EC.text_to_be_present_in_element(result_locator, "15"))
        return self.driver.find_element(*result_locator).text
