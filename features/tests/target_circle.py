from selenium.webdriver.common.by import By
from behave import given, when, then

@given('User is on the Target Circle page')
def step_given_user_on_target_circle_page(context):
    context.driver.get("https://www.target.com/circle")
    assert "Target Circle" in context.driver.title, "Target Circle page did not load correctly"

@then('There should be at least 10 benefit cells on the page')
def step_then_verify_at_least_10_benefit_cells(context):
    benefit_cells = context.driver.find_elements(By.CSS_SELECTOR, "[data-test='benefit-cell']")
    assert len(benefit_cells) >= 10, f'Expected at least 10 benefit cells, but found {len(benefit_cells)}.'