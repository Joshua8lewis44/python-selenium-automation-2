from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Set up WebDriver
driver = None
wait = None

@given('I navigate to the Target sign-in page')
def step_impl(context):
    global driver, wait
    driver = webdriver.Chrome(executable_path='/path/to/chromedriver')  # Specify your chromedriver path
    driver.maximize_window()
    wait = WebDriverWait(driver, 10)
    driver.get("https://www.target.com/account/login")

@when('I enter the correct email and click Continue')
def step_impl(context):
    email_field = wait.until(EC.presence_of_element_located((By.ID, "username")))  # Real locator for email input
    email_field.send_keys("testuser@example.com")  # Use your test email
    continue_button = driver.find_element(By.ID, "login")  # Real locator for the "Continue" button
    continue_button.click()

@when('I enter the incorrect password and click Sign In')
def step_impl(context):
    password_field = wait.until(EC.presence_of_element_located((By.ID, "password")))  # Real locator for password input
    password_field.send_keys("incorrectpassword123")  # Use an incorrect password
    sign_in_button = driver.find_element(By.ID, "login")  # Real locator for the "Sign In" button
    sign_in_button.click()

@then('I should see an error message indicating invalid password')
def step_impl(context):
    error_message = wait.until(EC.presence_of_element_located((By.ID, "password--ErrorMessage")))  # Real locator for error message
    assert error_message.is_displayed(), "Error message not displayed"
    print("Error message is displayed: Password is incorrect")

    driver.quit()