from behave import given, when, then
from pages.main_page import MainPage
from pages.sign_in_page import SignInPage

@given('Open target main page')
def step_given_open_target_main_page(context):
    context.page = MainPage(context.driver)  # Create an instance of MainPage
    context.page.open()  # Open the main page

@when('Click Sign In on header')
def step_when_click_sign_in_on_header(context):
    context.page.click_sign_in_from_header()  # Click Sign In from header

@then('Verify Sign In form opened')
def step_then_verify_sign_in_form_opened(context):
    sign_in_page = SignInPage(context.driver)  # Create an instance of SignInPage
    sign_in_page.verify_sign_in_form()  # Verify that the sign-in form is displayed
