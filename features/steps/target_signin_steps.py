from behave import given, when, then
from selenium.webdriver.common.by import By
from time import sleep

@given('Open target main page')
def open_target_main(context):
    context.driver.get('https://www.target.com/')

@when('Click account icon')
def click_account_icon(context):
    context.driver.find_element(By.CSS_SELECTOR, 'a[data-test="@web/AccountLink"]').click()

@when('Click Sign In from side menu')
def click_sign_in_from_menu(context):
    context.driver.find_element(By.CSS_SELECTOR, 'button[data-test="accountNav-signIn"]').click()

@then('Verify Sign In form is shown')
def verify_sign_in_form(context):
    expected_text = "Sign in or create account"
    actual_text = context.driver.find_element(By.CSS_SELECTOR, 'h1.styles_ndsHeading__HcGpD').text
    assert expected_text == actual_text, f'Expected '{expected_text}', but got '{actual_text}'"
