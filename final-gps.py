import time

from selenium.webdriver import Chrome, ChromeOptions 
from selenium.webdriver.common.by import By

options = ChromeOptions()
options.add_argument("--headless")
driver = Chrome(options=options)
driver.execute_cdp_cmd(
    "Browser.grantPermissions",
    {
        "origin": "https://ghanapostgps.com/map/",
        "permissions": ["geolocation"]
    },
)
driver.execute_cdp_cmd(
    "Emulation.setGeolocationOverride",
    {
        "latitude": 5.5596814989670555,
        "longitude": -0.2002429962158203,
        "accuracy": 100,
    },
)
driver.get("https://ghanapostgps.com/map/")
# gps_location = driver.find_element(By.ID, "location-detail")
# print(f'GPS Address: ', gps_location)

#Gemini
gps_location_text = driver.find_element(By.CLASS_NAME, "da-code").text
print(f'GPS Address: {gps_location_text}')

time.sleep(3) 
gps_img = driver.save_screenshot(f"GhanaPostGPS {gps_location_text}.png")
print(f'Screenshot saved as ghanapostgps_address.png', gps_img)
# print(driver.title)
driver.quit()