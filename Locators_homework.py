from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

#get the path from webdriver executable
driver_path = ChromeDriverManager().install()

#create a new chrome browser instance
service = Service(driver_path)
driver = webdriver.Chrome(service=service)
driver.maximize_window()

# Setup
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# Open Amazon Sign In Page
driver.get("https://www.amazon.com/ap/signin")

# Example of accessing elements by locators
amazon_logo = driver.find_element(By.CSS_SELECTOR, "a.nav-logo-link")
email_field = driver.find_element(By.ID, "ap_email")
continue_button = driver.find_element(By.ID, "continue")
conditions_of_use_link = driver.find_element(By.LINK_TEXT, "Conditions of Use")
privacy_notice_link = driver.find_element(By.LINK_TEXT, "Privacy Notice")
need_help_link = driver.find_element(By.LINK_TEXT, "Need help?")
forgot_password_link = driver.find_element(By.LINK_TEXT, "Forgot your password?")
other_issues_link = driver.find_element(By.LINK_TEXT, "Other issues with Sign-In")
create_account_button = driver.find_element(By.ID, "createAccountSubmit")

# Sleep for 2 seconds to observe the elements, then close the browser
sleep(2)
driver.quit()