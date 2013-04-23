from fixtures.abstract_page import AbstractPage


class HomePage(AbstractPage):

    def __init__(self):
        self.url = "http://localhost:8000/"

    def get_list_of_polls(self):
        polls = []
        return polls

    def is_poll_list_present(self):
        return self.browser.is_element_present_by_id("list_of_polls")
