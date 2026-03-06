"""
elements.py
Page model for Demo home page
Author(s): Pandi Saikumar <pandisaikumar.tech@gmail.com>
"""
import os 
import time 
import yaml 
import logging

from selenium.webdriver.common.by import By 
from selenium.webdriver.common.keys import Keys 
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.common.action_chains import ActionChains 
from selenium.webdriver.support import expected_conditions as EC 
from selenium.common.exceptions import NoSuchElementException, TimeoutException

log = logging.getLogger(os.path.basename(__file__))
log.setLevel(logging.INFO)

DEFAULT_WAITIME = 60

class Elements:
    """
    Page model for Elements 
    :param driver: selenium driver
    :type driver: object
    """

    def __init__(self, driver):
        """
        Constructor for Elements page
        """
        self.driver = driver 
        current_dir = os.path.dirname(os.path.abspath(__file__))
        self.locators = current_dir + "/../locators/elements.yaml"

        with open(self.locators, 'r') as file:
            self.xpaths = yaml.safe_load(file)
    
    def is_elements_page_loaded(self):
        """
        Returns True if elements page loaded 
        False otherwise
        :returns: bool
        """
        page = 'Elements page'
        timeout = DEFAULT_WAITIME
        is_elements_page_loaded = True
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_all_elements_located((
                    By.XPATH, self.xpaths["elements_groups"]["xpath"])))
        
        except (NoSuchElementException, TimeoutException) as e:
            is_elements_page_loaded = False
            log.error(f"{page} not loaded: {e}")

        try:
            WebDriverWait(self.driver, timeout).until(
                EC.element_to_be_clickable((
                    By.XPATH, self.xpaths["elements_groups"]["xpath"])))
        
        except (NoSuchElementException, TimeoutException) as e:
            is_elements_page_loaded = False
            log.error(f"{page} not loaded: {e}")
        
        return is_elements_page_loaded

    def select_dropdown_item(self, dropdown_xpath, dropdown_items_xpath, dropdown_item):
        """
        Generic function to select <dropdown> from <dropdown_xpath>>
        
        param: drpdown_xpath: Drpdown xpath
        :type drpdown_xpath: str
        :param drpdown_items: Dropdown items xpath
        :type drpdown_items: list
        """
        is_dropdown_selected = False 
        dropdown_element = self.driver.find_element(By.XPATH, dropdown_xpath)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", dropdown_element)
        dropdown_element.click()
        time.sleep(0.5)

        dropdown_item_elements = self.driver.find_element(By.XPATH, dropdown_items_xpath)
        for dropdown_item_element in dropdown_item_elements:
            if dropdown_item_element.text == dropdown_item:
                self.driver.execute_script("arguments[0].scrollIntoView(true);", dropdown_item_element)
                dropdown_item_element.click()
                is_dropdown_selected = True 
                break
            if not is_dropdown_selected:
                log.error(f"Dropdown item '{dropdown_item}' not found in dropdown")
        return is_dropdown_selected

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
        
    def click_elements_button(self):
        """
        Clicks on the Elements button 
        """
        return self.click_button(xpath=self.xpaths["elements_wrapper"]["xpath"])
    
    def click_buttons_sections(self):
        """
        Clicks on the Button sections
        """
        return self.click_button(xpath=self.xpaths["elements_groups"]["buttons_section"]["xpath"])
    
    def click_text_box_button(self):
        """
        Clicks on the Text Box button
        """
        return self.click_button(xpath=self.xpaths["elements_groups"]["text_box"]["xpath"])

    def click_webtable_button(self):
        """
        Clicks on the Web Table button
        """
        return self.click_button(xpath=self.xpaths["elements_groups"]["web_tables"]["xpath"])

    def get_web_table_data(self):
        """
        Return Table data 
        :returns: Dict data
        :rtype: dict 
        """
        table_info = {}

        first_name_eles = self.driver.find_elements(By.XPATH, self.xpaths["web_table"]["firstname"]["xpath"])
        last_name_eles = self.driver.find_elements(By.XPATH, self.xpaths["web_table"]["lastname"]["xpath"])
        age_eles = self.driver.find_elements(By.XPATH, self.xpaths["web_table"]["age"]["xpath"])
        email_eles = self.driver.find_elements(By.XPATH, self.xpaths["web_table"]["email"]["xpath"])
        salary_eles = self.driver.find_elements(By.XPATH, self.xpaths["web_table"]["salary"]["xpath"])
        department_eles = self.driver.find_elements(By.XPATH, self.xpaths["web_table"]["department"]["xpath"])
        if not first_name_eles:
            log.info("No data found in the table")
            return table_info

        for index, first_name_ele in enumerate(first_name_eles):
            last_name_ele = last_name_eles[index]
            age_ele = age_eles[index]
            email_ele = email_eles[index]
            salary_ele = salary_eles[index]
            department_ele = department_eles[index]

            first_name = first_name_ele.text.strip()
            last_name = last_name_ele.text.strip()
            age = age_ele.text.strip()
            email = email_ele.text.strip()
            salary = salary_ele.text.strip()
            department = department_ele.text.strip()

            table_data = {
                "Firstname": first_name,
                "Lastname": last_name,
                "Age": age,
                "Email": email,
                "Salary": salary,
                "Department": department
            }

            table_info[first_name] = table_data

        return table_info

    def click_add_button(self):
        """
        Function to click on Add button
        """
        return self.click_button(xpath=self.xpaths['elements_groups']['add_button']['xpath'])

    def is_registration_form_loaded(self):
        """
        Returns True if registration form loaded
        False otherwise 
        :returns: bool
        """
        page = 'Registration form'
        timeout = DEFAULT_WAITIME
        is_registration_form_loaded = True 
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_all_elements_located((
                    By.XPATH, self.xpaths["elements_groups"]["registration_form"]["all_reg_form_fields"]['xpath'])))
        
        except (NoSuchElementException, TimeoutException) as e:
            is_registration_form_loaded = False
            log.error(f"{page} is not loaded within {timeout} seconds: {e}")

        try:
            WebDriverWait(self.driver, timeout).until(
                EC.element_to_be_clickable((
                    By.XPATH, self.xpaths["elements_groups"]["registration_form"]["all_reg_form_fields"]['xpath'])))
        
        except (NoSuchElementException, TimeoutException) as e:
            is_registration_form_loaded = False
            log.error(f"{page} is not loaded within {timeout} seconds: {e}")


    def enter_text(self, xpath, value):
        """
        Clear the textbox contents if any and 
        then enter the new value

        :param xpath: filed xpath
        :type xpath: str
        :param value: Value to be entered in the textbox
        :type value: str 
        """
        text_ele = self.driver.find_element(By.XPATH, xpath)

        """
        Using javascript method to scroll to element before entering the text 
        in the textbox or textarea. This is implemented due to known bug with firefox 
        browser.
        https://stackoverflow.com/questions/44777053/selenium-movetargetoutofboundsexception-with-firefox/52045231
        """
        self.driver.execute_script("arguments[0].scrollIntoView(true);", text_ele)
        time.sleep(0.5)
        text_ele.click()
        time.sleep(0.5)
        text_ele.clear()
        time.sleep(0.5)
        text_ele.send_keys(Keys.CONTROL + 'a' + Keys.DELETE)
        time.sleep(0.5)
        text_ele.clear()
        time.sleep(0.5)
        text_ele.send_keys(value)
        time.sleep(0.5)
        text_ele.send_keys(Keys.TAB)
        time.sleep(0.5)
        text_ele = self.driver.find_element(By.XPATH, xpath)
        entered_value = text_ele.get_attribute('value')
        log.info(f"Entered value: {entered_value} in the field")

    def enter_first_name(self, firstname):
        """
        Enter First name 
        :param first_name: name
        :type first_name: str
        """
        log.info("Entering first name")
        return self.enter_text(xpath=self.xpaths['elements_groups']['registration_form']['firstname']['xpath'], value=firstname)

    def enter_last_name(self, lastname):
        """
        Enter Last name 
        :param last_name: name
        :type last_name: str
        """
        log.info("Entering last name")
        return self.enter_text(xpath=self.xpaths['elements_groups']['registration_form']['lastname']['xpath'], value=lastname)

    def enter_email(self, email):
        """
        Enter email
        :param email: email
        :type email: str
        """
        log.info("Entering email")
        return self.enter_text(xpath=self.xpaths['elements_groups']['registration_form']['email']['xpath'], value=email)

    def enter_age(self, age):
        """
        Enter age
        :param age: age
        :type age: str
        """
        log.info("Entering age")
        return self.enter_text(xpath=self.xpaths['elements_groups']['registration_form']['age']['xpath'], value=age)

    def enter_salary(self, salary):
        """
        Enter salary
        :param salary: salary
        :type salary: str
        """
        log.info("Entering salary")
        return self.enter_text(xpath=self.xpaths['elements_groups']['registration_form']['salary']['xpath'], value=salary)

    def enter_department(self, department):
        """
        Enter department
        :param department: department
        :type department: str
        """
        log.info("Entering department")
        return self.enter_text(xpath=self.xpaths['elements_groups']['registration_form']['department']['xpath'], value=department)

    def click_submit_button(self):
        """
        Click on the submit button
        """
        return self.click_button(xpath=self.xpaths['elements_groups']['registration_form']['submit_button']['xpath'])

    def enter_registration_form_details(self, api_payload):
        """
        Function to fill the registration form

        :param_api_payload: API payload with user data
        :type api_payload: dict
        : 
        """
        self.click_add_button()
        self.is_registration_form_loaded()
        if not api_payload:
            raise ValueError("API payload is empty. Cannot fill registration form")
        if 'firstname' in api_payload:
            self.enter_first_name(api_payload['firstname'])
        if 'lastname' in api_payload:
            self.enter_last_name(api_payload['lastname'])
        if 'email' in api_payload:
            self.enter_email(api_payload['email'])
        if 'age' in api_payload:
            self.enter_age(api_payload['age'])  
        if 'salary' in api_payload: 
            self.enter_salary(api_payload['salary'])
        if 'department' in api_payload:
            self.enter_department(api_payload['department'])

        self.click_submit_button()
        time.sleep(0.5)
        return True 
    
    def fill_registration_form(self, api_payload):
        """
        Function to fill the registration form with user data
        :param api_payload: API payload with user data
        :type api_payload: dict
        """
        log.info("Filling registration form with user data")
        validation_msg = self.enter_registration_form_details(api_payload)
        if validation_msg:
            log.info("Registration form filled successfully")
        else:
            raise Exception("Failed to fill registration form")


