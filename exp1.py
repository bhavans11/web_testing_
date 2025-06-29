import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
service =Service("C:\Webdriver\chromedriver-win64\chromedriver.exe")
driver = webdriver.Chrome(service=service)
url=driver.get("https://www.saucedemo.com")
username=driver.find_element(By.XPATH, "/html/body/div/div/div[2]/div[1]/div/div/form/div[1]/input")
password= driver.find_element(By.XPATH, "/html/body/div/div/div[2]/div[1]/div/div/form/div[2]/input")
username.send_keys("standard_user")
password.send_keys("secret_sauce")
time.wait(30)
