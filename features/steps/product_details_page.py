from selenium.webdriver.common.by import By
from pages.base_page import Page

class ProductDetailsPage(Page):
    # Locators for product details page
    PRODUCT_NAME = (By.CSS_SELECTOR, "h1.product-name")
    ADD_TO_CART_BUTTON = (By.CSS_SELECTOR, "[data-test='add-to-cart-button']")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".product-price")

    def add_to_cart(self):
        self.click(*self.ADD_TO_CART_BUTTON)

    def get_product_name(self):
        element = self.find_element(*self.PRODUCT_NAME)
        return element.text

    def get_product_price(self):
        element = self.find_element(*self.PRODUCT_PRICE)
        return element.text

