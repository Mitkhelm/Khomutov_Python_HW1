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


driver.get("http://the-internet.herokuapp.com/inputs")

check_input = driver.find_element(By.TAG_NAME, "input")

check_input.send_keys("12345")
time.sleep(2)
check_input.clear()
check_input.send_keys("54321")

time.sleep(2)

driver.quit()