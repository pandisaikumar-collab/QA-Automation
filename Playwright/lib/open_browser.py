# lib/open_browser.py
from playwright.sync_api import sync_playwright

class OpenBrowser:
    def __init__(self, playwright):
        self.playwright = playwright
        self.browser = None
        self.context = None
        self.page = None

    def open_browser(self, browser_type=None, headless=True):
        if browser_type == 'chromium':
            self.browser = self.playwright.chromium.launch(headless=headless)
        elif browser_type == 'firefox':
            self.browser = self.playwright.firefox.launch(headless=headless)
        elif browser_type == 'webkit':
            self.browser = self.playwright.webkit.launch(headless=headless)
        else:
            self.browser = self.playwright.chromium.launch(headless=headless)
        self.context = self.browser.new_context()
        self.page = self.context.new_page()
        return self.page
