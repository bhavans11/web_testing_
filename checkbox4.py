from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.chrome.service import Service
service=Service("C:\Webdriver\chromedriver-win64\\chromedriver.exe")
browser = webdriver. Chrome(service=service)
browser.get('https://www.tutorialspoint.com/selenium/practice/selenium_automation_practice.php')
browser.maximize_window()
time.sleep(5)
browser. execute_script("window.scrollTo(0, document. body. scrollHeight);")
checkboxes = browser. find_elements(By.XPATH,"/html/body/main/div/div/div[2]/form/div[7]/div/div/div[1]/input")
for checkbox in checkboxes:
        checkbox.send_keys(Keys.SPACE)
checked_count =0
for checkbox in checkboxes:
     if checkbox.is_selected():
        checked_count +=1
expected_checked_count = 9
if checked_count == expected_checked_count:
    print('Checkbox count verified')
else:
    print('Checkbox count is mismatch')
time.sleep(5)
browser.close()
