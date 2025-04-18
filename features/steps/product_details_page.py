from selenium.webdriver.common.by import By
from behave import given, then
from selenium.webdriver.support import expected_conditions as EC

COLOR_OPTIONS = (By.CSS_SELECTOR, "div[data-test='colorSwatch'] li img")
SELECTED_COLOR = (By.CSS_SELECTOR, "[data-test='@web/VariationComponent'] div")

@given('Open target product {product_id} page')
def open_target_product(context, product_id):
    context.driver.get(f'https://www.target.com/p/{product_id}')
    context.driver.wait.until(
        EC.presence_of_element_located(COLOR_OPTIONS),
        message='Color swatches did not load'
    )

@then('Verify user can click through and confirm colors')
def click_and_verify_each_color(context):
    colors = context.driver.find_elements(*COLOR_OPTIONS)
    selected_colors = []

    for index in range(len(colors)):
        # Re-locate the elements each time to avoid stale element error
        colors = context.driver.find_elements(*COLOR_OPTIONS)
        color = colors[index]
        context.driver.execute_script("arguments[0].scrollIntoView(true);", color)
        color.click()

        context.driver.wait.until(
            EC.visibility_of_element_located(SELECTED_COLOR),
            message='Selected color not visible'
        )

        selected_text = context.driver.find_element(*SELECTED_COLOR).text
        color_name = selected_text.split("\n")[1] if '\n' in selected_text else selected_text
        print(f"Selected color: {color_name}")
        selected_colors.append(color_name)

    print("All selected colors:", selected_colors)
    assert len(selected_colors) > 1, "Expected multiple colors to be selected"
