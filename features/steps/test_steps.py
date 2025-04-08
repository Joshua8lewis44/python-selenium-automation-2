from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By  # Importing By to locate elements
from selenium.webdriver.support.ui import Select  # Importing Select to interact with dropdowns
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from time import sleep
from pages.target_help_page import TargetHelpPage  # Import the TargetHelpPage class

# Step 1: Set up the browser and navigate to the Target Help page
@given('I navigate to the Target Help page')
def step_impl(context):
    # Initialize the Chrome WebDriver using webdriver-manager
    context.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    context.driver.get('https://help.target.com/help/SubCategoryArticle?childcat=Returns&parentcat=Returns+%26+Exchanges')
    context.driver.maximize_window()
    # Create an instance of the TargetHelpPage class
    context.target_help_page = TargetHelpPage(context.driver)

# Step 2: Select a different topic from the dropdown menu
@when('I select "{topic}" from the dropdown menu')
def step_impl(context, topic):
    # Call the method from the TargetHelpPage class to select the dropdown option
    context.target_help_page.select_dropdown_option(topic)
    # Use explicit wait to ensure page has loaded
    WebDriverWait(context.driver, 10).until(
        EC.url_changes(context.driver.current_url)
    )

# Step 3: Verify that the correct page URL is loaded after selecting the dropdown option
@then('I should be redirected to the correct page for "{topic}"')
def step_impl(context, topic):
    # Verify the current URL matches the expected URL for the selected topic
    expected_url = f'https://help.target.com/help/SubCategoryArticle?childcat={topic.replace(" ", "+")}&parentcat={topic.replace(" ", "+")}'
    assert context.driver.current_url == expected_url, f"Expected URL {expected_url}, but got {context.driver.current_url}"
    # Close the browser
    context.driver.quit()
