# lib/elements.py

MAXTIME = 5000

class Elements:
    def __init__(self, page):
        self.page = page

    def click_element(self, xpath):
        """
        Scroll into view first and then
        Click on the element
        arg(s): xpath
        """
        element = self.page.wait_for_selector(xpath, timeout=MAXTIME)
        element.scroll_into_view_if_needed()
        return element.click()

    def click_on_elements_tab(self):
        """
        Click on Elements Tab
        """
        elements_tab_xpath = "//div[@class='card-body']//h5[text()='Elements']"
        self.click_element(elements_tab_xpath)

    def expand_sidebar_item_and_click_sub_item(self, item_xpath, sub_item_xpath):
        """
        Expand the sidebar item and click on the sub item
        arg(s): item_xpath, sub_item_xpath
        if item is already expanded, it will just click on the sub item
        """
        item_element = self.page.wait_for_selector(item_xpath, timeout=MAXTIME)
        aria_expanded = item_element.get_attribute("aria-expanded")
        if aria_expanded == "false":
            item_element.click()
        self.click_element(sub_item_xpath)

    def click_on_textbox_sidebar_item(self):
        """
        Click on Text Box sidebar item
        """
        elements_tab_xpath = "//div[@class='header-text']//..//*[text()='Elements']"
        text_box_sidebar_item_xpath = "//div[@class='header-text']//..//*[text()='Elements']//following::ul[@class='menu-list']//span[text()='Text Box']"
        self.expand_sidebar_item_and_click_sub_item(elements_tab_xpath, text_box_sidebar_item_xpath)

    def fill_textbox(self, textbox_xpath, text):
        """
        Fill the textbox with the given text
        arg(s): textbox_xpath, text
        """
        textbox_ele = self.page.wait_for_selector(textbox_xpath, timeout=MAXTIME)
        textbox_ele.scroll_into_view_if_needed()
        print("Filling textbox with text:", text)
        return textbox_ele.fill(text)

    def submit(self):
        """
        Click on the submit button
        """
        submit_button_xpath = "//button[@id='submit']"
        self.click_element(submit_button_xpath)

    def fill_text_data(self, dict_data):
        """
        Fill the text data in the textboxes
        arg(s): dict_data
        like: {
            "userName": "Saikumar",
            "userEmail": "sample.com",
            "currentAddress": "address1",
            "permanentAddress": "address2"
        }
        """
        userName_xpath = "//h1[text()='Text Box']//..//input[@id='userName']"
        userEmail_xpath = "//h1[text()='Text Box']//..//input[@id='userEmail']"
        currentAddress_xpath = "//h1[text()='Text Box']//..//textarea[@id='currentAddress']"
        permanentAddress_xpath = "//h1[text()='Text Box']//..//textarea[@id='permanentAddress']"

        if not isinstance(dict_data, dict):
            print("Invalid data format. Expected a dictionary.")
            return
        if 'userName' in dict_data:
            self.fill_textbox(userName_xpath, dict_data['userName'])
        if 'userEmail' in dict_data:
            self.fill_textbox(userEmail_xpath, dict_data['userEmail'])
        if 'currentAddress' in dict_data:
            self.fill_textbox(currentAddress_xpath, dict_data['currentAddress'])
        if 'permanentAddress' in dict_data:
            self.fill_textbox(permanentAddress_xpath, dict_data['permanentAddress'])
        self.submit()

    def check_and_uncheck_checkbox(self, checkbox_xpath, check=True):
        """
        Check or uncheck the checkbox based on the 'check' parameter
        arg(s): checkbox_xpath, check (True/False)
        """
        checkbox_ele = self.page.wait_for_selector(checkbox_xpath, timeout=MAXTIME)
        checkbox_ele.scroll_into_view_if_needed()
        is_checked = checkbox_ele.is_checked()
        if check:
            if not is_checked:
                checkbox_ele.check()
        else:
            if is_checked:
                checkbox_ele.uncheck()

    def click_checkbox_sidebar_item(self):
        """
        Click on Check Box sidebar item
        """
        elements_tab_xpath = "//div[@class='header-text']//..//*[text()='Elements']"
        checkbox_xpath = "//div[@class='header-text']//..//*[text()='Elements']//following::ul[@class='menu-list']//span[text()='Check Box']"
        self.expand_sidebar_item_and_click_sub_item(elements_tab_xpath, checkbox_xpath)

    def check_home_checkbox(self):
        """
        Check the Home checkbox
        """
        home_checkbox_xpath = "//h1[text()='Check Box']//..//span[@class='rct-checkbox']"
        self.check_and_uncheck_checkbox(home_checkbox_xpath, check=True)

    def click_web_tables_sidebar_item(self):
        """
        Click on Web Tables sidebar item
        """
        elements_tab_xpath = "//div[@class='header-text']//..//*[text()='Elements']"
        web_tables_xpath = "//div[@class='header-text']//..//*[text()='Elements']//following::ul[@class='menu-list']//span[text()='Web Tables']"
        self.expand_sidebar_item_and_click_sub_item(elements_tab_xpath, web_tables_xpath)

    def get_web_table_data(self):
        """
        Get the web table data as list of dictionaries
        """
        all_rows = "//div[@class='rt-tbody']//div[@role='row']"
        rows = self.page.query_selector_all(all_rows)
        if not rows:
            print("No data found in the web table.")
            return []

        firstname_ele = self.page.query_selector_all("//div[@class='rt-tbody']//div[@role='gridcell'][1]")
        lastname_ele = self.page.query_selector_all("//div[@class='rt-tbody']//div[@role='gridcell'][2]")
        age_ele = self.page.query_selector_all("//div[@class='rt-tbody']//div[@role='gridcell'][3]")
        email_ele = self.page.query_selector_all("//div[@class='rt-tbody']//div[@role='gridcell'][4]")
        salary_ele = self.page.query_selector_all("//div[@class='rt-tbody']//div[@role='gridcell'][5]")
        department_ele = self.page.query_selector_all("//div[@class='rt-tbody']//div[@role='gridcell'][6]")

        table_data = []
        for i in range(len(rows)):
            row_data = {
                "firstname": firstname_ele[i].inner_text().strip(),
                "lastname": lastname_ele[i].inner_text().strip(),
                "age": age_ele[i].inner_text().strip(),
                "email": email_ele[i].inner_text().strip(),
                "salary": salary_ele[i].inner_text().strip(),
                "department": department_ele[i].inner_text().strip(),
            }
            table_data.append(row_data)
        return table_data




















