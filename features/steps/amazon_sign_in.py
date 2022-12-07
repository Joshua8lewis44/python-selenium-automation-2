# Home_work_3 by Andy_Piri, Automation-12

#0 Coded during the class
from behave import given, then
import selenium.webdriver.common.by
from selenium.webdriver.common.by import By

@given("Open the Amazon Page")
def step_impl(context):
    context.driver.get("https://www.amazon.com/")


# @step("click on 'icon_logo' button: icon_logo, 'Amazon'")
# def step_impl(context):
# # HW3_2: Update a test case to verify that logged out user sees "Sign_In when clicked on Returns and Orders to use Behave (BDD)
# # Init driver
#         driver=webdriver.Chrome(executable_path='/users/owner/Desktop/JobEasy/12-selenium-automation/chromedriver')
#         driver.maximize_window()
#         driver.get('https://www.amazon.com/')
#         driver.find_element(By.ID, 'nav-orders).click')()
#         Expected_text= 'Sign in'
#         actual_text= driver.find_element (By.XPATH, "//h1/(@class 'a-spacing-small')").text
#         assert actual_text=='expected_text', ('Expected {expected_text} but got {actual_text})'
#
#  # Verify Sign In header is visible
#         assert driver.find_element (By.Class, 'Create_account'),'Create account field not visible'
#
#  # Verify email field is present
#         assert driver.find_element (By.ID,'ap_email'), 'Email field not shown'
#         driver.quit()


@step("Click on Orders button")
def step_impl(context):
    context.driver.find_element(By.ID, "nav-orders").click()


@then("Sign in page opened: Sign In header is visible, email input field is present.")
def step_impl(context):
    sign_in_expected = "Sign in"

    sign_in_text_actual = context.driver.find_element(By.XPATH, "//h1[@class='a-spacing-small']").text
    print(sign_in_text_actual)
    assert sign_in_expected == sign_in_text_actual, f'Expected Text not found'


@step("Click on the Cart icon")
def step_impl(context):
    context.driver.find_element(By.PARTIAL_LINK_TEXT, "Cart").click()


@then('Verify that "Your Amazon Cart is empty" message is displayed')
def step_impl(context):
    expected_text = "Your Amazon Cart is empty"
    actual_text = context.driver.find_element(By.XPATH, "//div[@class='a-row sc-your-amazon-cart-is-empty']/h2").text
    assert expected_text == actual_text, f'Expected Text not found, but found [{actual_text}]'


@given("Open the Amazon Bestseller  Page")
def step_impl(context):
    context.driver.get("https://www.amazon.com/gp/bestsellers/?ref_=nav_cs_bestsellers")


@then('Verify that user is able to see {expected_links} links')
def step_impl(context, expected_links):
    links = context.driver.find_elements(By.XPATH, "//div[@class='_p13n-zg-nav-tab-all_style_zg-tabs__EYPLq']/ul/li/div/a")
    actual_link_count = len(links)
    assert  expected_links == str(actual_link_count), f"Expected {expected_links} links but found {str(actual_link_count)} links"
