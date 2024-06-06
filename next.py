from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# Start a new Chrome session
driver = webdriver.Chrome()

# Open Google Maps
driver.get("https://ghanapostgps.com/map/")

# Find the search input field
search_box = driver.find_element(By.ID, 'addrsearch')

# Enter the coordinates into the search box
search_box.send_keys("5.600251, -0.178339" + Keys.RETURN)

# Wait for the address to load
driver.implicitly_wait(15)

# Find the address element
address_element = driver.find_element(By.ID, "address-list")
#da-code animated bounceIn text-uppercase

# Extract the address text
address = address_element.text

# Print the address
print("GPS Address:", address)

# Close the browser
driver.quit()
