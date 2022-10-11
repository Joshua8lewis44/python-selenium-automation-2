from selenium import webdriver
from selenium.webdriver.common.by import By
# 1 Repeat everything I coded during the class

driver = webdriver.Chrome(executable_path="C:\\Users\\owner\\Desktop\\Automation\\python-selenium-automation\\chromedriver.exe")
driver.get('https://www.amazon.com/')
driver.find_element(By.ID, "twotabsearchbox").send_keys("Coffee")

# By XPATH
XPATH="//tagname[@attribute='value']"
driver=webdriver.Chrome(executable_path ='/users/')

#By XPATH
driver.find_element(By.XPATH, "//@href='ref=nav_logo']")
driver.find_element(By.XPATH, "//@class=nav.logo-link nav-progressive-attribute']")

#By Tad Only
driver.find_element(By.XPATH,"//input")

#By attribute Only
driver.find_element(By.XPATH,"//*[@class'nav_logon.link nav_progressive-attribute']")
driver.find_element(By.XPATH, "//*[@hret='ref=nav_logo']")

#BY Text
driver.find_element(By.XPATH, "//a([text()='Back to School']")

#By Multiple Attributes
driver.find_element(By.XPATH,"//a[@class'nav-a'and@href='/backtoschool?ref_=nav_cs_bts']")

#By Multiple Attributes and Text
driver.find_element(By.XPATH,"//a[@class='nav-a'and@href='/backtoschool?ref_=new_cs_bts'and text()='Back to School']")

#By Partial Text/Attribute=>contains()
driver.find_element(By.XPATH, "//a[contains(text),'Back to'))")
driver.find_element(By.XPATH,"//a[contains(href,'Backtoschool'))")



from selenium.webdriver.common.by import By

#Syntax for XPATH
#   //tagname[@attribute='value']

Amazon_Logo = (By.XPATH, "//i[@class='a-icon a-icon-logo']")
Continue_Button = (By.XPATH, "//input[@id='continue']")
Need_Help_link = (By.XPATH, "//a[@class='a-expander-header a-declarative a-expander-inline-header a-link-expander']")
Forgot_Your_Password_Link = (By.XPATH, "//a[@id='auth-fpp-link-bottom']")
Other_Issues_Sign_In_Link = (By.XPATH, "//a[@class='a-link-normal']")
Create_your_Amazon_account_button = (By.XPATH, "//a[@Class='a-size-base a-text-bold']")
Conditions_of_use_link = (By.XPATH, "//a[href='/gp/aw/help/ref=ap_mobile_signin_notification_conditions_of_use? id=508088']")
Privacy_Notice_link = (By.XPATH, "//a[href='/gp/aw/help/ref=ap_mobile_signin_notification_privacy_notification_notice? id=468496']")

#
