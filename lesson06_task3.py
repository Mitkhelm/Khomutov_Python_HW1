from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

waiter = WebDriverWait(driver, 10)

driver.get("https://bonigarcia.dev/selenium-webdriver-java/loading-images.html")

waiter.until(
    EC.text_to_be_present_in_element((By.CLASS_NAME, "col-12.py-2"), "Done!")
)

pictures = driver.find_elements(By.CSS_SELECTOR, "img")

third_image = pictures[3]

att = third_image.get_attribute('src')
print(att)

driver.quit()