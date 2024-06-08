from selenium import webdriver

from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.log import Log
from selenium.webdriver.chrome.options import Options

import time

# service = Service(executable_path="chromedriver.exe")
# driver = webdriver.Chrome(service=service)
url = "https://ghanapostgps.com/map/"
options = webdriver.ChromeOptions()
options.add_argument("--headless")  
with webdriver.Chrome(options=options) as driver: #modified 
    driver.get(url)

    try:
        
        # driver.get("https://ghanapostgps.com/map/")
        # driver.maximize_window()
        # driver.refresh()
        # driver.set_page_load_timeout(30)
        # print(driver.get_window_size())
        # print(driver.get_window_position())
        time.sleep(15)

        #Searching for the coordinates
        search_box = driver.find_element(By.ID, 'addrsearch')
        search_box.send_keys('5.569711, -0.195554')
        time.sleep(15)
        print(driver.title)

        #Finding the Location based on the coordinates given
        gps_location = driver.find_element(By.ID, "location-detail")

        gps = gps_location.text

        print(f'GPS Address: ', gps)

    finally:
        # Close the WebDriver
        driver.quit()