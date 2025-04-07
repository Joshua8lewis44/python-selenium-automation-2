from selenium.webdriver.common.by import By
from pages.base_page import Page

class Header(Page):
    # Locators
    SEARCH_BAR = (By.CSS_SELECTOR, "input[aria-label='Search']")
    LOGO = (By.CSS_SELECTOR, "a[aria-label='Go to homepage']")
    ACCOUNT_MENU = (By.CSS_SELECTOR, "button[aria-label='Account menu']")
    CART_ICON = (By.CSS_SELECTOR, "button[aria-label='Cart icon']")
    SIGN_IN_LINK = (By.CSS_SELECTOR, "[data-test='signInLink']")

    def click_sign_in(self):
        self.click(*self.SIGN_IN_LINK)

    def search_for_product(self, product_name):
        self.send_keys(*self.SEARCH_BAR, product_name)

    def click_logo(self):
        self.click(*self.LOGO)

    def open_account_menu(self):
        self.click(*self.ACCOUNT_MENU)

    def view_cart(self):
        self.click(*self.CART_ICON)
