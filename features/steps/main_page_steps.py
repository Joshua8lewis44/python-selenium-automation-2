from selenium.webdriver.common.by import By


class MainPageSteps:
    # Locators
    SEARCH_BAR = (By.CSS_SELECTOR, "input[name='search']")
    SEARCH_BUTTON = (By.XPATH, "//button[@type='submit']")
    SIGN_IN_BUTTON = (By.CSS_SELECTOR, "button[data-testid='signin-button']")

    def __init__(self, driver):
        self.driver = driver

    def enter_search_query(self, query):
        search_bar = self.driver.find_element(*self.SEARCH_BAR)
        search_bar.send_keys(query)

    def click_search_button(self):
        search_button = self.driver.find_element(*self.SEARCH_BUTTON)
        search_button.click()

    def click_sign_in(self):
        sign_in_button = self.driver.find_element(*self.SIGN_IN_BUTTON)
        sign_in_button.click()
