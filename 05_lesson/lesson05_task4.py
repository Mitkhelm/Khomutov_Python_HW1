from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.common.keys import Keys


firefox_options = Options()
driver = webdriver.Firefox()
driver.maximize_window()


driver.get("http://the-internet.herokuapp.com/login")

username = driver.find_element(By.ID, "username")
username.send_keys("tomsmith")
password = driver.find_element(By.ID, "password")
password.send_keys("SuperSecretPassword!")
login = driver.find_element(By.CLASS_NAME, 'radius')
login.click()
text = driver.find_element(By.ID, "flash").text
print(text)


time.sleep(2)

driver.quit()