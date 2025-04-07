from pages.sign_in_page import SignInPage
from pages.header import Header
from pages.main_page import MainPage
from pages.side_nav_page import SideNavPage  # Import the new SideNavPage

class Application:
    def __init__(self, driver):
        self.driver = driver
        self.header = Header(driver)
        self.main_page = MainPage(driver)
        self.sign_in_page = SignInPage(driver)
        self.side_nav_page = SideNavPage(driver)