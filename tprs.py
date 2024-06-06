from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import pytesseract
from PIL import Image
import requests
from io import BytesIO

import time

import pytesseract

pytesseract.pytesseract.tesseract_cmd = r'C:\Users\Benjamin Kwame Ampah\AppData\Local\Tesseract-OCR'

def getImage(img_url):
    # Send a GET request to the URL to get the image data
    response = requests.get(img_url)
# C:\Users\Benjamin Kwame Ampah\AppData\Local\Tesseract-OCR
    # Check if the request was successful
    if response.status_code == 200:
        # Open the image using Pillow
        return BytesIO(response.content)
        
    else:
        print("Failed to download the image.")
        return None

service_obj= Service(executable_path="chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)

driver.get("https://gogtprs.com/index.php?action=login&attempt_in=1")


userName = driver.find_element(By.NAME, "usname")
userName.send_keys("benjamin@FGLT")
# codeField = driver.find_element(By.NAME, "txtcaptha")
turingImg = driver.find_element(By.ID, "turingimg").get_attribute("src")

result = getImage(turingImg)
if result is None:
    print("Turing img is none")
##From Gpt
image = Image.open(result)

# Use pytesseract to do OCR on the image
text = pytesseract.image_to_string(image)

# Print the recognized text
print(text)
passWord = driver.find_element(By.NAME, "pwd")
passWord.send_keys("test")

login = driver.find_element(By.CLASS_NAME , "login100-form-btn").click()
time.sleep(15)
print(driver.title)
