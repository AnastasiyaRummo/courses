from selenium.webdriver.common.by import By


class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    def open(self):
        self.driver.get("https://www.saucedemo.com/")

    def login(self, username):
        self.driver.find_element(By.ID, "user-name").send_keys(username)

        password_text = self.driver.find_element(
            By.CSS_SELECTOR, ".login_password").text
        colon_index = password_text.find(':')

        if colon_index != -1:
            password = password_text[colon_index + 1:].strip()
            self.driver.find_element(By.ID, "password").send_keys(password)
        else:
            raise Exception("Пароль не найден на странице")

        self.driver.find_element(By.ID, "login-button").click()
