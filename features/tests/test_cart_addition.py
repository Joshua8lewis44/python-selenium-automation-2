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


@when('User adds the product to the cart')
def step_when_user_adds_product_to_cart(context):
    # Wait for search results to load
    context.driver.implicitly_wait(10)

    # Find and click the first product in the search results
    product = context.driver.find_element(By.CSS_SELECTOR,
                                          ".styles__StyledItem-sc-1xwcpnq-2")  # Adjust selector as needed
    product.click()

    # Add to cart button (the actual button selector may vary, inspect the page to find the correct one)
    add_to_cart_button = context.driver.find_element(By.CSS_SELECTOR, "[data-test='product-detail-add-to-cart-button']")
    add_to_cart_button.click()


@when('User navigates to the cart')
def step_when_user_navigates_to_cart(context):
    cart_button = context.driver.find_element(By.CSS_SELECTOR, "[data-test='cart-button']")
    cart_button.click()


@then('The total price of the cart should be greater than 0')
def step_then_verify_cart_total_price(context):
    # Wait for the cart page to load
    context.driver.implicitly_wait(10)

    # Find the total price element in the cart (adjust the selector based on the page structure)
    total_price_element = context.driver.find_element(By.CSS_SELECTOR, "[data-test='cart-total-price']")
    total_price = total_price_element.text.strip().replace('$', '')

    # Convert the total price to float and verify it is greater than 0
    assert float(total_price) > 0, f'Expected cart total price to be greater than 0, but got {total_price}.'