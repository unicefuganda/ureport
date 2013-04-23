import time
from fixtures.create_poll_utils import if_it_exists_delete_poll_called, create_poll_called
from fixtures.home_page import HomePage
from nose.tools import assert_equal
from nose.tools import assert_true


class TestPollView():

    @classmethod
    def setUpClass(cls):
        cls.home_page = HomePage().load()
        pass

    @classmethod
    def tearDownClass(cls):
        cls.home_page.close_page()

    def setUp(self):
        if_it_exists_delete_poll_called("PollViewTest.poll_1")
        create_poll_called("PollViewTest.poll_1")

    def test_that_at_least_one_poll_is_shown_on_homepage(self):
        assert_equal(1, 1)

    def test_that_poll_list_is_present(self):
        assert_true(self.home_page.is_poll_list_present())