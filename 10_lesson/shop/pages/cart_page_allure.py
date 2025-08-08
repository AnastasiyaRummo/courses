import allure
from selenium.webdriver.common.by import By


class CartPage:
    def __init__(self, driver):
        self.driver = driver

    @allure.step("Переход к оформлению заказа (Checkout)")
    def proceed_to_checkout(self):
        self.driver.find_element(By.ID, "checkout").click()
