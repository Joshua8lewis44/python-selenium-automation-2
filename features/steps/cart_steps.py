from selenium.webdriver.common.by import By
from pages.base_page import Page

class CartSteps(Page):
    # Locators for interacting with cart steps
    CART_ICON = (By.CSS_SELECTOR, "button[aria-label='Cart icon']")
    CHECKOUT_BUTTON = (By.CSS_SELECTOR, "button[data-test='checkout']")

    def click_cart_icon(self):
        self.click(*self.CART_ICON)

    def click_checkout_button(self):
        self.click(*self.CHECKOUT_BUTTON)
