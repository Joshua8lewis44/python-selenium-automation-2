from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

def before_scenario(context, scenario):
    # Setup the driver before each scenario
    context.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    context.driver.maximize_window()  # Optional: Maximize window for better visibility

def after_scenario(context, scenario):
    # Cleanup the driver after each scenario
    context.driver.quit()