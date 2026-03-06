"""
widgets.py 
Page model for all Widgets sections
Author(s): Pandi Saikumar <pandisaikumar.tech@gmail.com>
"""

import os
import yaml
import time 
import logging

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException, TimeoutException

log = logging.getLogger(os.path.basename(__file__))
log.setLevel(logging.INFO)

DEFAULT_WAITTIME = 60


class ProgressBar:
    """
    Page model for Widgets 
    :param driver: selenium driver 
    :type driver: object 
    """

    def __init__(self, driver):
        """
        Constructor for Widgets page
        :param driver: selenium driver instance
        """
        self.driver = driver
        current_dir = os.path.dirname(os.path.abspath(__file__))
        self.locators = os.path.join(current_dir, '../locators/widgets.yaml')

        with open(self.locators, 'r') as file:
            self.xpaths = yaml.safe_load(file)

    def is_widgets_page_loaded(self):
        """
        Returns True if widgets page is loaded, False otherwise.
        :return: bool
        """
        page = "Widgets"
        timeout = DEFAULT_WAITTIME
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_element_located((By.XPATH, self.xpaths['progress_bar_section']['xpath']))
            )

            WebDriverWait(self.driver, timeout).until(
                EC.element_to_be_clickable((By.XPATH, self.xpaths['start_button']['xpath']))
            )
            log.info(f"{page} loaded successfully.")
            return True

        except (NoSuchElementException, TimeoutException) as e:
            log.error(f"{page} not loaded: {e}")
            return False

    def click_button(self, xpath):
        """
        Metthod to click on a button using xpath
        :param xpath: ele xpath
        :type xpath: str
        """
        ele_text = self.driver.find_element(By.XPATH, xpath)
        log.info(f"Clicking on button with text: {ele_text.text}")
        ele = self.driver.find_element(By.XPATH, xpath)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", ele)
        time.sleep(0.5)
        ele.click()

    def click_progress_bar_section(self):
        """
        Clicks on the Progress Bar 
        """
        return self.click_button(xpath=self.xpaths['progress_bar_section']["xpath"])

    def click_start_button(self):
        """
        Click start button
        """
        return self.click_button(self.xpaths['start_button']['xpath'])

    def handle_progress_bar(self):
        """
        Starts the progress bar and checks every 5 seconds until it reaches 100%.
        :return: True if progress bar completed, False otherwise
        :rtype: bool
        """
        try:
            self.click_start_button()
            progress_bar_xpath = self.xpaths['progress_bar']['xpath']
            log.info("Started progress bar..")

            max_wait = DEFAULT_WAITTIME
            elapsed_time = 0

            while elapsed_time < max_wait:
                try:
                    progress_text = self.driver.find_element(By.XPATH, progress_bar_xpath).text.strip()
                    log.info(f"Progress: {progress_text}")

                    # Normalize and check if progress reached 100%
                    if progress_text.replace('%', '').strip() == "100":
                        log.info("Progress bar is completed.")
                        return True

                except Exception as e:
                    log.warning(f"Progress bar element not found, retrying... {e}")

                time.sleep(5)
                elapsed_time += 5

        except Exception as error:
            log.error(f"Error while handling progress: {error}")
            raise


                
                
