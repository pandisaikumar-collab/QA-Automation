import os
import yaml
import time
import pytest
import logging
from selenium import webdriver
from models.demohome import DemoHome
from models.elements import Elements
from models.elements import Buttons

log = logging.getLogger(os.path.basename(__file__))
log.setLevel(logging.INFO)

# Load config once per session
@pytest.fixture(scope='session')
def config():
    config_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'config', 'config.yaml')
    with open(config_path) as file:
        return yaml.safe_load(file)

# Use a single browser session for all tests
@pytest.fixture(scope='session')
def driver(config):
    if config['browser'] == 'chrome':
        driver = webdriver.Chrome()
    elif config['browser'] == 'firefox':
        driver = webdriver.Firefox()
    else:
        raise Exception("Unsupported browser in config.")

    driver.get(config['base_url'])
    driver.maximize_window()
    time.sleep(5)
    log.info("Waiting 10 seconds for website to stabilize")
    yield driver
    driver.quit()


@pytest.fixture()
def home_obj(driver):
    return DemoHome(driver)

@pytest.fixture()
def elements_obj(driver):
    return Elements(driver)

@pytest.fixture()
def buttons_obj(driver):
    return Buttons(driver)

def test_demo_home_page(driver, config, home_obj, elements_obj):
    if home_obj.is_demoqa_page_loaded():
        home_obj.click_elements_button()
        if elements_obj.is_elements_page_loaded():
            assert True, "Elements page loaded successfully"
            elements_obj.click_webtable_button()
            table_data = elements_obj.get_web_table_data()
            if table_data:
                log.info(f"Table data: %s", table_data)
            else:
                pytest.fail("No data found in the web table")
    else:
        pytest.fail("Failed to load Demo Home page")

# @pytest.mark.skip
def test_fill_registration_form(driver, config, elements_obj):
    payload = {
        'firstname': config['registration_form']['firstname'],
        'lastname': config['registration_form']['lastname'],
        'email': config['registration_form']['email'],
        'age': config['registration_form']['age'],
        'salary': config['registration_form']['salary'],
        'department': config['registration_form']['department']
    }

    if not payload:
        pytest.fail("No registration payload found in config file")
    else:
        elements_obj.fill_registration_form(payload)
        #elements_obj.click_submit_button()
        time.sleep(10)

def test_buttons_operations(driver,elements_obj,buttons_obj):
    elements_obj.click_buttons_sections()
    page = buttons_obj.is_buttons_page_loaded()
    if page == True:
        assert buttons_obj.double_click()
        time.sleep(5)
        assert buttons_obj.right_click()
        time.sleep(5)
        assert buttons_obj.click_me()
        time.sleep(5)
    else:
        pytest.fail("Failed to button operation")
    
