from selenium.webdriver.common.by import By
from pages.base_page import Page


class SignInPage(Page):
    SIGN_IN_FORM = (By.CSS_SELECTOR, "form[method='post']")  # Sign-In form
    EMAIL_FIELD = (By.ID, "username")  # Email field
    PASSWORD_FIELD = (By.ID, "password")  # Password field
    SIGN_IN_BUTTON = (By.ID, "login")  # Sign In button

    def verify_sign_in_form(self):
        self.wait_until_visible(*self.SIGN_IN_FORM)
        assert self.find_element(*self.SIGN_IN_FORM), "Sign In form not displayed"

    def open(self):
        """Open the Sign-In page"""
        self.open_page("/sign-in")  # This should work if open_page is defined in the Page class
