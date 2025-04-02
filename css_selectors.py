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
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

# Get the path to the ChromeDriver executable
driver_path = ChromeDriverManager().install()

# Create a new Chrome browser instance
service = Service(driver_path)
driver = webdriver.Chrome(service=service)
driver.maximize_window()

# Open the Amazon Create Account page
driver.get('https://www.amazon.com/ap/register')

# Wait until the elements are present
try:
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'input[name="customerName"]')))
    driver.find_element(By.CSS_SELECTOR, 'input[name="customerName"]').send_keys("Test User")

    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'input[name="email"]')))
    driver.find_element(By.CSS_SELECTOR, 'input[name="email"]').send_keys("testuser@example.com")

    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'input[name="password"]')))
    driver.find_element(By.CSS_SELECTOR, 'input[name="password"]').send_keys("TestPassword123")

    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'input[name="passwordCheck"]')))
    driver.find_element(By.CSS_SELECTOR, 'input[name="passwordCheck"]').send_keys("TestPassword123")

    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, '#continue')))
    driver.find_element(By.CSS_SELECTOR, '#continue').click()

except Exception as e:
    print(f"Error: {e}")

# Close the browser window
driver.quit()