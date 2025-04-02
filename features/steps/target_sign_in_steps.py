from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Initialize WebDriver correctly for Selenium 4
def init_driver():
    options = Options()
    options.headless = False  # Set to True if you don't want the browser window to open
    service = Service(ChromeDriverManager().install())  # Service for ChromeDriver path
    driver = webdriver.Chrome(service=service, options=options)
    driver.maximize_window()
    return driver

# Step Definitions

@given('I am on the Target homepage')
def step_impl(context):
    context.driver = init_driver()  # Initialize WebDriver and store in context
    context.driver.get("https://www.target.com")
    # Wait for the page to load completely and cart icon to be present
    WebDriverWait(context.driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'a[href="/cart"]')))

@when('I click on the "Sign In" link in the navigation menu')
def step_impl(context):
    sign_in_link = context.driver.find_element(By.CSS_SELECTOR, 'a[href="/account"]')
    sign_in_link.click()
    # Wait for the Sign In link to load
    WebDriverWait(context.driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'a[href="/account/signin"]')))

@when('I click the "Sign In" option from the right-side navigation menu')
def step_impl(context):
    sign_in_button = context.driver.find_element(By.CSS_SELECTOR, 'a[href="/account/signin"]')
    sign_in_button.click()
    # Wait for the Sign In form to appear
    WebDriverWait(context.driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'form#sign-in-form')))

@then('I should see the Sign In form')
def step_impl(context):
    # Verify that the Sign In form is visible
    sign_in_form = context.driver.find_element(By.CSS_SELECTOR, 'form#sign-in-form')
    assert sign_in_form.is_displayed(), "Sign In form was not displayed!"
    context.driver.quit()  # Close the browser after the test is done