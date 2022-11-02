from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path="C:\\Users\\owner\\Desktop\\Automation\\python-selenium-automation\\chromedriver.exe")

# Step1:
driver.get("https://www.amazon.com/")

# Step 2:
driver.find_element(By.ID, "nav-orders").click()

#Step 3:
sign_in_expected = "Sign in"

sign_in_text_actual = driver.find_element(By.XPATH, "//h1[@class='a-spacing-small']").text
print(sign_in_text_actual)
assert sign_in_expected == sign_in_text_actual, f'Expected Text not found'

driver.close()

# Step 4
assert driver.find_element(By.ID, "ap_email"), f"Email field not available"