from urllib import request
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time
service=Service("C:\Webdriver\chromedriver-win64\\chromedriver.exe")
driver=webdriver.Chrome(service=service)
driver.get("https://the-internet.herokuapp.com/broken_images")
driver.maximize_window()
images = driver.find_elements(By.TAG_NAME, value: "img")
broken_images = []
for image in images:
    src = image.get_attribute("src")
if src:
    response = request.get(src)
if response.status_code != 200:
    broken_images.append(src)
    print(f"Broken Image found")

if broken_images:
    print("list of broken images:")
for broken_image in broken_images:
    print(broken_image)
else:
    print("No broken Images found")

