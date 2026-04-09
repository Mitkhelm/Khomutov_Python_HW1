from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.get("http://uitestingplayground.com/textinput?")

search_locator = "#newButtonName"
search_input = driver.find_element(By.CSS_SELECTOR, search_locator)
search_input.send_keys("SkyPro")

accept = driver.find_element(By.CSS_SELECTOR, "#updatingButton").click()
txt = driver.find_element(By.CSS_SELECTOR, "#updatingButton").text
print(txt)

driver.quit()