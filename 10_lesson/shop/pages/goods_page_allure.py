import allure
from selenium.webdriver.common.by import By


class GoodsPage:
    def __init__(self, driver):
        self.driver = driver

    @allure.step("Добавление товаров в корзину")
    def add_items_to_cart(self):
        self.driver.find_element(
            By.ID, "add-to-cart-sauce-labs-backpack").click()
        self.driver.find_element(
            By.ID, "add-to-cart-sauce-labs-bolt-t-shirt").click()
        self.driver.find_element(
            By.ID, "add-to-cart-sauce-labs-onesie").click()

    @allure.step("Переход в корзину")
    def go_to_cart(self):
        self.driver.find_element(By.ID, "shopping_cart_container").click()
