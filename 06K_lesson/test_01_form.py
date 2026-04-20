import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture

def driver():

    edge_driver_path = r"C:\Users\Professional\Downloads\edgedriver_win64\msedgedriver.exe"
    driver = webdriver.Edge(service=EdgeService(edge_driver_path))
    yield driver
    driver.quit()



def test_form_submission(driver):

    driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")

    WebDriverWait(driver, 7).until(EC.presence_of_element_located((By.NAME, 'first-name')))

    form_data = {

        "first-name": "Иван",
        "last-name": "Петров",
        "address": "Ленина, 55-3",
        "e-mail": "test@skypro.com",
        "phone": "+7985899998787",
        "city": "Москва",
        "country": "Россия",
        "job-position": "QA",
        "company": "SkyPro"
    }

    for field_name, value in form_data.items():
        driver.find_element(By.NAME, field_name).send_keys(value)

    driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

    zip_code = driver.find_element(By.ID, "zip-code")
    actual_color = zip_code.value_of_css_property("border-top-color")
    expected_color = "rgba(245, 194, 199, 1)"
    assert actual_color == expected_color

    fields = ["first-name",
              "last-name",
              "address",
              "e-mail",
              "phone",
              "city",
              "country",
              "job",
              "company"
              ]
    for field in fields:
        field = driver.find_element(By.CLASS_NAME, "alert-success")
        actual_color_2 = field.value_of_css_property("border-top-color")
        expected_color_2 = "rgba(186, 219, 204, 1)"
        assert actual_color_2 == expected_color_2

    driver.quit()