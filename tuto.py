from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

# current_url = "https://ghanapostgps.com/map/"
url = "https://www.scrapingcourse.com/ecommerce/"
# driver = webdriver.Chrome()
# driver.get(url)
# with webdriver.Chrome() as driver:
#     driver.get(url)
options = webdriver.ChromeOptions()
options.add_argument("--headless")

with webdriver.Chrome(options=options) as driver:
    # driver.get(url)
    # print(driver.title)
    print("Page URL:", driver.current_url) 
    print("Page Title:", driver.title)
    parent_elements = driver.find_elements(By.XPATH, "") 
