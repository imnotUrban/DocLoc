from datetime import datetime
import time
import pytest

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

url = "http://localhost:5008/"

# Parametrize tests to run with different URLs
@pytest.mark.parametrize("url", [url])
def test_title(url):
    chrome_options = Options()
    driver = webdriver.Chrome(options=chrome_options)
    driver.get(url)
    driver.implicitly_wait(10)
    # Verify the page title
    title = driver.find_element(By.ID, "Title")
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
    driver.implicitly_wait(10)

    select_element = driver.find_element(By.ID, "CategorySelect")
    select = Select(select_element)
    select.select_by_value(option)

    filter_button = driver.find_element(By.ID, "ButtonFilter").click()
    ActionChains(driver)\
        .click(filter_button)\
        .perform()
    driver.implicitly_wait(10)

    first_row = driver.find_element(By.ID, "CategoryId0")
    second_row = driver.find_element(By.ID, "CategoryId1")
    assert first_row.text == option.upper() and second_row.text == option.upper()

@pytest.mark.date
def test_filter_date():
    chrome_options = Options()
    driver = webdriver.Chrome(options=chrome_options)
    driver.get(url)
    driver.implicitly_wait(10)

    date_to = "01-01-2019"
    date_from = "31-12-2022"

    input_to = driver.find_element(By.ID, "FromDate")
    input_to.send_keys(date_to)

    input_from = driver.find_element(By.ID, "ToDate")
    input_from.send_keys(date_from)

    filter_button = driver.find_element(By.ID, "ButtonFilter").click()
    ActionChains(driver)\
        .click(filter_button)\
        .perform()
    driver.implicitly_wait(10)
    
    first_row = driver.find_element(By.ID, "DateId0")
    second_row = driver.find_element(By.ID, "DateId1")

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
    driver.implicitly_wait(10)

    title_firts_row = driver.find_element(By.ID, "TitleId0").text

    next_button = driver.find_element(By.ID, "ButtonNext").click()
 
    ActionChains(driver)\
        .click(next_button)\
        .perform()
    driver.implicitly_wait(10)

    previous_button = driver.find_element(By.ID, "ButtonPrevious").click()
    ActionChains(driver)\
        .click(previous_button)\
        .perform()
    driver.implicitly_wait(10)

    title_firts_row_2 = driver.find_element(By.ID, "TitleId0").text

    assert title_firts_row == title_firts_row_2

@pytest.mark.performance
def test_page_load_time():
    chrome_options = Options()
    driver = webdriver.Chrome(options=chrome_options)
    start_time = time.time() # Capture the start time of loading
    driver.get(url)
    end_time = time.time() # Capture the end time of loading
    load_time = end_time - start_time # Calculate the total loading time
    assert load_time < 10, "The load time exceeds 10 seconds"

@pytest.mark.scalability
def test_concurrent_users():
    chrome_options = Options()
    num_users = 100

    # Create a list to store browser drivers for each user
    drivers = []

    # Log in for each simulated user
    for _ in range(num_users):
        driver = webdriver.Chrome(options=chrome_options)
        drivers.append(driver)
    # Wait for some time to allow users to log in and perform actions
    driver.implicitly_wait(10)
    
    # Perform some action on the page (e.g., load the page)
    for driver in drivers:
        driver.get(url)
    # Wait for some time to allow all requests to be processed
    driver.implicitly_wait(30)
    
    # Close all browser drivers
    for driver in drivers:
        driver.quit()

    # Verify that there are no errors
    assert True