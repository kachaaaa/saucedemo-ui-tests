from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class CartPage(BasePage):

    CART_ITEMS = (By.CLASS_NAME, "cart_item")

    def get_cart_items_count(self):
        return len(self.find_all(self.CART_ITEMS))
