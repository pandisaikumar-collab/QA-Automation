"""
Maximize Browser: args=['--start-maximized']
"""
from playwright.sync_api import sync_playwright
import time

class DemoQATest:

    def __init__(self, headless=False):
        self.headless = headless
        self.playwright = None
        self.browser = None

    def launch_browser_and_maximized(self):
        self.playwright = sync_playwright().start()
        self.browser = self.playwright.chromium.launch(
            headless=self.headless, args=['--start-maximized'])
        self.page = self.browser.new_page(no_viewport=True)
        time.sleep(2)

    def close_browser(self):
        self.browser.close()
        self.playwright.stop()

demo_obj = DemoQATest()
demo_obj.launch_browser_and_maximized()
demo_obj.close_browser()