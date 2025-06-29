from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.chrome.service import Service
service = Service("C:\Webdriver\chromedriver-win64\\chromedriver.exe")
browser = webdriver.Chrome(service=service)
browser.get('https://www.tutorialspoint.com/selenium/practice/selenium_automation_practice.php')
browser.maximize_window()
browser. execute_script("window.scrollTo(0, document. body. scrollHeight);")
browser. find_element(By. XPATH, "/html/body/main/div/div/div[2]/form/div[7]/div/div/div[1]/input"). click()
time. sleep(3)
browser. find_element(By. XPATH, "/html/body/main/div/div/div[2]/form/div[7]/div/div/div[1]/input"). click()
time. sleep(15)
browser. find_element(By. XPATH,"/html/body/main/div/div/div[2]/form/div[7]/div/div/div[2]/input"). click()
time. sleep(15)
browser. find_element(By. XPATH, "/html/body/main/div/div/div[2]/form/div[7]/div/div/div[2]/input").click()
time. sleep(3)
