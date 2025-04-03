from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from behave import given, when, then
from time import sleep

 @@ -12,14 +13,16 @@
@given('Open target main page')
def open_target_main(context):
    context.driver.get('https://www.target.com/')
    context.driver.wait.until(
        EC.element_to_be_clickable(SEARCH_FIELD),
        message='Search field not clickable'
    )

@when('Search for {search_word}')
def search_product(context, search_word):
    context.driver.find_element(*SEARCH_FIELD).send_keys(search_word)
    context.driver.find_element(*SEARCH_BTN).click()
    sleep(7)


@when('Click on Cart icon')