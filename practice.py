from selenium import webdriver

#creating a service object
from selenium.webdriver.chrome.service import Service

#invoking the browser

service_obj = Service(executable_path="chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)

driver.get(
    "https://www.python.org"
)