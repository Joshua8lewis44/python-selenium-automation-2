from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

# Set up ChromeDriver
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

# Step 1: Open Target.
driver.get("https://www.target.com/")

# Step 2: Wait for the "Sign In" button to be present in the DOM
sign_in_button = driver.find_element(By.XPATH, '//*[contains(text(), "Sign In")]')
print("Sign In button found.")

# Step 3: Click the SignIn button
sign_in_button.click()

sleep(2)

# Step 5: Click SignIn from side navigation
sign_in_side_nav = driver.find_element(By.XPATH, '//*[contains(text(), "Sign In")]')
sign_in_side_nav.click()

# Step 6: Verify SignIn page opened
sign_in_text = driver.find_element(By.XPATH, '//*[contains(text(), "Sign into your Target account")]')
print("Sign-in text found:", sign_in_text.is_displayed())

# Sleep for 2 seconds to allow for observation, then quit the browser
sleep(2)
driver.quit()