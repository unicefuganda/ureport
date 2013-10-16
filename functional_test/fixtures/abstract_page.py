from splinter import Browser
from splinter import Browser


class AbstractPage:

    url = "NO_URL_FOR_ABSTRACT_SCREEN"

    def load(self):
        self.browser = Browser()
        self.browser.visit(self.url)
        return self

    def close_page(self):
        self.browser.quit()
