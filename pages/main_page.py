from selenium.webdriver.common.by import By
from pages.base_page import Page

class MainPage(Page):
    SIGN_IN_LINK_HEADER = (By.CSS_SELECTOR, ".sc-43f80224-3.gBSMpH")  # Header Sign In link

    def click_sign_in_from_header(self):
        self.click(*self.SIGN_IN_LINK_HEADER)  # Click on Sign In from header

