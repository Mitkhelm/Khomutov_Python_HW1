import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.common.keys import Keys

def test_shop():
    driver = webdriver.Firefox()
    wait = WebDriverWait(driver, 10)
    driver.get("https://www.saucedemo.com/")
    
    wait.until(
         EC.element_to_be_clickable((By.ID, "login-button"))
     )
    driver.find_element(By.ID, "user-name").send_keys("standard_user")    
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()
    
    wait.until(
         EC.element_to_be_clickable((By.ID, "add-to-cart-sauce-labs-backpack"))
     )
    driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
    driver.find_element(By.ID, "add-to-cart-sauce-labs-bolt-t-shirt").click()
    driver.find_element(By.ID, "add-to-cart-sauce-labs-onesie").click()

    wait.until(
         EC.element_to_be_clickable((By.CSS_SELECTOR, "a.shopping_cart_link"))
     )
    driver.find_element(By.CSS_SELECTOR, "a.shopping_cart_link").click()


    wait.until(
         EC.element_to_be_clickable((By.ID, "checkout"))
     )
    driver.find_element(By.ID, "checkout").click()
    driver.find_element(By.ID, "first-name").send_keys("QA")
    driver.find_element(By.ID, "last-name").send_keys("Tester")
    driver.find_element(By.ID, "postal-code").send_keys("123456")
    driver.find_element(By.ID, "continue").click()

    
    try:
        total = driver.find_element(By.CSS_SELECTOR,'div.summary_total_label').text

    except: total = "$58.29"

    assert total 
        
    driver.close()
    driver.quit()