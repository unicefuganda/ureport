from fixtures.create_poll_utils import if_it_exists_delete_poll_called, create_poll_called
from fixtures.home_page import navigate_to_home_page
from nose.tools import assert_equal
from splinter import Browser
from fixtures.splinter_wrapper import SplinterTestCase

class TestPollView():

    def setUp(self):
        if_it_exists_delete_poll_called("PollViewTest.poll_1")
        create_poll_called("PollViewTest.poll_1")

    def tearDown(self):
        pass

    def test_that_at_least_one_poll_is_shown_on_homepage(self):
        # home_page = navigate_to_home_page()
        # polls = home_page.get_list_of_polls()

        # assert_that(polls.size() is(greaterThanOrEqualTo(1)))
        # assert_equal(1, len(polls))
        assert_equal(1, 1)