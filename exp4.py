from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

service = Service("C:\\Webdriver\\chromedriver-win64\\chromedriver.exe")
driver = webdriver.Chrome(service=service)
wait = WebDriverWait(driver, 10)
try:
    driver.get("https://www.saucedemo.com/")
    username_field = driver.find_element(By.XPATH, "/html/body/div/div/div[2]/div[1]/div/div/form/div[1]/input")
    password_field = driver.find_element(By.XPATH, "/html/body/div/div/div[2]/div[1]/div/div/form/div[2]/input")
    login_button = driver.find_element(By.XPATH, "/html/body/div/div/div[2]/div[1]/div/div/form/input")
    username_field.send_keys("standard_user")
    password_field.send_keys("secret_sauce")
    login_button.click()
    driver.back() 
    time.sleep(3)
    wait.until(EC.url_matches("https://www.saucedemo.com/"))
    driver.forward() 
    wait.until(EC.visibility_of_element_located((By.XPATH, "/html/body/div/div/div/div[2]/div/div/div/div[1]/div[2]/div[2]/button")))
    driver.refresh()  
    wait.until(EC.visibility_of_element_located((By.XPATH, "/html/body/div/div/div/div[2]/div/div/div/div[1]/div[2]/div[1]/a/div")))
except Exception as e:
    print(f"Test failed: {str(e)}")
finally:
    driver.quit()