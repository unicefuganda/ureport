from splinter import Browser

class UreportApplication:

    def __init__(self):
        self.browser = Browser()

    def close(self):
        self.browser.quit()

    def navigate_to_home_page(self):
        return HomePage(self.browser).load()


class HomePage():

    def __init__(self, browser):
        self.browser = browser

    def load(self):
        self.browser.visit("http://localhost:8088/")
        return self

    def get_list_of_polls(self):
        polls = []
        return polls

    def number_of_previous_polls(self):
        return len(self.get_list_of_polls())

    def is_poll_list_present(self):
        return self.browser.is_element_present_by_id("list_of_polls")
