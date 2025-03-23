from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from time import sleep

# Setup Chrome options for Incognito mode
chrome_options = Options()
chrome_options.add_argument("--incognito")

# Set up the driver with Chrome options
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

# Open Amazon Sign In Page
driver.get("https://www.amazon.com/ap/signin")

# Example of accessing elements by XPath and ID
amazon_logo = driver.find_element(By.XPATH, '//*[@id="nav-logo-sprites"]')  # Amazon logo by XPath
email_field = driver.find_element(By.ID, "ap_email")  # Email field by ID
continue_button = driver.find_element(By.ID, "continue")  # Continue button by ID
conditions_of_use_link = driver.find_element(By.XPATH, '//*[text()="Conditions of Use"]')  # Conditions of Use link by XPath
privacy_notice_link = driver.find_element(By.XPATH, '//*[text()="Privacy Notice"]')  # Privacy Notice link by XPath
need_help_link = driver.find_element(By.XPATH, '//*[text()="Need help?"]')  # Need Help link by XPath
forgot_password_link = driver.find_element(By.XPATH, '//*[text()="Forgot your password?"]')  # Forgot your password link by XPath
other_issues_link = driver.find_element(By.XPATH, '//*[text()="Other issues with Sign-In"]')  # Other issues link by XPath
create_account_button = driver.find_element(By.ID, "createAccountSubmit")  # Create your Amazon account button by ID

# Sleep for 2 seconds to observe the elements, then close the browser
sleep(2)
driver.quit()