from selenium.webdriver.common.by import By
from pages.base_page import Page

class SearchResultsPage(Page):
    # Locators for search results page
    RESULTS_LIST = (By.CSS_SELECTOR, ".search-results")
    FIRST_PRODUCT = (By.CSS_SELECTOR, ".search-results .product-item")

    def get_first_product(self):
        return self.find_element(*self.FIRST_PRODUCT)

    def get_results_list(self):
        return self.find_elements(*self.RESULTS_LIST)
