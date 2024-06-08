from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time


def get_gps_coordinates(url, coordinates_string):
    options = Options()
    options.add_argument("--headless")  # This enables headless mode

    driver = webdriver.Chrome(options=options)  # No need for Service

    try:
        driver.get(url)
        driver.set_page_load_timeout(30)

        # Searching for the coordinates
        search_box = driver.find_element(By.ID, 'addrsearch')
        search_box.send_keys(coordinates_string)
        search_box.send_keys(Keys.RETURN)

        # Wait for element containing coordinates to appear
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "location-detail"))
        )

        # Get the GPS location text and extract coordinates (assuming format)
        gps_location = driver.find_element(By.ID, "location-detail").text
        # Modify this line to extract specific parts (latitude, longitude) based on actual content
        coordinates = gps_location.split(",")[0:2]  # Assuming first two elements are lat/lon

        print(f'GPS Coordinates: {", ".join(coordinates)}')  # Print coordinates

    except Exception as e:
        print(f"Error: {e}")  # Basic error handling

    finally:
        driver.quit()


# Example usage
url = "https://ghanapostgps.com/map/"
coordinates_string = "5.569711, -0.195554"
get_gps_coordinates(url, coordinates_string)
