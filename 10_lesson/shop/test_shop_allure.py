import allure
import pytest
from selenium import webdriver
from pages.login_page_allure import LoginPage
from pages.goods_page_allure import GoodsPage
from pages.cart_page_allure import CartPage
from pages.checkout_page_allure import CheckoutPage


@pytest.fixture
def driver():
    """
    Фикстура для инициализации и завершения работы драйвера.
    :return: WebDriver – экземпляр браузера Firefox.
    """
    driver = webdriver.Firefox()
    driver.maximize_window()
    yield driver
    driver.quit()


@allure.title("Покупка товаров в интернет-магазине")
@allure.description("Проверка корректности добавления товаров "
                    "в корзину и оформления заказа.")
@allure.feature("Интернет-магазин")
@allure.severity(allure.severity_level.CRITICAL)
def test_shop(driver):
    """
        Тест сценария покупки товаров: вход, добавление в корзину,
        оформление, проверка суммы.
    """
    with allure.step("Авторизация пользователя"):
        login = LoginPage(driver)
        login.open()
        login.login("standard_user")

    with allure.step("Добавление товаров в корзину"):
        goods = GoodsPage(driver)
        goods.add_items_to_cart()
        goods.go_to_cart()

    with allure.step("Переход к оформлению заказа"):
        cart = CartPage(driver)
        cart.proceed_to_checkout()

    with allure.step("Заполнение формы оформления заказа"):
        checkout = CheckoutPage(driver)
        checkout.fill_form("Anastasiya", "Rummo", "198207")

    with allure.step("Получение итоговой суммы заказа"):
        total = checkout.get_total()

    with allure.step("Проверка итоговой суммы"):
        assert abs(total - 58.29) < 0.001, f"Expected 58.29, but got {total}"
