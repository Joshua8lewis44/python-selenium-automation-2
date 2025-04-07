from selenium.webdriver.common.by import By
from pages.base_page import Page

class SideNavPage(Page):
    # Locator for the Sign In link in the right-side navigation
    SIGN_IN_LINK_NAV = (By.CSS_SELECTOR, "[data-test='sideNavSignInLink']")

    def click_sign_in_from_side_nav(self):
        self.click(*self.SIGN_IN_LINK_NAV)