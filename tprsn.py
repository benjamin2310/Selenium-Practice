from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from PIL import Image
import pytesseract
import time
import io
import base64

# Ensure the path to Tesseract executable is correctly set
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'


def get_image_from_element(driver, element):
    # Get the location and size of the element
    location = element.location
    size = element.size
    # Take a screenshot of the entire page
    screenshot = driver.get_screenshot_as_png()
    screenshot = Image.open(io.BytesIO(screenshot))
    # Calculate the bounding box of the element
    left = location['x']
    top = location['y']
    right = location['x'] + size['width']
    bottom = location['y'] + size['height']
    # Crop the image to the bounding box
    captcha_image = screenshot.crop((left, top, right, bottom))
    return captcha_image


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

        # Capture the CAPTCHA image
        turing_img_element = driver.find_element(By.ID, "turingimg")
        captcha_image = get_image_from_element(driver, turing_img_element)

        if captcha_image is None:
            print("Failed to capture CAPTCHA image.")
            return

        # Process the image with pytesseract
        try:
            text = pytesseract.image_to_string(captcha_image)
            print(f"Recognized text: {text.strip()}")
        except Exception as e:
            print(f"Error processing the image: {e}")
            return

        # Enter CAPTCHA and password
        captcha_input = driver.find_element(By.NAME, "captcha")
        captcha_input.send_keys(text.strip())

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
