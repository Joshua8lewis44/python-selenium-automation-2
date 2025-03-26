#User opens Target.com, clicks on cart icon, and verifies the empty cart message
   # Given the user is on the Target homepage
  #  When the user clicks on the cart icon
   # Then the "Your cart is empty" message should be displayed
   # Verify the empty cart message on Target.com

from selenium import webdriver
from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

# Set up the WebDriver

def before_all(context):
    context.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    context.driver.maximize_window()

def after_all(context):
    context.driver.quit()


@given('the user is on the Target homepage')
def step_given_user_is_on_target_homepage(context):
    global driver
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.maximize_window()
    driver.get("https://www.target.com")


@when('the user clicks on the cart icon')
def step_when_user_clicks_cart_icon(context):
    # Find and click the cart icon using CSS Selector
    cart_icon = driver.find_element(By.CSS_SELECTOR,
                                    ".CartIcon")  # Replace with the actual CSS selector of the cart icon
    cart_icon.click()


@then('the "{expected_message}" message should be displayed')
def step_then_message_should_be_displayed(context, expected_message):
    # Wait for the message to appear (optional sleep for waiting in this case)
    time.sleep(2)  # For better synchronization, use WebDriverWait in production

    # Get the message text using CSS Selector
    message_element = driver.find_element(By.CSS_SELECTOR, ".cart-empty-message")  # Replace with actual selector
    actual_message = message_element.text

    # Verify the message
    assert expected_message == actual_message, f"Expected message '{expected_message}', but got '{actual_message}'"

    # Clean up by closing the browser
    driver.quit()