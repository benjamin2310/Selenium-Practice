from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# Start a new Chrome session
driver = webdriver.Chrome()

# Open Google Maps
driver.get("https://www.google.com/maps")

# Find the search input field
search_box = driver.find_element(By.ID, "searchboxinput")

# Enter the coordinates into the search box
search_box.send_keys("5.600251, -0.178339" + Keys.RETURN)

# Wait for the address to load
driver.implicitly_wait(5)

# Find the address element
address_element = driver.find_element(By.XPATH, "//span[@class='widget-pane-link']")

# Extract the address text
address = address_element.text

# Print the address
print("GPS Address:", address)
print(address_element.title)
# Close the browser
driver.quit()
