from splinter import Browser


def navigate_to_home_page():
    return HomePage().load()


class HomePage:

    def load(self):
        self.browser = Browser('firefox')
        self.browser.visit('/')
        return self

    def get_list_of_polls(self):
        polls = []
        return polls

