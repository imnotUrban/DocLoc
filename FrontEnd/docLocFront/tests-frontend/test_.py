import pytest
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

url = "https://docloc.completoschile.online/"

# Parametrize tests to run with different URLs
@pytest.mark.parametrize("url", [url])
#def test_title(browser, url):
def test_title(url):
    chrome_options = Options()
    driver = webdriver.Chrome(options=chrome_options)
    driver.get(url)
    time.sleep(2)
    # Verify the page title
    title = driver.find_element(By.CSS_SELECTOR, "#root > div > div.css-k008qs > div.css-14igsv4 > div > p")
    assert title.text == "GEOLOCALIZACIÓN DE DOCUMENTOS TERRITORIALES"

# Prueba de distintas opciones de select para el filtro
@pytest.mark.parametrize("option", [
    "entretenimiento",
    "tecnologia",
    "medio_ambiente",
    "ciencia",
    "politica",
    "internacional",
    "accidentes",
    "educacion",
    "salud",
    "economia",
    "deportes"
])

@pytest.mark.select
def test_all_select(option):
    chrome_options = Options()
    driver = webdriver.Chrome(options=chrome_options)
    driver.get(url)
    time.sleep(2)

    select_element = driver.find_element(By.CSS_SELECTOR, "#CategorySelect")
    select = Select(select_element)
    select.select_by_value(option)
    filter_button = driver.find_element(By.CSS_SELECTOR, "#root > div > div.css-k008qs > div.css-n8bf2u > div > div.css-1p4ja0v > div:nth-child(4) > button").click()
    ActionChains(driver)\
        .click(filter_button)\
        .perform()
    time.sleep(2)
    
    first_row = driver.find_element(By.CSS_SELECTOR, "#root > div > div.css-k008qs > div.css-n8bf2u > div > div.css-1o8xpnk > div > table > tbody > tr:nth-child(1) > td:nth-child(2)")
    second_row = driver.find_element(By.CSS_SELECTOR, "#root > div > div.css-k008qs > div.css-n8bf2u > div > div.css-1o8xpnk > div > table > tbody > tr:nth-child(2) > td:nth-child(2)")
    assert first_row.text == option.upper() and second_row.text == option.upper()

