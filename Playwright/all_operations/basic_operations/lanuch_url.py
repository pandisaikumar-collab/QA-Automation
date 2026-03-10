"""
method: goto('url')
"""
from playwright.sync_api import sync_playwright
import time

class DemoQATest:

    def __init__(self, headless=False):
        self.headless = headless
        self.playwright = None
        self.browser = None

    def launch_browser(self):
        self.playwright = sync_playwright().start()
        self.browser = self.playwright.chromium.launch(
            headless=self.headless)
        self.page = self.browser.new_page(no_viewport=True)

    def navigate_url(self):
        self.page.goto("https://demoqa.com/")
        time.sleep(5)

    def close_browser(self):
        self.browser.close()
        self.playwright.stop()

demo_obj = DemoQATest()
demo_obj.launch_browser()
demo_obj.navigate_url()
demo_obj.close_browser()