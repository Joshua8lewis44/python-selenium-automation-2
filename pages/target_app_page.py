from selenium.webdriver.common.by import By
from pages.base_page import Page


class TargetAppPage(Page):
    # Updated locator using a class name
    TERMS_AND_CONDITIONS_LINK = (By.XPATH, "//a[contains(@class, 'styles_ndsLink')]")

    def open_target_app(self):
        self.open_url('https://www.target.com/login')

    def click_terms_conditions_link(self):
        # Click the Terms and Conditions link using the updated class-based locator
        self.click(*self.TERMS_AND_CONDITIONS_LINK)

    def verify_terms_conditions_opened(self):
        # Verify that the URL of the newly opened window contains 'terms-conditions'
        self.verify_partial_url('terms-conditions')
