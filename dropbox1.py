from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time
service=Service("C:\Webdriver\chromedriver-win64\\chromedriver.exe")
driver =webdriver.Chrome(service=service)
driver.get("https://www.tutorialspoint.com/selenium/practice/selenium_automation_practice.php")
dropdown_element = driver.find_element(By.XPATH, "/html/body/main/div/div/div[2]/form/div[10]/div/div[1]/select")
select=Select(dropdown_element)
select.select_by_index(1)
time.sleep(20)