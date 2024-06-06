from selenium import webdriver

from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.log import Log

import time

service = Service(executable_path="chromedriver.exe")
driver = webdriver.Chrome(service=service)

try:
    
    driver.get("https://ghanapostgps.com/map/")
    driver.maximize_window()
    driver.refresh()
    driver.set_page_load_timeout(30)
    print(driver.get_window_size())
    print(driver.get_window_position())
    time.sleep(15)
    search_box = driver.find_element(By.ID, 'addrsearch')
    search_box.send_keys('Silver Star Tower')
    search_box.send_keys(Keys.RETURN)
    time.sleep(15)
    print(driver.title)
    location_elements = driver.find_elements(By.CLASS_NAME, 'col')
    element = location_elements[-1]
    data = element.text.split("\n")
    lat,lon = str(data[1]).split(",")
    print(f'Latitude is {lat} Longitude is {lon}')


    # for element in location_elements:
    #     print(element.text)

        
    
    # coordinates_element = driver.find_element(By.ID, 'coordinates')
    

    # location = location_element.text
    # coordinates = coordinates_element.text
    # print(f'Location: {location}')
    # print(f'Coordinates: {coordinates}')
    # print(location_elements)

finally:
    # Close the WebDriver
    driver.quit()