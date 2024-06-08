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

    #Searching for the coordinates
    search_box = driver.find_element(By.ID, 'addrsearch')
    search_box.send_keys('5.569711, -0.195554')
    # search_box.send_keys(Keys.RETURN)
    time.sleep(15)
    print(driver.title)
    #Displaying the Latitude and Longitude based on a search
    # location_elements = driver.find_elements(By.CLASS_NAME, 'col')
    # element = location_elements[-1]
    # data = element.text.split("\n")
    # lat,lon = str(data[1]).split(",")
    # #Final Display of the result
    # print(f'Latitude is {lat} Longitude is {lon}')

    #Finding the Location based on the coordinates given
    gps_location = driver.find_element(By.ID, "location-detail")

    #Returns all the address details
    # gps_location = driver.find_element(By.CLASS_NAME, "address-list")

    gps = gps_location.text

    print(f'GPS Address: ', gps)

finally:
    # Close the WebDriver
    driver.quit()