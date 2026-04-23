from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage


class InventoryPage(BasePage):

    INVENTORY_ITEMS = (By.CLASS_NAME, "inventory_item")
    ADD_TO_CART_BUTTONS = (By.CSS_SELECTOR, ".btn_inventory")
    CART_BADGE = (By.CLASS_NAME, "shopping_cart_badge")
    CART_LINK = (By.CLASS_NAME, "shopping_cart_link")

    MENU_BUTTON = (By.ID, "react-burger-menu-btn")
    LOGOUT_LINK = (By.ID, "logout_sidebar_link")

    # -------------------------
    # Inventory actions
    # -------------------------

    def get_items_count(self):
        return len(self.find_all(self.INVENTORY_ITEMS))

    def add_first_item_to_cart(self):
        buttons = self.find_all(self.ADD_TO_CART_BUTTONS)
        buttons[0].click()

    # -------------------------
    # Cart actions
    # -------------------------

    def get_cart_badge_count(self):
        return self.get_text(self.CART_BADGE)

    def open_cart(self):
        self.click(self.CART_LINK)

    # -------------------------
    # Auth actions
    # -------------------------

    def logout(self):
        self.click(self.MENU_BUTTON)

        self.wait.until(
            EC.element_to_be_clickable(self.LOGOUT_LINK)
        ).click()
