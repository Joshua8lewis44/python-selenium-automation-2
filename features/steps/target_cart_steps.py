from behave import given, when, then
from selenium.webdriver.common.by import By

@given('Open target main page')
def open_target_main(context):
    context.driver.get('https://www.target.com/')

@when('Click on Cart icon')
def click_cart_icon(context):
    context.driver.find_element(By.CSS_SELECTOR, 'a[data-test="@web/CartLink"]').click()

@then('Verify cart is empty message is shown')
def verify_cart_empty_message(context):
    expected_text = "Your cart is empty"
    actual_text = context.driver.find_element(By.CSS_SELECTOR, 'h1.styles_ndsHeading__HcGpD.styles_fontSize1__i0fbt.styles_x2Margin__M5gHh').text
    assert expected_text == actual_text, f'Expected "{expected_text}", but got "{actual_text}"'