class Buttons(object):
    """
    Page model to cover Buttons section
    :param driver: selenium driver
    :type driver: object
    """
    def __init__(self, driver):
        """
        Constructor for Buttons page
        """
        self.driver = driver
        current_dir = os.path.dirname(os.path.abspath(__file__))
        self.locators = current_dir + "/../locators/elements.yaml"
        with open(self.locators, 'r') as file:
            self.xpaths = yaml.safe_load(file)

    def is_buttons_page_loaded(self):
        """
        Returns True if elements page loaded 
        False otherwise
        :returns: bool
        """
        page = 'Buttons page'
        timeout = DEFAULT_WAITIME
        is_buttons_page_loaded = True
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_all_elements_located((
                    By.XPATH, self.xpaths["buttons_section"]["all_buttons"]["xpath"])))
        
        except (NoSuchElementException, TimeoutException) as e:
            is_buttons_page_loaded = False
            log.error(f"{page} not loaded: {e}")

        try:
            WebDriverWait(self.driver, timeout).until(
                EC.element_to_be_clickable((
                    By.XPATH, self.xpaths["buttons_section"]["all_buttons"]["xpath"])))
        
        except (NoSuchElementException, TimeoutException) as e:
            is_buttons_page_loaded = False
            log.error(f"{page} not loaded: {e}")
        
        return is_buttons_page_loaded
    
    def double_click(self):
        """
        Returns:bool: True if double-click was successful, False otherwise.
        """
        timeout = DEFAULT_WAITIME
        try:
            double_ele = WebDriverWait(self.driver, timeout).until(
                EC.element_to_be_clickable(
                    (By.XPATH, self.xpaths['buttons_section']['double_click_button']["xpath"])
                )
            )
            ActionChains(self.driver).move_to_element(double_ele).double_click().perform()
            return True
        except Exception as e:
            log.error(f"Double click action failed: {e}")
            return False

        try:
            double_msg = self.driver.find_element(By.XPATH, self.xpaths["buttons_section"]["double_click_msg"]["xpath"])
            time.sleep(0.5)
            msg_txt = double_ele.text 
            log.info("Double click message: ", msg_txt)
        
        except Exception as e:
            log.error("Double click text msg not getting.")

    
    def right_click(self):
        """
        Function to Right click
        """
        timeout = DEFAULT_WAITIME
        try:
            right_ele = WebDriverWait(self.driver, timeout).until(
                EC.element_to_be_clickable((By.XPATH, self.xpaths["buttons_section"]["right_click_button"]["xpath"]))
            )
            ActionChains(self.driver).move_to_element(right_ele).context_click().perform()
            return True 
        except Exception as e:
            log.error(f"Failed to right click: {e}")
            return False 
        
    def click_me(self):
        """
        Function to Click
        """
        timeout = DEFAULT_WAITIME
        try:
            click_me = WebDriverWait(self.driver, timeout).until(
                EC.element_to_be_clickable((By.XPATH, self.xpaths["buttons_section"]["click_me_button"]["xpath"]))
            )
            ActionChains(self.driver).move_to_element(click_me).click().perform()
            return True 
        except Exception as e:
            log.error(f"Failed to click: {e}")
            return False 
    
    
        


