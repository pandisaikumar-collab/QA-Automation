import os
import datetime
import pytest
import webbrowser
import yaml

from selenium import webdriver

from models.demohome import DemoHome
from models.elements import Elements, Buttons
from models.widgets import ProgressBar

def pytest_configure(config):
    os.makedirs("htmlreports", exist_ok=True)
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    report_path = f"htmlreports/report_{timestamp}.html"
    config._html_report_path = os.path.abspath(report_path)
    config.option.htmlpath = report_path
    config.option.self_contained_html = True

def pytest_unconfigure(config):
    report_path = getattr(config, "_html_report_path", None)
    if report_path and os.path.exists(report_path):
        webbrowser.open_new_tab(report_path)


@pytest.fixture(scope="session")
def config():
    config_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "config", "config.yaml")
    with open(config_path, encoding="utf-8") as file:
        return yaml.safe_load(file)


@pytest.fixture(scope="session")
def driver(config):
    browser = config.get("browser", "").lower()
    if browser == "chrome":
        driver_instance = webdriver.Chrome()
    elif browser == "firefox":
        driver_instance = webdriver.Firefox()
    else:
        raise ValueError("Unsupported browser in config.")

    driver_instance.get(config["base_url"])
    driver_instance.maximize_window()
    yield driver_instance
    driver_instance.quit()


@pytest.fixture()
def home_obj(driver):
    return DemoHome(driver)


@pytest.fixture()
def elements_obj(driver):
    return Elements(driver)


@pytest.fixture()
def buttons_obj(driver):
    return Buttons(driver)


@pytest.fixture()
def progress_bar(driver):
    return ProgressBar(driver)
