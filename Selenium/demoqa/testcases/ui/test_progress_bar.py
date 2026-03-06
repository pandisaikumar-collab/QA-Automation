import os 
import yaml 
import time 
import pytest 
import logging 

from selenium import webdriver  

from models.demohome import DemoHome
from models.elements import Elements
from models.elements import Buttons
from models.widgets import ProgressBar

log = logging.getLogger(os.path.dirname(__file__))
log.setLevel(logging.INFO)


@pytest.fixture(scope='session')
def config():
    config_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'config', 'config.yaml')
    with open(config_path) as file:
        return yaml.safe_load(file)


@pytest.fixture(scope='session')
def driver(config):
    if config['browser'] == 'chrome':
        driver = webdriver.Chrome()
    elif config['browser'] == 'firefox':
        driver = webdriver.Firefox()
    else:
        raise Exception("Unsupported browser in config file.")

    driver.get(config['base_url'])
    driver.maximize_window()
    time.sleep(5)
    log.info("Waiting 5 seconds for website to stabilize")
    yield driver
    driver.quit()

@pytest.fixture()
def home_obj(driver):
    return DemoHome(driver)

@pytest.fixture()
def elements_obj(driver):
    return Elements(driver)

@pytest.fixture()
def progress_bar(driver):
    return ProgressBar(driver)


def test_demo_home_page(driver, config, home_obj, elements_obj, progress_bar):
    if home_obj.is_demoqa_page_loaded():
        home_obj.click_elements_button()
        if elements_obj.is_elements_page_loaded():
            home_obj.click_widgets_section()
            #assert progress_bar.click_widgets_section()
        # if elements_obj.is_widgets_page_loaded():
        #     assert True, "Widgets page loaded successfully"
        #     elements_obj.click_progress_bar_section()
            # table_data = elements_obj.get_web_table_data()
            # if table_data:
            #     log.info(f"Table data: %s", table_data)
            # else:
            #     pytest.fail("No data found in the web table")
    else:
        pytest.fail("Failed to load Demo Home page")


def test_progress_bar(driver, config, progress_bar):
    #progress_bar.is_widgets_page_loaded()
    progress_bar.click_progress_bar_section()
    time.sleep(5)
    progress_bar.handle_progress_bar()
    time.sleep(5)
    
    


