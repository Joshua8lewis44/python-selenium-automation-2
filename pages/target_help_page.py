from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


class TargetHelpPage:
    def __init__(self, driver):
        self.driver = driver

    def select_dropdown_option(self, option_text):
        # Find the dropdown element using the real ID
        dropdown = self.driver.find_element(By.ID, 'j_id0:contentTemplate:j_id79:j_id80:viewHelpTopics:ViewHelpTopics')
        select = Select(dropdown)
        # Select the option by visible text
        select.select_by_visible_text(option_text)

    def get_current_url(self):
        return self.driver.current_url

