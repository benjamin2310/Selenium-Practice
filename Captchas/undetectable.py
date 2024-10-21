import undetected_chromedriver as uc
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import requests

# Set up ChromeDriver with undetected_chromedriver
options = uc.ChromeOptions()
driver = uc.Chrome(options=options)

try:
    driver.get("https://gogtprs.com/index.php?action=login&attempt_in=1")

    # Example: Find captcha image element and get its source
    captcha_image = driver.find_element(By.XPATH, 'xpath_to_captcha_image')
    captcha_image_src = captcha_image.get_attribute('src')

    # Send captcha image to 2Captcha or similar service
    api_key = 'your_2captcha_api_key'
    response = requests.post('http://2captcha.com/in.php', {
        'key': api_key,
        'method': 'base64',
        'body': captcha_image_src
    })

    # Parse the captcha response
    request_id = response.text.split('|')[1]
    solution = None
    while not solution:
        response = requests.get(f'http://2captcha.com/res.php?key={api_key}&action=get&id={request_id}')
        if 'OK' in response.text:
            solution = response.text.split('|')[1]

    # Enter the captcha solution into the form
    captcha_input = driver.find_element(By.XPATH, 'xpath_to_captcha_input')
    captcha_input.send_keys(solution)

    # Submit the form or continue with further automation
    submit_button = driver.find_element(By.XPATH, 'xpath_to_submit_button')
    submit_button.click()

finally:
    driver.quit()
import undetected_chromedriver as uc
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import requests

# Set up ChromeDriver with undetected_chromedriver
options = uc.ChromeOptions()
driver = uc.Chrome(options=options)

try:
    driver.get("https://gogtprs.com/index.php?action=login&attempt_in=1")

    # Example: Find captcha image element and get its source
    captcha_image = driver.find_element(By.XPATH, 'xpath_to_captcha_image')
    captcha_image_src = captcha_image.get_attribute('src')

    # Send captcha image to 2Captcha or similar service
    api_key = 'your_2captcha_api_key'
    response = requests.post('http://2captcha.com/in.php', {
        'key': api_key,
        'method': 'base64',
        'body': captcha_image_src
    })

    # Parse the captcha response
    request_id = response.text.split('|')[1]
    solution = None
    while not solution:
        response = requests.get(f'http://2captcha.com/res.php?key={api_key}&action=get&id={request_id}')
        if 'OK' in response.text:
            solution = response.text.split('|')[1]

    # Enter the captcha solution into the form
    captcha_input = driver.find_element(By.XPATH, 'xpath_to_captcha_input')
    captcha_input.send_keys(solution)

    # Submit the form or continue with further automation
    submit_button = driver.find_element(By.XPATH, 'xpath_to_submit_button')
    submit_button.click()

finally:
    driver.quit()
