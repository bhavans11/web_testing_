from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.service import Service
from selenium.webdriver.chrome.service import Service
import time
service = Service("C:\Webdriver\chromedriver-win64\\chromedriver.exe")
driver = webdriver.Chrome(service=service)

driver.get("https://www.tutorialspoint.com/selenium/practice/selenium_automation_practice.php")
driver.maximize_window()
driver.execute_script("window.scrollTo(0, document. body. scrollHeight);")
driver.find_element(By.XPATH,"/html[1]/body[1]/main[1]/div[1]/div[1]/div[2]/form[1]/div[7]/div[1]/div[1]/div[1]/input[1]").click()
time.sleep(10)

