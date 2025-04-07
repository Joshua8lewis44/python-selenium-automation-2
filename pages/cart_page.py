from selenium.webdriver.common.by import By
from pages.base_page import Page

class CartPage(Page):
    CART_ICON = (By.CSS_SELECTOR, "svg[use*='Cart']")  # Cart icon
    CHECKOUT_BUTTON = (By.CSS_SELECTOR, "[data-test='checkout-button']")  # Checkout button
    REMOVE_ITEM_BUTTON = (By.CSS_SELECTOR, "[data-test='cartItem-deleteBtn']")  # Remove item button
    EMPTY_CART_MESSAGE = (By.CSS_SELECTOR, ".styles_ndsHeading__HcGpD")  # Empty cart message

    def remove_item_from_cart(self):
        self.click(*self.REMOVE_ITEM_BUTTON)

    def proceed_to_checkout(self):
        self.click(*self.CHECKOUT_BUTTON)

    def get_cart_items(self):
        return self.find_elements(*self.CART_ITEMS)
