"""
method: hover
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

    def select_buttons(self):
        text_box_ele = self.page.locator("//span[text()='Buttons']")
        text_box_ele.click()
        time.sleep(2)

    def remove_ads(self):
        self.page.evaluate("""
            document.querySelectorAll("iframe").forEach(el => el.remove());
        """)

    def hover_on_click_me(self):
        click_me_ele = self.page.locator("//button[text()='Click Me']")
        if click_me_ele.hover():
            print("hover click me")
        else:
            print("not hover click me")

        time.sleep(2)


if __name__ == '__main__':
    demo_obj = DemoQATest()
    demo_obj.launch_browser()
    demo_obj.navigate_to_homepage("https://demoqa.com/")
    demo_obj.select_elements_tab()
    demo_obj.select_buttons()
    demo_obj.remove_ads()
    demo_obj.hover_on_click_me()

    demo_obj.close_browser()

