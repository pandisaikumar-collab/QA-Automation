import pytest
from selenium import webdriver

#fixture: use to set up and tear down the test environment
#scope: function, class, module, session

import pytest
from selenium import webdriver


# Function scope: (Default)
# -New browser for every test function
# Recommended for independent tests
# No state sharing

# @pytest.fixture(scope='function')
# def driver():
#     driver = webdriver.Chrome()
#     driver.maximize_window()
#     driver.implicitly_wait(30)
#     driver.get('https://demoqa.com/')
#     yield driver
#     driver.quit()
#
#
# # Class scope: (One browser per testcases)
# # Suitable for workflow testcaess
# @pytest.fixture(scope='class')
# def driver():
#     driver = webdriver.Chrome()
#     driver.maximize_window()
#     driver.implicitly_wait(30)
#     driver.get('https://demoqa.com/')
#     yield driver
#     driver.quit()


# Module scope: (One browser for test file)
@pytest.fixture(scope="module")
def driver():
    driver = webdriver.Firefox()
    driver.maximize_window()
    driver.implicitly_wait(10)
    driver.delete_all_cookies()
    driver.get("https://demoqa.com/")

    yield driver

    driver.quit()


# # Package scope: (One browser for test folder)
# @pytest.fixture(scope='module')
# def driver():
#     driver = webdriver.Chrome()
#     driver.maximize_window()
#     driver.implicitly_wait(30)
#     driver.get('https://demoqa.com/')
#     yield driver
#     driver.quit()
#
#
# # Session scope: (One browser for entaire pytest execution)
# @pytest.fixture(scope='module')
# def driver():
#     driver = webdriver.Chrome()
#     driver.maximize_window()
#     driver.implicitly_wait(30)
#     driver.get('https://demoqa.com/')
#     yield driver
#     driver.quit()