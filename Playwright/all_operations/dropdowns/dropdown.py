"""
method: inner_text (for extracting text)
"""
import time
from playwright.sync_api import sync_playwright

MAX_WAIT = 60000

class DemoQATest:

    def __init__(self, headless=False):
        self.headless = headless
        self.playwright = None
        self.browser = None
        self.page = None

    def launch_browser(self):
        self.playwright = sync_playwright().start()
        self.browser = self.playwright.chromium.launch(
            headless=self.headless, args=['--start-maximized'])
        self.page = self.browser.new_page(no_viewport=True)

    def close_browser(self):
        self.browser.close()
        self.playwright.stop()

    def navigate_to_homepage(self, url):
        self.page.goto(url)

    def select_elements_tab(self):
        elements_ele = "//h5[text()='Elements']"
        elements_card = self.page.locator(elements_ele)
        elements_card.scroll_into_view_if_needed()
        elements_card.click()
        time.sleep(2)

    def select_forms_tab(self):
        self.page.locator("//*[text()='Forms']").click()
        time.sleep(2)
        self.page.locator("//*[text()='Practice Form']").click()
        time.sleep(5)

    def select_dropdown(self):
        self.page.locator("//*[text()='State and City']//following::div[text()='Select State']").click()
        time.sleep(5)
        self.page.select_option("//*[text()='State and City']//following::div[text()='Select State']//following::*", value=2)
        time.sleep(5)

if __name__ == '__main__':
    demo_obj = DemoQATest()
    demo_obj.launch_browser()
    demo_obj.navigate_to_homepage("https://demoqa.com/")
    demo_obj.select_elements_tab()
    demo_obj.select_forms_tab()
    demo_obj.select_dropdown()
    demo_obj.close_browser()

