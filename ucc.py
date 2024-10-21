from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
service_obj = Service(executable_path="chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)
# driver.get("https://www.saucedemo.com/")
driver.get("https://portal.ucc.edu.gh/reset/login.php")

driver.maximize_window()
driver.refresh()
driver.set_page_load_timeout(30)
print(driver.get_window_size())
print(driver.get_window_position())
driver.find_element(By.NAME, "username").send_keys('PS/ITC/18/0075')
driver.find_element(By.NAME, "password").send_keys("191554")
driver.find_element(By.CLASS_NAME, "btn").click()
time.sleep(15)
print(driver.title)
driver.close()
driver.quit()