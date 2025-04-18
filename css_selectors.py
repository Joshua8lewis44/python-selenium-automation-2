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

# open the Amazon Create Account page directly
driver.get('https://www.amazon.com/ap/register')

# CSS Selectors for Create Account Page

# Amazon Logo
driver.find_element(By.CSS_SELECTOR, 'i.a-icon.a-icon-logo')

# Header: "Sign in or create account"
driver.find_element(By.CSS_SELECTOR, 'h1.a-size-medium-plus.a-spacing-small')

# "Enter mobile number or email" paragraph
driver.find_element(By.CSS_SELECTOR, 'p.a-spacing-micro.a-text-bold')

# Continue Button
driver.find_element(By.CSS_SELECTOR, 'input.a-button-input[type="submit"][aria-labelledby="continue-announce"]')

# Conditions of Use link
driver.find_element(By.CSS_SELECTOR, 'a[href*="condition_of_use"]')

# Privacy Notice link
driver.find_element(By.CSS_SELECTOR, 'a[href*="privacy_notice"]')
