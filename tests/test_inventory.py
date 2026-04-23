from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage


def test_inventory_items_displayed(driver):
    login_page = LoginPage(driver)
    inventory_page = InventoryPage(driver)

    login_page.open()
    login_page.login("standard_user", "secret_sauce")

    items_count = inventory_page.get_items_count()

    assert items_count > 0

def test_add_item_to_cart(driver):
    login_page = LoginPage(driver)
    inventory_page = InventoryPage(driver)

    login_page.open()
    login_page.login("standard_user", "secret_sauce")

    inventory_page.add_first_item_to_cart()

    assert inventory_page.get_cart_badge_count() == "1"
