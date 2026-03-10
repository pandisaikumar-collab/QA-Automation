"""
method: self.page.once("dialog", lambda dialog: dialog.accept())
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

    def select_alerts_and_frames_tab(self):
        alerts_ele = "//h5[text()='Alerts, Frame & Windows']"
        alerts_card = self.page.locator(alerts_ele)
        alerts_card.scroll_into_view_if_needed()
        alerts_card.click()
        time.sleep(2)

    def remove_ads(self):
        self.page.evaluate("""
            document.querySelectorAll("iframe").forEach(el => el.remove());
        """)

    def click_on_alerts(self):
        new_tab_ele = self.page.locator("//span[text()='Alerts']")
        new_tab_ele.click()
        time.sleep(10)

    def click_first_me(self):
        first_me = self.page.locator("//button[@class='btn btn-primary' and @id='timerAlertButton']")
        first_me.click()
        time.sleep(10)
        self.page.once('dialog', lambda dialog: dialog.accept())
        time.sleep(2)




if __name__ == '__main__':
    demo_obj = DemoQATest()
    demo_obj.launch_browser()
    demo_obj.navigate_to_homepage("https://demoqa.com/")
    demo_obj.select_alerts_and_frames_tab()
    demo_obj.remove_ads()
    demo_obj.click_on_alerts()
    demo_obj.click_first_me()
    demo_obj.close_browser()

