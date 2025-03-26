# for name field : driver.find_element(By.CSS_SELECTOR, "input#ap_customer_name")
# for email field : driver.find_element(By.CSS_SELECTOR, "input#ap_email")
# for password field using css selectors : driver.find_element(By.CSS_SELECTOR, "input#ap_password")
# for reenter password field : driver.find_element(By.CSS_SELECTOR, "input#ap_password_check")
# for create an account button : driver.find_element(By.CSS_SELECTOR, "input#continue")
# for error message if validation fails : driver.find_element(By.CSS_SELECTOR, ".a-alert-content")

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

# get the path to the ChromeDriver executable
driver_path = ChromeDriverManager().install()

# create a new Chrome browser instance
service = Service(driver_path)
driver = webdriver.Chrome()
driver.maximize_window()

# open the Amazon Create Account page
driver.get('https://www.amazon.com/ap/register')

# Fill out the registration form using optimal CSS selectors
driver.find_element(By.CSS_SELECTOR, "input#ap_customer_name").send_keys("John Doe")
driver.find_element(By.CSS_SELECTOR, "input#ap_email").send_keys("johndoe@example.com")
driver.find_element(By.CSS_SELECTOR, "input#ap_password").send_keys("SecureP@ssw0rd")
driver.find_element(By.CSS_SELECTOR, "input#ap_password_check").send_keys("SecureP@ssw0rd")

# Submit the registration form
driver.find_element(By.CSS_SELECTOR, "input#continue").click()

# Optional: wait to verify the action
sleep(5)

# Close the browser after completion
driver.quit()

