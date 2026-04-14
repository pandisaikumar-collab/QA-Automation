import os
import sys
import time
from playwright.sync_api import sync_playwright

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from lib.open_browser import OpenBrowser
from lib.page_loaded import PageLoaded
from lib.elements import Elements

class TestBasicOperation:
    """ Testcase to Perform Basic Operations"""

    def test_basic_operations(self):
        with sync_playwright() as playwright:
            open_browser_obj = OpenBrowser(playwright)
            page = open_browser_obj.open_browser(browser_type='chromium', headless=False)
            print("*********** Browser Launched ***********")
            page.goto("https://demoqa.com/")
            print("*********** Lib objects initialized ***********")
            page_obj = PageLoaded(page)
            elements_obj = Elements(page)
            if page_obj.is_page_loaded():
                print(f"Is Page Loaded Completely")
            elements_obj.click_on_elements_tab()
            elements_obj.click_on_textbox_sidebar_item()
            time.sleep(10)

            text_box_data = {}
            text_box_data["userName"] = 'Saikumar'
            text_box_data["userEmail"] = 'pandi.saikumar.tech@gmail.com'
            text_box_data["currentAddress"] = 'Chennai'
            text_box_data["permanentAddress"] = 'Chennai'
            elements_obj.fill_text_data(text_box_data)
            elements_obj.click_checkbox_sidebar_item()
            time.sleep(10)
            elements_obj.check_home_checkbox()
            elements_obj.click_web_tables_sidebar_item()
            table_data = elements_obj.get_web_table_data()
            print(type(table_data))
            print(f"Web Table Data: {table_data}")

            print('\n')
            print("*********** Closing Browser ***********")
            page.context.browser.close()
            print("*********** Browser Closed ***********")


if __name__ == "__main__":
    test_obj = TestBasicOperation()
    test_obj.test_check_page_loaded_completely()




