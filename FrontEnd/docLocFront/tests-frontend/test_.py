from datetime import datetime
import time

import pytest

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

url = "https://docloc.completoschile.online/"

# Parametrize tests to run with different URLs
@pytest.mark.parametrize("url", [url])
def test_title(url):
    chrome_options = Options()
    driver = webdriver.Chrome(options=chrome_options)
    driver.get(url)
    time.sleep(2)
    # Verify the page title
    title = driver.find_element(By.CSS_SELECTOR, "#root > div > div.css-k008qs > div.css-14igsv4 > div > p")
    assert title.text == "GEOLOCALIZACIÓN DE DOCUMENTOS TERRITORIALES"

# Different select options for the filter
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

@pytest.mark.date
def test_filter_date():
    chrome_options = Options()
    driver = webdriver.Chrome(options=chrome_options)
    driver.get(url)
    time.sleep(2)

    date_to = "01-01-2019"
    date_from = "31-12-2022"

    input_to = driver.find_element(By.CSS_SELECTOR, "#root > div > div.css-k008qs > div.css-n8bf2u > div > div.css-1p4ja0v > div:nth-child(2) > input[type=date]")
    input_to.send_keys(date_to)

    input_from = driver.find_element(By.CSS_SELECTOR, "#root > div > div.css-k008qs > div.css-n8bf2u > div > div.css-1p4ja0v > div:nth-child(3) > input[type=date]")
    input_from.send_keys(date_from)

    filter_button = driver.find_element(By.CSS_SELECTOR, "#root > div > div.css-k008qs > div.css-n8bf2u > div > div.css-1p4ja0v > div:nth-child(4) > button").click()
    ActionChains(driver)\
        .click(filter_button)\
        .perform()
    time.sleep(2)
    
    first_row = driver.find_element(By.CSS_SELECTOR, "#root > div > div.css-k008qs > div.css-n8bf2u > div > div.css-1o8xpnk > div > table > tbody > tr:nth-child(1) > td:nth-child(3)")
    second_row = driver.find_element(By.CSS_SELECTOR, "#root > div > div.css-k008qs > div.css-n8bf2u > div > div.css-1o8xpnk > div > table > tbody > tr:nth-child(2) > td:nth-child(3)")
    
    to_date = datetime.strptime(date_to, "%d-%m-%Y")
    from_date = datetime.strptime(date_from, "%d-%m-%Y")
    firts_date = datetime.strptime(first_row.text, "%Y-%m-%d")
    second_date = datetime.strptime(second_row.text, "%Y-%m-%d")

    assert to_date <= firts_date and from_date >= firts_date and \
      to_date <= second_date and from_date >= second_date

@pytest.mark.navigation
def test_navigation_buttons():
    chrome_options = Options()
    driver = webdriver.Chrome(options=chrome_options)
    driver.get(url)
    time.sleep(2)

    title_firts_row = driver.find_element(By.CSS_SELECTOR, "#root > div > div.css-k008qs > div.css-n8bf2u > div > div.css-1o8xpnk > div > table > tbody > tr:nth-child(1) > td.css-hffdsd")

    next_button = driver.find_element(By.CSS_SELECTOR, "#root > div > div.css-k008qs > div.css-n8bf2u > div > div.css-gmuwbf > div > button:nth-child(3)").click()
    ActionChains(driver)\
        .click(next_button)\
        .perform()
    
    previous_button = driver.find_element(By.CSS_SELECTOR, "#root > div > div.css-k008qs > div.css-n8bf2u > div > div.css-gmuwbf > div > button:nth-child(1)").click()
    ActionChains(driver)\
        .click(previous_button)\
        .perform()

    title_firts_row_2 = driver.find_element(By.CSS_SELECTOR, "#root > div > div.css-k008qs > div.css-n8bf2u > div > div.css-1o8xpnk > div > table > tbody > tr:nth-child(1) > td.css-hffdsd")

    assert title_firts_row.text == title_firts_row_2.text
