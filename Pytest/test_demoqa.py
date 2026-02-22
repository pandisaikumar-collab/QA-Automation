import time

import pytest
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

MAXTIME = 60
def test_elements(driver):
    time.sleep(60)
    wait = WebDriverWait(driver, MAXTIME)
    element_xpath = "//h5[text()='Elements']"
    elements = wait.until(EC.element_to_be_clickable((By.XPATH, element_xpath)))
    driver.execute_script("arguments[0].scrollIntoView();", elements)
    time.sleep(5)
    elements.click()

@pytest.mark.skip
def test_text_box(driver):
    wait = WebDriverWait(driver, MAXTIME)
    text_box = wait.until(EC.element_to_be_clickable((By.XPATH, "//span[text()='Text Box']")))
    time.sleep(5)
    text_box.click()





