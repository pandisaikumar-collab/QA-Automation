"""
method:
    except(self.page).to_have_titile('DEMOQA')
    except(self.page).to_have_url('url')
    element = self.page.get_by_text('elements')
    expcet(element).to_be_visible()
"""
from playwright.sync_api import sync_playwright, expect
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

    def assertions(self):
        expect(self.page).to_have_title('demosite')
        expect(self.page).to_have_url('https://demoqa.com/')


    def close_browser(self):
        self.browser.close()
        self.playwright.stop()

demo_obj = DemoQATest()
demo_obj.launch_browser()
demo_obj.navigate_url()
demo_obj.assertions()
demo_obj.close_browser()