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

    def get_number_of_previous_polls(self):
        list_of_polls = self.browser.find_by_id("list_of_polls")
        return len(list_of_polls.find_by_name("poll"))
