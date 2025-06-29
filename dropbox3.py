from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

from selenium.webdriver.support.ui import Select
service = Service("C:\Webdriver\chromedriver-win64\\chromedriver.exe")
driver=webdriver.Chrome(service=service)
driver.get("https://www.tutorialspoint.com/selenium/practice/selenium_automation_practice.php")
dropdown=driver.find_element(By.XPATH,"/html/body/main/div/div/div[2]/form/div[10]/div/div[1]/select")
select=Select(dropdown)
target_value="Rajasthan"
for values in select.options:
    if values.text==target_value:
        values.click()
        print(f"found {target_value}")
        break
else:
    print("Error")
