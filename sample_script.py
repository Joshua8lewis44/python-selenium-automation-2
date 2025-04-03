from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

#get the path from webdriver executable
driver_path = ChromeDriverManager().install()

#create a new chrome browser instance
service = Service(driver_path)
driver = webdriver.Chrome(service=service)
#driver.implicitly_wait(8)
driver.maximize_window()
driver.wait = WebDriverWait(driver, 10)

# open the url
driver.get('https://www.google.com/')

search = driver.find_element(By.NAME, 'q')
search.clear()
search.send_keys('car')

# wait for 4 sec
#sleep(10)
driver.wait.until(EC.element_to_be_clickable(By.NAME, 'btnK'))

# click search
#driver.find_element(By.NAME, 'btnK').click()

sleep(3)

# verify
assert 'car' in driver.current_url.lower(), f"Expected query not in {driver.current_url.lower()}"
print('Test Passed')

driver.quit()

