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

    def remove_ads(self):
        self.page.evaluate("""
            document.querySelectorAll("iframe").forEach(el => el.remove());
        """)

    def select_web_tables(self):
        web_table_ele = self.page.locator("//span[text()='Web Tables']")
        web_table_ele.click()
        time.sleep(2)

    def get_web_tables(self):
        self.select_web_tables()
        first_name = self.page.query_selector_all(
            "//h1[text()='Web Tables']//following::table//tbody//tr//td[1]")
        last_name = self.page.query_selector_all(
            "//h1[text()='Web Tables']//following::table//tbody//tr//td[2]")
        age = self.page.query_selector_all(
            "//h1[text()='Web Tables']//following::table//tbody//tr//td[3]")
        email = self.page.query_selector_all(
            "//h1[text()='Web Tables']//following::table//tbody//tr//td[4]")
        salary = self.page.query_selector_all(
            "//h1[text()='Web Tables']//following::table//tbody//tr//td[5]")
        department = self.page.query_selector_all(
            "//h1[text()='Web Tables']//following::table//tbody//tr//td[6]")
        web_table_data = []
        for index, element in enumerate(first_name):
            if element.inner_text() == "":
                break
            table_data = {}
            table_data.update({'firstName': first_name[index].inner_text().strip()})
            table_data.update({'lastName': last_name[index].inner_text().strip()})
            table_data.update({'age': age[index].inner_text().strip()})
            table_data.update({'email': email[index].inner_text().strip()})
            table_data.update({'salary': salary[index].inner_text().strip()})
            table_data.update({'department': department[index].inner_text().strip()})
            web_table_data.append(table_data)
        return web_table_data



if __name__ == '__main__':
    demo_obj = DemoQATest()
    demo_obj.launch_browser()
    demo_obj.navigate_to_homepage("https://demoqa.com/")
    demo_obj.select_elements_tab()
    #demo_obj.handle_alerts()
    demo_obj.remove_ads()
    data = demo_obj.get_web_tables()
    print(data)
    firstName = []
    for d in data:
        firstName.append(d["firstName"])
    print(firstName)
    demo_obj.close_browser()

