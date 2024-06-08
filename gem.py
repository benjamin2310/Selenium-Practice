from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time

options = Options()
options.add_argument("--headless")  # This enables headless mode

service = Service(executable_path="chromedriver.exe")
driver = webdriver.Chrome(service=service, options=options)

try:
    driver.get("https://ghanapostgps.com/map/")
    driver.set_page_load_timeout(30)

    # Print window size without maximizing (headless doesn't support maximize)
    # print(driver.get_window_size())
    # print(driver.get_window_position())

    time.sleep(10)  # Adjust wait time as needed (may take less time in headless)

    # Searching for the coordinates
    search_box = driver.find_element(By.ID, 'addrsearch')
    search_box.send_keys('5.569711, -0.195554')
    search_box.send_keys(Keys.RETURN)

    # Wait for element containing coordinates to appear
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "location-detail"))
    )

    # Get the GPS location text
    gps_location = driver.find_element(By.ID, "location-detail").text

    print(f'GPS Address: ', gps_location)

finally:
    driver.quit()
