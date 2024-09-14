import pytest
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage

@pytest.mark.parametrize("username,password", [("standard_user", "secret_sauce")])
def test_purchase_flow(driver, username, password):
    driver.get("https://www.saucedemo.com")

    login_page = LoginPage(driver)
    login_page.login(username, password)

    inventory_page = InventoryPage(driver)
    inventory_page.add_item_to_cart()
    inventory_page.go_to_cart()

    cart_page = CartPage(driver)
    cart_page.proceed_to_checkout()

    checkout_page = CheckoutPage(driver)
    checkout_page.fill_information("John", "Doe", "12345")
    checkout_page.finish_order()

    assert checkout_page.get_confirmation_message() == "THANK YOU FOR YOUR ORDER"

