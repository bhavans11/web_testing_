from selenium import webdriver
from selenium. webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
service = Service("C:\Webdriver\geckodriver-win64\geckodriver.exe")
driver = webdriver.Firefox(service=service)
driver.maximize_window()
username = "standard_user"
password = "secret_sauce"
login_url = "https://www.saucedemo.com/"
driver.get(login_url)
username_field = driver. find_element(By.XPATH,"/html/body/div/div/div[2]/div[1]/div/div/form/div[1]/input")
password_field = driver. find_element(By.XPATH, "/html/body/div/div/div[2]/div[1]/div/div/form/div[2]/input")
username_field.send_keys(username)
password_field.send_keys(password)
login_button = driver.find_element(By.XPATH, "/html/body/div/div/div[2]/div[1]/div/div/form/input")
assert not login_button.get_attribute("disabled")
login_button.click()


