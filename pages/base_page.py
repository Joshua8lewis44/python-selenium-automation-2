from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Page:
    def __init__(self, driver):
        self.driver = driver

    def open_page(self, url):
        """Opens a page by the given URL"""
        self.driver.get(url)  # Use WebDriver's get() method to open the page

    def wait_until_visible(self, *locator):
        """Wait until an element is visible on the page"""
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(locator)
        )

    def find_element(self, *locator):
        """Find a single element"""
        return self.driver.find_element(*locator)

    def send_keys(self, *locator, text):
        """Send keys to an input field"""
        element = self.find_element(*locator)
        element.clear()
        element.send_keys(text)

    def click(self, *locator):
        """Click on an element"""
        element = self.find_element(*locator)
        element.click()

    def is_element_present(self, *locator):
        """Check if an element is present on the page"""
        try:
            self.find_element(*locator)
            return True
        except:
            return False
