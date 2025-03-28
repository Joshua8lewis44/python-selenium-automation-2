from selenium.webdriver.common.by import By
from behave import given, when, then


@given('User is on the Target homepage')
def step_given_user_on_homepage(context):
    context.driver.get("https://www.target.com")
    assert "Target" in context.driver.title, "Target homepage did not load correctly"


@when('User searches for a product "{product_name}"')
def step_when_user_searches_for_product(context, product_name):
    search_box = context.driver.find_element(By.CSS_SELECTOR, "input[data-test='search-input']")
    search_box.send_keys(product_name)
    search_box.submit()


@then('Results for "{product_name}" should be displayed')
def step_then_results_for_product_displayed(context, product_name):
    # Check if the results page has loaded correctly
    result_text = context.driver.find_element(By.CSS_SELECTOR, "span[data-test='search-header-title']").text
    assert product_name.lower() in result_text.lower(), f'Expected search results for "{product_name}" but got "{result_text}"'


@then("Verify 'Your cart is empty' message is shown")
def verify_cart_empty(context):
    expected_result = 'Your cart is empty'
    actual_result = context.driver.find_element(By.CSS_SELECTOR, "[data-test='boxEmptyMsg']").text
    assert expected_result == actual_result, f'Expected {expected_result} did not match actual {actual_result}'