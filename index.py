from selenium import webdriver
from selenium.webdriver.chrome.service import Service

service_object =Service(executable_path="chromedriver.exe")
driver = webdriver.Chrome(service=service_object)
driver.get("https://www.google.com")
driver.minimize_window()
driver.maximize_window()
driver.refresh()
driver.set_page_load_timeout(30)
driver.set_window_size(500, 500)
print(driver.get_window_size())
print(driver.get_window_position()) 
print(driver.title)