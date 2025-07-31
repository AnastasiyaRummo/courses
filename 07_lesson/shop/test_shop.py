from selenium import webdriver
from pages.login_page import LoginPage
from pages.goods_page import GoodsPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage


def test_shop():
    driver = webdriver.Firefox()
    driver.maximize_window()

    login = LoginPage(driver)
    login.open()
    login.login("standard_user")

    goods = GoodsPage(driver)
    goods.add_items_to_cart()
    goods.go_to_cart()

    cart = CartPage(driver)
    cart.proceed_to_checkout()

    checkout = CheckoutPage(driver)
    checkout.fill_form("Anastasiya", "Rummo", "198207")

    total = checkout.get_total()

    assert abs(total - 58.29) < 0.001, f"Expected 58.29, but got {total}"
    driver.quit()
