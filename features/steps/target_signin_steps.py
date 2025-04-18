from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


@given('Open target main page')
def open_target_main(context):
    context.driver.get('https://www.target.com/')


@when('Click Sign In')
def click_sign_in(context):
    context.driver.find_element(By.CSS_SELECTOR, 'button.styles_ndsBaseButton__W8Gl7.styles_ndsButtonPrimary__tqtKH').click()



@when('Click Sign In from side menu')
def click_sign_in_menu(context):
    context.driver.find_element(By.CSS_SELECTOR, 'button[data-test="accountNav-signIn"]').click()



@then('Verify Sign In form is shown')
def verify_sign_in_form(context):
    expected_text = 'Sign into your Target account'
    actual_text = context.driver.find_element(By.XPATH, "//h1[contains(@class, 'styles_ndsHeading')]").text
    assert expected_text in actual_text, f'Expected "{expected_text}" but got "{actual_text}"'
