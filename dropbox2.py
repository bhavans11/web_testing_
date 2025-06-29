from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

from selenium.webdriver.support.ui import Select
service = Service("C:\Webdriver\chromedriver-win64\\chromedriver.exe")
driver=webdriver.Chrome(service=service)
driver.get("https://www.tutorialspoint.com/selenium/practice/selenium_automation_practice.php")
driver.execute_script("window.scrollTo(0, document. body. scrollHeight);")
dropbox=driver.find_element(By.XPATH, "/html/body/main/div/div/div[2]/form/div[10]/div/div[1]/select")
select=Select(dropbox)
option_count = len(select.options)
expected_count = 4
if  option_count == expected_count: 
    print("Test case passed.Count is Correct")
else:
    print("Test case failed")

select.select_by_index(1)
time.sleep(10)
