from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.maximize_window()

driver.get("http://uitestingplayground.com/classattr")
sleep(1.5)

button = driver.find_element(By.CLASS_NAME, 'btn-primary').click()
sleep(2)

driver.switch_to.alert.accept()
sleep(2)

driver.quit()