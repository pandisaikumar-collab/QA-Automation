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

    def select_text_box(self):
        text_box_ele = self.page.locator("//span[text()='Text Box']")
        text_box_ele.click()
        time.sleep(2)

    def remove_ads(self):
        self.page.evaluate("""
            document.querySelectorAll("iframe").forEach(el => el.remove());
        """)

    def handle_alerts(self):
        self.page.on('dialog', lambda dialog: dialog.accept())

    def enter_text(self, userName):
        username_ele = self.page.locator("//input[@id='userName']")
        username_ele.fill(userName)
        time.sleep(2)

    def submit(self):
        self.page.keyboard.press('Enter')

    def select_check_box_menu(self):
        checkbox_ele = self.page.locator("//span[text()='Check Box']")
        checkbox_ele.click()
        time.sleep(2)

    def check_and_uncheck(self, flag):
        checkbox_ele = self.page.locator("//span[contains(@class, 'checkbox') and @aria-label='Select Home']")
        if flag == True:
            print("Clicking on check box")
            checkbox_ele.check()

        elif flag == False:
            print("Disable checkbox")
            checkbox_ele.uncheck()

        time.sleep(2)





if __name__ == '__main__':
    demo_obj = DemoQATest()
    demo_obj.launch_browser()
    demo_obj.navigate_to_homepage("https://demoqa.com/")
    demo_obj.select_elements_tab()
    demo_obj.select_text_box()
    #demo_obj.handle_alerts()
    demo_obj.remove_ads()
    demo_obj.enter_text("Saikumar")
    demo_obj.submit()
    demo_obj.select_check_box_menu()
    demo_obj.check_and_uncheck(True)


    demo_obj.close_browser()

