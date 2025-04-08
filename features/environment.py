from selenium import webdriver

def before_all(context):
    # Set up the WebDriver (initialize before all tests)
    context.driver = webdriver.Chrome(executable_path='path_to_your_chromedriver')

def after_all(context):
    # Clean up after all tests
    context.driver.quit()

def before_scenario(context, scenario):
    # Setup code before each scenario (if needed)
    pass

def after_scenario(context, scenario):
    # Cleanup code after each scenario (if needed)
    pass
