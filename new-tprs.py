from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import pytesseract
from PIL import Image
import requests
from io import BytesIO
import time

# Ensure the path to Tesseract executable is correctly set
pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files (x86)/Tesseract-OCR/tesseract.exe'
    # r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def get_image(img_url):
    try:
        # Send a GET request to the URL to get the image data
        response = requests.get(img_url)
        response.raise_for_status()  # Raises an HTTPError for bad responses
        # Open the image using Pillow
        return BytesIO(response.content)
    except requests.RequestException as e:
        print(f"Failed to download the image: {e}")
        return None

def main():
    # Set up ChromeDriver
    service_obj = Service(executable_path="chromedriver.exe")
    driver = webdriver.Chrome(service=service_obj)
    
    try:
        # Open the target website
        driver.get("https://gogtprs.com/index.php?action=login&attempt_in=1")

        # Enter username
        user_name = driver.find_element(By.NAME, "usname")
        user_name.send_keys("benjamin@FGLT")

        # Retrieve the Turing image
        turing_img_url = driver.find_element(By.ID, "turingimg").get_attribute("src")
        image_stream = get_image(turing_img_url)

        if image_stream is None:
            print("Failed to retrieve or process Turing image.")
            return

        # Process the image with pytesseract
        try:
            image = Image.open(image_stream)
            text = pytesseract.image_to_string(image)
            print(f"Recognized text: {text}")
        except Exception as e:
            print(f"Error processing the image: {e}")

        # Enter password and submit
        pass_word = driver.find_element(By.NAME, "pwd")
        pass_word.send_keys("Africa@1tprs")
        login_button = driver.find_element(By.CLASS_NAME, "login100-form-btn")
        login_button.click()

        # Wait for the login process to complete
        time.sleep(15)
        print(f"Page title after login: {driver.title}")

    finally:
        # Close the driver
        driver.quit()

if __name__ == "__main__":
    main()
