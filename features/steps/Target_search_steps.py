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


def step_impl(context):
    context.driver = init_driver()  # Initialize WebDriver and store in context
    context.driver.get("https://www.target.com")
    # Wait for the page to load completely and cart icon to be present
    WebDriverWait(context.driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'a[href="/cart"]')))

@when('I click on the cart icon')
def step_impl(context):
    cart_icon = context.driver.find_element(By.CSS_SELECTOR, 'a[href="/cart"]')
    cart_icon.click()
    # Wait for the cart page to load and the empty message to be visible
    WebDriverWait(context.driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, '.cart-empty-message')))

@then('I should see the "Your cart is empty" message')
def step_impl(context):
    empty_message = context.driver.find_element(By.CSS_SELECTOR, '.cart-empty-message')
    assert "Your cart is empty" in empty_message.text, f"Expected message 'Your cart is empty', but got {empty_message.text}"
    context.driver.quit()  # Close the browser after the test is done