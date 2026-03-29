"""
method: expect_popup() as new_tab_info,
        new_tab = new_tab_info.value (it contains new page values)
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
        time.sleep(5)

    def select_alerts_and_frames_tab(self):
        alerts_ele = "//h5[text()='Alerts, Frame & Windows']"
        alerts_card = self.page.locator(alerts_ele)
        alerts_card.scroll_into_view_if_needed()
        alerts_card.click()
        time.sleep(2)

    def click_on_frames(self):
        nested_frame_ele = self.page.locator("//span[text()='Frames']").click()
        time.sleep(5)

    def handle_frames(self):
        frame = self.page.frame_locator("#frame1")
        text = frame.locator("//h1[@id='sampleHeading']")
        print(text.inner_text())



if __name__ == '__main__':
    demo_obj = DemoQATest()
    demo_obj.launch_browser()
    demo_obj.navigate_to_homepage("https://demoqa.com/")
    demo_obj.select_alerts_and_frames_tab()
    demo_obj.click_on_frames()
    demo_obj.handle_frames()
    demo_obj.close_browser()

