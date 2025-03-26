#User opens Target.com, clicks Sign In, and verifies the Sign In form is opened
   # Given the user is on the Target homepage
   # When the user clicks on Sign In
   # And the user clicks Sign In from the right side navigation menu
   # Then the Sign In form should be displayed

   #finally, verify that a logged-out user can navigate to the Sign In page

from selenium import webdriver
from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time


# Setup WebDriver for Behave
def before_all(context):
    # Initialize the Chrome driver before running tests
    context.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    context.driver.maximize_window()


def after_all(context):
    # Close the browser after tests
    context.driver.quit()


# Step Definitions (outside of setup and teardown functions)

@given('the user is on the Target homepage')
def step_given_user_is_on_target_homepage(context):
    context.driver.get("https://www.target.com")


@when('the user clicks on Sign In')
def step_when_user_clicks_sign_in(context):
    # Find and click the Sign In link (you can inspect the actual selector)
    sign_in_link = context.driver.find_element(By.CSS_SELECTOR, "a[data-test='accountNav-signIn']")
    sign_in_link.click()


@when('the user clicks Sign In from the right side navigation menu')
def step_when_user_clicks_sign_in_from_right_side_nav(context):
    # Find and click the Sign In link in the right-side navigation menu
    side_nav_sign_in = context.driver.find_element(By.CSS_SELECTOR, "a[data-test='accountNav-signIn']")
    side_nav_sign_in.click()


@then('the Sign In form should be displayed')
def step_then_sign_in_form_should_be_displayed(context):
    # Wait for the Sign In form to be visible (optional sleep for better synchronization)
    time.sleep(2)  # You can replace this with WebDriverWait for better synchronization

    # Verify if the Sign In form is displayed (use an appropriate selector)
    form_element = context.driver.find_element(By.CSS_SELECTOR, "#login-form")  # Update with actual selector
    assert form_element.is_displayed(), "Sign In form is not displayed"

    #This is for a single-test setup