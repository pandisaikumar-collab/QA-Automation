# lib/page_loaded.py

class PageLoaded:
    def __init__(self, page):
        self.page = page

    def is_page_loaded(self):
        """
        Return True if page is loaded, False otherwise.
        """
        try:
            home_body_xpath = "//div[@class='home-body']//div[contains(@class, 'category-cards')]"
            home_body_ele = self.page.wait_for_selector(home_body_xpath, timeout=5000)
            if home_body_ele:
                return True
        except Exception as e:
            print(f"Exception occurred while checking page load: {e}")
            return False
