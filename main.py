from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
#Using the automation tool
service = Service(executable_path="chromedriver.exe")
driver = webdriver.Chrome(service=service)

#Making a Request

driver.get("https://google.com")

#Interact with HTML Elements (IDs, Classes)
input_element = driver.find_element(By.CLASS_NAME,"L3eUgb")
input_element.send_keys("Developer is Here" + Keys.ENTER)
time.sleep(15)

driver.quit()
