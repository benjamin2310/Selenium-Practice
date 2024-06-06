from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# Start a new Chrome session
driver = webdriver.Chrome()

# Open the website where you can search by coordinates
driver.get("https://ghanapostgps.com/map/")  # Replace "https://example.com/" with the actual website URL

# Find the input field for coordinates
coordinate_input = driver.find_element(By.ID, "addrsearch")  # Adjust XPATH as per the actual website

# Enter the coordinates
coordinate_input.send_keys("5.600251, -0.178339" + Keys.RETURN)  # Adjust coordinates as needed

# Wait for the GPS address to load
driver.implicitly_wait(15)  # Adjust waiting time as needed

# Find the GPS address element
gps_address_element = driver.find_element(By.CLASS_NAME, "da-code animated bounceIn text-uppercase")  # Adjust XPATH as per the actual website

# Extract the GPS address text
gps_address = gps_address_element.text

# Print the GPS address
print("GPS Address:", gps_address)

# Close the browser
driver.quit()
